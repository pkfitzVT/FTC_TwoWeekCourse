# Day 3, Session 6: Chassis Readiness, Controller Mapping, and Drive Tuning

## Purpose

Use chassis readiness as the entry condition for safe first drive, then compare D-pad and joystick controls, collect driving evidence, and make a first controller mapping and drive power/speed decision.

## Learning Target

Students can check whether the chassis is mechanically ready for safe powered testing, compare D-pad and joystick drive approaches, collect simple driving data, and choose a first controller mapping and drive power/speed setting.

## Success Criteria

- Motors and wheels are secure.
- Wires and electronics have planned space.
- Teams identify readiness issues before turning on the robot.
- Teams compare `DemoDriveDPad.java` and `DemoDriveJoy.java` with controlled trials.
- Teams connect controller mapping to the Robot Behavior Specification.
- Teams record a first control decision, drive power/speed tuning decision, and next test.

## Teacher Preparation

Prepare safe test area, batteries, basic inspection criteria, repair supplies, storage procedure, Driver Station/Robot Controller devices, OnBot Java access, D-pad and joystick demo OpModes, controller mapping comparison activity, timing/measurement tools, and clear test boundaries.

## Student Background Reading / Preparation

- [Principles of robot assembly](../../02_student_materials/readings/principles_of_robot_assembly_day3.md)
- [Chassis physics and space background](../../02_student_materials/readings/day3_session5_chassis_physics_space_background.md)
- [Subsystem design cycle guide](../../02_student_materials/guides/subsystem_design_cycle_guide.md)
- [Human-centered controller mapping background](../../02_student_materials/readings/future_human_controller_mapping_background.md)
- [Controller mapping drive comparison activity](../../02_student_materials/decision_menus/controller_mapping_drive_comparison_activity.md)
- [Controller Mapping SLD handout](../../02_student_materials/sld_prompts/day3_session6_controller_mapping_sld.md)
- [Drive Power / Motor Tuning SLD handout](../../02_student_materials/sld_prompts/day3_session6_drive_power_tuning_sld.md)
- [OnBot Java code examples](../../02_student_materials/code_examples/onbot_java/README.md)
- [DemoDriveDPad.java](../../02_student_materials/code_examples/onbot_java/DemoDriveDPad.java)
- [DemoDriveJoy.java](../../02_student_materials/code_examples/onbot_java/DemoDriveJoy.java)
- [Robot Behavior Specification template](../../90_templates/robot_behavior_specification_template.md)
- [Student-Led Discussion Tally Sheet template](../../90_templates/student_led_discussion_tally_sheet_template.md)
- Relevant Day 2 chassis decision menus.

## Student-Led Discussion / Decision

Before comparing D-pad and joystick controls, teams must confirm that the chassis is safe enough for powered testing.

Readiness prompt: What evidence will show that our chassis is ready for powered testing?

Controller Mapping SLD: Which control mapping best helps our drivers make the robot perform the behaviors in our Robot Behavior Specification?

Drive Power / Motor Tuning SLD: What motor power settings give our team the best balance of control, accuracy, speed, and safety for the robot behaviors we need?

Use the student-facing Controller Mapping SLD handout with the controller mapping comparison activity, SLD tally sheet, and engineering notebook to record the first control decision. Then use the Drive Power / Motor Tuning SLD handout to choose starting power settings for forward/backward driving, turning, and precision movement or slow mode if used.

Core idea:

```text
Robot behaviors describe what the robot must do.
Controller mapping helps humans make the robot do those behaviors reliably.
Drive tuning helps the robot balance speed, control, accuracy, and safety.
```

## Work Time Options

- Assembly: finish drivetrain/chassis structure.
- Testing: hand-spin wheels, check rubbing, inspect fasteners, and update the frame/drivetrain subsystem cycle.
- Safe first drive: test on blocks first, then run controlled floor tests only after teacher/mentor approval.
- Controller comparison: test D-pad drive using `DemoDriveDPad.java` and joystick drive using `DemoDriveJoy.java`.
- Data collection: record loop time, turning, parking/line-up accuracy, driver confidence, and notes from more than one driver if possible.
- SLD: decide D-pad, joystick, or hybrid and choose an initial drive power/speed setting.
- Documentation: readiness checklist, issue list, test data, control decision, speed setting, and next test.

## Suggested Activity Flow

