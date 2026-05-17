# Challenge by Choice: Courses, Careers, and Team Contributions

## Purpose

Robotics is not one subject. It is where **math**, **science**, **coding**, **design**, **communication**, and **teamwork** meet.

In this course, every team is building a working robot. Some students may also choose a **Challenge by Choice** pathway. These pathways let students go deeper into a part of the project that connects to high school courses, college pathways, and future careers.

You do not need to be an expert to choose a challenge. The goal is to learn something useful, contribute to your team, and build evidence of your growth.

These course and career connections are not meant to sort students into tracks. They are meant to show that robotics opens many doors. A student who enjoys building may discover engineering. A student who enjoys art may discover CAD or design. A student who enjoys math may discover physics, statistics, or data science. A student who enjoys writing or speaking may discover technical communication, leadership, or entrepreneurship.

## Why Challenge by Choice?

A robotics team works best when everyone has meaningful work to do. Not everyone needs to work on the same part at the same time. Some students may be building the chassis. Others may be organizing code, testing the shooter, collecting data, designing a laser-cut part, preparing the presentation, or checking the robot for safety.

This approach helps the team because different students can make temporary contributions:

- A student who likes drawing, art, or geometry might try the **CAD/Fabrication Challenge**.
- A student who likes logic, games, apps, or AP Computer Science might try the **Software Engineering Challenge**.
- A student who likes math, motion, sports, physics, or data might try the **Physics/Data Challenge**.
- A student who likes careful checking, tools, and reliability might try the **Inspection/Reliability Challenge**.
- A student who likes writing, speaking, humor, visuals, or leadership might try the **Presentation/Judging Challenge**.

The goal is not to separate students by skill level. The goal is to let every student find a way into robotics that feels real and valuable.

These challenges are not permanent jobs. You can choose one challenge, try part of a challenge, work with a partner, switch later, or bring what you learn back to your team. Everyone should still build, test, code, document, and present in some way during the course.

## Robotics Connects Courses to Real Work

Some students may be younger and still deciding what courses to take in high school. Other students may already have taken courses like AP Computer Science A, AP Calculus, AP Physics, or AP Statistics but have not had many chances to use that knowledge on a physical project.

Robotics gives both groups a bridge.

Younger students can see why these courses matter. Older students can use what they already know to solve real problems.

## Challenge Pathways

| Challenge Pathway | Connects to Courses | Team Contribution | Possible Careers |
|---|---|---|---|
| CAD / Fabrication | Geometry, art/design, engineering, architecture | Design laser-cut parts and mounting templates | Mechanical engineering, architecture, industrial design, drafting, product design |
| Software Engineering | AP Computer Science A, Java, robotics programming, entrepreneurship | Organize robot code into methods or classes | Software development, robotics, app development, AI tools, startup work |
| Physics / Data | AP Physics, AP Calculus, AP Statistics, data science | Analyze ball motion and tune the shooter | Physics, engineering, data science, quantitative analysis |
| Reliability / Inspection | Engineering, manufacturing, aviation, motorsports | Make the robot safer, more reliable, and inspection-ready | Quality engineering, safety engineering, manufacturing, aerospace |
| Presentation / Judging | English, business, design, leadership | Tell the team’s engineering story clearly | Business, marketing, product management, engineering leadership, communication |

## Pathway 1: CAD / Fabrication Challenge

### What You Do

The CAD/Fabrication Challenge invites you to design a part that can be made with tools such as a laser cutter, 3D printer, or CNC machine.

In this course, one possible CAD challenge is to design an **adjustable shooter mount**. The mount could be laser-cut from 1/4 inch plywood and attached to aluminum channel. The aluminum channel holds the flywheel shooter. The plywood side plate provides a pivot hole and a curved slot so the team can adjust the launch angle.

### Courses This Connects To

- Geometry
- Art and design
- Engineering design
- Architecture
- Physics
- Manufacturing

### Why Geometry Matters

