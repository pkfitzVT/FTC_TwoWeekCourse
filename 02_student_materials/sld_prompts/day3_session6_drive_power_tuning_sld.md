# Drive Power / Motor Tuning SLD

## Session / Course Phase

Day 3, Session 6: Chassis Readiness, Controller Mapping, and Drive Tuning

## Why This Discussion Matters

Your team has chosen or narrowed how the robot should be controlled. Now you need to decide how strongly the robot should respond when the driver uses those controls.

```text
Controller mapping decides what the buttons/sticks do.
Motor tuning decides how strongly the robot responds.
```

A robot that is too fast may be hard to control. A robot that is too slow may be easy to control but too slow for scoring loops. A good starting value balances control, accuracy, safety, and speed.

This is a design decision based on evidence, not just a guess or a choice to use maximum power.

SLD is the process. The deliverable is the work product that comes out of the discussion.

## Main Discussion Question

What motor power settings give our team the best balance of control, accuracy, speed, and safety for the robot behaviors we need?

Student version:

How fast should the robot move for each driving behavior so our drivers can control it well?

## What This Discussion Must Produce

By the end of this SLD, your team should record a Drive Power / Motor Tuning Decision that includes:

- starting power level for forward/backward driving
- starting power level for turning
- starting power level for precision movement or slow mode, if used
- whether the team wants one speed or multiple speed modes
- evidence from power-level trials
- driver/operator notes
- which robot behaviors the power settings support
- biggest concern or tradeoff
- next tuning test or code revision

Your team may choose different power settings for different movements. Examples include:

- forward/backward power
- turning power
- slow/precision mode power
- lining-up power
- parking power

You do not need all of these today. Use them as a starting framework.

## Evidence / Resources to Use

Use evidence from at least three sources. Do not choose maximum speed just because it seems powerful.

- Robot Behavior Specification
- Team Strategy Guide
- Controller Mapping SLD decision
- D-pad or joystick test trials
- motor power test data
- loop time data
- turning accuracy data
- line-up or parking accuracy data
- driver confidence notes
- driver/operator observations
- `DemoDriveDPad.java` or `DemoDriveJoy.java`
- SLD tally sheet

## Suggested Motor Power Test Data

Before discussing the final choice, review what happened at different power levels. The example values below are `0.4`, `0.6`, and `0.8`, but your team may use different values depending on the code and teacher directions.

| Movement / Skill | Power Setting | Trial 1 | Trial 2 | Trial 3 | Driver Notes |
|---|---:|---|---|---|---|
| Drive straight | 0.4 |  |  |  |  |
| Drive straight | 0.6 |  |  |  |  |
| Drive straight | 0.8 |  |  |  |  |
| Turn left/right | 0.4 |  |  |  |  |
| Turn left/right | 0.6 |  |  |  |  |
| Turn left/right | 0.8 |  |  |  |  |
| Line up with target | 0.4 |  |  |  |  |
| Line up with target | 0.6 |  |  |  |  |
| Line up with target | 0.8 |  |  |  |  |
| Park accurately | 0.4 |  |  |  |  |
| Park accurately | 0.6 |  |  |  |  |
| Park accurately | 0.8 |  |  |  |  |

## Tradeoff Review

| Power Setting | What worked well? | What was hard to control? | Best use |
|---|---|---|---|
| Low power |  |  |  |
| Medium power |  |  |  |
| High power |  |  |  |

## Discussion Roles

One person may hold more than one role if your team is small.

| Role | Job |
|---|---|
| Facilitator | Keeps the team focused on evidence and the decision record. |
| Tally keeper | Uses the SLD tally sheet. |
| Recorder | Records the power/tuning decision. |
| Data checker | Points to power trial results before claims are accepted. |
| Driver representative | Explains what the robot felt like at different speeds. |
| Safety checker | Asks whether any setting makes the robot unsafe or hard to stop. |
| Behavior checker | Asks which power settings support the Robot Behavior Specification. |

## Sentence Stems

Use these stems to make claims, use evidence, and name tradeoffs.

```text
At low power, the robot was easier/harder to control because ___.
At medium power, the robot ___.
At high power, the robot ___.
The data shows that ___.
For driving straight, I think we should use ___ because ___.
For turning, I think we should use ___ because ___.
For lining up or parking, I think we should use ___ because ___.
A slow mode would help when ___.
A higher speed would help when ___.
One risk of using too much power is ___.
One risk of using too little power is ___.
This power setting supports our robot behavior plan because ___.
Before we finalize, we should test ___.
I could support this tuning choice if ___.
```

## Decision Record / Work Product

| Drive Power / Motor Tuning Decision | Team Response |
|---|---|
| Controller mapping used for this tuning decision |  |
| Forward/backward power setting |  |
| Turning power setting |  |
| Slow/precision mode power setting, if used |  |
| Lining-up or parking power setting, if different |  |
| Do we need one speed or multiple speed modes? |  |
| Best evidence from low-power trials |  |
| Best evidence from medium-power trials |  |
| Best evidence from high-power trials |  |
| Driver/operator observations |  |
| Biggest speed/control tradeoff |  |
| Safety concern, if any |  |
| Next tuning test or code revision |  |
| Can all team members support this starting tuning plan? |  |

## Motor Tuning Readiness Check

Before recording our decision, our team has:

- [ ] Confirmed the chassis was safe enough for powered testing.
- [ ] Chosen or narrowed a controller mapping approach.
- [ ] Tested at least two power levels.
- [ ] Tested forward/backward movement.
- [ ] Tested turning.
- [ ] Tested one precision task such as lining up or parking.
- [ ] Collected at least one type of driving data.
- [ ] Heard from at least one driver.
- [ ] Checked the Robot Behavior Specification.
- [ ] Named one speed/control tradeoff.
- [ ] Recorded the starting power settings.
- [ ] Named the next tuning test or code revision.

## SLD Tally Sheet Reminder

Use `90_templates/student_led_discussion_tally_sheet_template.md` or the generated site version of that template.

Use the SLD tally sheet to track discussion moves: Q, C, E, B, O, D, X.

At the end, record one discussion strength and one target for the next design or testing SLD.

## Portfolio Connection

Add the Drive Power / Motor Tuning Decision Record to the engineering portfolio. Include:

- power test data
- final starting power settings
- driver/operator notes
- speed/control tradeoff accepted
- slow mode decision, if any
- next tuning target

Update the controls/programming or chassis/drivetrain copy of the Subsystem Design Cycle Template if the tuning decision changes how the robot will be programmed, tested, or driven.

## Growth Target for Next Design or Testing SLD

During the next design or testing SLD, our team should improve by:

- using more data
- comparing tradeoffs more clearly
- inviting quieter voices
- listening to driver/operator experience
- recording decisions more clearly
- connecting tuning choices to robot behaviors
