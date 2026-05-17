# Coteacher Weekend Review Packet

## What This Course Is

This is a 10-day, 20-session modified FIRST Tech Challenge robotics course. Students build, program, test, document, and present a working FTC-style robot in two weeks.

The course is designed as a real engineering experience, not just a kit build. Students make team decisions, compare trade-offs, use shared materials responsibly, collect evidence, and explain their robot at the end.

## What Students Will Do

Students will move through a build/program/test/present cycle:

- learn FIRST/FTC culture, safety, and borrowed-equipment expectations,
- form teams and choose team norms,
- choose a game strategy,
- program basic TeleOp driving,
- plan, build, and wire a drivetrain/chassis,
- map controller functions,
- prototype or add a simple mechanism,
- test and revise with evidence,
- add autonomous or scripted behavior if realistic,
- practice driving and collect final performance evidence,
- organize an engineering notebook,
- prepare and deliver a judging-style presentation and final demonstration.

## The Basic Teaching Pattern

The recurring class pattern is:

background reading -> decision menu -> student-led discussion -> team decision -> build/program/test -> engineering notebook evidence

The purpose of the pattern is to keep student work evidence-based. Students should not jump straight to grabbing parts or changing code. They should understand the constraint, compare options, discuss trade-offs, make a decision, test it, and record what happened.

## 10-Day Course Snapshot

| Day | Sessions | Main focus | Major student deliverable |
|---:|---|---|---|
| 1 | 1-2 | Course entry, FIRST/FTC culture, safety, borrowed equipment, personal goals, collaborative teams | Personal goal, safety/community commitment, first SLD reflection, teamwork contribution note |
| 2 | 3-4 | Team identity, team norms, game strategy, first programming session | Team name/norm decision tables, strategy decision table, programming notebook entry |
| 3 | 5-6 | Chassis design planning, build start, build continuation, readiness for powered testing | Chassis design tables, sketches, build log, chassis photo/sketch, readiness checklist, issue list |
| 4 | 7-8 | Controller mapping, first TeleOp, drivetrain testing | Controller mapping plan, TeleOp test record |
| 5 | 9-10 | Strategy check, mechanism planning, robot improvement sprint | Mechanism decision table, sketch, build-risk note, sprint log |
| 6 | 11-12 | Testing methods, data collection, iteration from evidence | Test plan, data table, iteration record |
| 7 | 13-14 | Autonomous/scripted behavior, driver practice, reliability tuning | Autonomous plan/test results, driver practice log |
| 8 | 15-16 | Documentation, portfolio organization, final robot improvements | Portfolio evidence checklist, final improvement record, final test evidence |
| 9 | 17-18 | Practice challenge evidence, presentation planning | Match/practice data, reliability reflection, presentation outline |
| 10 | 19-20 | Presentation rehearsal, final demo, final reflection | Rehearsal feedback, final revision list, final reflection, completed notebook/portfolio |

## What Is Ready Enough To Use

Course map:

- `00_course_map/course_overview.md`
- `00_course_map/20_session_scope_sequence.md`

Session shells:

- 20 shell files in `01_session_plans/day01/` through `01_session_plans/day10/`
- Each shell has the same structure: setup, opening, mini-lesson, SLD, team task, build/program/test time, notebook evidence, reflection, cleanup, teacher notes.

Decision menus:

- `02_student_materials/decision_menus/day1_session1_individual_goal_menu.md`
- `02_student_materials/decision_menus/day2_session3_team_name_menu.md`
- `02_student_materials/decision_menus/day2_session3_team_norms_menu.md`
- `02_student_materials/decision_menus/day2_session4_game_strategy_goals_menu.md`
- `02_student_materials/decision_menus/day2_session4_chassis_shape_menu.md`
- `02_student_materials/decision_menus/day2_session4_chassis_material_menu.md`
- `02_student_materials/decision_menus/day2_session4_wheel_selection_menu.md`
- `02_student_materials/decision_menus/day2_session4_motor_placement_menu.md`
- `02_student_materials/decision_menus/day2_session4_electronics_battery_placement_menu.md`

Readings:

- `02_student_materials/readings/day1_session1_borrowed_equipment_expectations.md`
- `02_student_materials/readings/day1_session1_robotics_safety_norms.md`
- `02_student_materials/readings/day1_session2_collaborative_engineering_teams.md`
- `02_student_materials/readings/day2_session3_why_team_names_matter.md`
- `02_student_materials/readings/day2_session4_decode_scoring_strategy_background.md`
- `02_student_materials/readings/day2_session4_programming_background.md`
- `02_student_materials/readings/day2_session4_reading_basic_teleop.md`
- `02_student_materials/readings/day3_session5_chassis_physics_space_background.md`
- FIRST/FTC orientation readings remain at the repo root pending duplicate review.

Engineering notebook skeleton:

- `02_student_materials/engineering_notebook/student_engineering_notebook_master.md`

Teacher overview:

- `03_teacher_materials/teacher_guides/two_week_course_teacher_overview.md`

Teacher / design support:

- `03_teacher_materials/teacher_guides/day1_session1_sld_shared_materials_teacher_guide.md`
- `04_research_and_design_rationale/research_brief_design_menu_cards.md`
- `04_research_and_design_rationale/research_brief_student_led_discussions.md`
- Templates in `90_templates/`

## What Still Needs Work

- Polished Day 1 materials: duplicate FIRST/FTC readings need a source-of-truth decision, and Day 1 packet order needs to be set.
- Full teacher setup notes: safety, tools, batteries, controllers, field space, cleanup, and borrowed equipment routines.
- Print packets: packet PDFs need manifests listing source Markdown files.
- Rubrics: robot performance, notebook, teamwork, presentation, and final reflection rubrics are not built.
- Programming handouts: TeleOp setup, drivetrain code/configuration, controller mapping implementation, troubleshooting.
- Flywheel materials: design options, safety notes, testing procedure, and notebook page are missing.
- Servo/hopper materials: design options, wiring/control notes, testing procedure, and notebook page are missing.
- Autonomous materials: code examples, safe test procedure, and test table are missing.
- Inspection checklist: chassis/electronics/fastener/wiring/safety inspection page is missing.
- Judging/presentation pages: planning sheet, rehearsal feedback form, rubric, and final demo scoring sheet are missing.

## Questions For Coteacher Feedback

- Does the 10-day sequence feel realistic for the students and the available class time?
- Are the build milestones in the right order?
- Where do students need more structure?
- Where can students safely have more agency?
- What materials must be printed before Day 1?
- What tools/parts need to be staged before each day?
- Which sessions are most likely to run long?
- Which decisions should be made by students, and which should be constrained by teachers for safety/time?
- What robot functions are realistic for all teams, and what should be optional stretch work?
- What evidence should every team be required to have by the final presentation?

## Immediate Next Build Priorities

1. Polish Sessions 1-4 into usable timed teacher plans and decide the Day 1 print packet order.
2. Turn `02_student_materials/engineering_notebook/student_engineering_notebook_master.md` into printable daily student pages.
3. Create teacher setup/checklists for tools, parts, batteries, controllers, safety, cleanup, and materials checkout.
4. Build programming supports for TeleOp, controller mapping, troubleshooting, and autonomous.
5. Build mechanism/testing/presentation supports: flywheel, servo/hopper, inspection checklist, judging presentation pages, and final demo/reflection materials.
