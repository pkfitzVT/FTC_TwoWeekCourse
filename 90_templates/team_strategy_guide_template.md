# Team Strategy Guide Template

Use this guide after your team has formed, chosen a team name, and selected team norms. Copy it into your engineering portfolio or shared team document, then revisit it before major design decisions.

Core idea:

> Team norms tell us how we will work together.  
> Game strategy tells us what we are trying to accomplish.  
> Robot design turns that strategy into a physical system.

Before making a major robot decision, ask:

> What scoring strategy does this support?

Before adding complexity, ask:

> Will this improve our expected score enough to be worth the risk?

---

# 1. Team Identity

| Field | Team Response |
|---|---|
| Team name |  |
| Team members |  |
| Robot name, if any |  |
| Team color / artifact color, if assigned |  |
| Date first created |  |
| Current version date |  |

---

# 2. Team Norms Connection

Team norms describe how we work together. Strategy describes what we are trying to accomplish in the game. Use your norms to make strategy decisions fair, clear, and evidence-based.

| Prompt | Team Response |
|---|---|
| How will we make design decisions? |  |
| How will we handle disagreement? |  |
| How will we decide when to revise the strategy? |  |
| How will we make sure everyone understands the strategy? |  |
| Which team norm matters most when a design idea is exciting but risky? |  |

---

# 3. Game Understanding

Summarize the modified game in your own words. Use the current rules and scoring guide, not memory.

| Question | Team Summary |
|---|---|
| What scores points? |  |
| What causes penalties? |  |
| What earns advancement points? |  |
| What matters in qualification matches? |  |
| What matters in playoffs? |  |
| What rule or scoring detail might affect our robot design the most? |  |

---

# 4. Competition Video Observation

Before finalizing your strategy, watch or observe real robot matches. The goal is not to copy those robots. The goal is to notice strategy, reliability, field movement, driver choices, and trade-offs.

Optional observation source:

https://www.youtube.com/watch?v=lQfSZJ88kf8&list=PLPvv0LBFty8lVODuZcozGehrMbCWU87Tn

This playlist includes Norwich Qualifier match videos.

| What We Observed | Notes |
|---|---|
| How robots move around the field |  |
| How often robots score |  |
| How often robots get stuck or delayed |  |
| Simple mechanisms that appear effective |  |
| How drivers line up for scoring |  |
| How robots manage game pieces |  |
| Risks or failures we noticed |  |
| Ideas that might apply to our modified half-field game |  |

Observation takeaway:

______________________________________________________________________________

______________________________________________________________________________

---

# 5. Primary Strategy

Choose the main scoring approach your team will design, build, practice, and explain.

Possible strategies:

- Reliable parking + simple scoring
- High-volume TeleOp loops
- Accurate scoring from one known position
- Scoring from multiple positions
- Autonomous-first strategy
- Human-operator/artifact-management strategy
- Defensive avoidance and safe driving strategy
- Combination strategy: ________________________________________________

Our primary strategy:

______________________________________________________________________________

Why this is realistic for our team:

______________________________________________________________________________

What we must be able to do reliably:

______________________________________________________________________________

Evidence that will show whether this strategy is working:

______________________________________________________________________________

---

# 6. Backup Strategy

If the primary strategy is too difficult, unreliable, unsafe, or too slow, what will we switch to?

Our backup strategy:

______________________________________________________________________________

What evidence would tell us to switch:

______________________________________________________________________________

What design choices should stay flexible so we can switch:

______________________________________________________________________________

---

# 7. Autonomous Plan

| Prompt | Team Plan |
|---|---|
| Will we try to score in autonomous? |  |
| Will we drive off the back wall? |  |
| Will we get off the line? |  |
| What is the simplest autonomous task we can make reliable? |  |
| What code must be consistent? |  |
| What setup or starting position must be consistent? |  |
| What field position or field mark matters? |  |
| How many successful tests in a row should we require before trusting it? |  |

Autonomous priority:

______________________________________________________________________________

---

# 8. TeleOp Plan

| Prompt | Team Plan |
|---|---|
| Will we push artifacts to the human operator? |  |
| Will we score artifacts in the goal? |  |
| Will we release artifacts from a sleeve? |  |
| Will we make multiple scoring runs? |  |
| Will we score from one location or multiple locations? |  |
| How will gamepad1 and gamepad2 roles be divided? |  |
| What should the driver practice first? |  |
| What should the human operator or coach practice first? |  |

TeleOp route or operating sequence:

1. 
2. 
3. 
4. 
5. 

---

# 9. Endgame Plan

| Prompt | Team Plan |
|---|---|
| Will we park? |  |
| Will we fully park? |  |
| Can we coordinate with the other team so both teams fully park? |  |
| How much time should we reserve for endgame? |  |
| What robot size, shape, or driving issue could make parking harder? |  |
| What should we do if our scoring plan runs late? |  |

Endgame rule for drivers:

______________________________________________________________________________

---

# 10. Expected Score Model

Use estimates, then update them when you have test data.

```text
Expected Score = Autonomous Points + TeleOp Points + Endgame Points - Penalties
```

```text
TeleOp Points = Scoring Loops x Shots per Loop x Success Rate
```

| Estimate Item | First Estimate | Test Data / Updated Estimate | Notes |
|---|---:|---:|---|
| Autonomous points |  |  |  |
| Number of TeleOp scoring loops |  |  |  |
| Shots/artifacts attempted per loop |  |  |  |
| Success rate |  |  |  |
| Expected TeleOp score |  |  |  |
| Expected endgame score |  |  |  |
| Expected penalties |  |  |  |
| Expected total score |  |  |  |

Calculation notes:

______________________________________________________________________________

What number are we least certain about?

______________________________________________________________________________

What test will improve this estimate?

______________________________________________________________________________

---

# 11. Design Implications

Explain how the strategy affects robot design. If a design choice does not support the strategy, question it.

| Design Area | What Our Strategy Requires | Design Choice or Priority |
|---|---|---|
| Chassis/frame choice |  |  |
| Shooter or scoring mechanism |  |  |
| Hopper/artifact management |  |  |
| Trigger/release mechanism |  |  |
| Driver controls |  |  |
| Programming priorities |  |  |
| Testing/data collection |  |  |
| Reliability and repair access |  |  |

Biggest design risk:

______________________________________________________________________________

Simplest version that could still support the strategy:

______________________________________________________________________________

---

# 12. Revision Log

This is a living document. Revise it when evidence changes your thinking.

Good reasons to revise:

- The robot cannot score as accurately as expected.
- The robot cannot complete enough scoring loops.
- The mechanism jams.
- The driver cannot aim or line up reliably.
- The robot risks contact penalties.
- Parking is more reliable or less reliable than expected.
- Autonomous is too difficult or more successful than expected.
- Test data shows a better strategy.

| Date | What changed? | Evidence that led to the change | Design/code changes needed |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

# 13. Strategy Check Before Design Decisions

Before making a major design choice, ask:

> What scoring strategy does this support?

Before adding complexity, ask:

> Will this improve our expected score enough to be worth the risk?

Before changing the plan, ask:

- What evidence changed our thinking?
- Does everyone understand the new strategy?
- What design, code, driver practice, or documentation must change next?
- Is this change consistent with our team norms?

Decision checkpoint:

| Design Choice Being Considered | Strategy It Supports | Expected Score Benefit | Risk / Cost | Decision |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |

Future option: create one team folder per team and copy the strategy guide template into each folder. For now, keep the reusable blank template in `90_templates/`, link it from the engineering notebook, and have teams copy it into their portfolio or shared team document.
