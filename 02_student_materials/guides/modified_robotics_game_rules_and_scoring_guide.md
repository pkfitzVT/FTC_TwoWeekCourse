# Modified Robotics Game Rules and Scoring Guide

## Purpose of the Game

This robotics challenge is designed to help teams experience the full engineering cycle:

> **Strategy → Design → Build → Test → Revise → Compete → Reflect**

Your team should not begin by simply attaching parts to the robot. Your team should begin by asking:

> **What are we trying to score, and what kind of robot would help us do that reliably?**

Your robot design should be driven by your game strategy. Your team may revise the strategy as you learn more, but your design choices should always connect back to the way your team plans to score points.

---

# Big Idea: Strategy Drives Design

A robot is not just a collection of parts. A robot is a strategy made physical.

In nature, structures often match functions:

- A bird’s beak shape helps it eat certain foods.
- A fish’s body shape helps it move through water.
- A tree’s branches help it capture sunlight.
- A bridge’s shape helps it carry weight.
- A building’s frame helps it resist forces.

Robots work the same way.

The shape, frame, motors, mechanisms, code, and driver controls should all support what the team is trying to accomplish in the game.

Before choosing a chassis, mechanism, shooter, pusher, hopper, or code feature, ask:

> **Does this choice help our scoring strategy?**

---

# Game Overview

Teams will compete head-to-head using a modified robotics scoring game.

- One team will use **purple artifacts**.
- One team will use **green artifacts**.
- Teams will compete on a modified half-field.
- Teams will score by moving artifacts, scoring artifacts in the goal, and parking during endgame.
- Teams will also be rewarded for reliable, safe, and controlled driving.

The goal is not only to score points. The goal is to design a robot that can execute a strategy repeatedly.

---

# Match Phases

Each match has three phases:

1. **Autonomous**
2. **TeleOp**
3. **Endgame**

---

## 1. Autonomous Phase

During autonomous, the robot runs without direct driver control.

Possible autonomous goals include:

- Drive off the back wall.
- Get off the starting line.
- Score an artifact in the goal.
- Move into a better starting position for TeleOp.

### Autonomous Scoring

| Action | Points |
|---|---:|
| Score an artifact in the goal during autonomous | 3 points |

Autonomous scoring is valuable because it requires the robot and code to behave predictably.

---

## 2. TeleOp Phase

During TeleOp, drivers and operators control the robot.

Possible TeleOp goals include:

- Push artifacts toward the human operator.
- Collect or manage artifacts.
- Score artifacts in the goal.
- Release artifacts from a sleeve or holder.
- Make multiple scoring runs.
- Score from one reliable position.
- Score from multiple positions.
- Coordinate driver and operator roles.

### TeleOp Scoring

| Action | Points |
|---|---:|
| Score an artifact in the goal during TeleOp | 1 point |

TeleOp scoring is worth less than autonomous scoring, but it can happen repeatedly.

Teams should estimate:

- How many scoring loops they can complete.
- How many artifacts they can attempt per loop.
- What percentage of attempts are likely to score.
- Whether their design is fast, accurate, and reliable enough.

---

## 3. Endgame Phase

During endgame, teams try to park safely and reliably.

Possible endgame goals include:

- Park partially.
- Fully park.
- Fully park while the neighboring/opposing team also fully parks.

### Endgame Scoring

| Action | Points |
|---|---:|
| Park | 1 point |
| Fully park | 2 points |
| Both teams fully park | 3 points |

The “both teams fully park” score encourages safe driving, field awareness, and thoughtful match strategy.

---

# Penalties

Safety and robot protection matter. Teams should compete hard, but not recklessly.

| Violation | Penalty |
|---|---:|
| Robot contact with another robot | -1 point |
| Failure to move for 10 seconds or more | -1 point |
| Intentional contact with another robot | -3 points |
| Damage to another robot | Elimination from the match or event, at instructor discretion |

## Penalty Notes

- Accidental light contact may still receive a penalty if it affects the match.
- Intentional contact is more serious because this is a controlled engineering challenge, not a pushing contest.
- Damage to another robot is treated as a major safety and sportsmanship issue.
- The instructor may stop a match if a robot creates a safety risk.

The goal is to build a robot that is effective, controlled, and safe.

---

# Advancement Points

In addition to match score, teams earn advancement points during qualification matches.

| Result | Advancement Points |
|---|---:|
| Win the match | 1 advancement point |
| Both teams fully park | 1 advancement point for each team |

This means a team can earn advancement points by winning, but also by participating in a match where both teams complete the cooperative parking goal.

## Why Advancement Points Matter

Advancement points are used to rank teams after qualification matches.

A team with a reliable strategy may rank well even if it does not have the highest single-match score.

---

