# Subsystem Design Cycle Template

Copy this template into your engineering portfolio or shared team document each time your team designs, revises, or integrates a subsystem.

After a design SLD, your team should update this template with the design choice, evidence, physical build plan, and next test. SLD is the decision process. The subsystem design template is one of the work products.

Use one copy for each subsystem:

- frame / drivetrain
- shooter
- hopper / artifact holder
- trigger / release mechanism
- controls / programming
- integrated match system

Cycle:

```text
Decide -> Build -> Program -> Test -> Document -> Integrate
```

---

# 1. Subsystem Identity

| Field | Team Response |
|---|---|
| Subsystem name |  |
| Date |  |
| Team name |  |
| Team members working on it |  |
| Current version |  |

---

# 2. Subsystem Job

| Prompt | Team Response |
|---|---|
| What should this subsystem do? |  |
| What phase of the game does it support? |  |
| What part of our team strategy does it support? |  |
| What robot behavior does it make possible? |  |

---

# 3. Must / Should / Could Goals

| Priority | Goal | Why it matters |
|---|---|---|
| Must |  |  |
| Must |  |  |
| Should |  |  |
| Could |  |  |

---

# 4. Design Choices

| Prompt | Team Response |
|---|---|
| What design choice did we make after discussion? |  |
| What evidence or resource supported this choice? |  |
| What parts or materials are we considering? |  |
| Where might this subsystem attach? |  |
| What space must stay open? |  |
| What other subsystem might this affect? |  |
| What design tradeoffs are we making? |  |

First sketch, photo, or idea location:

______________________________________________________________________________

---

# 5. Physical Build Plan

This section turns the design idea into something the team can actually build.

## Required Design Sketch or Photo

Draw a sketch, insert a photo, or link to a photo of the subsystem design.

Label as many of these as apply:

- motors
- servos
- sensors
- wheels / shafts / moving parts
- brackets / connectors / mounts
- fasteners / collars / spacers
- wiring path
- Control Hub / Expansion Hub ports
- battery or Control Hub access
- where this subsystem attaches to the chassis
- space that must stay open for other subsystems
- possible collision, rubbing, or jam points

Sketch / photo link:

______________________________________________________________________________

______________________________________________________________________________

## Parts and Materials

| Item | Team Response |
|---|---|
| Major structural parts |  |
| Motors used |  |
| Servos used |  |
| Sensors used, if any |  |
| Wheels / shafts / gears / pulleys |  |
| Brackets / connectors / mounts |  |
| Fasteners / collars / spacers |  |
| Other important parts |  |

## Attachment and Mounting Plan

| Prompt | Team Response |
|---|---|
| Where does this subsystem attach to the robot? |  |
| What parts hold it in place? |  |
| What needs to be square, level, centered, or aligned? |  |
| What might loosen, bend, rub, or shift? |  |
| How will we make this strong enough for testing? |  |
| How will we make this easy enough to repair or adjust? |  |

## Wiring, Ports, and Configuration Names

| Hardware Item | Port / Location | Configuration Name | Notes |
|---|---|---|---|
| Motor / Servo / Sensor 1 |  |  |  |
| Motor / Servo / Sensor 2 |  |  |  |
| Motor / Servo / Sensor 3 |  |  |  |
| Motor / Servo / Sensor 4 |  |  |  |

Configuration names must match the names used in the Java code exactly.

## Space and Interference Check

| Question | Team Response |
|---|---|
| What space must stay open for this subsystem to work? |  |
| What other subsystem could block this subsystem? |  |
| What could this subsystem block? |  |
| Could wires, balls/artifacts, hands, tools, or moving parts interfere? |  |
| What will be hard to reach after this is attached? |  |
| What should we test before permanently tightening or finalizing? |  |

---

# 6. Programming / Controls

| Prompt | Team Response |
|---|---|
| What motor, servo, or sensor names are involved? |  |
| What OpMode will test this subsystem? |  |
| What gamepad input controls it? |  |
| What telemetry would help us test it? |  |
| What safe starting state is needed? |  |

---

# 7. Test Plan

Plan small tests before full-power or full-speed tests. Test fit, rubbing, wiring, and safe motion before final tightening when possible.

| Test | Success Criteria | Result | What changed next? |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

# 8. Evidence

| Prompt | Team Response |
|---|---|
| What photo, data table, video, or observation shows whether this worked? |  |
| What physical build evidence belongs in the portfolio? |  |
| What wiring, port, configuration, or code evidence belongs in the portfolio? |  |
| What did we learn? |  |
| What should we revise? |  |

---

# 9. Integration Check

| Prompt | Team Response |
|---|---|
| Is this subsystem ready to connect to the full robot? |  |
| What could it block or interfere with? |  |
| What could block or interfere with this subsystem? |  |
| What must stay accessible for repair, battery changes, wiring, or Control Hub access? |  |
| Does code from this subsystem need to combine with other code? |  |
| What should we test after integration? |  |

Ready to integrate?

- [ ] Not yet
- [ ] Yes, with teacher/mentor check
- [ ] Yes, after one more test: _____________________________________________

---

# 10. Revision Log

| Date | Change | Evidence / Reason | Result |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

# Working Robot Rule

> Do not add the next subsystem until the current subsystem has a working version, a control plan, and at least one test result.

You are allowed to experiment, but your team is responsible for keeping a working version of the robot alive.
