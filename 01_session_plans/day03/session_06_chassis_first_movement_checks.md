# Session 6: Chassis Readiness, Controller Mapping, and Drive Tuning

## Session Snapshot
- Day: 3
- Session: 6
- Big goal: Move from a safe chassis to evidence-based first drive, controller mapping, and initial drive-speed decisions.
- Student-facing objective: I can help my team check chassis readiness, compare D-pad and joystick driving, collect evidence, and choose a first controller mapping and drive power/speed setting.
- Main deliverable: Chassis readiness checklist, D-pad vs joystick comparison evidence, controller mapping decision, drive power/speed tuning decision, and next test.
- Existing materials to use: `02_student_materials/decision_menus/day2_session4_chassis_shape_menu.md`; `02_student_materials/decision_menus/day2_session4_wheel_selection_menu.md`; `02_student_materials/decision_menus/day2_session4_motor_placement_menu.md`; `02_student_materials/decision_menus/day2_session4_electronics_battery_placement_menu.md`; `02_student_materials/decision_menus/controller_mapping_drive_comparison_activity.md`; `02_student_materials/sld_prompts/day3_session6_controller_mapping_sld.md`; `02_student_materials/readings/future_human_controller_mapping_background.md`; `02_student_materials/code_examples/onbot_java/README.md`; `02_student_materials/code_examples/onbot_java/DemoDriveDPad.java`; `02_student_materials/code_examples/onbot_java/DemoDriveJoy.java`; `90_templates/robot_behavior_specification_template.md`; `02_student_materials/guides/subsystem_design_cycle_guide.md`; `90_templates/subsystem_design_cycle_template.md`; `90_templates/student_led_discussion_tally_sheet_template.md`
- Materials still needed: TODO: Drive Power / Speed Tuning SLD handout; teacher troubleshooting guide; test area norms.

## Teacher Setup Before Class

TODO: Prepare safe test area, inspection criteria, batteries/electronics procedures, repair supplies, Driver Station/Robot Controller devices, the D-pad and joystick demo OpModes, controller mapping comparison activity, timing/measurement tools, and clear test boundaries.

## Opening Move

Frame first movement as an inspection problem before it is a driving problem. Before comparing D-pad and joystick controls, teams must confirm that the chassis is safe enough for powered testing.

Core idea:

```text
Robot behaviors describe what the robot must do.
Controller mapping helps humans make the robot do those behaviors reliably.
Drive tuning helps the robot balance speed, control, accuracy, and safety.
```

## Background / Mini-Lesson

Mini-lesson on alignment, secure wheels, motor mounting, wire protection, battery/electronics access, and why controls must support the Robot Behavior Specification.

Examples:

- If the robot must line up accurately with the goal, controls must support precise turning and small adjustments.
- If the robot must make multiple scoring loops, controls must support quick but reliable driving.
- If the robot must park safely, controls must support predictable final positioning.
- If driver/operator roles matter, controls must be clear enough for two students to coordinate.

## Student-Led Discussion

Readiness prompt: What evidence will show that our chassis is ready for powered testing?

Controller Mapping SLD: Which control mapping best helps our drivers make the robot perform the behaviors in our Robot Behavior Specification?

Drive Power / Speed Tuning SLD placeholder: What drive power or speed setting gives our team the best balance of control, accuracy, speed, and safety?

Use the student-facing Controller Mapping SLD handout with the controller mapping comparison activity, SLD tally sheet, and engineering notebook to record the first control decision. The Drive Power / Speed Tuning SLD still needs a standalone student-facing handout later.

## Team Task

Teams inspect the chassis against readiness criteria, update the frame/drivetrain subsystem cycle, and identify issues before power-on. Once approved, teams run controlled D-pad and joystick trials, compare evidence, choose a first control approach, choose an initial drive power/speed setting, and record the next test.

## Suggested Activity Flow

| Time | Activity |
|---|---|
| 5-10 min | Chassis readiness and safety check |
| 10-15 min | Test D-pad drive using `DemoDriveDPad.java` |
| 10-15 min | Test joystick drive using `DemoDriveJoy.java` |
| 10 min | Collect driving data: loop time, turning, parking/line-up accuracy, driver confidence |
| 10 min | Controller Mapping SLD: D-pad, joystick, or hybrid? |
| 10 min | Drive Power / Speed Tuning SLD: what speed setting balances control and speed? |
| 5 min | Record decision, evidence, and next test in the portfolio |

Shortened version if time is tight: test one driver with D-pad, test one driver with joystick, record observations, and choose what to keep testing next.

## Build / Program / Test Time

Teams continue assembly only until readiness is met. Approved teams conduct controlled first movement checks, first on blocks and then in the safe test area.

## Data Collection Expectations

Run three short trials for each mapping approach when possible. If time allows, test more than one driver.

| Driver | Control Type | Trial 1 | Trial 2 | Trial 3 | Notes |
|---|---|---|---|---|---|
| Driver A | D-pad |  |  |  |  |
| Driver A | Joystick |  |  |  |  |
| Driver B | D-pad |  |  |  |  |
| Driver B | Joystick |  |  |  |  |

| Skill | Control Type | Result / Score | Notes |
|---|---|---|---|
| Drive straight | D-pad |  |  |
| Drive straight | Joystick |  |  |
| Turn around obstacle | D-pad |  |  |
| Turn around obstacle | Joystick |  |  |
| Line up with target | D-pad |  |  |
| Line up with target | Joystick |  |  |
| Park accurately | D-pad |  |  |
| Park accurately | Joystick |  |  |

This data should inform the SLD rather than replace discussion.

## Engineering Notebook Evidence

Teams complete a readiness checklist, subsystem test note, issue list, D-pad vs joystick comparison evidence, Controller Mapping SLD work product, Drive Power / Speed Tuning SLD work product, and next actions.

Controller Mapping SLD work product:

- chosen control approach: D-pad, joystick, or hybrid
- evidence from test trials
- driver/operator notes
- gamepad mapping decision
- next test or revision

Drive Power / Speed Tuning SLD work product:

- initial drive power/speed setting
- reasoning based on speed/control tradeoff
- evidence from trials
- slow mode decision, if applicable
- next tuning target

## Share-Out / Reflection

Teams share one issue caught before testing, one control choice supported by evidence, and one speed/control adjustment to test next.

## Cleanup

Power down safely, store batteries/electronics properly, save code notes, and secure robots.

## Teacher Notes

Record recurring build issues, teams ready/not ready for powered testing, control mappings selected, and teams that need help with motor direction, hardware names, driver overcorrection, or speed scaling.
