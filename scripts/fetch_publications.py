#!/usr/bin/env python3
"""
Fetch publications from ORCID + Crossref and write _data/publications.auto.yml.

- ORCID gives us the list of works (mostly DOIs + put-codes).
- Crossref gives us clean author lists, venue, year, and BibTeX.
- _data/publications.overrides.yml lets us pin/patch fields per DOI.

Run locally:  python3 scripts/fetch_publications.py
Run in CI:    see .github/workflows/update-publications.yml

The current _data/publications.yml is NEVER touched by this script.
Once you're happy with publications.auto.yml, rename or copy its contents
into publications.yml to make it live.
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    import yaml  # type: ignore
except ImportError:
    sys.exit("Missing dependency: pip install pyyaml")


# Force YAML to write multi-line strings (BibTeX) as literal `|` blocks.
class _LiteralStr(str):
    pass


def _literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(_LiteralStr, _literal_representer)


def _clean(s: str) -> str:
    """Unescape HTML entities Crossref returns (e.g. '&amp;' -> '&')."""
    if not s:
        return s
    return html.unescape(s).strip()


def _tidy_bibtex(raw: str) -> str:
    """Crossref returns BibTeX on a single line. Pretty-print so the `|` block reads nicely."""
    if not raw:
        return ""
    s = html.unescape(raw).strip()
    # Split "@type{key, field={...}, field={...}}" into one field per line
    m = re.match(r"(@\w+\{[^,]+),\s*(.*)\}\s*$", s, flags=re.DOTALL)
    if not m:
        return s + "\n"
    head, body = m.group(1), m.group(2)
    # Split on ", " that appears at brace-balance 0
    fields: list[str] = []
    depth = 0
    buf = []
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        if depth == 0 and body[i:i + 2] == ", ":
            fields.append("".join(buf).strip())
            buf = []
            i += 2
            continue
        buf.append(ch)
        i += 1
    if buf:
        fields.append("".join(buf).strip())
    lines = [head + ","]
    for f in fields:
        lines.append(f"  {f},")
    # Drop trailing comma on last field
    if lines[-1].endswith(","):
        lines[-1] = lines[-1][:-1]
    lines.append("}")
    return "\n".join(lines) + "\n"

ORCID = os.environ.get("ORCID_ID", "0009-0006-8410-7156").strip()
UA = (
    "fazlurnu.github.io publication fetcher "
    "(+https://fazlurnu.github.io; mailto:fazlur.rahman.ae@gmail.com)"
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "publications.auto.yml"
OVERRIDES_FILE = ROOT / "_data" / "publications.overrides.yml"


# ---------- HTTP helpers ----------

def _request(url: str, accept: str) -> bytes:
    req = Request(url, headers={"Accept": accept, "User-Agent": UA})
    with urlopen(req, timeout=30) as r:
        return r.read()


def fetch_json(url: str) -> dict:
    return json.loads(_request(url, "application/json").decode("utf-8"))


def fetch_text(url: str, accept: str) -> str:
    return _request(url, accept).decode("utf-8")


# ---------- Overrides ----------

def load_overrides() -> dict[str, dict]:
    if not OVERRIDES_FILE.exists():
        return {}
    data = yaml.safe_load(OVERRIDES_FILE.read_text()) or []
    if not isinstance(data, list):
        print(f"! {OVERRIDES_FILE.name} should be a YAML list; ignoring.")
        return {}
    out: dict[str, dict] = {}
    for o in data:
        if isinstance(o, dict) and o.get("doi"):
            out[str(o["doi"]).lower()] = o
    return out


# ---------- Crossref mapping ----------

def short_authors(full_list: list[dict]) -> str:
    """Crossref author list -> 'M. F. Rahman, J. Ellerbroek, et al.'"""
    out: list[str] = []
    for a in full_list:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        # Initials of each space/hyphen-separated given name part
        parts = given.replace(".", " ").replace("-", " ").split()
        initials = " ".join(f"{p[0]}." for p in parts if p)
        if family:
            name = (initials + " " + family).strip()
        else:
            name = a.get("name", "").strip()
        if name:
            out.append(name)
    if len(out) > 4:
        out = out[:3] + ["et al."]
    return ", ".join(out)


def entry_from_crossref(doi: str) -> dict:
    data = fetch_json(f"https://api.crossref.org/works/{doi}")["message"]

    title = _clean((data.get("title") or [""])[0])
    venue = ""
    for key in ("container-title", "short-container-title"):
        arr = data.get(key) or []
        if arr:
            venue = _clean(arr[0])
            break
    if not venue:
        venue = _clean(data.get("publisher") or "")

    # Prefer print year to avoid "online-first 2026" surprises for still-in-2025 papers
    date_parts = (
        data.get("published-print", {}).get("date-parts")
        or data.get("published-online", {}).get("date-parts")
        or data.get("issued", {}).get("date-parts")
        or [[None]]
    )
    year = date_parts[0][0] if date_parts and date_parts[0] else None

    authors = short_authors(data.get("author") or [])

    try:
        bibtex = _tidy_bibtex(fetch_text(
            f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex",
            accept="application/x-bibtex",
        ))
    except (HTTPError, URLError) as e:
        print(f"    ! no bibtex from crossref: {e}")
        bibtex = ""

    url = data.get("URL") or f"https://doi.org/{doi}"

    return {
        "title": title,
        "authors": authors,
        "venue": venue,
        "year": year,
        "url": url,
        "bibtex": _LiteralStr(bibtex) if bibtex else "",
        "doi": doi,
    }


# ---------- ORCID ----------

def extract_dois(orcid_works: dict) -> list[str]:
    """Return DOIs in the order ORCID returned them."""
    dois: list[str] = []
    seen: set[str] = set()
    for group in orcid_works.get("group", []):
        for ws in group.get("work-summary", []):
            ext_ids = ((ws.get("external-ids") or {}).get("external-id")) or []
            for ext in ext_ids:
                if (ext.get("external-id-type") or "").lower() == "doi":
                    doi = (ext.get("external-id-value") or "").strip().lower()
                    if doi and doi not in seen:
                        seen.add(doi)
                        dois.append(doi)
                    break
            else:
                continue
            break
    return dois


# ---------- Main ----------

def apply_override(entry: dict, override: dict) -> dict:
    for k, v in override.items():
        if k == "doi":
            continue
        if v is not None:
            entry[k] = v
    return entry


def main() -> int:
    print(f"Fetching ORCID works for {ORCID} …")
    try:
        works = fetch_json(f"https://pub.orcid.org/v3.0/{ORCID}/works")
    except (HTTPError, URLError) as e:
        print(f"! ORCID fetch failed: {e}")
        return 1
    dois = extract_dois(works)
    print(f"  found {len(dois)} DOI-bearing works")

    overrides = load_overrides()
    if overrides:
        print(f"  {len(overrides)} override(s) loaded")

    entries: list[dict] = []
    for doi in dois:
        print(f"  crossref: {doi}")
        try:
            entry = entry_from_crossref(doi)
        except (HTTPError, URLError) as e:
            print(f"    ! {e} — skipping")
            continue
        ov = overrides.get(doi)
        if ov:
            entry = apply_override(entry, ov)
        entries.append(entry)
        time.sleep(0.2)  # be polite to Crossref

    # Also surface override-only entries (e.g. things not on ORCID yet)
    seen = {e["doi"] for e in entries if e.get("doi")}
    for doi, ov in overrides.items():
        if doi in seen:
            continue
        if not ov.get("title"):
            continue
        bib = ov.get("bibtex", "")
        entries.append({
            "title": ov.get("title", ""),
            "authors": ov.get("authors", ""),
            "venue": ov.get("venue", ""),
            "year": ov.get("year"),
            "url": ov.get("url", f"https://doi.org/{doi}"),
            "bibtex": _LiteralStr(bib) if bib else "",
            "doi": doi,
        })

    # Sort newest first
    entries.sort(key=lambda e: (e.get("year") or 0), reverse=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# Auto-generated from ORCID + Crossref. Do not hand-edit.\n"
        "# Source: scripts/fetch_publications.py\n"
        "# Overrides: _data/publications.overrides.yml (per-DOI).\n"
        "# The live file consumed by the site is _data/publications.yml.\n"
        "# This file is a preview — promote by copying into publications.yml.\n"
    )
    with OUT.open("w") as f:
        f.write(header)
        # yaml.dump (not safe_dump) so our _LiteralStr representer is applied
        yaml.dump(
            entries,
            f,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
            default_flow_style=False,
        )
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
