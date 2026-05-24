"""Build the lightweight FTC/YES robotics course static site.

Markdown remains the source of truth. This script converts selected Markdown
documents into browseable HTML pages under site/generated/ and regenerates the
main site navigation pages.
"""

from __future__ import annotations

import argparse
import html
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
GENERATED = SITE / "generated"
CSS = SITE / "assets" / "css" / "styles.css"


@dataclass(frozen=True)
class Page:
    source: Path
    output: Path
    title: str
    section: str


def title_from_markdown(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("_", " ").title()


def collect_pages() -> list[Page]:
    patterns = [
        ("02_student_materials/readings/*.md", "student/readings", "Student Readings"),
        ("02_student_materials/guides/*.md", "student/guides", "Student Guides"),
        ("02_student_materials/code_examples/**/*.md", "student/code_examples", "Code Examples"),
        (
            "02_student_materials/engineering_notebook/*.md",
            "student/engineering_notebook",
            "Engineering Notebook",
        ),
        ("02_student_materials/decision_menus/*.md", "student/decision_menus", "Decision Menus"),
        ("02_student_materials/sld_prompts/*.md", "student/sld_prompts", "SLD Prompts"),
        (
            "02_student_materials/challenge_by_choice/*.md",
            "student/challenge_by_choice",
            "Challenge by Choice",
        ),
        ("docs/sessions/*.md", "sessions", "Sessions"),
        ("00_course_map/*.md", "course_map", "Course Maps"),
        ("03_teacher_materials/**/*.md", "teacher/teacher_materials", "Teacher Materials"),
        ("docs/*.md", "teacher/docs", "Teacher Docs"),
        ("docs/impact_study/*.md", "teacher/impact_study", "Impact Study"),
        ("90_templates/*.md", "templates", "Templates"),
    ]

    pages: list[Page] = []
    seen: set[Path] = set()
    for pattern, out_dir, section in patterns:
        for source in sorted(ROOT.glob(pattern)):
            if source in seen:
                continue
            seen.add(source)
            relative_source = source.relative_to(ROOT)
            output = GENERATED / out_dir / relative_source.with_suffix(".html").name
            pages.append(Page(source=source, output=output, title=title_from_markdown(source), section=section))
    return pages


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return slug or "section"


def convert_inline(text: str, current_page: Page, source_map: dict[Path, Path]) -> str:
    escaped = html.escape(text)

    def replace_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = html.unescape(match.group(2))
        if target.startswith(("http://", "https://", "mailto:")) or target.startswith("#"):
            href = target
        else:
            base_target, fragment = (target.split("#", 1) + [""])[:2] if "#" in target else (target, "")
            source_target = (current_page.source.parent / base_target).resolve()
            if source_target.suffix.lower() == ".md" and source_target in source_map:
                href_path = os.path.relpath(source_map[source_target], current_page.output.parent)
                href = href_path.replace(os.sep, "/")
                if fragment:
                    href += f"#{fragment}"
            else:
                href_path = os.path.relpath(source_target, current_page.output.parent)
                href = href_path.replace(os.sep, "/")
                if fragment:
                    href += f"#{fragment}"
        return f'<a href="{html.escape(href, quote=True)}">{label}</a>'

    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def flush_paragraph(lines: list[str], output: list[str], current_page: Page, source_map: dict[Path, Path]) -> None:
    if lines:
        output.append(f"<p>{convert_inline(' '.join(lines), current_page, source_map)}</p>")
        lines.clear()


def flush_list(items: list[str], output: list[str], current_page: Page, source_map: dict[Path, Path]) -> None:
    if items:
        output.append("<ul>")
        for item in items:
            output.append(f"<li>{convert_inline(item, current_page, source_map)}</li>")
        output.append("</ul>")
        items.clear()


def render_table(rows: list[str], current_page: Page, source_map: dict[Path, Path]) -> str:
    parsed = [[cell.strip() for cell in row.strip().strip("|").split("|")] for row in rows]
    if len(parsed) >= 2 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in parsed[1]):
        header = parsed[0]
        body = parsed[2:]
    else:
        header = []
        body = parsed

    out = ["<div class=\"table-wrap\"><table>"]
    if header:
        out.append("<thead><tr>")
        for cell in header:
            out.append(f"<th>{convert_inline(cell, current_page, source_map)}</th>")
        out.append("</tr></thead>")
    out.append("<tbody>")
    for row in body:
        out.append("<tr>")
        for cell in row:
            out.append(f"<td>{convert_inline(cell, current_page, source_map)}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def markdown_to_html(markdown: str, current_page: Page, source_map: dict[Path, Path]) -> str:
    output: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    table_rows: list[str] = []
    in_code = False
    code_lines: list[str] = []

    def flush_table() -> None:
        nonlocal table_rows
        if table_rows:
            output.append(render_table(table_rows, current_page, source_map))
            table_rows = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            flush_paragraph(paragraph, output, current_page, source_map)
            flush_list(list_items, output, current_page, source_map)
            flush_table()
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(raw_line)
            continue

        if not line.strip():
            flush_paragraph(paragraph, output, current_page, source_map)
            flush_list(list_items, output, current_page, source_map)
            flush_table()
            continue

        if line.startswith("|") and line.endswith("|"):
            flush_paragraph(paragraph, output, current_page, source_map)
            flush_list(list_items, output, current_page, source_map)
            table_rows.append(line)
            continue
        flush_table()

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush_paragraph(paragraph, output, current_page, source_map)
            flush_list(list_items, output, current_page, source_map)
            level = len(heading.group(1))
            text = heading.group(2).strip()
            anchor = slugify(text)
            output.append(f'<h{level} id="{anchor}">{convert_inline(text, current_page, source_map)}</h{level}>')
            continue

        bullet = re.match(r"^[-*]\s+(.*)$", line)
        if bullet:
            flush_paragraph(paragraph, output, current_page, source_map)
            list_items.append(bullet.group(1).strip())
            continue

        if line.startswith(">"):
            flush_paragraph(paragraph, output, current_page, source_map)
            flush_list(list_items, output, current_page, source_map)
            quote = line.lstrip(">").strip()
            output.append(f"<blockquote>{convert_inline(quote, current_page, source_map)}</blockquote>")
            continue

        paragraph.append(line.strip())

    flush_paragraph(paragraph, output, current_page, source_map)
    flush_list(list_items, output, current_page, source_map)
    flush_table()
    if in_code:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(output)


def site_nav(prefix: str = "") -> str:
    return f"""
      <nav class="nav" aria-label="Main navigation">
        <a href="{prefix}index.html">Home</a>
        <a href="{prefix}students/index.html">Students</a>
        <a href="{prefix}teachers/index.html">Teachers</a>
        <a href="{prefix}sessions/index.html">Sessions</a>
        <a href="{prefix}materials/index.html">Materials</a>
      </nav>
    """


def html_shell(title: str, body: str, css_href: str, nav_prefix: str = "", intro: str | None = None) -> str:
    intro_html = f"<p>{html.escape(intro)}</p>" if intro else ""
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)} | FTC/YES Robotics Course</title>
    <link rel="stylesheet" href="{css_href}">
  </head>
  <body>
    <header class="site-header">
      <h1>{html.escape(title)}</h1>
      {intro_html}
      {site_nav(nav_prefix)}
    </header>
    <main>
{body}
    </main>
  </body>