| Time | Activity |
|---|---|
| 5-10 min | Chassis readiness and safety check |
| 10-15 min | Test D-pad drive using `DemoDriveDPad.java` |
| 10-15 min | Test joystick drive using `DemoDriveJoy.java` |
| 10 min | Collect driving data: loop time, turning, parking/line-up accuracy, driver confidence |
| 10 min | Controller Mapping SLD: D-pad, joystick, or hybrid? |
| 10 min | Drive Power / Motor Tuning SLD: what motor power settings balance control, accuracy, speed, and safety? |
| 5 min | Record decision, evidence, and next test in the portfolio |

Shortened version if time is tight: test one driver with D-pad, test one driver with joystick, record observations, and choose what to keep testing next.

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

## Must / Should / Could

- **Must:** Complete a mechanical readiness check before powered testing, run safe first-drive evidence if approved, and record one D-pad vs joystick comparison.
- **Should:** Use the Robot Behavior Specification to justify a first controller mapping and drive power/speed setting.
- **Could:** Test more than one driver, compare slow mode or reduced power, or create a short inspection/control-test routine another team could use.

## Deliverables

- Build photos.
- Chassis readiness checklist.
- Issue/fix list.
- D-pad vs joystick comparison evidence.
- Controller Mapping SLD work product: chosen D-pad, joystick, or hybrid approach; test evidence; driver/operator notes; gamepad mapping decision; next test or revision.
- Drive Power / Motor Tuning SLD work product: starting power settings for forward/backward driving, turning, and precision movement or slow mode if used; speed/control tradeoff reasoning; trial evidence; slow mode decision if applicable; next tuning target.
- Engineering portfolio entry.

## Engineering Portfolio Evidence

Teams should add what was checked, what failed readiness, frame/drivetrain subsystem evidence, D-pad vs joystick trial evidence, controller mapping decision, drive power/speed tuning decision, what was fixed, and what remains.

Controls should connect to robot behaviors:

- If the robot must line up accurately with the goal, the controls must support precise turning and small adjustments.
- If the robot must make multiple scoring loops, the controls must support quick but reliable driving.
- If the robot must park safely, the controls must support predictable final positioning.
- If driver/operator roles matter, the controls must be clear enough for two students to coordinate.

## Reflection / Share-Out

- What issue did the team catch before it became a powered-test problem?
- Which control choice is currently supported by the best evidence?
- What speed/control adjustment should the team test next?

## Teacher Notes

Do not let teams power robots until wheels, motors, battery, hub, switch, and wires are reasonably safe. Frame inspection as normal engineering. Keep first drive slow and controlled; the goal is evidence for a control decision, not fast driving.

## Linked Resources

- [Principles of robot assembly](../../02_student_materials/readings/principles_of_robot_assembly_day3.md)
- [Wheel selection menu](../../02_student_materials/decision_menus/day2_session4_wheel_selection_menu.md)
- [Motor placement menu](../../02_student_materials/decision_menus/day2_session4_motor_placement_menu.md)
- [Electronics and battery placement menu](../../02_student_materials/decision_menus/day2_session4_electronics_battery_placement_menu.md)
- [Controller mapping drive comparison activity](../../02_student_materials/decision_menus/controller_mapping_drive_comparison_activity.md)
- [Controller Mapping SLD handout](../../02_student_materials/sld_prompts/day3_session6_controller_mapping_sld.md)
- [Drive Power / Motor Tuning SLD handout](../../02_student_materials/sld_prompts/day3_session6_drive_power_tuning_sld.md)
- [Human-centered controller mapping background](../../02_student_materials/readings/future_human_controller_mapping_background.md)
- [OnBot Java code examples](../../02_student_materials/code_examples/onbot_java/README.md)
- [DemoDriveDPad.java](../../02_student_materials/code_examples/onbot_java/DemoDriveDPad.java)
- [DemoDriveJoy.java](../../02_student_materials/code_examples/onbot_java/DemoDriveJoy.java)
- [Robot Behavior Specification template](../../90_templates/robot_behavior_specification_template.md)
- [Subsystem Design Cycle template](../../90_templates/subsystem_design_cycle_template.md)
- [Student-Led Discussion Tally Sheet template](../../90_templates/student_led_discussion_tally_sheet_template.md)
- [Engineering notebook](../../02_student_materials/engineering_notebook/student_engineering_notebook_master.md)
