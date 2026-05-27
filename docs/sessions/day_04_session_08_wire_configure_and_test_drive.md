# Day 4, Session 8: Wire, Configure, Test Drive, and Round-Robin Challenge

## Purpose

Connect physical wiring and robot configuration to Java TeleOp control, then use a two-robot timed challenge to test drive reliability, communication, and control decisions.

## Learning Target

Students can use driving evidence to improve chassis reliability, controller mapping, drive tuning, and drive-team communication.

## Success Criteria

- Robot is tested on blocks before floor driving.
- Configuration names match code.
- Teams debug one issue at a time and record results.
- Ready teams complete a two-robot timed run and record time, penalties, adjustments, and driver/operator role evidence.

## Teacher Preparation

Prepare charged batteries, Driver Stations, Robot Controllers/Control Hubs, motor wires, safe blocks, test space, cones or markers, starting zones, timer, and a troubleshooting routine.

## Student Background Reading / Preparation

- [Wiring, configuration, and first drive](../../02_student_materials/readings/day4_session8_wiring_configuration_and_first_drive.md)
- [Troubleshooting basic drive](../../02_student_materials/readings/day4_session8_troubleshooting_basic_drive.md)
- [Programming background](../../02_student_materials/readings/day2_session4_programming_background.md)
- [Reading basic TeleOp](../../02_student_materials/readings/day2_session4_reading_basic_teleop.md)
- [Human-centered controller mapping background](../../02_student_materials/readings/future_human_controller_mapping_background.md)
- [OnBot Java code examples](../../02_student_materials/code_examples/onbot_java/README.md)
- [Controller mapping drive comparison activity](../../02_student_materials/decision_menus/controller_mapping_drive_comparison_activity.md)
- [Controller Mapping SLD](../../02_student_materials/sld_prompts/day3_session6_controller_mapping_sld.md)
- [Drive Power / Motor Tuning SLD](../../02_student_materials/sld_prompts/day3_session6_drive_power_tuning_sld.md)
- [Robot Operations Role Plan SLD](../../02_student_materials/sld_prompts/reusable_robot_operations_role_plan_sld.md)
- [Drive Reliability Round-Robin Challenge](../../02_student_materials/guides/day4_session8_drive_reliability_round_robin_challenge.md)
- [Subsystem design cycle guide](../../02_student_materials/guides/subsystem_design_cycle_guide.md)

## Key Idea

```text
A robot that works alone may behave differently when another robot is sharing the field.
Good drive teams manage speed, space, timing, communication, and recovery from mistakes.
```

This is a controlled driving challenge, not bumper cars. The goal is fast, clean, controlled driving.

## Student-Led Discussion / Decision

- Troubleshooting prompt: What should we change first when the robot does not drive the way we expected?
- Robot Operations Role Plan SLD prompt: How should our team assign and practice robot operation roles so we are safe, fair, competitive, and prepared if someone is absent?
- Post-challenge reflection prompt: What did the driving challenge reveal about our chassis, controls, drive tuning, and driver communication?

Competition roles should be based on evidence, fairness, growth, and team needs. The best role plan includes backups.

## Differentiated Session Pathways

| Team Status | Session 8 Pathway |
|---|---|
| Robot not safely driving | Wiring, configuration, chassis repair, first drive |
| Robot drives but is unreliable | Controller mapping, power tuning, practice laps |
| Robot drives reliably | Two-robot round-robin timed challenge |
| Advanced team | Revise tuning, rotate drivers, improve clean-run score |

Teams enter the challenge when they are ready. Teams that are not ready to race should still aim for at least a practice run or readiness check.

## Work Time Options

- Wiring: connect motors and manage wires safely.
- Programming: confirm hardwareMap names and compare drive-only D-pad and joystick TeleOp examples.
- Testing: first drivetrain subsystem test on blocks, then controlled D-pad and joystick floor tests if safe.
- Challenge: run a two-robot round-robin timed course when the robot is ready.
- Documentation: test table, code/config notes, race run record, adjustment log, and role decision record.

## Two-Robot Round-Robin Challenge

Use this structure with four teams if time allows:

| Round | Match |
|---|---|
| 1 | Team A vs Team B |
| 2 | Team C vs Team D |
| 3 | Team A vs Team C |
| 4 | Team B vs Team D |
| 5 | Team A vs Team D |
| 6 | Team B vs Team C |

