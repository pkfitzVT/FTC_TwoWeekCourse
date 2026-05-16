# Wheel Selection Menu

## How Should Our Robot Touch the Field?

## Graduate Expectation Tags

- **[Purple: Curiosity & Creativity]** We explore different wheel types and imagine how they affect robot movement.
- **[Red: Critical Thinking & Problem Solving]** We compare traction, turning, speed, control, and reliability.
- **[Green: Personal Development]** We make responsible choices based on available materials and team skill.
- **[Blue: Effective Communication]** We explain wheel choices using sketches, test data, and observations.

## Decision Being Made

Your team is choosing the wheels for the chassis. Wheels affect how the robot drives, turns, accelerates, pushes, stops, and handles contact with the field or game objects.

Teams may have access to wheels from different systems, including Tetrix, REV, goBILDA, and others. Wheel sizes, tread patterns, rubber density, hubs, axles, and connectors may all be different.

## Background Sources

Use ideas from:

- **Chassis Shape Menu**
- **Chassis Material Menu**
- **Chassis Physics and Space Planning**
- robot driving observations,
- available wheel bins,
- mentor demonstrations,
- and your team's chassis sketch.

## Why This Decision Matters

Wheels are not just "the things that roll." They determine how the robot interacts with the floor.

Wheel choice affects:

- traction,
- turning,
- speed,
- stability,
- pushing ability,
- driver control,
- autonomous consistency,
- clearance,
- and how easily the wheels attach to motors, hubs, shafts, and the chassis.

A wheel that looks good may not fit the shaft. A wheel that grips well may make turning harder. A wheel that turns easily may not push well. Your team needs to choose based on the job the robot needs to do.

## How to Use This Menu

1. Review the wheel options.
2. Check which wheels are actually available.
3. Check whether the wheels fit your hubs, shafts, axles, and chassis.
4. Decide which wheels are powered and which wheels support the robot.
5. Sketch the wheel layout.
6. Record your choice, reasoning, trade-off, and evidence plan in the portfolio.

---

# Wheel Design Factors

## Wheel Size

Larger wheels can move the robot farther with each rotation, which can make the robot faster. They can also increase clearance off the floor. Smaller wheels may be easier to fit and may give more control.

| Larger Wheels | Smaller Wheels |
|---|---|
| More distance per rotation | More compact |
| More floor clearance | Often easier to fit |
| May increase speed | May feel easier to control |
| May need more torque | May reduce clearance |

## Tread and Rubber

Soft rubber and grippy tread can help the robot push and accelerate. Harder wheels or smoother wheels may slip more but can sometimes turn more easily.

| More Grip | Less Grip |
|---|---|
| Better pushing and acceleration | Easier turning in some layouts |
| More control when driving straight | Less strain during turns |
| May resist sideways movement | May slip under load |
| Can make turning harder | May reduce pushing power |

## Fit and Connection

Before choosing a wheel, check:

- Does the wheel fit the hub?
- Does the hub fit the shaft or axle?
- Is the shaft round or hex?
- Is the set screw tight?
- Is the wheel supported?
- Does the wheel rub the frame?
- Do we have spacers to stop side-to-side sliding?
- Does the wheel match the motor placement and chassis shape?

---

# Menu Options

## Option A: Standard Traction Wheels

**Graduate Expectation Connection:** [Red: Critical Thinking & Problem Solving]

**What it means:**  
Traction wheels are regular wheels designed to grip the floor.

**What it helps:**  
They provide pushing power, acceleration, and strong forward/backward movement.

**Best for:**  
Drive wheels powered by motors.

**Ease of use:** Easy to medium

**Likelihood of success:** High if they fit the hub and shaft

**Time to implement:** Fast to moderate

**Material / tooling needs:**  
Wheels, hubs, shafts/axles, set screws, spacers, bearings or supports, and hex tools.

**Possible trade-offs:**  
Too much grip can make turning harder, especially if all four wheels are traction wheels.

**Evidence we might watch:**  
Does the robot drive straight? Does it turn smoothly? Do the wheels slip or scrub during turns?

