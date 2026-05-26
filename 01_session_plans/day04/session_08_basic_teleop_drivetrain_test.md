# Session 8: Wire, Configure, Test Drive, and Round-Robin Challenge

## Session Snapshot
- Day: 4
- Session: 8
- Big goal: Wire, configure, and test safe TeleOp driving, then use a two-robot round-robin challenge to collect evidence about drive reliability, communication, and control decisions.
- Student-facing objective: I can use driving evidence to improve chassis reliability, controller mapping, drive tuning, and drive-team communication.
- Main deliverable: Drive reliability record with wiring/config evidence, timed runs, penalties, adjustment log, role decision record, and next revision.
- Existing materials to use: `02_student_materials/readings/day4_session8_wiring_configuration_and_first_drive.md`; `02_student_materials/readings/day4_session8_troubleshooting_basic_drive.md`; `02_student_materials/guides/day4_session8_drive_reliability_round_robin_challenge.md`; `02_student_materials/readings/day2_session4_programming_background.md`; `02_student_materials/readings/day2_session4_reading_basic_teleop.md`; `02_student_materials/readings/future_human_controller_mapping_background.md`; `02_student_materials/code_examples/onbot_java/README.md`; `02_student_materials/code_examples/onbot_java/DemoDriveDPad.java`; `02_student_materials/code_examples/onbot_java/DemoDriveJoy.java`; `02_student_materials/decision_menus/controller_mapping_drive_comparison_activity.md`; `02_student_materials/sld_prompts/day3_session6_controller_mapping_sld.md`; `02_student_materials/sld_prompts/day3_session6_drive_power_tuning_sld.md`; `02_student_materials/guides/subsystem_design_cycle_guide.md`; `90_templates/subsystem_design_cycle_template.md`; `90_templates/student_led_discussion_tally_sheet_template.md`
- Materials still needed: TODO: teacher wiring guide; step-by-step configuration screenshots; inspection checklist; optional future student-facing drive-team role SLD.

## Teacher Setup Before Class

Prepare programming devices, robot configurations, charged batteries, safe test blocks, Driver Stations, troubleshooting flow, cones or markers, a timed course, starting zones, and enough open space for two robots to drive safely.

## Opening Move

Review that unexpected robot motion is a testing and safety issue, not just a coding issue. Before any round-robin driving, teams must confirm that the robot is safe enough for powered floor testing.

## Background / Mini-Lesson

Use the wiring/configuration and troubleshooting readings to review motor ports, configuration names, hardwareMap, safe first-drive procedure, and one-change-at-a-time debugging. Then frame the challenge:

```text
A robot that works alone may behave differently when another robot is sharing the field.
Good drive teams manage speed, space, timing, communication, and recovery from mistakes.
```

This is a controlled driving challenge, not bumper cars. The goal is fast, clean, controlled driving.

## Differentiated Session Pathways

| Team Status | Session 8 Pathway |
|---|---|
| Robot not safely driving | Wiring, configuration, chassis repair, first drive |
| Robot drives but is unreliable | Controller mapping, power tuning, practice laps |
| Robot drives reliably | Two-robot round-robin timed challenge |
| Advanced team | Revise tuning, rotate drivers, improve clean-run score |

Teams enter the challenge when they are ready. Teams that are not ready to race should still aim for at least a practice run or readiness check.

## Student-Led Discussion

Troubleshooting prompt: What should we change first when the robot does not drive the way we expected?

Drive-team role prompt: How should our team assign and rotate drive-team roles so we are competitive, fair, and prepared if someone is absent?

Post-challenge reflection prompt: What did the driving challenge reveal about our chassis, controls, drive tuning, and driver communication?

## Team Task

Teams wire, configure, and test the drivetrain safely. Ready teams use a two-robot timed round-robin challenge to test controller mapping, drive power tuning, field awareness, driver/operator communication, and chassis reliability.

## Build / Program / Test Time

Teams program/configure basic TeleOp movement, run controlled drivetrain tests if safe, and record controller-mapping or drive-tuning decisions as needed.

For ready teams, use this round-robin structure if four teams are available:

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

## Engineering Notebook Evidence

Teams record observed behavior, code/config change, subsystem test result, D-pad versus joystick comparison evidence, timed run results, penalties, adjustment log, role decision record, photo/video evidence if available, and one chassis/control/driver-practice revision.

## Share-Out / Reflection

Teams share one bug or mismatch and how they diagnosed it, one adjustment made between runs, and one thing the challenge revealed about their drive team or chassis reliability.

## Cleanup

TODO: Save code, power down robots, store controllers, and note unresolved issues.

## Teacher Notes

Record common code/configuration problems for next-session support. Track which teams still need wiring/configuration help, which teams need additional control tuning, and which teams are ready for mechanism work after proving basic driving reliability.
