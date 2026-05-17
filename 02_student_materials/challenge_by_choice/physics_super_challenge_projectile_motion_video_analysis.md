# Physics Super Challenge: Analyze the Shooter Ball With Video, Graphs, and Calculus

This challenge is one way to contribute to your team. It does not make you the only person responsible for physics, data, or shooter tuning. Share what you learn, invite others to try, and connect your work back to the team's build and shot testing.

## Why This Challenge Matters

In robotics, a good shooter is not just something that “looks right.” A good shooter can be **tested**, **measured**, **modeled**, and **improved**. In this super challenge, you will use video analysis to study the path of a ball launched by your robot’s flywheel shooter.

This is the same kind of thinking used in physics, engineering, sports science, robotics, aerospace, data science, and quantitative finance. You collect data from the real world, turn that data into graphs, fit mathematical models, and use those models to make better decisions.

This challenge connects directly to several advanced courses:

- **AP Physics**: motion, projectiles, forces, energy, experimental design, and data analysis.
- **AP Statistics**: data collection, scatterplots, regression, residuals, variation, and evidence.
- **AP Calculus**: parametric equations, derivatives, velocity, speed, acceleration, and launch angle.

You do not need to have taken all of those courses to begin. There are levels to this challenge, so students can go as far as they are ready to go.

---

## Career Connections: Physics, Data, Engineering, and Finance

People who can collect data, model motion, and explain patterns are valuable in many careers. **Physicists** use mathematical models and experiments to understand the physical world. The U.S. Bureau of Labor Statistics reported a 2024 median annual wage of **$166,290** for physicists. **Data scientists** use data, coding, statistics, and modeling to find patterns and make predictions; BLS reported a 2024 median annual wage of **$112,590** and projected **34% employment growth from 2024 to 2034**, which is much faster than average. **Statisticians** use data to design studies, analyze variation, and make evidence-based conclusions; BLS reported a 2024 median annual wage of **$103,300** for statisticians. **Financial and investment analysts** use data and models to evaluate investments, with BLS reporting a 2024 median annual wage of **$101,350** for financial and investment analysts.

These skills can also connect to **data science**, **quantitative analysis**, and **investment research**. In investment firms, “quant” work often combines math, statistics, coding, financial data, and models. Compensation in some finance roles can be much higher than national medians, especially in major finance centers and at competitive firms, but the work can also be demanding and selective. The important takeaway is that the math, physics, and coding in this challenge are not isolated school skills. They are part of a broader skill set used to make decisions from evidence.

---

## Course Connections

### AP Physics

AP Physics courses ask students to understand motion through models, experiments, and evidence. AP Physics 1 includes kinematics, dynamics, and energy through hands-on laboratory work. Projectile motion is one of the most natural places to connect a robot shooter to physics because the ball moves horizontally while gravity changes its vertical motion.

### AP Statistics

AP Statistics is about collecting, analyzing, and drawing conclusions from data. In this challenge, your data comes from video. You will create scatterplots, fit regression models, and ask whether the models make sense. You will also think about variation: even if the robot is “the same,” two shots may not follow exactly the same path.

### AP Calculus

AP Calculus BC includes parametric equations and vector-valued functions. That is exactly how projectile motion can be modeled:

- horizontal position: `x(t)`
- vertical position: `y(t)`

A student who has taken calculus can find derivatives:

- `dx/dt` = horizontal velocity
- `dy/dt` = vertical velocity
- speed = size of the velocity vector
- launch angle = direction of the velocity vector at the moment the ball leaves the shooter

---

## Big Idea

A launched ball can be modeled with two equations:

```text
x = x(t)
y = y(t)
```

The horizontal coordinate often behaves approximately like **linear motion**:

```text
x(t) = a + bt
```

The vertical coordinate often behaves approximately like **quadratic motion**:

```text
y(t) = c + dt + et^2
```

This happens because, after launch, the ball continues moving forward while gravity accelerates it downward.

In real life, the data will not be perfect. The ball may spin, air resistance may matter, the video may have measurement error, and the launch may vary from shot to shot. That is why this is a physics and statistics challenge, not just a formula exercise.

---

## Tools

You may use:

- a phone or Chromebook camera
- a ruler, meter stick, or known reference object for scale
- Tracker Video Analysis, Tracker Online, or another video-analysis tool
- Desmos for graphing and regression
- spreadsheet software, if helpful
- calculator
- notebook or data table

