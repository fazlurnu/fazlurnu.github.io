# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# CLAUDE.md — 4-rule

These rules apply to every task in this project unless explicitly overridden.
Bias: caution over speed on non-trivial work. Use judgment on trivial tasks.

## Rule 1 — Think Before Coding
State assumptions explicitly. If uncertain, ask rather than guess.
Present multiple interpretations when ambiguity exists.
Push back when a simpler approach exists.
Stop when confused. Name what's unclear.

## Rule 2 — Simplicity First
Minimum code that solves the problem. Nothing speculative.
No features beyond what was asked. No abstractions for single-use code.
Test: would a senior engineer say this is overcomplicated? If yes, simplify.

## Rule 3 — Surgical Changes
Touch only what you must. Clean up only your own mess.
Don't "improve" adjacent code, comments, or formatting.
Don't refactor what isn't broken. Match existing style.

## Rule 4 — Goal-Driven Execution
Define success criteria. Loop until verified.
Don't follow steps. Define success and iterate.
Strong success criteria let you loop independently.

## What this is

Personal academic website for Muhammad Fazlur Rahman, built with Jekyll 4. Deployed via GitHub Pages. The site has three main sections: About (`index.html`), Research (`research.html`), and Blog (`blog.html`).

## Local development

**Preferred: Docker (no Ruby install required)**
```bash
docker compose up blog
# Site served at http://localhost:4000 with live reload
```

The `_site/` directory is the build output — never edit it directly.

## Adding a blog post

Create a Markdown file in `_posts/` (or a subdirectory) named `YYYY-MM-DD-slug.md` with this front matter:

```yaml
---
title: "Post Title"
date: YYYY-MM-DD
tags: [tag1, tag2]
excerpt: "One-sentence summary."
---
```

Posts automatically get the `post` layout (configured in `_config.yml` defaults). Tags appear in the tag-filter UI on `/blog/` automatically.

**Interactive widgets**: embed a widget by adding `{% include widget_name.html %}` in the post body. Widgets live in `_includes/`. MathJax is available via `{% include mathjax.html %}` (already included in the `post` layout).

## Layouts and includes

- `_layouts/default.html` — wraps every page: nav, social icons, BibTeX toggle/copy JS, blog tag-filter JS, chess.com live rating fetch
- `_layouts/post.html` — thin wrapper adding post header (date, tags, title) and MathJax; delegates body to `default.html`
- `_includes/mathjax.html` — loads MathJax for LaTeX math in posts
- `_includes/icon.html` — SVG icon helper used in nav social links
- `_includes/*_widget.html` — self-contained interactive widgets (vanilla JS + HTML) embedded in blog posts

## CSS

All styles are in `style.css` at the root. There is no build step for CSS — it is served directly. No CSS framework is used.

## Adding an interactive Python widget (pywidget)

Widgets run Python in the browser via **Pyodide** (no server). Each widget is a single self-contained `_includes/my_widget.html` file with three sections: HTML structure, scoped `<style>`, and a `<script type="module">`.

**Structure to copy exactly** (see `_includes/gaussian_widget.html` as the canonical example):

```html
<div class="py-widget">
  <!-- 1. Header bar -->
  <div class="py-widget-header">
    <span class="py-widget-lang">Python · Interactive</span>
    <span class="py-widget-status" id="pywidget-status">Loading runtime…</span>
  </div>

  <!-- 2. Controls (sliders, selects, etc.) — start disabled, enabled after load -->
  <div class="py-widget-controls">
    <div class="py-slider-row">
      <label for="my-slider">Label</label>
      <input type="range" id="my-slider" min="0" max="10" step="0.1" value="5" disabled>
      <output id="my-val">5.0</output>
    </div>
  </div>

  <!-- 3. Plot area -->
  <div class="py-widget-plot">
    <div id="pywidget-loading-msg">
      <div class="py-spinner"></div>
      <span>Loading Python (~10 s on first visit, cached after)</span>
    </div>
    <img id="my-img" alt="Plot description" style="display:none;width:100%;border-radius:8px;">
  </div>
</div>
```

**Style**: copy the `.py-widget`, `.py-widget-header`, `.py-widget-controls`, `.py-slider-row`, `.py-widget-plot`, `#pywidget-loading-msg`, `.py-spinner` CSS blocks verbatim from `gaussian_widget.html`. Use the same CSS variables (`--line`, `--accent`, `--accent-soft`, `--muted`, `--radius`, `--text`). Do not introduce new classes.

**Script pattern**:

```js
<script type="module">
import { loadPyodide } from "https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.mjs";

// 1. Get DOM refs
const statusEl  = document.getElementById("pywidget-status");
const loadingEl = document.getElementById("pywidget-loading-msg");
const imgEl     = document.getElementById("my-img");
const mySlider  = document.getElementById("my-slider");
const myOut     = document.getElementById("my-val");

// 2. Load Pyodide + packages
const pyodide = await loadPyodide();
await pyodide.loadPackage(["numpy", "matplotlib"]); // add scipy etc. as needed

// 3. Define render function in Python (use matplotlib Agg backend, return base64 PNG)
await pyodide.runPythonAsync(`
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, io, base64

def render(param):
    fig, ax = plt.subplots(figsize=(7, 3.2))
    # ... your plot code ...
    fig.patch.set_facecolor("white")
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=130, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()
`);

// 4. Enable controls, hide spinner
statusEl.textContent   = "Ready";
mySlider.disabled      = false;
loadingEl.style.display = "none";
imgEl.style.display    = "block";

// 5. Update on input with debounce (130 ms)
async function update() {
  const b64 = await pyodide.runPythonAsync(`render(${parseFloat(mySlider.value)})`);
  imgEl.src = "data:image/png;base64," + b64;
}

await update(); // initial render

let timer;
mySlider.addEventListener("input", () => {
  myOut.value = parseFloat(mySlider.value).toFixed(1);
  clearTimeout(timer);
  timer = setTimeout(update, 130);
});
</script>
```

**Rules**:
- One `<img>` element per widget; swap its `src` with the base64 PNG on each render.
- Always call `plt.close(fig)` to avoid memory leaks.
- Use `figsize=(7, 3.2)` and `dpi=130` for consistent sizing.
- Plot colors: primary line `#1a73e8`, fill `alpha=0.12`, reference lines `tomato` (dashed) and `#aaa` (dotted).
- Embed the widget in a post with `{% include my_widget.html %}`.
- Each widget file is standalone — no shared JS modules or external CSS.
