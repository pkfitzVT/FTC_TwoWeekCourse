# YES FTC Two-Week Robotics Course: Teacher Overview

## Course Purpose

This is a 10-day, 20-session modified FIRST Tech Challenge robotics course. Students build, program, test, document, and present a working FTC-style robot in two weeks.

The course is not only a build sprint. It is structured so students practice engineering decisions, teamwork, evidence collection, safety, repair, communication, and reflection. The current repo is strongest in early course culture, student-led discussion, decision menus, first programming readings, and chassis/strategy planning.

## What Students Will Build

Students will build a working FTC-style robot that can move, respond to driver controls, perform at least a simple game-related function, collect test evidence, and be explained in a final presentation.

The planned robot arc includes drivetrain/chassis, wiring/electronics placement, TeleOp driving, controller functions, mechanism work, autonomous or scripted behavior, inspection, practice challenge evidence, and a final demonstration.

## Daily Course Arc

| Day | Sessions | Main arc |
|---:|---|---|
| 1 | 1-2 | Course entry, FIRST/FTC culture, safety, borrowed equipment, student goals, collaborative teams |
| 2 | 3-4 | Team identity, team norms, game strategy, first programming session |
| 3 | 5-6 | Chassis design planning, build start, build continuation, readiness for powered testing |
| 4 | 7-8 | Controller mapping, first TeleOp, drivetrain testing |
| 5 | 9-10 | Strategy check, mechanism planning, robot improvement sprint |
| 6 | 11-12 | Testing methods, data collection, iteration from evidence |
| 7 | 13-14 | Autonomous/scripted behavior, driver practice, reliability tuning |
| 8 | 15-16 | Portfolio documentation, final robot improvements, final test round |
| 9 | 17-18 | Practice challenge evidence, presentation planning |
| 10 | 19-20 | Presentation rehearsal, final demo, final reflection |

## Repeating Session Rhythm

Most sessions should follow this pattern:

background -> design/strategy menu -> student-led discussion -> team decision -> build/program/test -> notebook evidence/reflection

This rhythm keeps the course from becoming random tinkering. Students read or review enough background to make an informed choice, use a menu to compare options, discuss trade-offs, make a team decision, then build/program/test with evidence. The notebook is where the team proves what it chose, what happened, and what changed.

## Teacher Role

The teacher role is to protect safety, time, materials, and learning quality.

Practically, that means:

- Set up materials, tools, batteries, controllers, and field/test spaces.
- Keep students using documented decisions instead of grabbing parts randomly.
- Ask teams for evidence before they make major changes.
- Keep builds scoped to what can be tested in two weeks.
- Watch for unequal participation and help quieter students enter the work.
- Enforce borrowed-equipment expectations and cleanup routines.
- Help teams simplify when complexity threatens a working robot.

## Student Agency Structure

Students are expected to make real choices. The course scaffolds those choices through menus, discussion prompts, decision tables, and notebook evidence.

Students should not simply follow a single teacher-built robot plan. They should choose team identity, norms, chassis priorities, materials, wheels, motor placement, electronics placement, strategy, controls, mechanism scope, test priorities, and presentation story. Teacher guidance should narrow unsafe or unrealistic choices, not remove student ownership.

## How Teams Make Decisions

Teams use design and strategy menus before major choices. Existing menus ask students to compare what each option helps, what it makes harder, how likely it is to succeed, how long it may take, and what evidence will show whether it is working.

The expected decision process is:

1. Review background and constraints.
2. Compare options.
3. Discuss trade-offs.
4. Choose a direction.
5. Record the choice, reason, trade-off, and evidence plan.
6. Test and revise when evidence justifies a change.

## Engineering Notebook Expectations

The notebook/portfolio is not fully built yet, but the intended evidence pattern is clear from the session map and menus.

Each team should collect:

- personal/team goals and norms,
- design decision tables,
- sketches and layout plans,
- build logs with photos or diagrams,
- code/configuration notes,
- test plans and data tables,
- iteration records,
- driver practice notes,
- final performance evidence,
- presentation outline,
- final reflection.

The notebook should answer: What did we choose, why did we choose it, what did we give up, what evidence did we collect, and what did we change?

