# Subsystem Design, Operation, Testing, and Tuning Cycle

## Big Idea

In this course, teams use a repeated design pattern. The pattern starts with the game goals and robot behavior targets. Those behavior targets tell the team what the robot needs to do. Each subsystem is then designed to help the robot perform those behaviors.

A subsystem connects hardware, software, and human operation. The hardware gives the robot a physical ability. The software or controls allow the robot or operator to activate that ability. The human operator uses the system during testing or competition. The team uses data and postmortem discussions to improve the system.

SLDs are not extra activities. They are part of the engineering process.

```text
Game Goals
-> Robot Behavior Targets
-> Design SLD
-> Build / Adapt with Available Parts
-> Programming / Configuration
-> Subsystem Test
-> Operations Role SLD
-> Integrated Performance Test
-> Postmortem / Tuning SLD
-> Revision or Acceptable Performance Range
-> Documentation
```

This process repeats for the chassis / drivetrain, flywheel shooter, hopper, trigger / servo, and whole-robot integration. Autonomous work adds another layer if time permits.

## What Counts as a Subsystem?

The subsystem is not just a physical mechanism. A subsystem includes hardware, software/control, human operation, testing evidence, and documentation.

| Subsystem | More Than the Physical Part |
|---|---|
| Chassis / drivetrain | Frame, wheels, drive controls, power tuning, driver skill, field awareness |
| Flywheel shooter | Motor, wheel, launch angle, motor power, ball contact, operator timing, scoring strategy |
| Hopper | Container, stability while driving, reload process, ball feeding, operator interaction |
| Trigger / servo | Servo, release timing, servo range, button mapping, consistency |
| Whole robot | Subsystem placement, code integration, role communication, scoring loop, repair access |

## The Repeated Cycle

### 1. Start with Game Goals

Identify what the game rewards and what the team wants the robot to accomplish.

Ask:

- What scores points?
- What avoids penalties?
- What can we realistically build, test, and explain?
- What strategy does our team want to protect?

### 2. Translate Goals into Robot Behavior Targets

Describe what the robot must actually do.

Examples:

- drive straight
- turn reliably
- push or collect a ball
- store balls
- launch balls
- release one ball at a time
- park
- avoid collisions
- complete a scoring loop

Game goals define what the robot needs to accomplish. Robot behavior targets describe what the robot must do. Subsystems connect hardware, software, and human operation so the robot can perform those behaviors.

### 3. Use Reading, Menus, and Evidence

Before designing, use:

- background readings
- design menus
- demo robot evidence
- data from earlier tests
- available parts
- strategy and behavior documents

Evidence keeps the team from choosing based only on what looks cool or what one person prefers.

### 4. Design SLD

Purpose:

```text
Turn evidence into a design decision.
```

Main question:

> What design should we build first, and what evidence supports that choice?

Work product:

- design decision
- sketch or diagram
- parts/material plan
- software/control need
- success criteria
- first test

### 5. Build and Adapt with Available Parts

Try to build the design, but expect to adapt.

Teams may need to adjust for:

- available materials
- space constraints
- ease of assembly
- fasteners and brackets
- repair access
- wire routing
- interference with other subsystems

Changing the design during building is normal. If the change affects the design, code, safety, or strategy, document it.

### 6. Program and Configure

Connect the subsystem to code and controls.

Examples:

- motor configuration names
- servo names
- button mapping
- drive power
- flywheel power
- trigger servo range
- autonomous method

Configuration names in the robot setup must match the names used in code.

### 7. Test Against Success Criteria

Before testing, define what good enough means.

Examples:

- chassis completes the course with fewer than two penalties
- flywheel scores 7 out of 10 shots from a target zone
- hopper holds balls during three driving loops
- trigger releases one ball at a time 8 out of 10 attempts
- autonomous drive lands within a target error range

The test should match the behavior target. If the target is reliable scoring, test more than one lucky attempt.

### 8. Operations Role SLD

Use this before performance testing.

Purpose:

```text
Decide who operates the system, who backs them up, and how the team will practice.
```

Main question:

> Who should operate this system, who is the backup, and what evidence supports our plan?

Work product:

- primary operator
- backup operator
- driver/operator/coach roles
- practice rotation
- absence plan
- role review conditions

Reference:

`02_student_materials/sld_prompts/reusable_robot_operations_role_plan_sld.md`

### 9. Integrated Performance Test

Test the subsystem as part of the larger robot.

Examples:

- chassis with driver controls
- flywheel mounted on the chassis
- hopper feeding the flywheel
- trigger releasing balls from the hopper
- whole robot completing a scoring cycle

A subsystem can work alone and still fail when integrated. Integration tests reveal those interactions.

### 10. Postmortem / Tuning SLD