CAD is geometry that can be built. A line might become the edge of a plate. A circle might become a pivot hole. An arc might become a curved adjustment slot. A rectangle might become the outline of a laser-cut part.

Students with an artist’s eye may enjoy CAD because it uses proportion, balance, symmetry, shape, and visual judgment. Students who like math may enjoy CAD because it uses radius, diameter, angle, distance, parallel lines, perpendicular lines, constraints, and measurement.

### Career Connection

CAD is used by mechanical engineers, architects, drafters, industrial designers, fashion designers, set designers, game artists, and product designers. Mechanical engineers had a 2024 median annual wage of $102,320, and employment is projected to grow faster than average from 2024 to 2034 (U.S. Bureau of Labor Statistics [BLS], 2025c). Architecture and engineering occupations as a group had a 2024 median annual wage of $97,310, which was higher than the median for all occupations (BLS, 2025j).

### Possible Team Deliverable

- A Fusion 360 sketch
- A DXF or SVG file for the laser cutter
- A cardboard prototype
- A plywood test part
- A short explanation of how the part works

## Pathway 2: Software Engineering Challenge

### What You Do

The Software Engineering Challenge invites you to organize the robot code so the team can understand, test, and reuse it.

A first challenge is to create **methods** for important actions, such as:

```java
shooterOn();
shooterOff();
triggerLoad();
triggerRelease();
fireOneBall();
```

A deeper challenge is to create a separate **ShooterSystem** class with methods inside it. The OpMode can then create an object and call its methods.

### Courses This Connects To

- AP Computer Science A
- Robotics programming
- Java
- Algebra and logic
- Entrepreneurship
- App development

### Why AP Computer Science A Matters

AP Computer Science A is an introductory college-level computer science course. Students learn to analyze, write, and test code while studying concepts such as variables, control structures, modularity, and methods (College Board, n.d.-b). The course focuses on object-oriented programming and problem-solving using Java (College Board, 2025). That connects directly to FTC-style robot programming because FTC robots are commonly programmed in Java.

### AI and Software Engineering

AI tools can help students write code, explain errors, and suggest better structure. But AI does not remove the need to understand the robot. A programmer still has to know what the robot should do, test the code safely, recognize when the code is wrong, and explain the design to teammates.

AI may make software development more accessible to students because a small group of people can now build prototypes, websites, apps, and automation tools with less money than before. Many startups begin with people using their own labor, open-source tools, cloud services, and AI-assisted development.

### Career Connection

Software developers had a 2024 median annual wage of $133,080, and software developer employment is projected to grow faster than average from 2024 to 2034 (BLS, 2025a). Computer and information technology occupations as a group had a 2024 median annual wage of $105,990, above the median for all occupations (BLS, 2025i). Entry-level software work can be competitive, but students who combine coding with robotics, math, data, communication, and project experience can build a stronger portfolio.

### Possible Team Deliverable

- Cleaner TeleOp code
- Named methods for shooter and trigger actions
- A `ShooterSystem` class
- A GitHub repository
- A short explanation of how the code is organized

## Pathway 3: Physics / Data Challenge

### What You Do

The Physics/Data Challenge invites you to study how the ball moves after it leaves the shooter.

One possible challenge is to take video of the ball in motion, use motion tracking software to collect position data, and graph the results. The student can show that:

- The horizontal position is modeled well by a linear function.
- The vertical position is modeled well by a quadratic function.
- The ball’s path can be described using parametric equations.

A student who is ready to try calculus can find derivatives of the parametric equations to estimate launch velocity and launch angle.

### Courses This Connects To

- AP Physics
- AP Calculus
- AP Statistics
- Algebra
- Data science

### Why the Math Matters

Projectile motion turns math into something visible. A graph is not just a classroom exercise; it describes the path of the actual ball the robot launched.

Statistics helps students collect data, fit regression models, and decide whether results are consistent. Calculus helps students connect position, velocity, and acceleration. Physics helps students understand forces, gravity, velocity, and projectile motion.

