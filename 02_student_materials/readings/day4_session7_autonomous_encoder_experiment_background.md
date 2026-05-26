# Autonomous Encoder Experiment Background

## Why This Matters

In TeleOp, the driver sends commands with the gamepad.

In autonomous, the code tells the robot what to do.

For the Autonomous Straight-Line Challenge, your team will give the robot a target distance. The code will convert that distance into encoder ticks. Then the motors will run until they reach the target encoder position.

The goal is not just to make the robot move. The goal is to use data, a model, and code to make the robot drive a target distance as accurately and straight as possible.

The pipeline looks like this:

```text
robot motion
-> motor encoder data
-> distance measurement
-> experimental design
-> linear function
-> Desmos regression
-> inches-to-ticks conversion
-> autonomous method
-> test and revise
```

## What Autonomous Code Does

Autonomous code runs without the driver holding the controller. A simple autonomous program might tell the robot:

1. Reset the motor encoders.
2. Set a target encoder position.
3. Turn on the motors.
4. Stop when the target position is reached.

This can make the robot more repeatable than human driving, but it is not automatically perfect. The robot can still slip, drift, overshoot, or stop short.

## What Motor Encoders Measure

A motor encoder counts rotation.

The encoder does not directly measure how far the robot moved across the floor. It counts motor movement.

Depending on the motor and system, the encoder may count rotations or partial rotations of the motor shaft. That count is often called ticks or counts.

If the motor turns more, the encoder count changes more. But that does not automatically tell us the exact number of inches the robot traveled.

## Wheels, Gears, and Distance

Wheel size matters. A wheel with a larger diameter travels farther in one rotation than a smaller wheel. Wheel circumference is approximately pi times diameter.

Gears also matter. Some motors or drivetrains use gears. Gears can change how motor rotation relates to wheel rotation.

In theory, you could calculate distance from:

- encoder ticks per motor rotation
- gear ratio
- wheel diameter
- wheel circumference

That theory is useful, but the real robot is messier. Motors, gears, wheels, friction, battery level, floor surface, and slipping all affect the result.

Because motors, gears, wheels, friction, and slipping all affect the result, this activity uses direct measurement. We compare encoder ticks to the actual distance the robot travels.

Theory helps us understand what should happen. Data tells us what our robot actually does.

## The Function We Need

For coding, think about the problem as an input and an output.

```text
Input: target distance in inches
Output: encoder ticks needed
```

A common model is a linear function:

```text
ticks = m x inches + b
```

In this equation:

- `m` is the slope, or about how many encoder ticks are needed per inch.
- `b` is the intercept, or a small adjustment in the model.

Some teams may use a simpler proportional model:

```text
ticks = ticks_per_inch x inches
```

A linear model makes sense because traveling about twice as far usually requires about twice as many encoder ticks.

## Planning the Experiment

Plan the experiment before collecting data. Changing too many things at once makes it hard to know what caused the result.

Good experiment choices:

- Choose short, medium, and long test distances or encoder targets.
- Keep motor power constant for the first model.
- Start from the same line each time.
- Measure from the same point on the robot each time.
- Keep the floor surface the same.
- Repeat trials when possible.
- Record notes about slipping, turning, or inconsistent starts.
- Measure sideways drift separately from forward distance.

For the first model, change only the encoder target or distance. Keep power, start location, robot setup, and measurement method as consistent as possible.

## Sources of Error

Error means the robot did not move exactly the way the model predicted.

Common sources of error include:

- wheel slip
- floor friction
- carpet/tile differences
- battery power
- different motor power settings
- robot not starting straight
- loose wheels or loose chassis parts
- unequal left/right motor behavior
- wheel diameter differences
- weight distribution
- momentum after the code tells the motor to stop
- lag between reaching an encoder target and the robot physically stopping
- measuring from a different point on the robot each time

If repeated trials give similar results, we can be more confident in the model.

If the robot travels different distances each time, we should be less confident and collect more data or fix the robot.

## Power, Momentum, and Overshoot

Motor power affects the model.

High power may cause:

- more wheel slip
- more overshoot
- more drift
- less precise stopping

Low power may cause:

- better control
- less overshoot
- slower movement
- inconsistent starts if the power is too low

Use one power setting while building the first model. If you change power, you may need a new model.

## Drift and Straightness

The robot can travel the right forward distance but still drift sideways.

Measure two things:

```text
forward distance traveled
sideways drift from the intended straight path
```

Forward distance tells you whether the inches-to-ticks model is close.

Sideways drift tells you whether the robot is driving straight.

Treat drift as a separate problem from distance prediction. If the forward distance is close but the robot drifts right, the team may keep the distance model and investigate wheel alignment, motor balance, weight distribution, or floor friction.

## Completed Example: Data to Code

This sample team tested different encoder targets at the same motor power. They measured how far the robot actually traveled.

| Trial | Encoder Ticks | Power | Distance Traveled (inches) | Sideways Drift (inches) | Notes |
|---|---:|---:|---:|---:|---|
| 1 | 500 | 0.5 | 10.5 | 0.5 | slight right drift |
| 2 | 1000 | 0.5 | 21.3 | 0.8 | fairly straight |
| 3 | 1500 | 0.5 | 31.8 | 1.4 | more right drift |
| 4 | 2000 | 0.5 | 42.6 | 2.0 | slight overshoot |

The team wants a model:

```text
ticks = m x inches + b
```

After graphing the data and using a regression in Desmos, the team gets this example model:

```text
ticks = 46.8 x inches + 8
```

For a 36-inch target:

```text
ticks = 46.8 x 36 + 8
ticks = 1692.8
```

So the team would use about:

```text
1693 encoder ticks
```

## Turning the Model Into Code

The model can become a method in Java:

```java
public int inchesToTicks(double inches) {
    double m = 46.8;  // encoder ticks per inch from our model
    double b = 8.0;   // intercept from our model
    return (int)Math.round(m * inches + b);
}
```

Then the autonomous code can use the method:

```java
int targetTicks = inchesToTicks(36);
```

Or a team might create a method that hides the conversion inside the movement command:

```java
moveForwardInches(36);
```

The important idea is that the code is using the team's data model, not just a guess.

## Checking the Result

Suppose the team tests the 36-inch target.

```text
target distance = 36 inches
actual distance = 35 inches
error = actual - target = -1 inch
absolute error = 1 inch
sideways drift = 1.5 inches
```

The robot was close in forward distance, but it still drifted sideways.

The team might keep the distance model but investigate the cause of drift.

Possible next questions:

- Did one wheel slip more than the other?
- Are the left and right motors behaving the same way?
- Is one wheel rubbing?
- Is the robot starting straight?
- Is weight balanced unevenly?
- Does lower power reduce drift or overshoot?

## Before You Start the Challenge

Make sure your team can explain:

- [ ] What an encoder measures.
- [ ] Why encoder ticks are not the same as inches.
- [ ] Why gears, wheel size, friction, and slipping can affect the result.
- [ ] Why we compare encoder ticks to measured distance.
- [ ] Why short, medium, and long trials help.
- [ ] Why motor power should stay constant for the first model.
- [ ] How drift is different from forward distance error.
- [ ] What the input and output of the function are.
- [ ] How the function helps the autonomous program.