Use this after testing.

Purpose:

```text
Classify what happened, choose limited changes, assign responsibility, and plan a retest.
```

Main question:

> What happened, what type of issue did we observe, and what should we change before the next run?

Use the four categories:

- Human Operation
- Mechanical System
- Software / Controls
- Strategy / Communication

Reference:

`02_student_materials/sld_prompts/reusable_performance_testing_postmortem_sld.md`

### 11. Tune Within an Acceptable Range

Make limited, evidence-based adjustments.

```text
Change one or two things at a time.
Look for patterns across multiple trials.
Stop tuning when performance is inside the acceptable range.
```

### 12. Document the Full Cycle

Documentation happens throughout the process, not only at the end.

Document:

- design decision
- sketch/photo
- parts used
- configuration names
- code snippet
- test data
- operator notes
- postmortem classification
- revision made
- final acceptable range

## Micro-Decisions During Work

Not every conversation is a full SLD. Teams also make many small work-session decisions:

- Who is doing what right now?
- Which bracket fits best?
- Is this wire route safe?
- Should we tighten this now or test-fit first?
- Is this part blocking the next subsystem?
- Do we need to pause and ask the team?
- Should this change be recorded in the notebook?

These micro-decisions are essential. If the decision changes the design, code, safety, or strategy, document it.

## The Tuning Trap: Do Not Chase Your Tail

Tuning is necessary, but it can become endless.

```text
Tuning can become a trap. If your team changes angle, power, bracket position, code, and operator timing after every run, you are chasing your tail.
```

### Drive Tuning

Drive tuning problems might include:

- drive power too high
- turns too sensitive
- slow mode too slow
- robot hard to control when facing the driver

If you change drive power, controller mapping, driver, course route, and wheel placement at the same time, you will not know which change helped.

### Flywheel Tuning

Flywheel tuning has many variables:

- launch angle
- flywheel power
- ball compression
- ball contact point
- hopper angle
- trigger timing
- shooting distance
- robot alignment
- battery level
- wheel wear/slip
- ball condition

```text
If the team changes launch angle, motor power, ball position, and trigger timing after every shot, the team will not know which change caused the result.
```

Recommended rule:

```text
Choose one test variable.
Run several trials.
Record the result.
Then decide whether to keep tuning that variable or move to a different one.
```

## How the Cycle Applies to Each Subsystem

| Subsystem | What It Must Do | Example Design SLD Focus | Example Test | Example Postmortem Categories |
|---|---|---|---|---|
| Chassis / Drivetrain | Move, turn, park, share space | Frame shape, motor placement, controls | Round-robin drive challenge | Human driving, wheel slip, control tuning, passing strategy |
| Flywheel Shooter | Launch balls consistently | Angle, wheel type, motor power, compression | Shots from target zone | Operator timing, mount flex, motor power, shooting strategy |
| Hopper | Store and feed balls | Angle, capacity, stability, loading | Drive loops with balls loaded | Human loading, ball jams, feed path, reload communication |
| Trigger / Servo | Release one ball at a time | Servo placement, horn/pusher, range | Repeated release trials | Operator timing, servo range, sticking, firing sequence |
| Whole Robot | Complete scoring loops | Integration and space management | Full scoring cycle | Role communication, subsystem interference, control mapping, strategy |

## Acceptable Performance Range

A subsystem is ready when it performs inside an acceptable range for the team's strategy.

Systems do not need to be perfect. They need to be reliable enough for the team goal.

Examples:

- drive system: controlled enough to complete the course safely
- flywheel: accurate enough from a known distance
- hopper: stable enough during normal driving
- trigger: consistent enough to release one ball at a time
- autonomous: close enough to be useful in the challenge

Decide the acceptable range before or during testing. Revisit it during the postmortem. If the strategy changes, the acceptable range may change too.

## Documentation Happens the Whole Time

The engineering portfolio should not be written only at the end. It should grow as the team makes decisions, tests, revises, and learns.

## Portfolio Evidence Checklist

- [ ] Game goal or robot behavior target
- [ ] Design SLD decision
- [ ] Sketch, diagram, or photo
- [ ] Parts/materials used
- [ ] Configuration names
- [ ] Code snippet or control mapping
- [ ] Test plan
- [ ] Test data
- [ ] Operator/driver notes
- [ ] Postmortem category
- [ ] Revision made
- [ ] Retest result
- [ ] Final acceptable range or next step

## Teacher Note

This guide can be reused throughout the course. Each subsystem does not need a completely new process. Teachers can refer students back to this cycle and then provide subsystem-specific readings, design menus, and SLD prompts.

The cycle helps students see that robotics is not just building. It is designing, programming, operating, testing, diagnosing, tuning, and documenting.
