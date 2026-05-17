# Session 8 Reading: Wiring, Configuration, and First Drive

## From Physical Robot to Code

Wiring and configuration connect the physical robot to the Java code. The robot cannot guess which motor is the left drive motor or which port has the shooter motor. Your team has to wire parts carefully, name them clearly, and use the same names in the program.

The key idea is simple: the robot configuration name must exactly match the name used in the Java code.

## Wiring and Code Vocabulary

The **Control Hub** is the main robot device that connects to motors, servos, sensors, power, and the Robot Controller system.

An **Expansion Hub** is an extra hub that can add more ports on some robots.

A **motor port** is a numbered place on the hub where a motor wire plugs in.

A **servo port** is a numbered place on the hub where a servo cable plugs in.

A **wire** carries electrical power or signals.

A **cable** is a covered group of wires or a finished wire connection.

A **connector** is the end of a wire or cable that plugs into a port.

A **battery** provides power to the robot.

A **power switch** turns robot power on and off.

A **configuration** is the Robot Controller setup that names the hardware plugged into the hub.

The **hardware map** is the FTC code tool that connects Java names to configured robot hardware.

A **variable** is a name in code that stores a value or object.

An **object** is a software version of something the robot can use, such as a motor.

A **DcMotor** is the FTC Java class used to control a DC motor.

**TeleOp** is the driver-controlled part of the match and also a common name for driver-control programs.

An **OpMode** is a robot program that appears on the Driver Station.

A **gamepad** is the controller the driver uses.

The **Driver Station** is the device drivers use to select OpModes and control the robot.

The **Robot Controller** is the robot-side system that runs the code and controls the hardware.

## Names Must Match

Look at this code:

```java
leftDrive = hardwareMap.get(DcMotor.class, "leftDrive");
rightDrive = hardwareMap.get(DcMotor.class, "rightDrive");
shooterMotor = hardwareMap.get(DcMotor.class, "shooterMotor");
```

In the first line, `leftDrive` before the equals sign is the Java variable name. It is the name the code uses for the motor object.

The `"leftDrive"` inside quotation marks is the configuration name. That quoted name must match the Robot Controller configuration exactly.

Capital letters matter. Spaces and underscores matter. `leftDrive`, `LeftDrive`, `left_drive`, and `left drive` are different names to the robot.

## Example Configuration Table

| Physical part | Motor port | Configuration name | Java variable |
|---|---:|---|---|
| Left drive motor | 0 | `leftDrive` | `leftDrive` |
| Right drive motor | 1 | `rightDrive` | `rightDrive` |
| Shooter motor | 2 | `shooterMotor` | `shooterMotor` |

Your team's table may be different. What matters is that the wiring, configuration, and code agree.

## First-Drive Testing Checklist

- Place the robot on blocks or lift the wheels off the floor.
- Turn on robot power.
- Connect the Driver Station.
- Select the correct TeleOp.
- Press INIT.
- Press START.
- Test one button at a time.
- Keep hands away from moving wheels.
- Stop the OpMode before changing wires.
- Write down what happened before changing code or configuration.

## Reflection

Why is it useful to test the robot with the wheels off the floor before driving it on the ground?