</html>
"""


def write_document_page(page: Page, source_map: dict[Path, Path]) -> None:
    source_text = page.source.read_text(encoding="utf-8")
    article = markdown_to_html(source_text, page, source_map)
    source_href = os.path.relpath(page.source, page.output.parent).replace(os.sep, "/")
    home_href = os.path.relpath(SITE / "index.html", page.output.parent).replace(os.sep, "/")
    body = f"""
      <article class="document">
        <p class="breadcrumb"><a href="{home_href}">Back to site home</a> | <a href="{source_href}">View source Markdown</a></p>
        {article}
      </article>
"""
    css_href = os.path.relpath(CSS, page.output.parent).replace(os.sep, "/")
    nav_prefix = os.path.relpath(SITE, page.output.parent).replace(os.sep, "/") + "/"
    page.output.parent.mkdir(parents=True, exist_ok=True)
    page.output.write_text(html_shell(page.title, body, css_href, nav_prefix), encoding="utf-8")


def link_for(page: Page, from_dir: Path) -> str:
    return os.path.relpath(page.output, from_dir).replace(os.sep, "/")


def list_items(pages: Iterable[Page], from_dir: Path) -> str:
    return "\n".join(
        f'          <li><a href="{link_for(page, from_dir)}">{html.escape(page.title)}</a></li>'
        for page in sorted(pages, key=lambda p: (p.section, p.source.name))
    )


def page_by_source(pages: list[Page], source: str) -> Page:
    target = (ROOT / source).resolve()
    for page in pages:
        if page.source.resolve() == target:
            return page
    raise KeyError(source)


def section_pages(pages: list[Page], section: str) -> list[Page]:
    return [page for page in pages if page.section == section]


def write_static_pages(pages: list[Page]) -> None:
    SITE.mkdir(exist_ok=True)
    (SITE / "students").mkdir(parents=True, exist_ok=True)
    (SITE / "teachers").mkdir(parents=True, exist_ok=True)
    (SITE / "sessions").mkdir(parents=True, exist_ok=True)
    (SITE / "materials").mkdir(parents=True, exist_ok=True)
    CSS.parent.mkdir(parents=True, exist_ok=True)

    CSS.write_text(STYLES, encoding="utf-8")

    home_body = """
      <section class="intro">
        <p>This Phase 2 site converts selected Markdown source files into browseable HTML pages. Markdown remains the editable source of truth; generated pages live under <code>site/generated/</code>.</p>
      </section>
      <section class="grid" aria-label="Course entry points">
        <article class="card"><span class="tag">Student-facing</span><h2><a href="students/index.html">Students</a></h2><p>Readings, reusable guides, decision menus, engineering notebook materials, and Challenge by Choice pathways.</p></article>
        <article class="card"><span class="tag">Teacher-facing</span><h2><a href="teachers/index.html">Teachers</a></h2><p>Course overviews, session plans, planning docs, impact-study materials, and teacher guides.</p></article>
        <article class="card"><span class="tag">10 days / 20 sessions</span><h2><a href="sessions/index.html">Sessions</a></h2><p>The pre-course page and all 20 teacher-facing session lesson plans.</p></article>
        <article class="card"><span class="tag">All materials</span><h2><a href="materials/index.html">Materials</a></h2><p>A category-based index for generated HTML pages and source materials.</p></article>
      </section>
