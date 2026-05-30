# Controller Mapping Drive Comparison Activity

## Purpose

Use evidence to decide how your team should control the frame/drivetrain subsystem.

You will compare two drive-only OpModes:

- [`DemoDriveDPad.java`](../../code_examples/onbot_java/DemoDriveDPad.java): D-pad and bumper driving with helper methods.
- [`DemoDriveJoy.java`](../../code_examples/onbot_java/DemoDriveJoy.java): joystick arcade driving with direct motor-power math.

Use the [OnBot Java code examples README](../../code_examples/onbot_java/README.md) before copying either file.

This is a controller-mapping decision. Your choice should support your Robot Behavior Specification, your Subsystem Design Cycle evidence, and your team strategy.

## Before You Start

Make sure your team has:

- a frame/drivetrain subsystem that is mechanically safe to test,
- Robot Controller configuration names `leftDrive` and `rightDrive`,
- wheels lifted for the first powered test,
- a test area with clear boundaries,
- one driver, one safety watcher, and one recorder.

Do not add shooter, hopper, trigger, or servo code during this activity. Test the drivetrain subsystem by itself first.

## Step 1: Run `DemoDriveDPad`

Copy `DemoDriveDPad.java` into OnBot Java, build it, and run it safely.

Record what happens when the driver uses:

- D-pad up
- D-pad down
- left bumper
- right bumper

## Step 2: Run `DemoDriveJoy`

Copy `DemoDriveJoy.java` into OnBot Java, build it, and run it safely.

Record what happens when the driver uses:

- left stick Y for forward/back
- right stick X for turning

## Drive Test Comparison

| Test | D-pad Drive Result | Joystick Drive Result | Notes |
|---|---|---|---|
| Drive straight 6 feet |  |  |  |
| Turn 90 degrees |  |  |  |
| Line up with goal |  |  |  |
| Park in target area |  |  |  |
| Avoid contact zone |  |  |  |

## Discussion Questions

Answer with evidence from testing.

| Question | Team Response |
|---|---|
| Which control scheme was easier for new drivers? |  |
| Which control scheme was smoother? |  |
| Which control scheme made turning easier? |  |
| Which control scheme made aiming or lining up easier? |  |
| Which control scheme helped avoid contact? |  |
| Which control scheme better supports scoring loops? |  |
| Which code file was easier to read? |  |
| Which code file would be easier to modify? |  |
| What changes would your team make before using this in a match? |  |

## Code Organization Challenge

`DemoDriveDPad` uses helper methods such as `driveForward()` and `allStop()`.

`DemoDriveJoy` puts the joystick math directly inside the main loop.

Challenge: rewrite `DemoDriveJoy` using helper methods so the main loop is easier to read.

Possible helper methods:

- `driveWithJoystick()`
- `setDrivePower(leftPower, rightPower)`
- `clipPower(power)`
- `showDriveTelemetry(drive, turn, leftPower, rightPower)`

## Decision Statement

Our team will use ______________________________ because ______________________________.

Evidence from our tests:

______________________________________________________________________________

Control changes we need before match use:

______________________________________________________________________________
