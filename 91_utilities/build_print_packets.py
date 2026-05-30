"""Build browser-printable student worksheet packets.

Markdown remains the source of truth. This script renders selected student-facing
Markdown files into print-friendly HTML under site/print/.
"""

from __future__ import annotations

import html
import os
from pathlib import Path

from build_static_site import ROOT, SITE, Page, collect_pages, markdown_to_html, title_from_markdown


PRINT_DIR = SITE / "print"
PRINT_CSS = SITE / "assets" / "css" / "print.css"


PACKET_SOURCES = [
    (
        "Student-Led Discussion Tally Sheet",
        "90_templates/student_led_discussion_tally_sheet_template.md",
        "Use during short team design discussions.",
    ),
    (
        "Demo Robot Design Analysis Activity",
        "02_student_materials/activities/demo_robot_design_analysis/demo_robot_design_analysis_activity.md",
        "Use during early paired rotations to operate, observe, and analyze multiple demo robots.",
    ),
    (
        "Demo Robot Design Observation Activity",
        "02_student_materials/activities/demo_robot_design_analysis/demo_robot_design_observation_activity.md",
        "Use while observing, sketching, photographing, and evaluating demo robot design choices.",
    ),
    (
        "Team Strategy Guide",
        "90_templates/team_strategy_guide_template.md",
        "Use after team norms and modified game-rule understanding.",
    ),
    (
        "Robot Behavior Specification",
        "90_templates/robot_behavior_specification_template.md",
        "Use to turn strategy into robot behavior goals and performance targets.",
    ),
    (
        "Subsystem Design Cycle Template",
        "90_templates/subsystem_design_cycle_template.md",
        "Use once for each major subsystem.",
    ),
    (
        "Controller Mapping Drive Comparison Activity",
        "02_student_materials/activities/controller_mapping_drive_comparison/controller_mapping_drive_comparison_activity.md",
        "Use after teams can run the D-pad and joystick drive demos.",
    ),
]

# Manual printables, such as
# 02_student_materials/activities/demo_robot_design_analysis/demo_robot_design_analysis.pdf,
# are maintained separately and should not be overwritten by this generated HTML packet.


def rel_href(target: Path, from_dir: Path) -> str:
    return os.path.relpath(target, from_dir).replace(os.sep, "/")


def shell(title: str, body: str, css_prefix: str = "../") -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)} | FTC/YES Robotics Course</title>
    <link rel="stylesheet" href="{css_prefix}assets/css/styles.css">
    <link rel="stylesheet" href="{css_prefix}assets/css/print.css">
  </head>
  <body class="print-page">
    <header class="print-header no-print">
      <h1>{html.escape(title)}</h1>
      <p>Print-friendly student materials. Source Markdown remains the source of truth.</p>
      <nav class="print-nav" aria-label="Print navigation">
        <a href="../index.html">Site Home</a>
        <a href="index.html">Print Index</a>
      </nav>
    </header>
    <main class="print-container">
{body}
    </main>
  </body>
</html>
"""


def source_map() -> dict[Path, Path]:
    return {page.source.resolve(): page.output for page in collect_pages()}


def render_source(source: Path, output: Path, mapping: dict[Path, Path]) -> str:
    page = Page(source=source, output=output, title=title_from_markdown(source), section="Print Packet")
    return markdown_to_html(source.read_text(encoding="utf-8"), page, mapping)


def build_packet() -> None:
    PRINT_DIR.mkdir(parents=True, exist_ok=True)
    packet_path = PRINT_DIR / "student_design_decision_packet.html"
    mapping = source_map()
    sections: list[str] = []

    for label, relative_source, note in PACKET_SOURCES:
        source = ROOT / relative_source
        if not source.exists():
            raise FileNotFoundError(f"Missing print packet source: {relative_source}")
        body = render_source(source, packet_path, mapping)
        source_link = rel_href(source, packet_path.parent)
        sections.append(
            f"""
      <section class="worksheet-section">
        <div class="print-source keep-together">
          <strong>{html.escape(label)}</strong><br>
          <span>{html.escape(note)}</span><br>
          <span>Source: <a href="{html.escape(source_link, quote=True)}">{html.escape(relative_source)}</a></span>
        </div>
        <article class="worksheet-content">
{body}
        </article>
      </section>
"""
        )

    packet_body = f"""
      <section class="packet-cover">
        <p class="kicker">Print-Friendly Packet</p>
        <h1>Student Design Decision Packet</h1>
        <p>This packet supports the early design workflow: observe, discuss, choose, build, test, and revise.</p>
        <p>Use browser print or Save as PDF. Check the preview before printing a class set.</p>
        <h2>Included Worksheets</h2>
        <ol>
          {''.join(f'<li>{html.escape(label)}</li>' for label, _, _ in PACKET_SOURCES)}
        </ol>
      </section>
{''.join(sections)}
"""
    packet_path.write_text(shell("Student Design Decision Packet", packet_body), encoding="utf-8")


def build_index() -> None:
    PRINT_DIR.mkdir(parents=True, exist_ok=True)
    index_body = """
      <section class="section">
        <h2>Print-Friendly Student Materials</h2>
        <p>Open a packet page, review the layout in the browser, then print or Save as PDF.</p>
        <ul class="link-list">
          <li><a href="student_design_decision_packet.html">Student Design Decision Packet</a></li>
        </ul>
      </section>
      <section class="section">
        <h2>Classroom Printing Workflow</h2>
        <ol>
          <li>Rebuild the static site and print packet pages.</li>
          <li>Open this print index in a browser.</li>
          <li>Open the packet and use Print Preview.</li>
          <li>Print a test copy or Save as PDF before printing multiple copies.</li>
        </ol>
      </section>
"""
    (PRINT_DIR / "index.html").write_text(shell("Print Packets", index_body), encoding="utf-8")


def main() -> None:
    build_packet()
    build_index()
    print(f"Built {PRINT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
