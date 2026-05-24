# Print Packet Workflow

This folder stores generated or exported PDF packets. The editable source of truth should remain in Markdown files under folders such as `02_student_materials/`, `90_templates/`, and `docs/`.

The current print workflow starts with browser-printable HTML under `site/print/`. Review the HTML layout in a browser before exporting to PDF or printing a class set.

## Build and Preview

From the repository root:

```powershell
python 91_utilities/build_static_site.py
python 91_utilities/build_print_packets.py
python 91_utilities/build_static_site.py --check-links
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/site/print/
```

Use the browser print dialog or Save as PDF.

## Current Browser-Printable Packet

- `site/print/student_design_decision_packet.html`

This packet combines early-course student worksheets for discussion, demo robot evaluation, strategy, behavior specification, subsystem design, and controller mapping.

## Manual Review Before Printing

Before classroom printing:

- Check that major worksheet sections start on reasonable pages.
- Check that tables have enough space for handwriting.
- Print one test copy before printing a class set.
- Export to PDF manually only after the browser preview looks acceptable.

Future option: add automated HTML-to-PDF generation after print layout has been reviewed in the browser.