---

## Option B: Omni Wheels

**Graduate Expectation Connection:** [Purple: Curiosity & Creativity] and [Red: Critical Thinking & Problem Solving]

**What it means:**  
Omni wheels have small rollers around the edge. They roll forward like normal wheels, but can slide sideways more easily.

**What it helps:**  
Omni wheels reduce sideways resistance during turns. A common beginner layout uses two powered traction wheels and two omni support wheels.

**Best for:**  
Helping a two-motor robot turn more smoothly.

**Ease of use:** Medium

**Likelihood of success:** High if installed correctly

**Time to implement:** Moderate

**Material / tooling needs:**  
Omni wheels, compatible hubs, shafts/axles, spacers, and supports.

**Possible trade-offs:**  
Omni wheels usually provide less sideways resistance, so the robot may be easier to push sideways. They may provide less traction than regular wheels.

**Evidence we might watch:**  
Does the robot turn more easily? Does it drift sideways? Does it still drive straight enough for testing?

---

## Option C: Four Traction Wheels

**Graduate Expectation Connection:** [Red: Critical Thinking & Problem Solving]

**What it means:**  
All four wheels are regular traction wheels.

**What it helps:**  
This can give the robot strong grip and pushing power.

**Best for:**  
Robots that need to push or hold position and do not need to turn very tightly.

**Ease of use:** Easy

**Likelihood of success:** Medium

**Time to implement:** Fast

**Material / tooling needs:**  
Four matching traction wheels, hubs, axles/shafts, spacers, and supports.

**Possible trade-offs:**  
The robot may fight itself while turning because all four wheels resist sideways sliding. This is called wheel scrub. It can make turning jerky, slow, or hard on motors.

**Evidence we might watch:**  
Does the robot turn smoothly? Do motors strain during turns? Does the robot jerk or skid?

---

## Option D: Two Traction Wheels + Two Omni Wheels

**Graduate Expectation Connection:** [Red: Critical Thinking & Problem Solving]

**What it means:**  
Two powered traction wheels move the robot. Two omni wheels support the robot and help it turn.

**What it helps:**  
This is a strong beginner layout because it balances powered movement with easier turning.

**Best for:**  
Two-motor course robots that need simple, reliable driving.

**Ease of use:** Medium

**Likelihood of success:** High

**Time to implement:** Moderate

**Material / tooling needs:**  
Two traction wheels, two omni wheels, compatible hubs/shafts/spacers, and supports.

**Possible trade-offs:**  
Less pushing power than four traction wheels. The robot may slide more easily from the omni-wheel side.

**Evidence we might watch:**  
Does the robot turn predictably? Does it drive straight? Can the driver control it easily?

---

## Option E: Mecanum Wheels

**Graduate Expectation Connection:** [Purple: Curiosity & Creativity] and [Red: Critical Thinking & Problem Solving]

**What it means:**  
Mecanum wheels have angled rollers that allow a robot to drive forward/backward, turn, and move sideways when used in a four-motor drivetrain.

**What it helps:**  
Mecanum drive can make it easier to line up with goals, move around field objects, and strafe sideways.

**Best for:**  
Advanced teams with enough motors, wheels, time, and programming support.

**Ease of use:** Hard

**Likelihood of success:** Risky for a short course unless the base already exists

**Time to implement:** Slow

**Material / tooling needs:**  
Four mecanum wheels, four drive motors, correct wheel orientation, motor controllers, more complex code, tuning, and driver practice.

**Possible trade-offs:**  
More expensive, more complex, more programming, more wiring, and more debugging. It may take time away from shooter, hopper, trigger, portfolio, and testing.

**Evidence we might watch:**  
Can the robot strafe reliably? Do all wheels spin in the correct direction? Can the driver control it under pressure?

---

## Option F: Reused Wheels From an Existing Chassis

**Graduate Expectation Connection:** [Green: Personal Development] and [Orange: Cultural Understanding & Civic Engagement]

**What it means:**  
The team uses wheels already mounted on a known chassis or salvages wheels from an existing robot base.

