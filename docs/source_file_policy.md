# Source File Policy

## Working Rule

Markdown files are the editable source files for course content.

PDF files are generated exports unless otherwise noted. PDFs should be used for printing, sharing, or packet review, but they should not be edited as the primary source of course content.

## Why This Matters

The repository currently contains both Markdown source files and PDF exports in the same root folder. Several PDFs appear to correspond directly to Markdown files, while larger packet PDFs appear to combine multiple Markdown sources.

Without a source policy, it can become unclear whether a PDF or a Markdown file contains the latest version of a handout, menu, or packet.

## Source File Expectations

- Edit Markdown when changing course wording, structure, prompts, menus, decision tables, or notebook deliverables.
- Regenerate PDFs from Markdown after source edits.
- Do not treat PDFs as source files unless a file-specific note says the PDF is original-only.
- Keep generated export filenames clearly connected to their source Markdown files or packet manifests.

## Print Packet Manifests

Future print packets should have a manifest listing:

- packet title,
- intended audience,
- related day/session,
- source Markdown files in packet order,
- export date,
- export method or tool,
- notes about omitted or added pages.

Suggested manifest filename pattern:

```text
packet_name_manifest.md
```

Example:

```text
day2_session4_chassis_design_discussion_packet_manifest.md
```

## Current PDF Interpretation

Until manifests are created, treat current PDFs as generated exports or compiled packets based on filename:

- Individual PDFs with matching Markdown names are likely generated exports.
- Larger packet PDFs are likely compiled print packets.
- Packet source order should be confirmed before re-exporting or distributing.

## Future Organization Recommendation

Keep source Markdown in content folders and generated PDFs in a print/export folder. For now, existing files should remain in place until a deliberate move/rename/archive pass is approved.
