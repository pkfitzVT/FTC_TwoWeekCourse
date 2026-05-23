# Static Course Site

This folder is a lightweight public navigation layer for the FTC/YES two-week robotics course.

It does not convert the course Markdown files into HTML yet. Instead, the pages in this folder link directly to the existing Markdown source files in the repository.

## How to Preview Locally

Open `site/index.html` in a browser.

If your browser blocks links to local Markdown files, use a simple static server from the repository root, such as:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/site/
```

## What This Folder Contains

- `index.html`: public home page.
- `students/index.html`: student-facing entry point.
- `teachers/index.html`: teacher-facing entry point.
- `sessions/index.html`: session lesson-plan index.
- `materials/index.html`: category-based materials index.
- `assets/css/styles.css`: simple shared styling.

## Adding Future Links

Keep links relative to the page location. Most links from nested site pages use `../../` to reach the repository root.

For example, from `site/students/index.html`:

```html
<a href="../../02_student_materials/readings/example.md">Example Reading</a>
```

## GitHub Pages Readiness

This folder is ready for a basic GitHub Pages-style static host, with one limitation: many links point directly to Markdown files. A later phase can convert selected Markdown files into styled HTML pages.

Suggested future phases:

- Phase 2: Convert selected Markdown files into styled HTML pages.
- Phase 3: Deploy with GitHub Pages.