Tracker is a free video analysis and modeling tool designed for physics education. It allows students to track the position of an object in video and create graphs of motion data.

---

## Level 1 Challenge: Record a Useful Video

### Goal

Record a video that can be analyzed.

### Setup

1. Place the camera so it views the ball’s motion from the side.
2. Keep the camera still. Do not pan or zoom during the shot.
3. Include a known measurement in the video, such as a meter stick or a marked distance.
4. Try to keep the ball’s motion in one flat plane.
5. Make sure the background makes the ball visible.
6. Record one shot at a time.

### Vocabulary

**Frame**: One still image from a video.

**Scale**: The relationship between distance in the video and real-world distance.

**Coordinate system**: A way to measure position using horizontal and vertical values.

**Reference object**: An object with known length used to set the scale.

**Controlled data collection**: Collecting data carefully so the results are easier to interpret.

### Reflection

What did your team do to make the video easier to measure?

---

## Level 2 Challenge: Track the Ball’s Position

### Goal

Use video analysis to collect position data for the ball.

### Steps

1. Open the video in Tracker or a similar tool.
2. Set the scale using a known object in the video.
3. Choose an origin and coordinate axes.
4. Track the center of the ball frame by frame.
5. Export or copy the data table.
6. Record time, horizontal position, and vertical position.

### Suggested Data Table

| Time `t` | Horizontal Position `x` | Vertical Position `y` |
|---:|---:|---:|
|  |  |  |
|  |  |  |
|  |  |  |

### Important Tip

Try to click the same part of the ball every time, such as the center. If you click the top of the ball in one frame and the center in another frame, your data will be less consistent.

### Reflection

Where do you think your measurement error came from?

---

## Level 3 Challenge: Graph the Motion in Desmos

### Goal

Graph the data and identify the type of motion.

Create two graphs:

1. `x` versus `t`
2. `y` versus `t`

### What You Should Notice

The `x` versus `t` graph should often look approximately linear.

The `y` versus `t` graph should often look approximately quadratic.

### Desmos Regression Examples

For horizontal motion:

```text
x1 ~ a + b t1
```

For vertical motion:

```text
y1 ~ c + d t1 + e t1^2
```

The exact Desmos variable names will depend on how your table is set up.

### Vocabulary

**Regression**: A method for finding an equation that fits data.

**Linear model**: A model with a constant rate of change.

**Quadratic model**: A model with a squared term, often used when acceleration is constant.

**Residual**: The difference between an actual data point and the model’s predicted value.

**Coefficient**: A number in an equation that changes the model’s shape or position.

### Reflection

Which graph looked more linear: `x` versus `t` or `y` versus `t`? Why does that make sense for projectile motion?

---

## Level 4 Challenge: Interpret the Equations

### Goal

Use your regression equations to explain the shot.

Suppose your models look like this:

```text
x(t) = a + bt
y(t) = c + dt + et^2
```

The coefficient `b` describes horizontal velocity.

The coefficient `d` describes the initial vertical velocity.

The coefficient `e` is related to vertical acceleration. If the units are meters and seconds, then `e` should be close to `-4.9` for ideal projectile motion because:

```text
y(t) = y0 + v0y t - 4.9t^2
```

In classroom video data, it may not be close. That is okay. Measurement scale, camera angle, tracking error, spin, air resistance, and inconsistent launch conditions can all affect the result.

### Questions to Answer

1. Was the horizontal motion close to constant speed?
2. Was the vertical motion close to quadratic?
3. Did the ball hit the goal, fall short, overshoot, or bounce out?
4. What does the model suggest your team should adjust?
5. Would you change launch angle, flywheel power, compression, distance, or trigger timing?

### Reflection

What did the data show that your eyes might have missed?

---

## Level 5 Calculus Challenge: Find Launch Velocity and Launch Angle

This level is for students who have taken or are taking calculus.

### Goal

Use derivatives of the parametric equations to estimate launch velocity and launch angle.

If:

```text
x(t) = a + bt
y(t) = c + dt + et^2
```

then:

```text
dx/dt = b
dy/dt = d + 2et
```

At launch, use `t = 0` or the first time value after the ball leaves the shooter.