# Qualification Matches

Each team will play **3 qualification matches**.

Qualification matches are used to rank teams for playoffs.

Teams should use qualification matches to:

- Test their strategy.
- Improve driver control.
- Collect data.
- Adjust scoring estimates.
- Identify reliability problems.
- Decide whether to revise their design or strategy before playoffs.

## Qualification Ranking

Teams may be ranked using:

1. Total advancement points.
2. Total match points.
3. Head-to-head result, if needed.
4. Instructor judgment or a short tie-breaker match, if needed.

---

# Playoff Format

After qualification matches, teams will be ranked.

With four teams, the playoff bracket begins:

| Match | Teams |
|---|---|
| Semifinal 1 | Rank 1 vs Rank 4 |
| Semifinal 2 | Rank 2 vs Rank 3 |

The playoffs will use a **double-elimination style bracket**.

This means a team is not out of the tournament after one loss. A team is eliminated after its second playoff loss.

## Expected Playoff Flow

For four teams, the playoff structure will usually require **6 matches**, and may require **7 matches** if there is a bracket reset in the final.

A likely structure is:

| Round | Match |
|---|---|
| 1 | Rank 1 vs Rank 4 |
| 2 | Rank 2 vs Rank 3 |
| 3 | Winners play each other |
| 4 | Losers play each other |
| 5 | Loser of winners match plays winner of losers match |
| 6 | Final match |
| 7, if needed | Bracket reset final if the undefeated finalist loses in Round 6 |

So the playoff tournament will likely have:

> **6–7 playoff matches total**

The exact format may be adjusted by the instructor based on time, robot readiness, and number of teams.

---

# Expected Score Planning

Teams should estimate their expected score before finalizing their robot design.

Use this planning model:

```text
Expected Score = Autonomous Points + TeleOp Points + Endgame Points - Penalties
```

For TeleOp:

```text
TeleOp Points = Scoring Loops × Shots per Loop × Success Rate × Points per Shot
```

Since TeleOp scoring is worth 1 point per scored artifact:

```text
TeleOp Points = Scoring Loops × Shots per Loop × Success Rate
```

## Example Strong Strategy Estimate

A strong team might estimate:

| Category | Estimate |
|---|---:|
| Autonomous score | 3 points |
| TeleOp loops | 3 loops |
| Shots per loop | 3 shots |
| Success rate | 50% |
| Expected TeleOp score | 4.5 points |
| Fully park | 2 points |
| Expected penalties | 0 points |
| Expected total | 9.5 points |

Another team might use a safer strategy:

| Category | Estimate |
|---|---:|
| Autonomous score | 0 points |
| TeleOp loops | 4 loops |
| Shots per loop | 2 shots |
| Success rate | 50% |
| Expected TeleOp score | 4 points |
| Fully park | 2 points |
| Expected penalties | 0 points |
| Expected total | 6 points |

A simpler robot that scores reliably may beat a complicated robot that rarely works.

---

# Strategy Planning Questions

Before building, your team should answer:

## Autonomous

- Will we attempt to score in autonomous?
- Will we focus on driving off the back wall?
- Will we focus on getting off the line?
- How risky is our autonomous plan?
- What code and setup must be reliable?

## TeleOp

- Will we focus on scoring artifacts in the goal?
- Will we focus on pushing artifacts to the human operator?
- Will we try to release artifacts from a sleeve?
- Will we score from one known position or many positions?
- How many scoring loops do we expect?
- How many artifacts can we attempt per loop?
- What success rate do we expect?

## Endgame

- Can we park reliably?
- Can we fully park reliably?
- Can we coordinate so both teams fully park?
- How much time should we leave for endgame?

## Safety and Penalties

- How will we avoid contact?
- How will we avoid getting stuck?
- How will we design for controlled driving?
- How will we protect other robots?

---

# Strategy Revision

Your team may revise its strategy as you learn.

Good reasons to revise a strategy include:

- The robot cannot score as accurately as expected.
- The robot cannot complete enough loops.
- The mechanism jams.
- The driver cannot aim reliably.
- The robot risks contact penalties.
- Parking is more reliable than expected.
- Autonomous is too difficult or more successful than expected.
- Test data shows a better strategy.

When you revise your strategy, record:

1. What your original strategy was.
2. What evidence changed your thinking.
3. What the new strategy is.
4. What design changes are needed.

---

# Final Design Rule

Before making a major design choice, ask:

> **What scoring strategy does this support?**

Before adding a feature, ask:

> **Will this help us score, park, avoid penalties, or improve reliability?**

Before making the robot more complicated, ask:

> **Will this improve our expected score enough to be worth the risk?**

The best robot is not the most complicated robot.

The best robot is the one that can execute a thoughtful strategy reliably.