"""
    (SITE / "index.html").write_text(
        html_shell(
            "FTC/YES Two-Week Robotics Course",
            home_body,
            "assets/css/styles.css",
            "",
            "A public navigation and preview site for an introductory FTC-style robotics course.",
        ),
        encoding="utf-8",
    )

    student_sources = [
        "02_student_materials/guides/what_should_i_be_doing_right_now_robotics_work_ahead_menu.md",
        "02_student_materials/guides/robotics_design_build_revise_process_handout.md",
        "02_student_materials/guides/subsystem_design_cycle_guide.md",
        "02_student_materials/guides/robot_troubleshooting_checklist.md",
        "02_student_materials/engineering_notebook/student_engineering_notebook_master.md",
        "02_student_materials/readings/day1_session1_what_is_first.md",
        "02_student_materials/readings/day1_session1_what_is_first_tech_challenge.md",
        "02_student_materials/readings/future_human_controller_mapping_background.md",
    ]
    student_body = f"""
      <section class="section"><h2>Start Here</h2><ul class="link-list">
{list_items([page_by_source(pages, source) for source in student_sources], SITE / "students")}
      </ul></section>
      <section class="section"><h2>All Student Readings</h2><ul class="link-list">
{list_items(section_pages(pages, "Student Readings"), SITE / "students")}
      </ul></section>
      <section class="section"><h2>Decision Menus and Challenge Pathways</h2><ul class="link-list">
{list_items(section_pages(pages, "Decision Menus") + section_pages(pages, "Challenge by Choice"), SITE / "students")}
      </ul></section>
      <section class="section"><h2>Code Examples</h2><ul class="link-list">
{list_items(section_pages(pages, "Code Examples"), SITE / "students")}
      </ul></section>
      <section class="section"><h2>Student Templates</h2><ul class="link-list">
{list_items(section_pages(pages, "Templates"), SITE / "students")}
      </ul></section>
"""
    (SITE / "students" / "index.html").write_text(
        html_shell("Student Materials", student_body, "../assets/css/styles.css", "../"),
        encoding="utf-8",
    )

    teacher_sources = [
        "docs/teacher_facing_robotics_course_overview.md",
        "docs/teacher_facing_robotics_course_lesson_plan.md",
        "docs/coteacher_weekend_review_packet.md",
        "00_course_map/20_session_scope_sequence.md",
        "00_course_map/course_overview.md",
        "docs/course_content_inventory.md",
    ]
    teacher_body = f"""
      <section class="section"><h2>Main Teacher Documents</h2><ul class="link-list">
{list_items([page_by_source(pages, source) for source in teacher_sources], SITE / "teachers")}
      </ul></section>
      <section class="section"><h2>Teacher Guides, Templates, and Impact Study</h2><ul class="link-list">
{list_items(section_pages(pages, "Teacher Materials") + section_pages(pages, "Templates") + section_pages(pages, "Impact Study"), SITE / "teachers")}
      </ul></section>
"""
    (SITE / "teachers" / "index.html").write_text(
        html_shell("Teacher Materials", teacher_body, "../assets/css/styles.css", "../"),
        encoding="utf-8",
    )

    session_body = f"""
      <section class="section"><h2>Course Maps</h2><ul class="link-list">
{list_items(section_pages(pages, "Course Maps"), SITE / "sessions")}
      </ul></section>
      <section class="section"><h2>Session Lesson Plans</h2><ul class="link-list">
{list_items(section_pages(pages, "Sessions"), SITE / "sessions")}
      </ul></section>
