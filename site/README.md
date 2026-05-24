# Static Course Site

This folder contains the generated static navigation site for the FTC/YES two-week robotics course.

Markdown remains the source of truth. Generated HTML files are written under `site/generated/`.

## Preview Locally

From the repository root, run:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/site/
```

## Rebuild the Site

Edit Markdown source files, then run:

```powershell
python 91_utilities/build_static_site.py
```

The script rebuilds:

- `site/index.html`
- `site/students/index.html`
- `site/teachers/index.html`
- `site/sessions/index.html`
- `site/materials/index.html`
- `site/generated/`
- `site/assets/css/styles.css`

## Source and Generated Files

Source files live in folders such as:

- `00_course_map/`
- `02_student_materials/`
- `03_teacher_materials/`
- `90_templates/`
- `docs/`
- `docs/sessions/`

Generated HTML pages live in:

- `site/generated/`
- `site/print/`

Each generated page includes a `View source Markdown` link.

## Build Print-Friendly Pages

Print-friendly worksheet pages are generated separately so the Markdown source files remain the source of truth.

```powershell
python 91_utilities/build_static_site.py
python 91_utilities/build_print_packets.py
python 91_utilities/build_static_site.py --check-links
```

Then preview:

```text
http://localhost:8000/site/print/
```

Use the browser print dialog or Save as PDF after checking the layout.