### Career Connection

Physicists had a 2024 median annual wage of $166,290, though many physics careers require graduate training (BLS, 2025d). Data scientists had a 2024 median annual wage of $112,590, and employment is projected to grow 34% from 2024 to 2034, much faster than average (BLS, 2025b). Statisticians had a 2024 median annual wage of $103,300 (BLS, 2025e). Financial and investment analysts had a 2024 median annual wage of $101,350 (BLS, 2025f). Quantitative analysis roles at investment firms can pay considerably more at the high end, but those jobs are highly competitive and usually require strong math, programming, statistics, and communication skills.

### Possible Team Deliverable

- A video of the ball trajectory
- A data table of x- and y-coordinates
- A Desmos graph with regression models
- A recommendation for launch angle or flywheel power
- A calculus extension estimating launch velocity and angle

## Pathway 4: Reliability / Inspection Challenge

### What You Do

The Reliability/Inspection Challenge invites you to help the robot pass safety and readiness checks. This work looks for problems before they cause failure.

This might include:

- Checking wires
- Checking sharp edges
- Confirming the robot fits inside the 18-inch cube
- Checking the power switch
- Making sure the battery is secure
- Making sure the robot starts and drives
- Checking that wheels, flywheels, and servos are safe to operate

### Courses This Connects To

- Engineering
- Manufacturing
- Robotics
- Aviation and aerospace
- Motorsports
- Technical writing

### Why Inspection Matters

Inspection is used in many serious engineering fields. Race cars are inspected before they compete. Airplanes are inspected before they fly. Spacecraft go through extensive checks before launch. Inspection is not about blame. It is about finding problems early enough to fix them.

### Career Connection

Reliability, inspection, and safety skills connect to engineering, manufacturing, aerospace, aviation, motorsports, construction, and quality control. Many technical careers require people who can notice risks, use checklists, document problems, and communicate clearly under time pressure.

### Possible Team Deliverable

- Inspection checklist
- List of fixes needed before demonstration
- Wiring and safety photo evidence
- Size-check documentation
- Final robot readiness sign-off

## Pathway 5: Presentation / Judging Challenge

### What You Do

The Presentation/Judging Challenge invites you to help the team explain what it built and what it learned.

The team presentation should be short, clear, visual, and compelling. A good goal is a 4-minute presentation with time left for 3–5 minutes of questions.

### Courses This Connects To

- English
- Business
- Public speaking
- Design
- Leadership
- Engineering communication

### Why the Story Matters

A robot is not just a machine. It is the result of choices, failures, teamwork, testing, and improvement. Judges want to understand the team’s process. A strong presentation explains:

- What the team tried first
- What failed
- What changed
- What evidence helped the team improve
- What each student contributed
- What the team would do next

### Career Connection

Nearly every technical career requires communication. Engineers, software developers, scientists, designers, and entrepreneurs all need to explain ideas to teammates, clients, managers, users, investors, or judges. A strong technical idea becomes more powerful when the team can explain it clearly.

### Possible Team Deliverable

- 4-minute presentation script
- Slide or visual plan
- Award evidence table
- Team growth story
- Practice answers to judge questions

## How Teams Should Use Challenge Pathways

Challenge work should support the team. A student working on a challenge should not disappear from the robot project. Instead, bring useful information back to the team and invite others to understand or try part of the work.

A helpful daily routine is a short challenge report-out:

1. What did I work on?
2. What did I learn?
3. What does the team need to know?
4. What is my next step?

## Example Team Contribution Plan

| Temporary Contribution | Main Work | Report-Out Question |
|---|---|---|
| Building support | Chassis, hopper, shooter, trigger | What changed physically on the robot today? |
| Programming support | TeleOp, trigger code, shooter methods | What can the robot do in code today? |
| CAD/Fabrication Challenge | Adjustable mount or laser-cut part | What part can we fabricate or revise? |
| Physics/Data Challenge | Shot testing and graphs | What data helps us tune the shooter? |
| Inspection support | Wires, size, safety, readiness | What must be fixed before testing? |
| Presentation support | Photos, story, script, awards | What story are we going to tell? |