```text
horizontal velocity = dx/dt
vertical velocity = dy/dt
```

The initial speed is:

```text
v0 = sqrt((dx/dt)^2 + (dy/dt)^2)
```

The launch angle is:

```text
theta = arctan((dy/dt)/(dx/dt))
```

Use your calculator or Desmos to convert the angle to degrees if needed.

### Important Note

Your launch time may not actually be `t = 0` unless you set your video analysis that way. If your first tracked point happens after the ball has already been in the air, then `dy/dt` at that time will be lower than the true initial vertical velocity because gravity has already slowed the upward motion.

### Reflection

How does the launch angle from your data compare with the physical angle of the shooter?

---

## Level 6 Statistics Challenge: Compare Multiple Shots

### Goal

Use statistics to measure consistency.

Record and analyze several shots using the same robot settings.

For each shot, record:

| Shot # | Launch Angle Setting | Flywheel Power | Hit / Miss | Notes |
|---:|---:|---:|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

Then compare:

- estimated launch speed
- estimated launch angle
- maximum height
- horizontal distance
- hit/miss result
- bounce-out result

### Questions to Answer

1. Were the shots consistent?
2. Which measurement varied the most?
3. Did higher launch speed always help?
4. Did a slower shot ever score more reliably?
5. What setting gave the best balance between reaching the goal and staying in the goal?

### Reflection

What does “reliable” mean for your shooter: one great shot or several repeatable shots?

---

## How This Helps the Robot

This challenge can help your team make better engineering decisions.

| Evidence From Video | Possible Design Decision |
|---|---|
| Ball falls short | Increase wheel speed, increase angle, reduce friction, or improve compression |
| Ball overshoots | Lower wheel speed or adjust angle |
| Ball hits hard and bounces out | Try a slower shot or higher arc |
| Ball path changes each shot | Improve trigger, hopper feed, compression, or flywheel recovery |
| Ball enters flywheel differently each time | Improve hopper and trigger alignment |
| Flywheel slows after each shot | Wait longer between shots or improve motor/flywheel design |

---

## Final Product Options

Choose one final product:

### Option A: One-Page Lab Report

Include:

- picture or screenshot from video analysis
- data table
- two graphs
- regression equations
- one conclusion about the shooter
- one recommended design change

### Option B: Team Presentation Slide

Include:

- one image of the shot path
- one graph
- one equation
- one design decision supported by data

### Option C: Advanced Calculus Explanation

Include:

- parametric equations
- derivatives
- estimated launch velocity
- estimated launch angle
- explanation of how this connects to the physical shooter

---

## Success Criteria

You are successful if you can:

- collect usable video data
- graph horizontal and vertical position separately
- identify linear horizontal motion and quadratic vertical motion
- use regression to model the shot
- explain one design decision based on evidence
- communicate uncertainty honestly

Advanced success includes:

- using derivatives to estimate velocity
- using trigonometry to estimate launch angle
- comparing multiple shots statistically
- explaining why real-world data does not perfectly match the ideal model

---

## References

College Board. (n.d.). *AP Calculus BC*. AP Students. https://apstudents.collegeboard.org/courses/ap-calculus-bc

College Board. (n.d.). *AP Physics 1: Algebra-Based*. AP Students. https://apstudents.collegeboard.org/courses/ap-physics-1-algebra-based

College Board. (n.d.). *AP Statistics*. AP Students. https://apstudents.collegeboard.org/courses/ap-statistics

Open Source Physics. (n.d.). *Tracker Video Analysis and Modeling Tool for Physics Education*. https://opensourcephysics.github.io/tracker-website/

U.S. Bureau of Labor Statistics. (2025). *Data Scientists: Occupational Outlook Handbook*. https://www.bls.gov/ooh/math/data-scientists.htm

U.S. Bureau of Labor Statistics. (2025). *Financial Analysts: Occupational Outlook Handbook*. https://www.bls.gov/ooh/business-and-financial/financial-analysts.htm

U.S. Bureau of Labor Statistics. (2025). *Mathematicians and Statisticians: Occupational Outlook Handbook*. https://www.bls.gov/ooh/math/mathematicians-and-statisticians.htm

U.S. Bureau of Labor Statistics. (2025). *Physicists and Astronomers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/life-physical-and-social-science/physicists-and-astronomers.htm
