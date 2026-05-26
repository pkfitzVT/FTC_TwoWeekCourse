# Controller Mapping SLD

## Session / Course Phase

Day 3, Session 6: Chassis Readiness, Controller Mapping, and Drive Tuning

## Why This Discussion Matters

Your team has started turning the chassis into a driving robot. Now you need to decide how humans should control it during TeleOp.

```text
Strategy chooses the game plan.
Robot behaviors describe what the robot must do.
Controller mapping helps humans make the robot do those behaviors reliably.
```

This is not a vote for the control style one person likes best. This is a design decision based on evidence from driving tests, robot behavior goals, and driver/operator experience.

SLD is the process. The deliverable is the work product that comes out of the discussion.

## Main Discussion Question

Which control mapping best helps our drivers make the robot perform the behaviors in our Robot Behavior Specification?

Student version:

Should our team use D-pad drive, joystick drive, or a hybrid approach, and why?

## What This Discussion Must Produce

By the end of this SLD, your team should record a Controller Mapping Decision that includes:

- chosen control approach: D-pad, joystick, or hybrid
- evidence from D-pad trials
- evidence from joystick trials
- driver/operator notes
- which robot behaviors the mapping supports
- `gamepad1` driver controls
- any `gamepad2` operator controls already known
- one concern or tradeoff
- one next test or revision
- whether the team needs a later speed/power tuning discussion

## Evidence / Resources to Use

Use evidence from at least three sources. Do not choose based only on preference.

- Robot Behavior Specification
- Team Strategy Guide
- D-pad test trials
- joystick test trials
- Controller Mapping Drive Comparison Activity
- `DemoDriveDPad.java`
- `DemoDriveJoy.java`
- driver/operator observations
- loop time data
- turning or obstacle data
- parking or line-up accuracy data
- SLD tally sheet

## Suggested Data Review

Before discussing the final choice, review what actually happened during testing.

| Evidence Source | D-pad Result / Notes | Joystick Result / Notes |
|---|---|---|
| Loop time |  |  |
| Drive straight |  |  |
| Turn around obstacle |  |  |
| Line up with target |  |  |
| Park accurately |  |  |
| Driver confidence |  |  |
| Partner/operator communication |  |  |
| Mistakes or control confusion |  |  |

| Driver | Which control felt more reliable? | Evidence or reason |
|---|---|---|
| Driver 1 |  |  |
| Driver 2 |  |  |
| Driver 3, if used |  |  |

## Discussion Roles

One person may hold more than one role if your team is small.

| Role | Job |
|---|---|
| Facilitator | Keeps the team focused on evidence, not just preferences. |
| Tally keeper | Uses the SLD tally sheet. |
| Recorder | Records the Controller Mapping Decision. |
| Data checker | Points to test results before claims are accepted. |
| Driver representative | Explains what the robot felt like to control. |
| Behavior checker | Asks whether the mapping supports the Robot Behavior Specification. |

## Sentence Stems

Use these stems to make claims, use evidence, and name tradeoffs.

```text
The D-pad worked well when ___.
The joystick worked well when ___.
The data shows ___.
As a driver, I felt more confident when ___ because ___.
This control style supports our robot behavior plan because ___.
If we need to line up accurately, then ___ might be better because ___.
If we need to complete scoring loops quickly, then ___ might be better because ___.
One risk of D-pad drive is ___.
One risk of joystick drive is ___.
A hybrid approach might make sense if ___.
I could support this mapping if ___.
Before we finalize, we should test ___.
```

## Decision Record / Work Product

| Controller Mapping Decision | Team Response |
|---|---|
| Chosen control approach: D-pad / joystick / hybrid |  |
| Why this supports our Robot Behavior Specification |  |
| D-pad evidence used |  |
| Joystick evidence used |  |
| Driver/operator observations |  |
| `gamepad1` driver controls |  |
| `gamepad2` operator controls, if known |  |
| Biggest concern or tradeoff |  |
| Next control test or revision |  |
| Should we tune speed/power next? |  |
| Can all team members support this starting control plan? |  |

## Controller Mapping Readiness Check

Before recording our decision, our team has:

- [ ] Confirmed the chassis was safe enough for powered testing.
- [ ] Tested D-pad drive.
- [ ] Tested joystick drive.
- [ ] Collected at least one type of driving data.
- [ ] Heard from more than one driver if possible.
- [ ] Checked the Robot Behavior Specification.
- [ ] Discussed driver/operator communication.
- [ ] Named one concern or tradeoff.
- [ ] Recorded the control mapping decision.
- [ ] Named the next test or tuning target.

## SLD Tally Sheet Reminder

Use `90_templates/student_led_discussion_tally_sheet_template.md` or the generated site version of that template.

Use the SLD tally sheet to track discussion moves: Q, C, E, B, O, D, X.

At the end, record one discussion strength and one target for the Drive Power / Motor Tuning SLD.

## Portfolio Connection

Add the Controller Mapping Decision Record to the engineering portfolio. Include:

- test data
- final mapping decision
- driver/operator notes
- tradeoff accepted
- next tuning target

Update the controls/programming or chassis/drivetrain copy of the Subsystem Design Cycle Template if the control decision changes how the robot will be programmed, tested, or driven.

## Growth Target for Drive Power / Motor Tuning SLD

During the Drive Power / Motor Tuning SLD, our team should improve by:

- using more data
- comparing tradeoffs more clearly
- inviting quieter voices
- listening to driver/operator experience
- recording decisions more clearly
- connecting controls to robot behaviors
