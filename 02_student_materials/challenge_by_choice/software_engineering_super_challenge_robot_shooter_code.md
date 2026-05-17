# Super Challenge: Organize the Shooter Code Like a Software Engineer

This challenge is one way to contribute to your team. It does not make you the only person responsible for code. Share what you learn, invite others to try, and connect your work back to the team's build and testing.

## Why Software Engineering Matters

**Software engineering** is the work of designing, building, testing, improving, and maintaining computer programs. In robotics, software is what connects the driver’s choices to the robot’s physical actions. When you press a button, the program decides what motor should turn, what servo should move, and what should happen next.

Software engineers work in many fields: robotics, video games, websites, apps, cybersecurity, finance, health care, aerospace, education, sports analytics, artificial intelligence, and manufacturing. The U.S. Bureau of Labor Statistics reported that software developers had a median annual wage of **$133,080** in May 2024, and software developer, quality assurance analyst, and tester jobs are projected to grow **15% from 2024 to 2034**, much faster than the average for all occupations. Computer and information technology occupations as a group had a median wage of **$105,990** in May 2024, compared with **$49,500** for all occupations. These numbers do not guarantee any individual person a salary, but they show that software remains a high-value skill.

AI is changing software work, especially at the entry level. Some simple coding tasks can now be started by tools like ChatGPT, Claude, GitHub Copilot, or Codex. That does **not** mean software engineering is disappearing. It means the valuable skill is shifting from “type every line alone” toward “understand the problem, design the structure, guide the AI, test the output, debug mistakes, and explain why the code works.” In other words, AI can help write code, but humans still need to decide what the robot should do and whether the program is safe, clear, and correct.

Software is also one of the few industries where small groups of people can start real projects with very little money. A team can build an app, a website, a robot control system, a data tool, or a game mostly with their own time, a computer, and open-source tools. AI makes this more possible because it can help a small team learn faster, generate starter code, explain errors, and organize projects. The most important advantage is not just knowing a programming language. It is learning how to turn an idea into a working system.

## AP Computer Science A Connection

**AP Computer Science A** is a high school course that introduces students to computer science through programming in **Java**. The College Board describes AP Computer Science A as focused on **object-oriented programming** and problem-solving using Java. The course includes designing solutions, using data structures, developing algorithms, analyzing solutions, and considering ethical and social implications of computing.

This robotics challenge connects directly to AP Computer Science A because FTC robot programming also uses Java. AP Computer Science A students learn ideas such as:

- variables
- methods
- parameters
- return values
- classes
- objects
- instantiation
- method calls
- algorithms
- program design
- debugging

In this challenge, you can see those ideas in a real machine. A method is not just something on a test. A method can turn on a flywheel, move a servo trigger, reset a mechanism, or run a shooting sequence.

## The Robotics Problem

Your robot has several connected parts:

- a **flywheel** that launches the ball
- a **servo trigger** that pushes or releases one ball
- a **hopper** that feeds balls toward the trigger
- a **driver control program** that listens to gamepad buttons
- a **sequence** for loading, firing, resetting, and waiting for the flywheel to recover

At first, students may write all of the code directly inside the main `while (opModeIsActive())` loop. That can work for a small test, but it becomes hard to read as the robot gets more complicated.

Software engineers solve this problem by organizing code into smaller pieces.

---

# Challenge 1: Organize the Shooter Code into Methods

## Goal

Rewrite the TeleOp code so that the shooter and trigger actions are organized into **methods**.

A **method** is a named block of code that performs one job. Instead of writing the same motor or servo commands repeatedly, you can give that action a name.

For example:

```java
public void shooterOn() {
    shooterMotor.setPower(1.0);
}

public void shooterOff() {
    shooterMotor.setPower(0.0);
}
```

Now the main program can say:

```java
if (gamepad1.y) {
    shooterOn();
}
```

That is easier to read. It tells the story of the robot action.

## Vocabulary

**Method**: A named block of code that performs a specific job.

**Method call**: A line of code that tells a method to run.

**Parameter**: An input value passed into a method.

**Sequence**: A set of actions that happen in order.

**Abstraction**: Hiding details inside a method so the main program is easier to understand.

**Debugging**: Finding and fixing problems in code.

**Telemetry**: Messages sent from the robot program to the Driver Station so the team can see what the robot is doing.

## Suggested Methods

Start by creating simple methods like these:

```java
public void shooterOn() {
    shooterMotor.setPower(1.0);
    telemetry.addLine("Shooter ON");
}

public void shooterOff() {
    shooterMotor.setPower(0.0);
    telemetry.addLine("Shooter OFF");
}

public void triggerLoad() {
    triggerServo.setPosition(0.2);
    telemetry.addLine("Trigger LOAD");
}

public void triggerRelease() {
    triggerServo.setPosition(0.8);
    telemetry.addLine("Trigger RELEASE");
}
```

