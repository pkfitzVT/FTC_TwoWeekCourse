# Session 4 Reading: Reading a Basic TeleOp Program

## The Big Idea

A TeleOp program listens to the gamepad and sends power commands to the robot’s motors.

The program usually follows this pattern:

1. Import the FTC tools the code needs.
2. Give the OpMode a name.
3. Create motor objects.
4. Connect the motor objects to the robot configuration.
5. Wait for the driver to press Start.
6. Repeatedly read the gamepad.
7. Send commands to the motors.
8. Stop the motors when no command is being given.

---

## The Package Line

At the top of the file, the code tells Java where this file belongs:

```java
package org.firstinspires.ftc.teamcode;
```

For this course, students do not need to change this line.

It helps organize the file inside the FTC robot app.

---

## Import Lines

Import lines give the program access to FTC classes.

For example:

```java
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
```

These imports let the program use FTC robot tools such as OpModes and motors.

---

## The TeleOp Name

This line controls the name that appears on the Driver Station:

```java
@TeleOp(name = "BasicDrive")
```

If the team selects `BasicDrive` on the Driver Station, this is the program that will run.

A clear name matters. During a match, teams are often rushed or nervous. A simple OpMode name helps the team avoid mistakes.

---

## The Class

The class is the main container for the program:

```java
public class BasicDrive extends LinearOpMode
```

For now, students should think of this as:

**This file defines a robot program called `BasicDrive`.**

`extends LinearOpMode` means the code runs as a step-by-step FTC OpMode.

---

## Motor Objects

The program creates motor objects:

```java
public DcMotor leftDrive = null;
public DcMotor rightDrive = null;
```

These are software names for physical motors.

At first, they are set to `null` because they have not yet been connected to the real configured hardware.

---

## Hardware Map

The hardware map connects software names to configured robot hardware:

```java
leftDrive = hardwareMap.get(DcMotor.class, "leftDrive");
rightDrive = hardwareMap.get(DcMotor.class, "rightDrive");
```

This is one of the most important parts of FTC programming.

The names in quotation marks must match the robot configuration exactly.

If the configuration says `leftDrive`, the code must also say `leftDrive`.

---

## Waiting for Start

This line pauses the program until the Driver Station starts the OpMode:

```java
waitForStart();
```

Code before this line is setup code.

Code after this line controls the robot during the active part of the OpMode.

---

## The Main TeleOp Loop

Most TeleOp programs contain a loop like this:

```java
while (opModeIsActive())
```

This means:

**As long as the OpMode is running, keep checking the gamepad and controlling the robot.**

Inside this loop, the robot repeatedly asks questions such as:

- Is the D-pad up pressed?
- Is the D-pad down pressed?
- Is a bumper pressed?
- Should the robot stop?

---

## Gamepad Inputs

The program can use gamepad inputs such as:

```java
gamepad1.dpad_up
gamepad1.dpad_down
gamepad1.left_bumper
gamepad1.right_bumper
```

These are **Boolean inputs**. That means each one is either true or false.

If `gamepad1.dpad_up` is true, the robot should drive forward.

If no drive button is pressed, the robot should stop.

---

## Helper Methods

Instead of writing motor commands directly inside the loop every time, the program can use helper methods:

```java
driveForward(power);
driveBackward(power);
turnLeft(power);
turnRight(power);
allStop();
```

These methods make the code easier to read.

A driver thinks:

**Go forward.**

The code says:

```java
driveForward(power);
```

That is much easier to understand than reading motor power numbers every time.

---

## Motor Power

Motors are controlled with values from `-1.0` to `1.0`.

Examples:

- `0.0` means stopped.
- `0.5` means half power in one direction.
- `1.0` means full power in one direction.
- `-0.5` means half power in the opposite direction.

Because the left and right motors are often mounted facing opposite directions, one motor may need positive power while the other needs negative power for the robot to drive straight.

---

## All Stop

Every TeleOp program needs a safe way to stop the robot.

The `allStop()` method sets both drive motors to zero:

```java
leftDrive.setPower(0);
rightDrive.setPower(0);
```

Without this, the robot might keep moving after the driver releases the button.

---

## BasicDrive Example

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;

@TeleOp(name = "BasicDrive")
public class BasicDrive extends LinearOpMode {

    public DcMotor leftDrive = null;
    public DcMotor rightDrive = null;

    public void runOpMode() {

        leftDrive = hardwareMap.get(DcMotor.class, "leftDrive");
        rightDrive = hardwareMap.get(DcMotor.class, "rightDrive");

        double power = 0.5;

        waitForStart();

        while (opModeIsActive()) {

            if (gamepad1.dpad_up) {
                driveForward(power);
            }
            else if (gamepad1.dpad_down) {
                driveBackward(power);
            }
            else if (gamepad1.left_bumper) {
                turnLeft(power);
            }
            else if (gamepad1.right_bumper) {
                turnRight(power);
            }
            else {
                allStop();
            }
        }
    }

    public void driveForward(double power) {
        leftDrive.setPower(-power);
        rightDrive.setPower(power);
    }

    public void driveBackward(double power) {
        leftDrive.setPower(power);
        rightDrive.setPower(-power);
    }

    public void turnLeft(double power) {
        leftDrive.setPower(power);
        rightDrive.setPower(power);
    }

    public void turnRight(double power) {
        leftDrive.setPower(-power);
        rightDrive.setPower(-power);
    }

    public void allStop() {
        leftDrive.setPower(0);
        rightDrive.setPower(0);
    }
}
```

---

## Key Vocabulary

**Import** — a line that gives the program access to code from another class or library.

**Class** — the main container for a Java program.

**Variable** — a name that stores a value or object.

**DcMotor** — an FTC class used to control a DC motor.

**hardwareMap** — the FTC tool that connects code names to configured robot hardware.

**Boolean** — a value that is either true or false.

**Loop** — code that repeats.

**Method** — a named action or function in Java.

**Motor power** — a number from `-1.0` to `1.0` that tells a motor how fast and which direction to spin.

---

## Think About It

Why is `allStop()` just as important as `driveForward()`?

---

## Engineering Notebook

Record:

- the name of the TeleOp,
- which gamepad buttons control each movement,
- the motor names used in the code,
- one change your team made,
- what happened when you tested it,
- and whether the problem was caused by code, wiring, configuration, or driving.
