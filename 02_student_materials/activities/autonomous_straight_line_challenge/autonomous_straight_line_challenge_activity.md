# Autonomous Straight-Line Challenge Guided Activity

Your team will collect data from your robot, build a function that converts inches to encoder ticks, use the function in autonomous code, and test how close your robot gets to a target distance.

```text
Experiment -> Data -> Function -> Code -> Test -> Revise
```

Use this activity after reading `02_student_materials/readings/day4_session7_autonomous_encoder_experiment_background.md`.

## 1. Readiness Check

Before starting the challenge, confirm:

- [ ] Our chassis can move safely.
- [ ] Our motors are configured correctly.
- [ ] Our robot can drive forward.
- [ ] We know which motor power setting we will use for the first model.
- [ ] We have a tape measure or measuring tool.
- [ ] We have a clear starting line.
- [ ] We know how we will measure forward distance.
- [ ] We know how we will measure sideways drift.
- [ ] We have read or reviewed the autonomous encoder background reading.

If your chassis is not ready, your Session 7 pathway is to keep working on chassis readiness, controller mapping, or drive tuning.

## 2. Challenge by Choice

| Level | Goal | Evidence / Work Product |
|---|---|---|
| Must | Collect encoder-distance data and make a prediction. | Data table and predicted ticks for a target distance |
| Should | Use Desmos to build a linear model. | Equation or screenshot of model |
| Could | Use the model in autonomous code. | `inchesToTicks()` or `moveForwardInches()` code snippet |
| Super Challenge | Improve accuracy or straightness. | Drift data, revised model, power comparison, or correction strategy |

## 3. Phase 1: Design the Experiment

Recommended beginner approach:

> Choose several encoder tick targets, run the robot, and measure how far it travels. Then use the data to build a model that predicts ticks from inches.

You may also choose fixed target distances and record the encoder ticks needed, if your teacher gives that option.

| Experiment Choice | Team Plan |
|---|---|
| Motor power for first model |  |
| Short encoder target or distance |  |
| Medium encoder target or distance |  |
| Long encoder target or distance |  |
| Number of trials at each setting |  |
| Where we measure from on the robot |  |
| How we measure forward distance |  |
| How we measure sideways drift |  |
| Who runs the robot |  |
| Who measures distance |  |
| Who records data |  |
| Who enters data into Desmos |  |
| Who edits or reviews code |  |

Keep motor power constant for the first model. If you change power, you may need a new model.

## 4. Phase 2: Collect Data

Start from the same line each time.

Measure from the same point on the robot each time.

Record sideways drift separately from forward distance.

Write notes about slipping, turning, stopping late, or starting crooked.

| Trial | Encoder Ticks | Motor Power | Distance Traveled (inches) | Sideways Drift (inches) | Notes |
|---|---:|---:|---:|---:|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |

## 5. Phase 3: Build the Function

The input is the target distance in inches. The output is the encoder ticks the robot should move.

Coding-focused model:

```text
ticks = m x inches + b
```

Simpler proportional model:

```text
ticks = ticks_per_inch x inches
```

| Model Item | Team Response |
|---|---|
| Model type: proportional or linear regression |  |
| Slope `m` or ticks per inch |  |
| Intercept `b`, if used |  |
| Our function for ticks from inches |  |
| Desmos equation or screenshot location |  |

## 6. Phase 4: Program the Function

Record your model values and code plan before editing the autonomous program.

```java
public int inchesToTicks(double inches) {
    double m = ___;  // ticks per inch from our model
    double b = ___;  // intercept, or 0 if not using one
    return (int)Math.round(m * inches + b);
}
```

Then use the function:

```java
int targetTicks = inchesToTicks(36);
```

Or use a movement method:

```java
moveForwardInches(36);
```

Use the OnBot Java examples in `02_student_materials/code_examples/onbot_java/` as code-organization references. This activity does not require a full new OpMode by itself.

| Code Item | Team Response |
|---|---|
| Method name we are using |  |
| Value of `m` |  |
| Value of `b` |  |
| Motor power used in autonomous |  |
| Target test distance |  |
| Predicted encoder ticks |  |
| Code file / OpMode used |  |

## 7. Phase 5: Test the Function

Use your function to predict ticks for a target distance, then test the robot.

```text
error = actual distance - target distance
absolute error = |actual distance - target distance|
```

Optional challenge score:

```text
challenge score = absolute distance error + sideways drift
```

Your teacher may choose whether drift is part of the contest score.

| Target Distance (inches) | Predicted Ticks | Actual Distance | Distance Error | Absolute Error | Sideways Drift | Notes |
|---:|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## 8. Phase 6: Revise

| Question | Team Response |
|---|---|
| What did our model predict well? |  |
| What did our model not predict well? |  |
| Did the robot drift? Which direction? |  |
| Did the robot overshoot or stop short? |  |
| Did power level seem too high, too low, or about right? |  |
| What should we revise: data, model, code, power, alignment, or robot build? |  |
| What is our next test? |  |

## 9. Engineering Portfolio Evidence

Add the work from this challenge to the engineering portfolio.

## Portfolio Checklist

- [ ] Experiment plan
- [ ] Encoder-distance data table
- [ ] Desmos model or equation
- [ ] `inchesToTicks()` or autonomous code snippet
- [ ] Challenge test result
- [ ] Error and drift measurement
- [ ] Revision note
- [ ] Photo/video evidence if available

## 10. Optional Competition Rules

Your teacher may give a mystery target distance. Your team will use your model to calculate encoder ticks and run one autonomous attempt. The closest robot wins.

Optional scoring:

```text
distance-only score = absolute distance error
distance + drift score = absolute distance error + sideways drift
```
