# Design Choice Menu Matrix

## Purpose

This matrix shows the major design choices teams need to make across the course and the student resources that should support those choices.

Design menus are not extra worksheets. Design menus are how teams turn discussion into design choices.

Student-led discussion helps the team make a decision, but the deliverable is the design choice the team records, builds toward, tests, and revises.

A design choice is not final because the team said it. A design choice becomes stronger when the team can explain it, build toward it, test it, and revise it based on evidence.

The strategy-to-design bridge should stay visible during every design choice:

```text
Strategy chooses the game plan.
Robot behaviors describe what the robot must do.
Subsystem designs explain how the robot will do it.
```

Later design choices should point back to the Team Strategy Guide and Robot Behavior Specification. If a design choice does not support the strategy or a required robot behavior, the team should revise the design choice or revise the strategy/behavior plan with evidence.

Demo robot analysis creates design evidence. Students use that evidence during strategy, robot behavior, and chassis design discussions.

## Course Design Process

```text
Modified game rules
-> Structure/function reading
-> Team strategy guide
-> Robot behavior specification
-> Subsystem design cycle
-> Design menus / design choices
-> Build toward a generative design
-> Revise based on materials, space, assembly constraints, testing, and evidence
```

Before finalizing a chassis design, each team must review Demo Robot Design Analysis notes and identify at least one design feature to borrow, one design feature to modify or avoid, and one question or test before building.

## Matrix