## Major Build Milestones

- Robot startup and driving: students need a powered, safe robot that can move under control.
- Team identity and strategy: teams choose names, norms, and a starting game strategy.
- First programming: teams read a basic TeleOp program and connect code names to configured hardware.
- Chassis design: teams choose chassis shape, material, wheels, motor placement, and electronics/battery placement as Day 3 build planning begins.
- Chassis build and wiring: teams assemble or modify the chassis and prepare for safe powered testing.
- First TeleOp: teams configure/program basic driver-controlled movement.
- Controller mapping/functions: teams connect controls to driver intuition and robot needs.
- Flywheel design/testing: TODO: dedicated materials are not yet present in the repo.
- Servo/hopper: TODO: dedicated materials are not yet present in the repo.
- Full-system TeleOp: TODO: shell sessions exist, but detailed programming/build materials are still needed.
- Autonomous: planned for Session 13; detailed code examples and test templates are still needed.
- Inspection: implied in chassis readiness, final testing, and demo preparation; a dedicated inspection checklist is still needed.
- Judging presentation: planned for Sessions 18-19; presentation template/rubric still needed.
- Final demonstration: planned for Session 20; final demo scoring/reflection materials still needed.

## What Is Already Built in the Repo

Course organization:

- `00_course_map/course_overview.md`
- `00_course_map/20_session_scope_sequence.md`
- 20 session shell files in `01_session_plans/`
- `docs/course_content_inventory.md`
- `docs/source_file_policy.md`
- `docs/proposed_file_move_plan.md`
- `docs/reorganization_log.md`

Student-facing materials:

- FIRST/FTC orientation files at the repo root, pending duplicate review.
- Readings in `02_student_materials/readings/`
- Decision menus in `02_student_materials/decision_menus/`
- Student SLD prompt in `02_student_materials/sld_prompts/`
- Day 1 student bio template at the repo root, pending placement review.

Teacher/design materials:

- SLD teacher guide in `03_teacher_materials/teacher_guides/`
- Research/design rationale in `04_research_and_design_rationale/`
- Templates in `90_templates/`

Print/export materials:

- Individual generated PDFs in `05_print_packets/`
- Larger packet PDFs remain at the repo root pending manifest review.

## What Still Needs To Be Created

Highest-need missing pieces:

- Full timed lesson plans for all 20 sessions.
- Consolidated student engineering notebook/workbook.
- Teacher guides beyond Session 1.
- Setup, cleanup, inspection, and materials checkout procedures.
- Programming materials for TeleOp, controller mapping implementation, autonomous, and troubleshooting.
- Mechanism materials for flywheel, servo/hopper, and full-system integration.
- Testing templates, driver practice drills, data tables, and iteration protocols.
- Presentation template, judging/presentation rubric, final reflection, and final demo scoring sheet.
- Print packet manifests listing source Markdown files.

## How To Use The Folder Structure

- `00_course_map/`: start here for the course overview and 20-session sequence.
- `01_session_plans/`: use these shells to plan each class meeting. They are not finished lessons yet.
- `02_student_materials/`: readings, decision menus, SLD prompts, and future notebook/workbook materials.
- `03_teacher_materials/`: teacher guides, future rubrics, and setup/cleanup materials.
- `04_research_and_design_rationale/`: rationale for the instructional design.
- `05_print_packets/`: generated PDFs for printing or packet review.
- `90_templates/`: reusable templates for menus, SLDs, and research briefs.
- `91_utilities/`: support scripts and notes that are not core course content.
- `docs/`: repository organization, policies, inventory, and reorganization notes.

## Immediate Weekend Priorities

1. Turn Sessions 1-4 into usable timed plans, with Session 4 focused on first programming.
2. Build the first version of the student engineering notebook/workbook so evidence collection is consistent from Day 1.
3. Create teacher setup/checklist materials for safety, tools, batteries, controllers, parts, and cleanup.
4. Draft missing programming supports for Sessions 7-8 and 13.
5. Draft mechanism/testing supports for flywheel, servo/hopper, full-system TeleOp, and inspection.
6. Create presentation and final demo materials for Sessions 18-20.
7. Add packet manifests for existing PDFs before relying on them as final print packets.