The exact servo values are examples. Your robot may need different values.

## Add Parameters for More Control

A more flexible method can use a parameter:

```java
public void setShooterPower(double power) {
    shooterMotor.setPower(power);
    telemetry.addData("Shooter power", power);
}
```

Now you can test different powers:

```java
if (gamepad1.y) {
    setShooterPower(1.0);
}

if (gamepad1.x) {
    setShooterPower(0.0);
}
```

## Build a Shooting Sequence

A shooting sequence might look like this:

1. Turn on flywheel.
2. Wait for flywheel to reach speed.
3. Release or push one ball.
4. Reset trigger.
5. Wait before firing again.

A first version could be:

```java
public void fireOneBall() {
    triggerRelease();
    sleep(300);
    triggerLoad();
}
```

Be careful: `sleep()` pauses the whole OpMode. That can be useful in a beginner test, but a robot used in a longer challenge often needs deeper timing logic so the driver does not lose control during the pause.

## Main Loop Example

```java
while (opModeIsActive()) {

    if (gamepad1.y) {
        shooterOn();
    }

    if (gamepad1.x) {
        shooterOff();
    }

    if (gamepad1.b) {
        fireOneBall();
    }

    telemetry.update();
}
```

## Why This Is Better

This version is easier to read because the main loop uses robot language:

- `shooterOn()`
- `shooterOff()`
- `fireOneBall()`
- `triggerLoad()`
- `triggerRelease()`

The details are still there, but they are organized into methods.

## Challenge 1 Reflection

What method name best describes the action your robot is performing?  
What code became easier to understand after you moved it into a method?

---

# Challenge 2: Create a Shooter Class with Methods

## Goal

The deeper challenge is to create a separate **class** that represents the shooter system.

A **class** is a blueprint for an object. An **object** is an instance of that class.

In this challenge, the shooter can become its own object.

Instead of putting all shooter code directly in the OpMode, you can create a `ShooterSystem` class with methods such as:

- `shooterOn()`
- `shooterOff()`
- `triggerLoad()`
- `triggerRelease()`
- `fireOneBall()`

Then the OpMode can create one shooter object and call its methods.

## Why This Goes Deeper

This is closer to how larger robot programs are organized. Teams often create separate classes for different robot subsystems:

- drivetrain
- shooter
- intake
- arm
- claw
- lift
- sensors

Each subsystem class contains the code for that part of the robot. The main OpMode then coordinates the subsystems.

## Example ShooterSystem Class

This example assumes a standard servo trigger and a DC motor flywheel.

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.HardwareMap;
import com.qualcomm.robotcore.hardware.Servo;
import org.firstinspires.ftc.robotcore.external.Telemetry;

public class ShooterSystem {

    private DcMotor shooterMotor;
    private Servo triggerServo;
    private Telemetry telemetry;

    private double loadPosition = 0.2;
    private double releasePosition = 0.8;
    private double shooterPower = 1.0;

    public ShooterSystem(HardwareMap hardwareMap, Telemetry telemetry) {
        this.telemetry = telemetry;

        shooterMotor = hardwareMap.get(DcMotor.class, "shooterMotor");
        triggerServo = hardwareMap.get(Servo.class, "triggerServo");
    }

    public void shooterOn() {
        shooterMotor.setPower(shooterPower);
        telemetry.addLine("Shooter ON");
    }

    public void shooterOff() {
        shooterMotor.setPower(0.0);
        telemetry.addLine("Shooter OFF");
    }

    public void setShooterPower(double power) {
        shooterPower = power;
        shooterMotor.setPower(power);
        telemetry.addData("Shooter power", power);
    }

    public void triggerLoad() {
        triggerServo.setPosition(loadPosition);
        telemetry.addLine("Trigger LOAD");
    }

    public void triggerRelease() {
        triggerServo.setPosition(releasePosition);
        telemetry.addLine("Trigger RELEASE");
    }

    public void setTriggerPositions(double load, double release) {
        loadPosition = load;
        releasePosition = release;
        telemetry.addData("Load position", loadPosition);
        telemetry.addData("Release position", releasePosition);
    }
}
```

## Example OpMode Using the ShooterSystem Object

```java
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

@TeleOp(name = "ShooterSystemTest")
public class ShooterSystemTest extends LinearOpMode {

    private ShooterSystem shooter;

