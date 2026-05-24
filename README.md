# FTC/YES Two-Week Robotics Course

This repository contains Markdown source materials for a two-week introductory FTC-style robotics course.

## Public Preview Site

The browseable static site starts at:

- [`site/index.html`](site/index.html)

To preview locally from the repository root:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/site/
```

## Rebuild Generated HTML

Markdown files are the editable source of truth. Generated HTML pages live under `site/generated/`.

After editing Markdown, rebuild the site with:

```powershell
python 91_utilities/build_static_site.py --check-links
```

## Main Documentation

- [`docs/README.md`](docs/README.md): documentation index.
- [`docs/teacher_facing_robotics_course_overview.md`](docs/teacher_facing_robotics_course_overview.md): teacher-facing course overview and session index.
- [`00_course_map/20_session_scope_sequence.md`](00_course_map/20_session_scope_sequence.md): 20-session course map.
