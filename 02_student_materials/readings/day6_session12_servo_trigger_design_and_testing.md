# Session 12 Reading: Servo Trigger Design and Testing

## Controlling the Feed

The trigger controls when a ball enters the flywheel. A good trigger is simple, light, and easy to test.

For this course, the trigger should release or push one ball at a time. Reliable feeding is part of a reliable shooter.

## Trigger Vocabulary

A **trigger** is the part that controls when a ball is released into the shooter.

A **gate** blocks or opens the ball path.

A **pusher** moves a ball forward into the flywheel.

A **latch** holds something in place until it is released.

The **load position** is the servo position where the ball waits and does not enter the flywheel.

The **release position** is the servo position where one ball is allowed or pushed into the flywheel.

**Reset** means returning the trigger to the load position after a release.

A **servo position** is a command value such as `0.2` or `0.8` that tells a standard servo where to move.

An **endpoint** is one end of the safe motion range.

**Clearance** is the space around the trigger, ball, horn, and frame.

**One ball at a time** means the trigger feeds a single ball instead of dumping the whole stack.

**Timing** means when the trigger moves compared with the flywheel speed and the next shot.

**Flywheel recovery** is the short time the flywheel needs to return to speed after launching a ball.

**Consistency** means the trigger and shooter behave the same way repeatedly.

**Test code** is simple code used to check one robot behavior.

**Telemetry** is information the robot sends to the Driver Station screen.

## Push the Bottom Ball or Release the Stack?

For this course, it is usually better to control the bottom ball one at a time instead of releasing the whole stack.

The flywheel slows down each time it launches a ball, so it needs time to recover. Feeding balls too quickly can make shots weaker or inconsistent.

A trigger that controls one ball at a time gives the team more control over timing and testing.

## Servo Trigger Design Rules

- The servo should move a light part.
- The servo should not fight a jammed stack of balls.
- The trigger should have a clear load position and release position.
- The ball should not push hard against the servo when it is stuck.
- The servo horn should not hit the frame.
- The linkage should not bind.
- The trigger should be easy to reset.
- The mechanism should be tested slowly before full-speed use.

## Simple Servo Test Code

```java
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.Servo;

@TeleOp(name = "ServoTriggerTest")
public class ServoTriggerTest extends LinearOpMode {

    private Servo triggerServo;

    @Override
    public void runOpMode() {
        triggerServo = hardwareMap.get(Servo.class, "triggerServo");

        waitForStart();

        while (opModeIsActive()) {
            if (gamepad1.a) {
                triggerServo.setPosition(0.2);
                telemetry.addLine("Trigger position: LOAD");
            }

            if (gamepad1.b) {
                triggerServo.setPosition(0.8);
                telemetry.addLine("Trigger position: RELEASE");
            }

            telemetry.update();
        }
    }
}
```

The exact values `0.2` and `0.8` are examples. Your team must test your own robot carefully.

## Testing Safely

- Start with the robot on blocks or disabled from launching.
- Remove balls for the first servo motion test.
- Test small position changes first.
- Watch for buzzing, binding, or hitting the frame.
- Stop if the servo strains.
- Add one ball only after the servo moves freely.
- Test the load position.
- Test the release position.
- Record the two position values that work best.

## Servo Trigger Test Log

| Test | Servo Position | Expected Result | Actual Result | Keep or Change? |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Reflection

What are your trigger's load and release positions? How do you know those positions are safe for the servo?