Each team gets three runs if time allows. If time is short, use one practice run, one official timed run, and one improvement run if possible.

Course rules:

- Two robots start from marked starting zones.
- Both robots follow the same general route or complete the same loop.
- Robots must avoid cones/markers, boundaries, and each other.
- Drivers may need to pass, wait, or adjust speed.
- Unsafe driving results in a reset, penalty, stop, rerun, or disqualification at teacher discretion.
- The teacher may modify the course for space and safety.

Scoring:

```text
final score = time + penalties
```

| Event | Penalty |
|---|---|
| Touches cone / marker / boundary | +5 seconds |
| Needs a reset | +10 seconds |
| Robot-to-robot contact | +10 seconds |
| Unsafe driving | Stop, rerun, or disqualification at teacher discretion |

Positive award categories: fastest clean run, best controlled driving, best driver/operator communication, best improvement between runs, best recovery from a mistake, and best evidence-based adjustment.

Between runs, teams should change only one or two things at a time and record what changed. Teams may adjust drive power, slow mode, controller mapping, driver/operator communication, starting strategy, passing/waiting strategy, wire management, loose parts, battery placement, or chassis alignment.

## Data Tables

Race Run Record:

| Run | Opponent | Driver | Operator | Time | Penalties | Final Score | Notes |
|---|---|---|---|---|---|---|---|
| Practice | | | | | | | |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

Adjustment Log:

| Between Runs | What We Changed | Why We Changed It | Result |
|---|---|---|---|
| After practice | | | |
| After Run 1 | | | |
| After Run 2 | | | |

Role Decision Record:

| Role | Student | Evidence / Reason | Backup |
|---|---|---|---|
| Driver | | | |
| Operator | | | |
| Coach / spotter, if used | | | |

## Must / Should / Could

- **Must:** Test basic drivetrain subsystem motion safely with wheels lifted first.
- **Should:** Record at least one symptom, likely cause, check, change, and result.
- **Could:** Complete a two-robot timed challenge, rotate drivers, improve clean-run score, or revise tuning based on run evidence.

## Deliverables

- Code/config notes.
- Wiring/configuration table.
- Testing results.
- Race run record, if ready.
- Adjustment log, if ready.
- Drive-team role decision record.
- Engineering portfolio entry.

## Engineering Portfolio Evidence

Teams should add motor port table, configuration names, Java variable names, subsystem test behavior, D-pad versus joystick comparison evidence, controller-mapping decision, timed run results, penalties, adjustment log, role decision record, photo/video evidence if available, and one chassis/control/driver-practice revision.

## Reflection / Share-Out

- What bug or mismatch did the team diagnose?
- What adjustment did the team make between runs?
- What did the challenge reveal about chassis reliability, controls, tuning, or driver/operator communication?

## Teacher Notes

Require students to stop OpModes before changing wires. Normalize debugging as engineering. Teams that are not ready for the full challenge should continue wiring, configuration, chassis repair, controller mapping, or drive tuning so they can participate in at least a practice run or readiness check.

## Linked Resources

- [Wiring, configuration, and first drive](../../02_student_materials/readings/day4_session8_wiring_configuration_and_first_drive.md)
- [Troubleshooting basic drive](../../02_student_materials/readings/day4_session8_troubleshooting_basic_drive.md)
- [Controller mapping drive comparison activity](../../02_student_materials/decision_menus/controller_mapping_drive_comparison_activity.md)
- [Controller Mapping SLD](../../02_student_materials/sld_prompts/day3_session6_controller_mapping_sld.md)
- [Drive Power / Motor Tuning SLD](../../02_student_materials/sld_prompts/day3_session6_drive_power_tuning_sld.md)
- [Robot Operations Role Plan SLD](../../02_student_materials/sld_prompts/reusable_robot_operations_role_plan_sld.md)
- [Drive Reliability Round-Robin Challenge](../../02_student_materials/guides/day4_session8_drive_reliability_round_robin_challenge.md)
- [OnBot Java code examples](../../02_student_materials/code_examples/onbot_java/README.md)
- [Subsystem Design Cycle template](../../90_templates/subsystem_design_cycle_template.md)
- [Student-Led Discussion Tally Sheet template](../../90_templates/student_led_discussion_tally_sheet_template.md)
- [Engineering notebook](../../02_student_materials/engineering_notebook/student_engineering_notebook_master.md)