## Choosing a Challenge

Choose a challenge if one of these sounds like you:

- I like drawing, design, shape, or precision.
- I like coding, logic, games, or apps.
- I like math, motion, graphs, or data.
- I like tools, safety, and making things reliable.
- I like speaking, writing, visuals, humor, or storytelling.
- I want to try something that might connect to a future course or job.

You can change contributions as the project develops. You can also work with another student. The goal is not to finish the hardest challenge. The goal is to contribute something real to the team.

## Final Message

Robotics is a place where different kinds of students can shine.

Some students are strong builders. Some are careful testers. Some are visual designers. Some are programmers. Some are data analysts. Some are storytellers. Some are leaders who help the team work together.

A good team needs all of these strengths.

The Challenge by Choice pathways are invitations. They let you try a skill that connects to future courses, college pathways, careers, and real engineering work.

## Suggested File Organization

A good repository structure would be:

```text
challenge_by_choice/
  README.md
  challenge_by_choice_courses_and_careers.md
  cad_challenge_adjustable_shooter_mount_handout.md
  software_engineering_super_challenge_robot_shooter_code.md
  physics_super_challenge_projectile_motion_video_analysis.md
```

The `README.md` can act as the menu page. This file can introduce the pathways, while the individual challenge files can give step-by-step directions.

If the course repository already has a `readings/` folder and you want these to appear as Day 1 or Day 2 readings, you could also link to this file from:

```text
readings/day1_session2_challenge_by_choice_courses_and_careers.md
```

or keep the master copy in `challenge_by_choice/` and reference it from the daily session plan.

## References

College Board. (2025). *AP Computer Science A course overview*. AP Central. https://apcentral.collegeboard.org/media/pdf/ap-computer-science-a-course-overview.pdf

College Board. (n.d.-a). *AP Computer Science A*. AP Students. https://apstudents.collegeboard.org/courses/ap-computer-science-a

College Board. (n.d.-b). *AP Computer Science A*. AP Central. https://apcentral.collegeboard.org/courses/ap-computer-science-a

U.S. Bureau of Labor Statistics. (2025a). *Software developers, quality assurance analysts, and testers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm

U.S. Bureau of Labor Statistics. (2025b). *Data scientists: Occupational Outlook Handbook*. https://www.bls.gov/ooh/math/data-scientists.htm

U.S. Bureau of Labor Statistics. (2025c). *Mechanical engineers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/architecture-and-engineering/mechanical-engineers.htm

U.S. Bureau of Labor Statistics. (2025d). *Physicists and astronomers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/life-physical-and-social-science/physicists-and-astronomers.htm

U.S. Bureau of Labor Statistics. (2025e). *Mathematicians and statisticians: Occupational Outlook Handbook*. https://www.bls.gov/ooh/math/mathematicians-and-statisticians.htm

U.S. Bureau of Labor Statistics. (2025f). *Financial analysts: Occupational Outlook Handbook*. https://www.bls.gov/ooh/business-and-financial/financial-analysts.htm

U.S. Bureau of Labor Statistics. (2025g). *Employment projections: 2024–2034 summary*. https://www.bls.gov/news.release/ecopro.nr0.htm

U.S. Bureau of Labor Statistics. (2025h). *Business and financial occupations: Occupational Outlook Handbook*. https://www.bls.gov/ooh/business-and-financial/

U.S. Bureau of Labor Statistics. (2025i). *Computer and information technology occupations: Occupational Outlook Handbook*. https://www.bls.gov/ooh/computer-and-information-technology/

U.S. Bureau of Labor Statistics. (2025j). *Architecture and engineering occupations: Occupational Outlook Handbook*. https://www.bls.gov/ooh/architecture-and-engineering/
