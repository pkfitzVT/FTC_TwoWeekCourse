# Session 8 Reading: Troubleshooting Basic Drive

## Debugging Is Engineering

The first drivetrain test almost never works perfectly. That does not mean the team failed. It means the team has evidence.

Troubleshooting is the process of using evidence to find the cause of a problem, make one careful change, and test again.

## Troubleshooting Vocabulary

To **troubleshoot** means to find and fix a problem step by step.

To **debug** means to find and fix a problem in code or a robot system.

A **symptom** is what you observe. For example, "the left wheel does not move" is a symptom.

A **cause** is the reason the symptom is happening.

**Evidence** is information you can see, hear, measure, or record.

A **hypothesis** is your best explanation for what might be causing the problem.

A **test** is a careful check to see whether your hypothesis is correct.

To **revise** means to change the design, code, wiring, or plan based on evidence.

A **compile error** happens when the code cannot build. The program usually will not appear as an OpMode until the error is fixed.

A **runtime error** happens while the program is running.

A **typo** is a typing mistake. In code and configuration names, a small typo can stop the robot from working.

A **loose connection** is a wire or connector that is not fully plugged in or secure.

A **reversed motor** spins the opposite direction from what the team expected.

**Motor direction** means which way the motor spins when it gets positive or negative power.

**Telemetry** is information the robot program sends to the Driver Station screen.

## Common First-Drive Problems

| Symptom | Possible Cause | First Thing to Check |
|---|---|---|
| OpMode does not appear | Code did not compile | Look for red errors or typos |
| Robot does not move | Battery, wire, or configuration issue | Check power and motor names |
| One side moves but the other does not | Motor unplugged, wrong port, or wrong name | Check motor wire and configuration |
| Robot spins when pressing forward | Motor directions are opposite of expected | Check signs in the code |
| Robot moves backward when pressing forward | Drive motor signs are reversed | Switch positive/negative power in code |
| Shooter motor does not turn on | Wrong button, typo, wrong configuration name, or loose wire | Check code and config name |
| Motor runs but wheel does not move | Loose hub or set screw | Check wheel attachment |
| Robot starts then stops | Low battery or loose connection | Check battery and wires |

## Only Change One Thing at a Time

When the robot does not work, it is tempting to change the code, wiring, configuration, and mechanical parts all at once. That makes troubleshooting harder.

Change one thing, then test. If the robot improves, you know which change helped. If it does not improve, you have useful evidence and can choose the next check.

Good troubleshooting sounds like this:

- "We think the right motor name is wrong."
- "We will check the configuration name only."
- "Then we will run the same test again."

## Use Telemetry

Telemetry can show messages on the Driver Station. This helps your team know what the code thinks is happening.

For example:

```java
telemetry.addLine("Shooter ON");
telemetry.update();
```

If the Driver Station shows `Shooter ON` but the shooter motor does not spin, the button press may be working and the problem may be wiring, configuration, or the motor command.

## Troubleshooting Log

| Test | Expected Result | Actual Result | Change Made | Result After Change |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Reflection

What problem did your team find today? What evidence helped you decide what to change?
