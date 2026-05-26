# Autonomous Encoder Experiment Design SLD

## Session / Course Phase

Day 4, Session 7: Build Drivetrain/Chassis and Ready-Team Autonomous Extension

## Why This Discussion Matters

Autonomous code needs a model.

A model needs data.

Good data starts with a good experiment plan.

This SLD is not about arguing over the perfect experiment. It is about making a clear, testable plan so your team can collect useful data quickly.

SLD is the decision process. The experiment plan is the work product.

## Main Discussion Question

What data should we collect so our robot can use a model to drive a target distance as accurately and straight as possible?

Student version:

What experiment should we run so our robot can learn how many encoder ticks match a target distance?

## What This Discussion Must Produce

By the end of this SLD, your team should complete an Autonomous Encoder Experiment Plan that includes:

- motor power setting for the first model
- short test value
- medium test value
- long test value
- whether the team is using encoder targets or distance targets first
- number of trials
- measurement method for forward distance
- measurement method for sideways drift
- how the team will keep variables controlled
- team roles
- what will count as good enough evidence to start building the model
- first Desmos/modeling plan
- first autonomous challenge test plan

## Evidence / Resources to Use

Use evidence from:

- Autonomous Encoder Experiment Background Reading
- Autonomous Straight-Line Challenge Guided Activity
- Robot Behavior Specification
- Drive Power / Motor Tuning SLD decision
- Controller Mapping SLD decision
- current chassis performance evidence
- SLD tally sheet

Do not change many variables at once.

For the first model, keep motor power constant. If you change power, you may need a new model.

## Discussion Roles

One person may hold more than one role if your team is small.

| Role | Job |
|---|---|
| Facilitator | Keeps the team focused on creating an experiment plan. |
| Tally keeper | Uses the SLD tally sheet. |
| Recorder | Writes the experiment plan. |
| Measurement checker | Asks how distance and drift will be measured. |
| Variable-control checker | Asks what the team will keep the same each trial. |
| Driver/programmer representative | Checks whether the plan is realistic for the robot and code. |

## Sentence Stems

Use these stems to make claims, use evidence, and keep the experiment focused.

```text
The data we need most is ___ because ___.
For our short test, we should use ___ because ___.
For our medium test, we should use ___ because ___.
For our long test, we should use ___ because ___.
We should keep ___ constant because ___.
If we change ___, it might affect the distance because ___.
We should measure forward distance by ___.
We should measure drift by ___.
A source of error we need to watch for is ___.
This plan gives us enough evidence because ___.
Before we collect data, we need to check ___.
I could support this experiment plan if ___.
```

## Short / Medium / Long Test Planning

Your teacher may suggest values based on the space available. The goal is to collect data across a useful range, not just one distance.

| Test Level | Encoder Target or Distance | Why This Value? |
|---|---|---|
| Short |  |  |
| Medium |  |  |
| Long |  |  |

## Variable Control Plan

Changing too many things at once makes it hard to know what caused the result.

| Variable | What We Will Keep the Same |
|---|---|
| Motor power |  |
| Starting line |  |
| Starting robot alignment |  |
| Floor surface |  |
| Measurement point on robot |  |
| Measuring tool |  |
| Code / OpMode |  |
| Battery condition, if possible |  |

## Measurement Plan

| Measurement Question | Team Plan |
|---|---|
| How will we measure forward distance? |  |
| What point on the robot will we measure from? |  |
| How will we measure sideways drift? |  |
| Who will measure? |  |
| Who will record? |  |
| What notes will we record after each trial? |  |

## Roles for Data Collection

| Role | Student |
|---|---|
| Robot runner / driver |  |
| Safety watcher |  |
| Distance measurer |  |
| Drift measurer |  |
| Data recorder |  |
| Desmos/modeling lead |  |
| Code reviewer/editor |  |

## Decision Record / Work Product

| Experiment Design Decision | Team Response |
|---|---|
| Are we starting with encoder targets or distance targets? |  |
| Motor power setting for first model |  |
| Short test value |  |
| Medium test value |  |
| Long test value |  |
| Number of trials |  |
| Forward distance measurement method |  |
| Sideways drift measurement method |  |
| Variables we will keep constant |  |
| Biggest source of error we expect |  |
| What counts as enough data to build our model? |  |
| First Desmos/modeling step |  |
| First autonomous challenge target or test |  |
| Can all team members support this experiment plan? |  |

## Experiment Design Readiness Check

Before collecting data, our team has:

- [ ] Confirmed the chassis can move safely.
- [ ] Reviewed the background reading.
- [ ] Reviewed the guided activity sheet.
- [ ] Chosen a motor power setting to keep constant.
- [ ] Chosen short, medium, and long test values.
- [ ] Decided how many trials to run.
- [ ] Decided how to measure forward distance.
- [ ] Decided how to measure sideways drift.
- [ ] Assigned roles.
- [ ] Named one likely source of error.
- [ ] Decided what counts as enough evidence to build the model.

## SLD Tally Sheet Reminder

Use `90_templates/student_led_discussion_tally_sheet_template.md` or the generated site version of that template.

Use the SLD tally sheet to track discussion moves: Q, C, E, B, O, D, X.

At the end, record one discussion strength and one target for the next testing or revision discussion.

## Portfolio Connection

Add the experiment plan to the engineering portfolio.

The experiment plan is the first piece of evidence for your autonomous challenge. It shows that your team made a plan before collecting data.

Later, add:

- data table
- Desmos model or equation
- code snippet
- challenge result
- error and drift measurement
- revision note

## Growth Target for Data Collection and Testing

During data collection and testing, our team should improve by:

- following the plan carefully
- recording data clearly
- keeping variables controlled
- noticing sources of error
- using evidence before changing the model or code
