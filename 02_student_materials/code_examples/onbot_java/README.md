# OnBot Java Code Examples

These files are example FTC OpModes for OnBot Java.

Teams copy one Java file at a time into the Robot Controller OnBot Java TeamCode area. Keep the package line exactly as written:

```java
package org.firstinspires.ftc.teamcode;
```

The Robot Controller configuration names must match the code exactly:

| Robot part | Required configuration name |
|---|---|
| Left drive motor | `leftDrive` |
| Right drive motor | `rightDrive` |

Start with one drive-only OpMode:

- [`DemoDriveDPad.java`](DemoDriveDPad.java): D-pad and bumper driving organized with helper methods.
- [`DemoDriveJoy.java`](DemoDriveJoy.java): joystick arcade drive with direct motor-power math in the main loop.

Do not add shooter, hopper, trigger, or servo code until the drivetrain works. Test one subsystem at a time:

1. Confirm the code builds.
2. Confirm the OpMode appears on the Driver Station.
3. Test with wheels lifted.
4. Record what the robot actually did.
5. Change one thing at a time.

## Student Challenge

After testing both drive styles, rewrite `DemoDriveJoy` using helper methods so the main loop is easier to read.

Possible helper methods:

- `driveWithJoystick()`
- `setDrivePower(leftPower, rightPower)`
- `clipPower(power)`
- `showDriveTelemetry(drive, turn, leftPower, rightPower)`

The goal is not only to make the robot drive. The goal is to decide which control style supports your robot behavior goals and which code organization your team can safely modify.
