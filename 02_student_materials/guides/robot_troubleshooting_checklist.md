# Robot Troubleshooting Checklist

Use this checklist before asking an instructor for help.

Do not just say:

> “The robot doesn’t work.”

Instead, figure out which part of the system is failing.

---

## Step 1: What were you trying to do?

Write one clear sentence.

```text
We were trying to:
```

Examples:

- Drive forward with gamepad1.
- Turn on the shooter motor with gamepad2 X.
- Move the trigger servo with gamepad2 right trigger.
- Read distance from the distance sensor.
- Run the full robot TeleOp.

---

## Step 2: What happened instead?

Choose one or more:

- Nothing happened.
- Code would not build.
- OpMode did not appear in the menu.
- OpMode appeared but crashed on INIT.
- OpMode initialized but crashed on PLAY.
- Motor moved the wrong direction.
- Servo moved unexpectedly.
- Robot disconnected.
- Robot moved, but not correctly.
- Telemetry did not show what we expected.

Notes:

```text
What we observed:
```

---

## Step 3: Connection Check

| Check | Yes / No | Notes |
|---|---|---|
| Robot battery is connected and charged | | |
| Control Hub is powered on | | |
| Chromebook is connected to the robot Wi-Fi | | |
| Driver Station is connected to Robot Controller | | |
| Robot Controller page / OnBot Java page opens | | |
| Correct robot is selected | | |

If any answer is “No,” fix the connection before changing code.

---

## Step 4: Code Build Check

| Check | Yes / No | Notes |
|---|---|---|
| We saved the file | | |
| We clicked Build | | |
| The build finished successfully | | |
| We read the first error message if the build failed | | |
| The OpMode appears in the Driver Station menu | | |

If the code does not build, the problem is probably in the Java code.

Common causes:

- Missing semicolon
- Misspelled variable
- Missing import
- Extra brace or missing brace
- Wrong class name
- File name and class name do not match

---

## Step 5: Configuration Name Check

This is one of the most common beginner problems.

For each device used in code, check the exact name.

| Device in Code | Name in Code | Name in Configuration | Exact Match? |
|---|---|---|---|
| Left drive motor | | | |
| Right drive motor | | | |
| Shooter motor | | | |
| Trigger servo | | | |
| Distance sensor | | | |

Remember:

```text
leftDrive
```

is not the same as:

```text
LeftDrive
leftdrive
left_drive
left Drive
```

The name must match exactly, including spelling, capitalization, spaces, and underscores.

---

## Step 6: Correct OpMode Check

| Check | Yes / No | Notes |
|---|---|---|
| We selected the correct OpMode from the menu | | |
| The OpMode menu name matches our reference sheet | | |
| We pressed INIT | | |
| Telemetry appeared after INIT | | |
| We pressed PLAY | | |
| We tested one control at a time | | |

Common mistake:

> Students edit one file but run a different OpMode.

---

## Step 7: Hardware and Wiring Check

| Check | Yes / No | Notes |
|---|---|---|
| Motor or servo is plugged into the expected port | | |
| Wire is fully inserted | | |
| Wire is not damaged or pinched | | |
| Power is connected | | |
| Servo wire is plugged in with correct orientation | | |
| Hub port matches configuration | | |
| Mechanism can move freely by hand when safe | | |

If the code and configuration are correct but nothing moves, check wiring and physical blockage.

---

## Step 8: Test One Device at a Time

Do not test the whole robot at once.

Choose one device:

```text
Device to test:
```

Choose one control:

```text
Control to test:
```

Record what happened:

```text
Result:
```

Examples:

- Test only `leftDrive`.
- Test only `rightDrive`.
- Test only `shooterMotor`.
- Test only `triggerServo`.
- Test only `distanceSensor` telemetry.

---

## Step 9: What Changed Since It Last Worked?

This is one of the most important troubleshooting questions.

| Possible Change | Notes |
|---|---|
| Code changed | |
| Configuration changed | |
| Wiring changed | |
| Battery changed | |
| Robot part moved | |
| Servo position changed | |
| Different OpMode selected | |
| Different Chromebook or Driver Station used | |

Ask:

> What is the last version that worked?

---

## Step 10: Ask for Help With Useful Information

Before asking an instructor, be ready to say:

1. What we were trying to do.
2. What happened instead.
3. Whether the code builds.
4. Which OpMode we ran.
5. Which configuration file is active.
6. Which device name might be the problem.
7. What changed since the last working version.
8. What we already tried.

Helpful request:

> “Our code builds, and the OpMode initializes, but the shooter motor does not move when we press X. The configuration name in code is `shooterMotor`, and the configuration file also says `shooterMotor`. We checked the wire and port. Can you help us decide the next test?”

Not helpful:

> “It doesn’t work.”

---

## Troubleshooting Rule

> Test the smallest part of the system that could explain the problem.

Do not change five things at once.

Change one thing, test, and record what happened.