| Subsystem | Design Choice | When to Decide | Resources to Use | Evidence to Consider | Student Deliverable | Later Choices Affected |
|---|---|---|---|---|---|---|
| Team Strategy / Game Plan | Primary scoring strategy | After modified game rules, structure/function reading, team norms, and demo robot rotations | Modified game rules; structure/function reading; `90_templates/team_strategy_guide_template.md`; `02_student_materials/decision_menus/day2_session4_game_strategy_goals_menu.md`; `02_student_materials/decision_menus/demo_robot_design_analysis_activity.md` | Game scoring opportunities; expected score model; competition video observations; demo robot reliability/difficulty evidence; driver/operator role evidence; team skill and time | Team Strategy Guide entry with primary strategy and evidence | Robot behavior goals; chassis space; shooter/hopper priorities; driver practice |
| Team Strategy / Game Plan | Strategy-to-robot-behavior translation | After primary strategy and before chassis choices | `02_student_materials/sld_prompts/day2_session4_strategy_to_robot_behavior_sld.md`; Robot Behavior Specification; Team Strategy Guide; Demo Robot Design Analysis notes | Required autonomous, TeleOp, and endgame behaviors; testability; subsystem responsibility; behaviors that seemed easy, hard, reliable, or operator-dependent on demo robots | Robot Behavior Specification with behavior-to-subsystem notes | Chassis geometry; controls; shooter/hopper/trigger design; tests |
| Team Strategy / Game Plan | Backup strategy | Before major build decisions | Team Strategy Guide; Robot Behavior Specification | Risk, time, material limits, reliability concerns | Backup strategy note | Simplification decisions; features to remove |
| Team Strategy / Game Plan | Autonomous priority | Before programming priorities and chassis testing | Modified game rules; Team Strategy Guide; Robot Behavior Specification; `02_student_materials/readings/day4_session7_autonomous_encoder_experiment_background.md`; `02_student_materials/sld_prompts/day4_session7_autonomous_encoder_experiment_design_sld.md`; `02_student_materials/guides/day4_session7_autonomous_straight_line_challenge_activity.md` | Available time; field setup consistency; reliability of simplest autonomous action; encoder-distance data; drift and distance error; variable-control plan | Autonomous plan and priority level; optional autonomous encoder experiment plan, straight-line challenge model, code snippet, and test result | Starting position; code tasks; driver setup |
| Team Strategy / Game Plan | TeleOp scoring approach | Before chassis and mechanism layout | Game strategy menu; Robot Behavior Specification; demo robot observations | Scoring loop time; loading plan; likely driver skill; penalties | TeleOp behavior plan | Shooter placement; hopper access; controls |
| Team Strategy / Game Plan | Endgame / parking priority | Before final frame dimensions and driver routine | Modified game rules; Team Strategy Guide; Robot Behavior Specification | Parking space, partner robot space, time needed | Endgame plan | Chassis footprint; driver practice; final match routine |
| Team Strategy / Game Plan | Risk level | Before adding features | Team norms; Team Strategy Guide; SLD tally sheet | Time remaining; repair access; test evidence; team disagreement | Risk statement and revision rule | Whether to add, remove, or simplify mechanisms |
| Frame / Drivetrain | Chassis geometry | Before frame assembly | `02_student_materials/sld_prompts/day3_session5_chassis_design_choice_sld.md`; `02_student_materials/decision_menus/day2_session4_chassis_shape_menu.md`; chassis physics reading; Demo Robot Design Analysis activity; demo robot observation activity | Robot behavior goals; available materials; field movement; future mechanisms; design feature to borrow; design feature to modify or avoid; question/test before building | Chassis decision record, labeled top-view chassis sketch, and first chassis test plan | Motor placement; wheel placement; shooter/hopper space |
| Frame / Drivetrain | Frame shape: O, U, A, H, or hybrid | Before cutting/assembling major frame pieces | Chassis shape menu; principles of assembly; demo robot observations | Open space, strength, repair access, scoring path | Frame shape choice with trade-off | Mechanism mounting; electronics access; stiffness |
| Frame / Drivetrain | Frame material | Before assembly | `02_student_materials/decision_menus/day2_session4_chassis_material_menu.md`; assembly principles | Material availability; tool access; strength; ease of repair | Material decision table | Weight, stiffness, mounting options |
| Frame / Drivetrain | Drive motor placement | Before powered drivetrain testing | `02_student_materials/decision_menus/day2_session4_motor_placement_menu.md`; mounting motors/wheels reading | Balance, wiring, chain/belt/direct drive constraints, repair access | Motor placement sketch | Wheel layout; wiring route; battery/hub placement |
| Frame / Drivetrain | Wheel placement and wheel choice | Before drivetrain assembly | `02_student_materials/decision_menus/day2_session4_wheel_selection_menu.md`; chassis build checklist | Turning behavior; traction; rubbing; available wheels | Wheel decision record and first test notes | Driving behavior; chassis width; controller mapping |
| Frame / Drivetrain | Control Hub and battery placement | Before finalizing frame layout | `02_student_materials/decision_menus/day2_session4_electronics_battery_placement_menu.md`; wiring/configuration reading | Weight distribution; wire length; switch access; safety | Electronics layout sketch | Wiring, inspection, repair access, center of mass |
| Frame / Drivetrain | Open space reserved for future mechanisms | Before locking frame shape | Robot Behavior Specification; subsystem design cycle template; demo robot observations | Shooter/hopper footprint; reload access; driver view | Reserved-space note on chassis sketch | Shooter location; hopper path; trigger mounting |
| Frame / Drivetrain | Repair and wiring access | Before and during assembly | Assembly principles; troubleshooting checklist; demo robot observations | Can hands/tools reach fasteners, wires, battery, hub, switch? | Repair-access note and photo | Inspection readiness; troubleshooting speed |
| Controller Mapping / Driver Controls | D-pad drive, joystick drive, or hybrid drive | After chassis readiness check and safe first drive | `02_student_materials/sld_prompts/day3_session6_controller_mapping_sld.md`; `02_student_materials/decision_menus/controller_mapping_drive_comparison_activity.md`; `02_student_materials/readings/future_human_controller_mapping_background.md`; `02_student_materials/code_examples/onbot_java/DemoDriveDPad.java`; `02_student_materials/code_examples/onbot_java/DemoDriveJoy.java`; Robot Behavior Specification | Driver comfort; smoothness; lineup accuracy; parking accuracy; avoiding contact; loop time; driver/operator notes; test results | Controller Mapping Decision Record with D-pad evidence, joystick evidence, gamepad controls, tradeoff, and next test | Driver practice; scoring loop timing; code organization |
| Controller Mapping / Driver Controls | Gamepad1 driver controls | Before driver practice | Human-centered controller mapping reading; Robot Behavior Specification | Driver intuition; urgency; mistakes to avoid | Gamepad1 map | TeleOp routine; slow mode; match OpMode |
| Controller Mapping / Driver Controls | Gamepad2 operator controls | Before shooter/hopper/trigger integration | Robot Behavior Specification; subsystem cycle template | Driver/operator role split; timing; safety | Gamepad2 map | Shooter spin-up; trigger timing; human operator routine |
| Controller Mapping / Driver Controls | Drive power / motor tuning and slow mode | During first drive tests and scoring tests, after the controller mapping decision | `02_student_materials/sld_prompts/day3_session6_drive_power_tuning_sld.md`; controller mapping activity; drivetrain tests; Robot Behavior Specification; Controller Mapping SLD decision | Aiming accuracy; parking accuracy; overcorrection; loop time; safety; driver confidence; power-level trial data | Starting power settings for forward/backward driving, turning, and precision movement or slow mode if used; slow-mode decision if applicable; next tuning target | Code complexity; driver practice |
| Controller Mapping / Driver Controls | Robot operations role plan and backups | During Session 8 drive reliability challenge and later practice runs, subsystem tests, practice matches, or qualification rounds | `02_student_materials/sld_prompts/reusable_robot_operations_role_plan_sld.md`; `90_templates/robot_operations_role_plan_sld_template.md`; `02_student_materials/guides/day4_session8_drive_reliability_round_robin_challenge.md`; Controller Mapping SLD; Drive Power / Motor Tuning SLD; engineering notebook | Timed runs; penalties; driver/operator notes; communication quality; accuracy under pressure; ability to recover from mistakes; safety, fairness, growth needs, absence risks | Robot Operations Role Plan with primary roles, backups, rotation plan, practice goals, evidence/reasons, and role review conditions | Driver practice; TeleOp routine; subsystem operation; match readiness; qualification-round planning; final presentation evidence |
| Integration / Whole Robot | Performance postmortem and next change | After a subsystem test, driving challenge, autonomous challenge, whole-robot scoring loop, practice match, or qualification round | `02_student_materials/sld_prompts/reusable_performance_testing_postmortem_sld.md`; `90_templates/performance_testing_postmortem_sld_template.md`; engineering notebook; test data; photos/video | Human operation evidence; mechanical evidence; software/control evidence; strategy/communication evidence; score/time/penalties; driver/operator notes; failure/fix data | Performance Postmortem Record with main issue category, one or two next changes, owner, retest plan, and portfolio evidence | Repair priorities; code changes; role plan revisions; strategy simplification; next test plan |
| Controller Mapping / Driver Controls | Button mapping for shooter, trigger, hopper, or sensors | During subsystem testing | Servo/trigger readings; setup reference sheet; troubleshooting checklist | Accidental activation risk; reachability; driver routine | Control map and code notes | Match OpMode; safety; integration |
| Controller Mapping / Driver Controls | Telemetry needed for drivers | During subsystem testing | OnBot Java examples; troubleshooting checklist | What the driver/operator needs to know during testing | Telemetry list | Debugging speed; driver confidence |
| Shooter Subsystem | Shooter location | Before shooter mount is built | Shooter readings; subsystem design cycle template; demo robot observations | Goal location; chassis open space; ball path; safety | Shooter location sketch | Hopper path; trigger placement; wiring |
| Shooter Subsystem | Shooter angle | Before shot testing | Projectile motion reading; target impact reading; demo observations | Distance to goal; height; shot arc; miss pattern | Angle choice and test plan | Support structure; scoring position; driver lineup |
| Shooter Subsystem | Wheel type and compression | During first shooter prototype | Flywheel speed/compression reading; build/test planning | Wheel firmness; ball deformation; consistency; motor load | Compression plan and first variable test | Motor current, safety, success rate |
| Shooter Subsystem | Motor placement and power transfer | Before powered shooter testing | Flywheel readings; assembly principles; demo observations | Direct-drive feasibility; stiffness; access; wiring | Motor placement sketch | Guarding, support structure, maintenance |
| Shooter Subsystem | Support structure | Before repeated shot tests | Subsystem design cycle; assembly principles | Flex, vibration, angle consistency | Support sketch/photo and test result | Accuracy; reliability; integration |
| Shooter Subsystem | Scoring position | During shot testing | Robot Behavior Specification; Team Strategy Guide; projectile readings | Success rate from known positions; lineup time | Chosen scoring position and data | Driver routine; chassis control; expected score |
| Shooter Subsystem | Safety, guarding, and access | Before high-speed testing | Safety norms; flywheel build planning; inspection materials | Contact risk; loose parts; ability to service | Safety/access note | Inspection, demonstration readiness |
| Hopper / Artifact Management | How artifacts are stored | Before hopper mockup | Gravity-fed hopper reading; demo observations; subsystem template | Number of artifacts; reload plan; available space | Hopper storage sketch | Shooter feed path; trigger geometry |
| Hopper / Artifact Management | How artifacts are guided | During hopper mockup | Hopper jams and ball path reading; demo observations | Ball path, rubbing, bridging, repeatability | Ball-path sketch and hand-test result | Trigger placement; shooter consistency |
| Hopper / Artifact Management | Whether gravity helps or hurts | During hand testing | Gravity-fed hopper reading; test data | Slope, jams, robot motion, ball speed | Gravity/slope decision | Jam prevention; trigger load |
| Hopper / Artifact Management | Jam prevention | Before powered integration | Hopper jams reading; troubleshooting checklist | Where jams happen; repeated hand tests | Jam-risk note and redesign | Trigger safety; match reliability |
| Hopper / Artifact Management | Connection to shooter | Before integration | Shooter build/test planning; whole-system testing | Alignment, timing, ball entry angle | Hopper-to-shooter interface sketch | Shot consistency; trigger reset |
| Hopper / Artifact Management | Number of artifacts to hold | Before final hopper build | Robot Behavior Specification; strategy guide | Rules, reload plan, weight, jams | Capacity decision | Cycle time; trigger control; driver/operator role |
| Hopper / Artifact Management | Operator access / reload plan | Before TeleOp routine practice | Robot Behavior Specification; team strategy | Human operator position; safe loading; time per loop | Reload plan | Hopper opening; driver path; controls |
| Trigger / Release Mechanism | Servo position values | During servo testing | Servo readings; robot setup reference sheet | Safe range of motion; buzzing/strain; release result | Servo position table | Code constants; safe start behavior |
| Trigger / Release Mechanism | Trigger geometry | Before mounting | Servo trigger design reading; demo observations | One-ball release, clearance, linkage motion | Trigger sketch/prototype | Hopper shape; shooter feed timing |
| Trigger / Release Mechanism | One-at-a-time vs batch release | Before shot testing | Robot Behavior Specification; trigger readings | Strategy, reliability, success rate, jams | Release-mode decision | Scoring loops; hopper capacity |
| Trigger / Release Mechanism | Safe start position | Before code testing | Servo readings; setup reference sheet | What moves at INIT; finger safety; jam risk | Safe start note and code constant | Inspection; driver confidence |
| Trigger / Release Mechanism | Right trigger/button mapping | Before driver/operator practice | Controller mapping reading; comparison activity | Reachability, accidental fire risk, operator role | Trigger control map | Match OpMode; safety |
| Trigger / Release Mechanism | Reset behavior and jam recovery | During first shots | Trigger implementation reading; troubleshooting checklist | Does trigger return? What happens after jam? | Reset/jam recovery plan | Whole-system reliability |
| Integration / Whole Robot | Final subsystem placement | Before full scoring loop practice | Whole-system testing reading; subsystem templates; demo observations | What blocks what; weight balance; repair access | Integrated layout sketch/photo | Inspection, driver routine, final presentation |
| Integration / Whole Robot | Wiring routing | Before final inspection | Wiring/configuration reading; robot readiness checklist | Wire strain, entanglement, access, labels | Wiring route photo and notes | Reliability, inspection, repair |
| Integration / Whole Robot | Code integration strategy | Before match OpMode | OnBot Java examples; code log; subsystem test code | Which code works alone; what must combine | Match OpMode plan | Controls, debugging, safety |
| Integration / Whole Robot | Match OpMode choice | Before driver practice | Code examples; subsystem code; controller map | Reliability, simplicity, driver familiarity | Match OpMode decision | Final demos, match readiness |
| Integration / Whole Robot | Features to remove or simplify | During final testing | Team strategy guide; SLD tally template; troubleshooting checklist | Time left, failures, expected score, safety | Keep/remove/simplify decision | Reliability, presentation story |
| Integration / Whole Robot | Pre-inspection / pre-demo test list | Before final demo or matches | Robot readiness checklist; whole-system testing; troubleshooting checklist | Safety, repeated scoring loop, parking, code stability | Readiness checklist | Final presentation and demonstration |

## Revision Rule

Teams should revise design choices when they encounter:

- material availability limits,
- geometry conflicts,
- blocked space,
- assembly difficulty,
- repair access problems,
- programming or wiring constraints,
- unsafe behavior,
- unreliable test results,
- or new evidence from driving, scoring, or demo robot observations.

The stronger engineering explanation is:

> We chose this design because it supports our strategy, robot behavior plan, available materials, space constraints, and testing evidence. We revised it when the evidence changed.
