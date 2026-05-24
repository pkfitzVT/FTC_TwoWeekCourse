# Robot Behavior Specification Template

Use this template after your team has a first strategy and before choosing major robot design details.

The Team Strategy Guide explains what your team is trying to accomplish. This behavior specification turns that strategy into specific robot requirements.

Example:

```text
Strategy: We want to score in TeleOp.

Behavior specification: Our robot must drive from the starting area to the scoring position, align with the goal, release or shoot 2 artifacts per scoring loop, return for more artifacts, avoid contact, and fully park with 15 seconds remaining.
```

Copy this template into your engineering portfolio or shared team document. Revisit it before choosing chassis geometry, frame material, motor placement, mechanism placement, shooter design, hopper design, trigger design, driver controls, or programming priorities.

---

# 1. Team and Strategy Reference

| Field | Team Response |
|---|---|
| Team name |  |
| Robot name |  |
| Date |  |
| Current strategy name |  |
| Team Strategy Guide link or location |  |
| Current version number |  |

Strategy summary:

______________________________________________________________________________

______________________________________________________________________________

---

# 2. Autonomous Behavior Goals

List what the robot should do without driver control. Keep the first version simple and testable.

Examples:

- Drive off the back wall.
- Get off the starting line.
- Score one artifact.
- Move to a safe starting position for TeleOp.
- Avoid contact.
- Stop in a predictable location.

| Behavior Description | Why It Matters for Strategy | Required Hardware | Required Code | Success Criteria | Testing Plan | Priority |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  | Must / Should / Could |
|  |  |  |  |  |  | Must / Should / Could |
|  |  |  |  |  |  | Must / Should / Could |

Autonomous setup requirements:

| Setup Item | Requirement |
|---|---|
| Starting position |  |
| Robot angle |  |
| Artifact position |  |
| Battery or power condition |  |
| Driver Station / OpMode selection |  |

---

# 3. TeleOp Behavior Goals

List what the robot should do during driver control.

Examples:

- Drive reliably.
- Turn without tipping or drifting.
- Push artifacts toward the human operator.
- Collect or guide artifacts.
- Score artifacts in the goal.
- Release artifacts from a sleeve or hopper.
- Make multiple scoring loops.
- Score from one known position.
- Score from multiple positions.
- Avoid contact penalties.

| Behavior Description | Driver / Operator Input Needed | Required Mechanism | Required Chassis / Frame Qualities | Success Criteria | Testing Plan | Priority |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  | Must / Should / Could |
|  |  |  |  |  |  | Must / Should / Could |
|  |  |  |  |  |  | Must / Should / Could |
|  |  |  |  |  |  | Must / Should / Could |

TeleOp scoring loop sequence:

1. 
2. 
3. 
4. 
5. 

Driver and operator roles:

| Role | Responsibilities | Controls Needed |
|---|---|---|
| Gamepad 1 |  |  |
| Gamepad 2 |  |  |
| Coach / spotter |  |  |
| Human operator |  |  |

---

# 4. Endgame Behavior Goals

List what the robot needs to do near the end of the match.

Examples:

- Park.
- Fully park.
- Fully park while another robot also parks.
- Reserve enough time for parking.
- Avoid contact while parking.

| Behavior Description | When We Start Endgame | Driver / Operator Action | Success Criteria | Risk | Priority |
|---|---|---|---|---|---|
|  |  |  |  |  | Must / Should / Could |
|  |  |  |  |  | Must / Should / Could |
|  |  |  |  |  | Must / Should / Could |

Endgame rule for our team:

______________________________________________________________________________

---

# 5. Performance Targets

Use estimates first. Replace them with test data as the robot improves.

## Scoring Targets

| Target | Estimate or Goal | Test Data / Updated Value | Notes |
|---|---:|---:|---|
| Scoring loops expected |  |  |  |
| Artifacts attempted per loop |  |  |  |
| Success rate |  |  |  |
| Time per loop |  |  |  |
| Autonomous points |  |  |  |
| TeleOp points |  |  |  |
| Endgame points |  |  |  |
| Likely penalties |  |  |  |
| Expected total score |  |  |  |

## Non-Scoring Targets

| Robot Behavior | Target | Test Method | Result |
|---|---|---|---|
| Drive straight over a fixed distance |  |  |  |
| Turn accurately |  |  |  |
| Complete a scoring loop within a target time |  |  |  |
| Score from a chosen position with a target success rate |  |  |  |
| Park within a target time |  |  |  |
| Run without disconnects or jams |  |  |  |

---

# 6. Design Implications

Connect desired behaviors to design choices. If a design choice does not support a required behavior, question it.

| Design Question | Team Answer |
|---|---|
| What chassis geometry best supports these behaviors? |  |
| What frame material best supports these behaviors? |  |
| Where should drive motors be placed? |  |
| Where should mechanism motors be placed? |  |
| What needs to stay open or accessible? |  |
| What might block movement, scoring, or repair access? |  |
| What sensors or telemetry would help? |  |
| What code features are required? |  |
| What driver controls are required? |  |

Most important design requirement:

______________________________________________________________________________

Design choice that creates the biggest trade-off:

______________________________________________________________________________

---

# 7. Must / Should / Could Prioritization

Sort behaviors by importance. A working robot needs the Must behaviors before it needs stretch goals.

| Priority | Behaviors |
|---|---|
| Must: required for a working robot |  |
| Should: important if time allows |  |
| Could: stretch goals |  |

What will we remove or simplify if we run out of time?

______________________________________________________________________________

---

# 8. Testing Plan

Test behaviors one at a time before testing the whole robot sequence.

| Behavior | Test | Success Criteria | Result | Revise? |
|---|---|---|---|---|
|  |  |  |  | Yes / No |
|  |  |  |  | Yes / No |
|  |  |  |  | Yes / No |
|  |  |  |  | Yes / No |

Next test to run:

______________________________________________________________________________

---

# 9. Revision Log

Update this table when evidence changes what the robot needs to do.

| Date | Behavior Changed | Why? | Evidence | Design / Code Impact |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

# 10. Decision Check

Before choosing chassis geometry, frame material, motor placement, or mechanism design, ask:

> Which robot behavior does this design choice support?

Before adding complexity, ask:

> Which performance goal will this improve, and how will we test it?

Final check before building:

| Design Choice | Robot Behavior It Supports | Performance Goal It Improves | Test We Will Use |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |

Future option: create one team folder per team and copy this template into each folder. For now, keep the reusable blank template in `90_templates/`, link it from the engineering notebook, and have teams copy it into their portfolio or shared team document.