**What it helps:**  
This can save time and reduce fit problems because the wheels, hubs, shafts, and supports may already work together.

**Best for:**  
Teams that want to prioritize robot reliability, programming, mechanisms, or testing time.

**Ease of use:** Easy to medium

**Likelihood of success:** High if the wheels are in good condition

**Time to implement:** Fast

**Material / tooling needs:**  
Existing chassis or wheel assemblies, inspection checklist, hex tools, replacement screws, spacers, or hubs if needed.

**Possible trade-offs:**  
The wheel layout may limit chassis shape, motor placement, ground clearance, or future mechanisms.

**Evidence we might watch:**  
Do the wheels spin freely? Are set screws tight? Does the robot drive straight and turn reliably?

---

# Wheel Layout Questions

Before finalizing the wheel choice, answer:

- Which wheels are powered by motors?
- Which wheels are support wheels?
- Where are the omni wheels, if used?
- Do the wheels fit the hubs and shafts?
- Are the set screws tight?
- Is the wheel supported on the axle?
- Does the wheel rub the frame?
- Is there enough clearance off the floor?
- Will the robot turn smoothly?
- Will the driver be able to control the robot?

---

# Wheel Assembly Checklist

| Check | Yes / No |
|---|---|
| Wheel fits the hub |  |
| Hub fits the shaft or axle |  |
| Set screw is tight |  |
| Wheel spins freely |  |
| Wheel does not rub the frame |  |
| Spacers stop side-to-side sliding |  |
| Axle or shaft is supported |  |
| Left and right drive wheels are aligned |  |
| Omni wheels roll in the correct direction |  |
| Robot has enough floor clearance |  |

---

# Comparison Table

| Option | Best Feature | Main Risk | Good For |
|---|---|---|---|
| Standard traction wheels | Grip and pushing | Turning may be harder | Powered drive wheels |
| Omni wheels | Easier turning | Less sideways resistance | Support wheels on simple drivetrains |
| Four traction wheels | Strong grip | Wheel scrub during turns | Pushing or holding position |
| Two traction + two omni | Balanced beginner drive | Less pushing than four traction | Reliable two-motor robot |
| Mecanum wheels | Sideways movement | Complex, expensive, needs four motors | Advanced competition-style driving |
| Reused wheel assemblies | Saves time | Limits design choices | Reliable fast start |

---

# Wheel Decision Table

Record your decision in your engineering portfolio.

| Decision Area | Our Choice | Why We Chose It | What We Gave Up | Evidence We Will Watch |
|---|---|---|---|---|
| Drive wheels |  |  |  |  |
| Support wheels |  |  |  |  |
| Wheel size |  |  |  |  |
| Wheel material/tread |  |  |  |  |
| Wheel layout |  |  |  |  |

---

# Must / Should / Could

| Level | Expectation |
|---|---|
| Must Do | Choose wheels that fit the chassis and identify which wheels are powered. |
| Should Do | Explain how the wheel choice affects turning, traction, control, and reliability. |
| Could Do | Compare two wheel layouts using a drive test, turning test, or driver feedback. |

---

# SLD Connection

## Main SLD Prompt

**Should our robot prioritize traction, easy turning, speed, or driver control when choosing wheels?**

## Supporting Questions

- What wheel choice gives us the best chance of driving reliably?
- When is more grip helpful?
- When can too much grip make turning harder?
- Should we use omni wheels to make turning easier?
- Is mecanum worth the extra complexity in a short course?
- Should we reuse a known wheel setup to save time?

---

# Portfolio Deliverable

Add the following to your engineering portfolio:

- selected wheel types,
- powered wheel locations,
- support wheel locations,
- wheel layout sketch,
- wheel assembly checklist,
- explanation of the main trade-off,
- and evidence the team will watch during testing.

---

# Reflection

Our wheel choice is:

______________________________________________________________________________

We chose this because:

______________________________________________________________________________

The main trade-off we accepted is:

______________________________________________________________________________

The evidence we will watch during testing is:

______________________________________________________________________________
