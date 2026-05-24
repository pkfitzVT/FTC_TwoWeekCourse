# Subsystem Design Cycle Guide

## Big Idea

A robot is not one design problem.

A robot is a set of connected subsystems.

Examples of robot subsystems include:

- frame / drivetrain
- shooter or scoring mechanism
- hopper / artifact holder
- trigger / release mechanism
- controls / programming
- integrated match system

Course norm:

> We are not building one robot all at once.  
> We are building a system made of smaller systems.  
> Each subsystem has a job.  
> Each subsystem must be designed, programmed, tested, and documented before we rely on it in the full robot.

---

# Why Subsystems Matter

Working one subsystem at a time helps your team:

- avoid making too many decisions at once,
- keep a working robot alive,
- test smaller pieces,
- identify what failed,
- divide team roles,
- make programming manageable,
- document evidence clearly,
- and integrate the robot with fewer surprises.

A subsystem can work by itself and still cause a problem when added to the full robot. That is why teams test both small subsystem behavior and whole-robot behavior.

---

# The Repeating Subsystem Cycle

For every subsystem, use this cycle:

```text
Decide -> Build -> Program -> Test -> Document -> Integrate
```

Each cycle should include:

1. Identify the job of the subsystem.
2. Connect it to the team strategy.
3. Define Must / Should / Could goals.
4. Make a rough design.
5. Build a simple working version.
6. Program or control it.
7. Test it.
8. Record evidence.
9. Revise it.
10. Decide whether it is ready to integrate.

Use `90_templates/subsystem_design_cycle_template.md` each time your team starts or revises a subsystem.

---

# Subsystem Sequence

## 1. Frame / Drivetrain

Essential question:

> How will our robot move reliably and leave space for future mechanisms?

Done means:

- robot drives,
- motors are configured,
- TeleOp works,
- team can drive forward, backward, and turn,
- team has reserved space for future mechanisms,
- team has documented chassis/frame decisions.

## 2. Shooter

Essential question:

> How will our robot launch or score artifacts reliably?

Done means:

- shooter motor can be controlled,
- artifact can be launched or moved toward the goal,
- team has test data,
- team knows success rate from at least one position.

## 3. Hopper / Trigger

Essential question:

> How will our robot hold, feed, and release artifacts predictably?

Done means:

- hopper holds artifacts,
- trigger releases one artifact at a time, or at least predictably,
- servo/control code works,
- team has tested jams or failures.

## 4. Controls / Programming

Essential question:

> How will drivers and operators control each subsystem safely and consistently?

Done means:

- gamepad roles are clear,
- motor and servo names match the robot configuration,
- each subsystem has a safe starting state,
- telemetry helps the team test,
- controls support the team's scoring routine.

## 5. Integration

Essential question:

> Can all subsystems work together during a scoring loop?

Done means:

- team can run a full scoring loop,
- team can park,
- team knows expected score,
- team has revised strategy based on evidence.

---

# Working Robot Rule

> Do not add the next subsystem until the current subsystem has a working version, a control plan, and at least one test result.

You are allowed to experiment, but your team is responsible for keeping a working version of the robot alive.

Before adding a new subsystem, ask:

- What working behavior are we protecting?
- What could this new subsystem block, loosen, overload, or make harder to repair?
- What code or controls will need to change?
- What test will prove the robot still works after integration?

The goal is not to build everything at once. The goal is to build one reliable subsystem, then connect it carefully to the next one.
