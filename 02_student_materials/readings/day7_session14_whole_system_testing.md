# Session 14 Reading: Whole-System Testing

## Separate Parts Become One Robot

A robot is a system of connected subsystems. The drivetrain, flywheel, hopper, servo trigger, battery, wires, frame, and driver controls may each work separately but still cause problems when used together.

Whole-system testing helps your team find those interactions before the final challenge.

## System Vocabulary

A **system** is a group of parts that work together.

A **subsystem** is one part of the robot that has its own job. The drivetrain is a subsystem because it moves the robot. The hopper is a subsystem because it stores and feeds balls. Subsystems must work together for the whole robot to work.

An **interaction** is when one part of the robot affects another part.

A **whole-system test** uses the robot the way it will be used in a challenge.

A **sequence** is the order of actions the driver or robot follows.

A **driver routine** is a repeated set of driver actions.

To **load** means to place or feed a ball into the ready position.

To **fire** means to release or push a ball into the flywheel so it launches.

To **reload** means to prepare the next ball.

To **reset** means to return the trigger or mechanism to its starting position.

**Interference** happens when one part blocks, hits, or disrupts another part.

**Vibration** is shaking that can loosen parts or change alignment.

A **loose connection** is a wire, fastener, or plug that is not secure.

**Reliability** means the robot works repeatedly without constant repair.

**Consistency** means the robot behaves in a similar way each time.

A **stress test** checks whether the robot still works after repeated use.

A **failure point** is the place most likely to stop working first.

A **refinement** is a small improvement based on evidence.

## What Is Whole-System Testing?

Whole-system testing means operating the robot like it will be used in a challenge:

- Drive or position the robot.
- Turn on the flywheel.
- Load or allow a ball to feed.
- Fire one ball.
- Reset the trigger.
- Reload.
- Fire again.
- Repeat.

A robot can pass a single-part test but fail during a full routine.

Examples:

- The hopper works until the robot moves and shakes.
- The servo works until the hopper presses on it.
- The flywheel works until several shots slow it down.
- The battery is fine until it slides and pulls on a wire.
- The drivetrain works until loose wires touch the wheels.
- The trigger works once but does not reset reliably.

## Subsystems Can Interact

| Subsystem Interaction | Possible Problem |
|---|---|
| Hopper + servo | Ball stack presses on trigger and servo strains |
| Flywheel + hopper | Balls enter too quickly and flywheel loses speed |
| Battery + drivetrain | Battery shifts and changes balance or pulls wires |
| Wires + wheels | Loose wires rub against moving parts |
| Frame + shooter | Shooter angle changes when frame flexes |
| Driver + mechanism | Driver fires before flywheel recovers speed |

## Build a Repeatable Operating Sequence

Write a simple driver routine, such as:

1. Aim or position robot.
2. Press Y to turn on flywheel.
3. Wait one second.
4. Press B to release one ball.
5. Press A to reset trigger.
6. Wait for flywheel to recover.
7. Repeat.

Good robots are not only designed; they are also operated consistently.

## Whole-System Test Log

| Run # | Sequence Tested | What Worked | What Failed | Next Adjustment |
|---:|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## Reflection

Which part worked alone but caused a problem when the whole robot operated together?