"""
    (SITE / "sessions" / "index.html").write_text(
        html_shell("Sessions", session_body, "../assets/css/styles.css", "../"),
        encoding="utf-8",
    )

    sections = [
        "Student Guides",
        "Student Readings",
        "Engineering Notebook",
        "Decision Menus",
        "Code Examples",
        "SLD Prompts",
        "Challenge by Choice",
        "Sessions",
        "Course Maps",
        "Teacher Materials",
        "Teacher Docs",
        "Impact Study",
        "Templates",
    ]
    materials_parts = []
    for section in sections:
        section_list = section_pages(pages, section)
        if section_list:
            materials_parts.append(
                f'<section class="section" id="{slugify(section)}"><h2>{html.escape(section)}</h2><ul class="link-list">\n'
                + list_items(section_list, SITE / "materials")
                + "\n      </ul></section>"
            )
    (SITE / "materials" / "index.html").write_text(
        html_shell("Materials Index", "\n".join(materials_parts), "../assets/css/styles.css", "../"),
        encoding="utf-8",
    )

    (SITE / "README.md").write_text(SITE_README, encoding="utf-8")


def check_links() -> list[tuple[Path, str, Path]]:
    missing: list[tuple[Path, str, Path]] = []
    for html_file in SITE.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = href.split("#", 1)[0]
            if not path_part:
                continue
            target = (html_file.parent / path_part).resolve()
            if href.endswith("/"):
                exists = (target / "index.html").exists()
            else:
                exists = target.exists()
            if not exists:
                missing.append((html_file.relative_to(ROOT), href, target))
    return missing


def build() -> None:
    pages = collect_pages()
    if GENERATED.exists():
        for old_html in GENERATED.rglob("*.html"):
            old_html.unlink()
    source_map = {page.source.resolve(): page.output for page in pages}
    for page in pages:
        write_document_page(page, source_map)
    write_static_pages(pages)


STYLES = """:root {
  --bg: #f7f8fb;
  --panel: #ffffff;
  --text: #1c2430;
  --muted: #5c6675;
  --line: #d9dee8;
  --accent: #1768ac;
  --accent-dark: #0f4f86;
  --soft: #eaf3fb;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text); font-family: Arial, Helvetica, sans-serif; line-height: 1.5; }
a { color: var(--accent); text-decoration: none; }
a:hover, a:focus { color: var(--accent-dark); text-decoration: underline; }
.site-header { background: #1d2735; color: #ffffff; padding: 28px 20px; }
.site-header h1 { margin: 0 0 8px; font-size: 2rem; }
.site-header p { margin: 0; max-width: 820px; color: #d8e0ea; }
.nav { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }
.nav a { color: #ffffff; border: 1px solid rgba(255, 255, 255, 0.35); border-radius: 6px; padding: 7px 11px; }
.nav a:hover, .nav a:focus { background: rgba(255, 255, 255, 0.12); text-decoration: none; }
main { max-width: 1120px; margin: 0 auto; padding: 28px 20px 44px; }
.intro { max-width: 860px; margin-bottom: 24px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; }
.card, .section, .document { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 18px; }
.card h2, .section h2 { margin-top: 0; font-size: 1.25rem; }
.card p, .section p { color: var(--muted); }
.section { margin-bottom: 18px; }
.link-list { padding-left: 1.1rem; }
.link-list li { margin: 7px 0; }
.tag { display: inline-block; background: var(--soft); color: var(--accent-dark); border-radius: 999px; padding: 3px 8px; font-size: 0.85rem; font-weight: 700; }
.breadcrumb { border-left: 4px solid var(--accent); background: var(--soft); padding: 10px 12px; }
.document h1, .document h2, .document h3 { line-height: 1.2; }
.document h1 { font-size: 2rem; }
.document h2 { border-top: 1px solid var(--line); margin-top: 1.7rem; padding-top: 1rem; }
blockquote { border-left: 4px solid var(--line); margin-left: 0; padding: 0.2rem 1rem; color: var(--muted); }
pre { background: #111827; color: #f8fafc; overflow-x: auto; padding: 14px; border-radius: 6px; }
code { font-family: Consolas, Monaco, monospace; }
:not(pre) > code { background: #eef2f7; padding: 2px 4px; border-radius: 4px; }
.table-wrap { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
th, td { border: 1px solid var(--line); padding: 8px; text-align: left; vertical-align: top; }
th { background: var(--soft); }
"""


SITE_README = """# Static Course Site

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

Each generated page includes a `View source Markdown` link.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static course site.")
    parser.add_argument("--check-links", action="store_true", help="Check local href targets after building.")
    args = parser.parse_args()
    build()
    print(f"Built {SITE.relative_to(ROOT)}")
    if args.check_links:
        missing = check_links()
        if missing:
            for source, href, target in missing:
                print(f"Missing: {source} -> {href} ({target})")
            raise SystemExit(1)
        print("All local site links resolve.")


if __name__ == "__main__":
    main()
