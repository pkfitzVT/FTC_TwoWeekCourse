# YES FTC Two-Week Robotics Course: Teacher Overview

## Course Purpose

This is a 10-day, 20-session modified FIRST Tech Challenge robotics course. Students build, program, test, document, and present a working FTC-style robot in two weeks.

The course is not only a build sprint. It is structured so students practice engineering decisions, teamwork, evidence collection, safety, repair, communication, and reflection. The current repo includes early course culture materials, student-led discussion support, decision menus, first programming readings, drivetrain/chassis readings, shooter/hopper/trigger readings, inspection and presentation readings, reusable student guides, Challenge by Choice materials, and website-ready teacher session pages.

## What Students Will Build

Students will build a working FTC-style robot that can move, respond to driver controls, perform at least a simple game-related function, collect test evidence, and be explained in a final presentation.

The planned robot arc includes drivetrain/chassis, wiring/electronics placement, TeleOp driving, flywheel shooter construction, projectile-motion reasoning, gravity-fed hopper design, servo trigger control, whole-system testing, inspection, practice challenge evidence, presentation preparation, and a final demonstration.

## Daily Course Arc

| Day | Sessions | Main arc |
|---:|---|---|
| 1 | 1-2 | Course entry, FIRST/FTC culture, safety, borrowed equipment, student goals, collaborative teams |
| 2 | 3-4 | Team identity, team norms, game strategy, first programming session |
| 3 | 5-6 | Chassis design planning, build start, build continuation, readiness for powered testing |
| 4 | 7-8 | Drivetrain/chassis build, wiring, configuration, first drive testing |
| 5 | 9-10 | Flywheel shooter construction basics, projectile motion, target behavior |
| 6 | 11-12 | Gravity-fed hopper design, servo positions, trigger control |
| 7 | 13-14 | Trigger implementation, first controlled shots, whole-system tuning |
| 8 | 15-16 | Robot inspection/readiness, presentation script, judging prep |
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

The engineering notebook master now exists in `02_student_materials/engineering_notebook/student_engineering_notebook_master.md`. It should be treated as the current portfolio structure, though printable daily student pages may still need formatting.

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
- Flywheel design/testing: Day 5 readings support motor speed, compression, build planning, projectile motion, target impact, and shot consistency.
- Servo/hopper: Day 6 readings support gravity-fed hopper design, hopper jams, servo positions, and trigger testing.
- Whole-system TeleOp/testing: Day 7 readings support trigger implementation, shot observation, full-system testing, quick adjustments, and tuning.
- Inspection: Day 8 readings include robot inspection, safety, and readiness checklist materials.
- Judging/presentation: Day 8 readings support presentation story, script, award/recognition claims, judging questions, and growth narrative.
- Final demonstration: planned for Session 20; final demo scoring/reflection materials still need final formatting.

## What Is Already Built in the Repo

Course organization:

- `00_course_map/course_overview.md`
- `00_course_map/20_session_scope_sequence.md`
- `docs/README.md`
- `docs/teacher_facing_robotics_course_overview.md`
- `docs/sessions/`
- 20 session shell files in `01_session_plans/`
- `docs/course_content_inventory.md`
- `docs/source_file_policy.md`
- `docs/proposed_file_move_plan.md`
- `docs/reorganization_log.md`

Student-facing materials:

- FIRST/FTC orientation files at the repo root, pending duplicate review.
- Readings in `02_student_materials/readings/`
- Reusable guides in `02_student_materials/guides/`
- Decision menus in `02_student_materials/decision_menus/`
- Student SLD prompt in `02_student_materials/sld_prompts/`
- Challenge by Choice materials in `02_student_materials/challenge_by_choice/`
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

- Timed agendas and setup quantities for all 20 sessions.
- Printable daily notebook/workbook pages derived from the engineering notebook master.
- Teacher setup, cleanup, safety, battery, controller, field, and materials checkout procedures.
- Final challenge rules, scoring sheets, rubrics, rehearsal feedback forms, and final demo/reflection materials.
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
- `docs/`: repository organization, policies, inventory, website-ready teacher overview, session pages, and impact-study planning.

## Immediate Weekend Priorities

1. Add timed agendas and setup quantities to the website-ready session pages.
2. Format printable daily engineering notebook pages.
3. Create teacher setup/checklist materials for safety, tools, batteries, controllers, parts, field flow, and cleanup.
4. Finalize challenge rules, scoring sheets, presentation rubric, and final reflection materials.
5. Add packet manifests for existing PDFs before relying on them as final print packets.
