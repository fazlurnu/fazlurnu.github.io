# Interactive Plot Widget Prompt

Create a Jekyll include file `_includes/NAME_widget.html` for an interactive Python plot embedded in a blog post. Follow these exact conventions used in the project:

## Structure
- Outer `<div class="py-widget">` with header, controls, and plot sections
- Header: `<span class="py-widget-lang">Python · Interactive</span>` + a status span with a unique ID
- Sliders use class `py-slider-row` with a `<label>`, `<input type="range">`, and `<output>`
- Plot area uses class `py-widget-plot` with a loading message div (spinner + text) and an `<img>` tag
- All element IDs must be unique (prefix with a short widget name, e.g. `gp-`)

## Styling
- No `<style>` block needed for `.py-widget`, `.py-widget-header`, `.py-slider-row`, `.py-widget-plot`, `.py-spinner` — those are already defined in `gaussian_widget.html`. Only add a `<style>` block for widget-specific classes.
- Colors: primary `#1a73e8`, secondary `tomato`, tertiary `#34a853`, fills at `alpha=0.10–0.15`

## JavaScript / Pyodide
- Load via `import { loadPyodide } from "https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.mjs"` inside `<script type="module">`
- Load packages: `await pyodide.loadPackage(["numpy", "matplotlib"])`
- Define a single Python `render(...)` function that returns a base64 PNG string
- Use `matplotlib.use("Agg")`, `fig.patch.set_facecolor("white")`, `bbox_inches="tight"`, `dpi=130`
- After loading: enable sliders, hide loading message, show img, call `render()` once
- Debounce slider input with `setTimeout(..., 130)`

## Button controls (use instead of sliders when the widget is sample-driven)
- Wrap buttons in a `<div class="py-btn-row">` (replaces `.py-widget-controls`)
- Use `<button class="py-widget-btn" disabled>Label</button>` for primary actions
- Use `class="py-widget-btn py-widget-btn-danger"` for destructive actions (e.g. Reset)
- Add `<span class="cd-count">0 samples</span>` (or widget-prefixed equivalent) at the end of the row for a live sample counter
- Disable all buttons during async Pyodide calls; re-enable after render completes
- Required CSS (add to the widget's `<style>` block):
```css
.py-btn-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--line);
  flex-wrap: wrap;
}
.py-widget-btn {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 12px;
  font-weight: 600;
  padding: 5px 14px;
  border-radius: 6px;
  border: 1.5px solid var(--accent);
  background: transparent;
  color: var(--accent);
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
  line-height: 1.4;
}
.py-widget-btn:hover:not(:disabled) { background: var(--accent); color: #fff; }
.py-widget-btn:disabled { border-color: var(--line); color: var(--muted); cursor: not-allowed; }
.py-widget-btn-danger { border-color: tomato; color: tomato; }
.py-widget-btn-danger:hover:not(:disabled) { background: tomato; color: #fff; }
.py-widget-btn-danger:disabled { border-color: var(--line); color: var(--muted); }
```
