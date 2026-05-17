# Session 4 Reading: How FTC Robot Programs Connect to the Robot

## The Big Idea

A robot program is a set of instructions that connects the driver’s choices to the robot’s hardware.

When a driver presses a button or moves a joystick, the robot program reads that input. Then the program sends commands to motors, servos, and other parts of the robot.

The basic connection looks like this:

**Driver Station → OpMode → Java code → hardware configuration names → motors and servos**

If any part of that chain is wrong, the robot may not move the way the team expects.

---

## What Is OnBot Java?

OnBot Java is a programming tool that runs through the Robot Controller. Students can open it in a web browser, write Java code, build the code, and run the program on the robot.

In this course, each robot should start with at least one working TeleOp program. A TeleOp program lets human drivers control the robot during the driver-controlled part of a match.

---

## What Is an OpMode?

An **OpMode** is a robot program that appears on the Driver Station.

When your team selects an OpMode and presses **Start**, the robot runs that program.

For this course, most teams will use one main TeleOp OpMode. That is helpful because during a match, teams can get nervous. If there is only one main TeleOp choice, it is harder to select the wrong program.

---

## The Configuration File Connects Names to Hardware

The robot has motors and servos plugged into numbered ports on the Control Hub.

The configuration file gives each piece of hardware a name.

For example:

- Motor port 0 might be named `leftDrive`
- Motor port 1 might be named `rightDrive`
- A shooter motor might be named `shooterMotor`

The Java code must use the exact same names.

If the configuration file says:

```java
leftDrive
```

but the code says:

```java
driveLeft
```

the robot will not know which motor the code means.

Spelling, capitalization, and spacing matter.

---

## Objects, Methods, and Inputs

FTC Java code uses **objects**.

An object is a thing in the program that represents something the robot can use.

For example:

```java
leftDrive
```

can be a software object that represents the physical left drive motor.

Objects have **methods**.

A method is an action the object can do.

For example:

```java
leftDrive.setPower(0.5);
```

means:

**Tell the `leftDrive` motor to run at 50% power.**

The input to the method is the value inside the parentheses.

In this example:

```java
0.5
```

is the input.

So this line has three important parts:

- **Object:** `leftDrive`
- **Method:** `setPower`
- **Input / parameter:** `0.5`

Together, they mean:

**Set the power of the left drive motor to 0.5.**

---

## What Is a Function?

A **function** is a named group of instructions.

In Java, functions inside a class are usually called **methods**.

Instead of writing the same motor commands again and again, a team can create a method such as:

```java
driveForward(power);
```

That method can contain the motor commands needed to drive forward.

Functions help programmers:

- organize code,
- avoid repeating the same lines,
- make code easier to read,
- and connect code to human ideas.

A method named `driveForward()` is easier to understand than two separate motor-power lines with no explanation.

---

## Why Start Simple?

A simple robot program is easier to test.

At first, the goal is not to make the most advanced code. The goal is to make a program that works, is easy to understand, and can be changed safely.

Good teams ask:

- Does the program build?
- Does the correct OpMode appear on the Driver Station?
- Do the hardware names match the configuration file?
- Does each button do what we expect?
- Can someone else on the team explain the code?

---

## Key Vocabulary

**Robot Controller** — the device or Control Hub that runs the robot program.

**Driver Station** — the device used by the drivers to select OpModes and control the robot.

**OnBot Java** — a browser-based tool for writing Java robot programs on the Robot Controller.

**OpMode** — an operational mode; a robot program that can be selected and run from the Driver Station.

**TeleOp** — the driver-controlled part of the match.

**Configuration file** — the robot setup file that names the motors, servos, and sensors connected to the Control Hub.

**Object** — a software representation of something the program can use, such as a motor.

**Method** — an action that an object can perform.

**Input / Parameter** — information given to a method, usually inside parentheses.

**Function** — a named group of instructions. In Java, functions inside a class are called methods.

---

## Think About It

Why is it important for the names in the configuration file to match the names in the program exactly?

---

## Engineering Notebook

Record:

- the name of your team’s TeleOp file,
- the name of the OpMode shown on the Driver Station,
- the hardware names used in the configuration file,
- the motor ports used by the robot,
- and one code change your team tested.