    @Override
    public void runOpMode() {

        shooter = new ShooterSystem(hardwareMap, telemetry);

        waitForStart();

        while (opModeIsActive()) {

            if (gamepad1.y) {
                shooter.shooterOn();
            }

            if (gamepad1.x) {
                shooter.shooterOff();
            }

            if (gamepad1.a) {
                shooter.triggerLoad();
            }

            if (gamepad1.b) {
                shooter.triggerRelease();
            }

            telemetry.update();
        }
    }
}
```

## What Instantiation Means

This line creates the shooter object:

```java
shooter = new ShooterSystem(hardwareMap, telemetry);
```

That is called **instantiation**. The program is creating one usable shooter system from the `ShooterSystem` class.

After that, the OpMode can call methods of the object:

```java
shooter.shooterOn();
shooter.triggerRelease();
```

This is the same kind of object-oriented programming that students study in AP Computer Science A.

## Challenge 2 Reflection

Why might a team want the shooter code in a separate class instead of putting everything in the OpMode?

---

# Using AI as a Programming Partner

Students may use ChatGPT, Claude, GitHub Copilot, or another AI coding assistant to help with this challenge, but the human student remains responsible for understanding, testing, and explaining the code.

Good AI prompts might sound like:

```text
I am writing FTC Java code in OnBot Java. I have a DcMotor named shooterMotor and a Servo named triggerServo. Help me organize the shooter code into methods for shooterOn, shooterOff, triggerLoad, and triggerRelease. Keep the code beginner-friendly.
```

Or:

```text
I am learning Java classes. Help me create a ShooterSystem class for FTC OnBot Java. The class should use HardwareMap to get a DcMotor named shooterMotor and a Servo named triggerServo. It should have methods to turn the shooter on and off and move the trigger between load and release positions.
```

Before using AI-generated code, students should check:

- Are the hardware names exactly the same as the Robot Controller configuration?
- Does the code use FTC Java imports?
- Does the code compile?
- Does the servo move safely?
- Does the motor turn on and off correctly?
- Can the student explain every method?

AI can help generate code, but AI can also make mistakes. A software engineer tests carefully.

---

# Optional GitHub / Copilot Workflow

Some students may want to go farther and use a professional-style workflow.

For this course, we are mostly using **OnBot Java**. We are not requiring Android Studio. However, a student who wants to go deeper could:

1. Create a small GitHub repository for the robot code.
2. Write or revise the Java files with GitHub Copilot or another AI coding assistant.
3. Commit changes to Git.
4. Copy and paste the tested code back into OnBot Java.
5. Run the code on the robot.
6. Record what worked and what needed debugging.

A team might eventually move to Android Studio, where the full FTC Robot Controller project can be managed with Git, branches, commits, and pull requests. For this short course, copying code back into OnBot Java is simpler.

## Important Safety Rule

Never run code on a robot just because an AI wrote it. Test in small steps:

1. Compile first.
2. Test without balls.
3. Test with robot wheels or launcher safely controlled.
4. Test one button at a time.
5. Watch telemetry.
6. Stop immediately if the servo strains, the motor behaves unexpectedly, or the robot becomes unsafe.

---

# Two Levels of the Programming Super Challenge

## Level 1: Methods Challenge

You succeed when:

- shooter actions are organized into methods
- trigger actions are organized into methods
- the main loop is easier to read
- the code compiles
- the robot can turn the shooter on/off and move the trigger

## Level 2: Object Challenge

You succeed when:

- you create a separate class, such as `ShooterSystem`
- the class has private motor/servo variables
- the class has methods for shooter and trigger actions
- the OpMode creates an object from the class
- the OpMode calls methods on that object
- you can explain what “class,” “object,” “method,” and “instantiate” mean

## Final Reflection

Which version of the code is easiest for a teammate to understand?  
How could organizing the code help a team debug the robot during a timed challenge or demonstration?

---

# References

College Board. (2025). *AP Computer Science A course overview*. AP Central. https://apcentral.collegeboard.org/media/pdf/ap-computer-science-a-course-overview.pdf

College Board. (2025). *AP Computer Science A course and exam description*. AP Central. https://apcentral.collegeboard.org/courses/ap-computer-science-a

GitHub. (n.d.). *GitHub Copilot*. https://github.com/features/copilot

U.S. Bureau of Labor Statistics. (2025). *Computer and information technology occupations: Occupational Outlook Handbook*. https://www.bls.gov/ooh/computer-and-information-technology/

U.S. Bureau of Labor Statistics. (2025). *Computer programmers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/computer-and-information-technology/computer-programmers.htm

U.S. Bureau of Labor Statistics. (2025). *Software developers, quality assurance analysts, and testers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
