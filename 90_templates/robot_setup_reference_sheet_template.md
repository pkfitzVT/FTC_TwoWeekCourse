# Robot Setup Reference Sheet Template

This sheet is the team’s master reference for one robot.

The reference sheet tells the team what the robot is supposed to be.  
The troubleshooting checklist helps the team find where reality differs from the plan.

---

## Robot Identity

| Item | Value |
|---|---|
| Team / Group Name | |
| Robot ID / Control Hub Name | |
| Robot Number / Label | |
| Date Created | |
| Last Updated | |
| Assigned Students | |

---

## Network Information

> Do not change borrowed Control Hub network names or passwords without instructor permission.

| Item | Value |
|---|---|
| Wi-Fi Network Name | |
| Wi-Fi Password | See printed robot reference card / instructor. Do not change borrowed Control Hub passwords. |
| Robot Controller Address | |
| Notes | |

---

## Configuration File

| Item | Value |
|---|---|
| Active Configuration File Name | |
| Backup Configuration File Name | |
| Date of Last Known Working Configuration | |
| Who Last Changed It? | |
| Reason for Change | |

### Suggested Configuration Naming Pattern

Use a name that includes the course, year, robot ID, and purpose.

Examples:

```text
YES_2026_Robot9721_BaseConfig
YES_2026_Robot9721_Day04_DriveWorking
YES_2026_Robot9721_Day06_ShooterAdded
```

### Configuration Rule

The names in the configuration file must match the names in the Java code **exactly**.

This includes:

- Spelling
- Capitalization
- Spaces
- Underscores
- camelCase

Example:

```java
hardwareMap.get(DcMotor.class, "leftDrive");
```

The configuration file must contain a motor named:

```text
leftDrive
```

---

# Hardware Naming Conventions

## Standard Naming Conventions

Use clear, consistent names. Avoid spaces unless your instructor requires them.

### Motors

```text
leftDrive
rightDrive
shooterMotor
intakeMotor
armMotor
```

### Servos

```text
triggerServo
gateServo
hopperServo
sensorServo
```

### Sensors

```text
distanceSensor
colorSensor
touchSensor
imu
```

---

## Drive Motors

| Physical Device | Configuration Name | Port | Direction Notes |
|---|---|---|---|
| Left drive motor | leftDrive | | |
| Right drive motor | rightDrive | | |

---

## Mechanism Motors

| Physical Device | Configuration Name | Port | Direction Notes |
|---|---|---|---|
| Shooter motor | shooterMotor | | |
| Intake motor | intakeMotor | | |
| Arm motor | armMotor | | |

---

## Servos

| Physical Device | Configuration Name | Port | Starting Position | Notes |
|---|---|---|---|---|
| Trigger servo | triggerServo | | | |
| Gate servo | gateServo | | | |
| Sensor servo | sensorServo | | | |

---

## Sensors

| Physical Device | Configuration Name | Port | Notes |
|---|---|---|---|
| Distance sensor | distanceSensor | | |
| Color sensor | colorSensor | | |
| Touch sensor | touchSensor | | |
| IMU | imu | Built-in | |

---

# OpMode Reference

## Current OpModes

| File Name | Menu Name on Driver Station | Purpose | Status |
|---|---|---|---|
| BasicDriveTeleOp.java | Basic Drive TeleOp | Drive test | |
| ShooterTriggerTeleOp.java | Shooter Trigger TeleOp | Shooter and trigger test | |
| FullRobotTeleOp.java | Full Robot TeleOp | Full demo control | |

## OpMode Status Options

Use one of these:

- Not tested
- Builds but not tested
- Runs with issues
- Working
- Last known working version

---

# Current Gamepad Map

## Gamepad 1: Driver

| Input | Robot Action |
|---|---|
| Left stick | |
| Right stick | |
| D-pad | |
| A | |
| B | |
| X | |
| Y | |
| Left bumper | |
| Right bumper | |
| Left trigger | |
| Right trigger | |

---

## Gamepad 2: Operator

| Input | Robot Action |
|---|---|
| Left stick | |
| Right stick | |
| D-pad | |
| A | |
| B | |
| X | Turn shooter on |
| Y | Turn shooter off |
| Left bumper | |
| Right bumper | |
| Left trigger | |
| Right trigger | Fire trigger servo |

---

# Last Known Working Setup

| Item | Notes |
|---|---|
| Last date robot drove successfully | |
| Last OpMode that worked | |
| Last configuration file that worked | |
| Last mechanism that worked | |
| What changed since then? | |

---

# Robot Change Log

Use this table whenever the team changes wiring, ports, configuration names, OpMode names, gamepad controls, or major robot parts.

| Date | What Changed? | Why? | Who Made the Change? | Tested? | Result |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

---

# Team Rule

Before changing the configuration file, code names, wiring, ports, or OpMode names, update this sheet.

If the robot stops working, this sheet is the first place to look.
