# Session 12 Reading: Intro to Servos and Positions

## What a Servo Does

A servo can move a small mechanism to a controlled position. Robots often use servos for triggers, gates, arms, small linkages, and latches.

Servos do not provide a lot of torque compared with drivetrain motors. They are useful for moving light parts, pushing a light ball, or releasing a small latch. They should not be expected to lift heavy parts, crush balls, or fight the full force of a jammed mechanism.

## Servo Vocabulary

A **servo** is a small motor unit that can move a mechanism in a controlled way.

A **standard servo** moves to a position and tries to hold that position.

A **continuous rotation servo** spins like a small motor instead of moving to one fixed angle.

A **servo horn** is the plastic or metal arm attached to the servo output shaft.

A **linkage** is a connected part that transfers servo motion to another part of the robot.

A **position** is the commanded place where a standard servo should move.

**Range of motion** means how far the servo and attached mechanism can move.

A **degree** is a unit used to measure an angle.

An **angle** describes how far something has turned.

**Torque** is twisting force. A servo with more torque can push or hold a stronger mechanism. A servo with low torque may work for a light trigger but fail if it has to push a heavy or jammed part.

A **stall** happens when a motor or servo is trying to move but cannot.

**Strain** means the servo or linkage is under too much force.

**Buzzing** can be a sign that the servo is fighting a blocked mechanism or trying to hold a difficult position.

An **endpoint** is one end of the safe motion range.

A **trigger** is a part that controls when a ball is released.

A **latch** is a part that holds something until it is released.

A **gate** blocks or allows motion through an opening.

A **release** is the action of letting a ball or part move.

## Standard Servo vs. Continuous Rotation Servo

| Type | What it does | Code meaning |
|---|---|---|
| Standard servo | Moves to a position and holds it | `0.0` to `1.0` means position |
| Continuous rotation servo | Spins like a small motor | Power controls speed and direction |

Standard servos are usually controlled with `setPosition()`:

```java
triggerServo.setPosition(0.0);
triggerServo.setPosition(0.5);
triggerServo.setPosition(1.0);
```

`0.0` is one end of the servo's range. `0.5` is near the middle. `1.0` is the other end of the range.

These values are not written in degrees. The physical angle depends on the servo model, mounting, horn position, and linkage.

## Why Servo Direction Feels Confusing

Moving toward `1.0` does not always mean right, left, open, closed, up, or down. It depends on how the servo is mounted.

The code tells the servo to move toward a position. The robot design determines whether that motion opens, closes, pushes, pulls, raises, or lowers something.

That means the same code can do different physical things on different robots.

## Do Not Force a Servo

If the servo is commanded to a position it cannot physically reach, it may buzz, strain, heat up, or damage the servo or linkage.

Test small position changes. Make sure the mechanism can move freely before using a larger motion.

If the servo buzzes or the linkage bends, stop and check what is blocking the motion.

## Reflection

Why might the same servo code open a trigger on one robot but close a trigger on another robot?
