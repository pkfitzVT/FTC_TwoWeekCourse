# CAD Challenge: Design a Laser-Cut Adjustable Shooter Mount

This challenge is one way to contribute to your team. It does not make you the only person responsible for CAD, fabrication, or the shooter mount. Share what you learn, invite others to try, and connect your work back to the team's build.

## Purpose

In this challenge, you will design a flat plywood side plate that can be cut on a laser cutter. The plate will help an aluminum shooter channel rotate around a fixed pivot point and lock at different launch angles.

The goal is not just to “make a part.” The goal is to learn how a designer uses geometry, measurement, constraints, and testing to create a useful robot component.

---

## Why CAD Matters

**CAD** stands for **computer-aided design**. CAD is how people turn an idea into a precise drawing, model, or manufactured part. In this robotics challenge, you are using CAD to design a laser-cut plywood plate with a pivot hole, a curved adjustment slot, and mounting holes. That may seem like a small part, but the same basic workflow is used by professionals who design cars, buildings, shoes, theater sets, video game environments, medical devices, furniture, robots, and spacecraft.

CAD is used in many different careers. **Mechanical engineers** use CAD to design machines, engines, tools, robots, and manufactured parts. The U.S. Bureau of Labor Statistics reports that mechanical engineers had a median pay of about **$102,320** in 2024, with employment projected to grow about **9% from 2024 to 2034** (U.S. Bureau of Labor Statistics, 2025a). **Architects** use CAD and building information modeling to design buildings and spaces; architects had median pay of about **$96,690** in 2024, with projected growth of about **4%** (U.S. Bureau of Labor Statistics, 2025b). **Drafters** specialize in turning sketches and engineering ideas into technical drawings; drafters had median pay of about **$65,380** in 2024, with little or no projected employment change from 2024 to 2034 (U.S. Bureau of Labor Statistics, 2025c). **Set and exhibit designers** use CAD-like tools to design theater sets, museum exhibits, trade-show booths, and themed spaces; their median pay was about **$66,280** in 2024 (U.S. Bureau of Labor Statistics, 2025d). **Fashion designers**, **industrial designers**, **interior designers**, animators, and video game artists also use digital design tools to create objects, spaces, characters, products, and visual worlds.

CAD is useful because it connects creativity with real-world making. Students who enjoy drawing, fashion, animation, architecture, robotics, games, sculpture, theater, or product design may find that CAD gives them a way to make their ideas precise enough to build.

People who enjoy CAD often like a mix of art, geometry, and problem-solving. CAD can appeal to students with an artist’s eye because it involves proportion, balance, symmetry, shape, negative space, and visual judgment. It can also appeal to students who like math because every sketch depends on geometry: points, lines, circles, arcs, radius, diameter, angle, distance, parallel lines, perpendicular lines, constraints, and measurement. In CAD, geometry becomes something you can build. A circle is not just a circle; it might become a pivot hole. An arc is not just a curve; it might become a slot that controls launch angle.

Career satisfaction varies. Some people love design work because it combines creativity, precision, teamwork, and problem-solving. Others find engineering or architecture stressful because real projects have deadlines, budgets, safety requirements, clients, and revisions. CareerExplorer survey data rates mechanical engineers at **3.0 out of 5** for career happiness and architects at **3.1 out of 5** (CareerExplorer, n.d.-a; CareerExplorer, n.d.-b). That does not mean these careers are bad. It means students should explore not only salary and demand, but also the daily work: Do you like solving hard problems? Do you like revising designs? Do you like making precise drawings? Do you like working between art, math, tools, and people? If yes, CAD may be a skill worth developing.

---

## CAD Career Connections

| Field | How CAD or 3D Design Is Used | 2024 Median Pay / Outlook |
|---|---|---|
| Mechanical engineering | Machines, motors, robots, tools, manufactured parts | $102,320; projected 9% growth |
| Architecture | Buildings, rooms, site plans, construction drawings | $96,690; projected 4% growth |
| Drafting | Technical drawings from engineering or architectural plans | $65,380; little or no projected employment change |
| Set and exhibit design | Theater sets, museum exhibits, trade-show spaces | $66,280; limited growth, but ongoing openings as workers leave the field |
| Fashion design | Clothing patterns, digital prototypes, product design | Projected 2% growth from 2024 to 2034 |
| Game art / animation | Characters, props, environments, visual effects | Special effects artists and animators: $99,800; limited growth, but ongoing openings |
| Industrial design | Products, tools, consumer goods, user-focused objects | $79,450; design work connected to manufacturing and product development |

---

## Nearby College and Training Connections

There are several nearby college pathways where students can continue learning CAD, design, engineering, architecture, or digital 3D art.

| School / Program | Connection to CAD and Design |
|---|---|
| University of Vermont | UVM offers engineering programs and an undergraduate certificate in **Computer-Aided Engineering Technology**. UVM describes CAET as computer-based tools used for development, communication, and evaluation of product and building designs. The certificate includes computerized automation techniques and three-dimensional form and location geometry (University of Vermont, n.d.-a). |
| UVM Engineering Courses | UVM’s engineering course catalog includes project-based engineering drawing and computer-aided drafting/design coursework (University of Vermont, n.d.-b). |
| Norwich University | Norwich offers architecture and design pathways. Its Design+Build work gives students experience designing and building full-scale projects, connecting design ideas to real construction (Norwich University, n.d.-a; Norwich University, n.d.-b). |
| Vermont State University | Vermont State University offers Architectural Engineering Technology programs where students learn architecture, design, engineering, construction, CAD, and BIM systems such as Autodesk Revit (Vermont State University, n.d.-a; Vermont State University, n.d.-b). |
| Champlain College | Champlain College offers game art and animation pathways where students build 2D and 3D art, environments, characters, and interactive media. This is a digital design pathway that connects artistic vision with technical tools. |

These are different pathways, but they all connect to the same idea: design starts as a visual idea, becomes a measured model, and then becomes something people can build, test, improve, or experience.

---

## The Robot Part You Are Designing

You are designing an **adjustable shooter side plate**.

The shooter itself is mounted to an **aluminum channel**. The channel holds the flywheel, motor, ramp, and possibly hopper pieces. The plywood plate does not directly hold the flywheel motor. Instead, the plywood plate lets the aluminum channel rotate and lock at different angles.

The side plate needs:

| Feature | Purpose |
|---|---|
| Outer rectangle or custom outline | Shape of the plywood part |
| Pivot hole | Fixed rotation point |
| Curved slot | Lets the aluminum channel rotate and lock |
| Mounting hole pattern | Lets the plywood plate attach to the robot structure |
| Labels and angle tick marks | Helps the team record launch-angle tests |

The design idea is:

1. A **pivot bolt** goes through the plywood plate and the aluminum channel.
2. A **lock bolt** goes through the curved slot and the aluminum channel.
3. When the lock bolt is loose, the channel rotates.
4. When the lock bolt is tightened with a washer and wing nut, the angle is locked.

---

## Why Geometry Matters

The curved slot must be centered on the pivot hole.

That means:

> The pivot hole is the center of the circle.  
> The curved slot follows part of that circle.

The radius of the slot is not random. It should match the center-to-center distance between the two holes you choose on the aluminum channel:

> **slot radius = distance from pivot hole to lock-bolt hole on the aluminum channel**

If the radius does not match, the lock bolt will not slide smoothly through the slot.

---

## Recommended Units

Use **metric units** for this project.

REV and goBILDA parts are based on metric patterns. Even if some of your bolts are inch-based, the robot building systems use millimeter spacing. Working in millimeters will make hole patterns easier.

Useful conversions:

| Measurement | Approximate metric value |
|---|---:|
| 1/4 inch plywood | 6.35 mm |
| 1 inch | 25.4 mm |
| 1/4 inch bolt clearance | about 7.5–8.0 mm |
| 8 mm spacing | about 0.315 inch |
| 16 mm spacing | about 0.63 inch |

---

## REV and goBILDA Hole Pattern Basics

Many robot building systems use repeated hole patterns. This lets parts line up without custom drilling.

| Build system | Hardware | Basic hole/grid idea | Student CAD note |
|---|---:|---:|---|
| REV DUO | M3 screws | 8 mm pitch/grid on many brackets and structural parts | Use about 3.3–3.5 mm clearance holes for M3 bolts |
| goBILDA | M4 screws | 4 mm holes on an 8 mm grid; 16 mm spacing is common for stronger structural patterns | Use about 4.3–4.5 mm clearance holes for M4 bolts |

For laser-cut plywood, holes should usually be a little oversized because the laser removes material, plywood can vary, and student assembly is not perfect.

---

## Pivot-to-Lock Hole Distance Options

The pivot-to-lock distance controls the radius of the curved slot. A longer distance usually makes the adjustment more stable because the lock bolt has more leverage.

A good classroom rule:

> Use at least **three hole spaces** between the pivot bolt and the lock bolt if possible.

If the holes are too close together, the angle may be harder to lock and the shooter may wobble more.

| System / spacing pattern | 2 spaces | 3 spaces | 4 spaces | 5 spaces |
|---|---:|---:|---:|---:|
| REV-style 8 mm pitch | 16 mm | 24 mm | 32 mm | 40 mm |
| goBILDA 8 mm grid | 16 mm | 24 mm | 32 mm | 40 mm |
| goBILDA common 16 mm structural spacing | 32 mm | 48 mm | 64 mm | 80 mm |

For an adjustable shooter plate, a radius closer to **48–80 mm** is often more useful than a very short radius, if the channel geometry allows it.

---

## Suggested Mounting Patterns

### REV-Friendly Mounting Row

Use M3 clearance holes on an 8 mm pitch.

```text
o---8 mm---o---8 mm---o---8 mm---o
```

Suggested hole diameter:

```text
3.3 mm to 3.5 mm
```

### goBILDA-Friendly Mounting Grid

Use M4 clearance holes on an 8 mm grid. For stronger mounting, emphasize 16 mm spacing.

```text
o---16 mm---o---16 mm---o
|           |           |
16 mm      16 mm      16 mm
|           |           |
o---16 mm---o---16 mm---o
```

Suggested hole diameter:

```text
4.3 mm to 4.5 mm
```

For a shooter support plate, use at least two mounting bolts. Four mounting bolts are better if the plate is holding load or resisting vibration.

---

# Fusion 360 Workflow

## Step 1: Create a New Design

Open Fusion 360 and create a new design.

Set the units to millimeters.

Suggested starting part size:

```text
Plate width: 160 mm
Plate height: 120 mm
Material thickness: 6.35 mm if modeling 1/4 inch plywood
```

You can change these dimensions later.

---

## Step 2: Start with a 2D Sketch

Create a new sketch on the front plane.

CAD usually starts with a **2D sketch**. In the sketch, you use geometric tools organized into menus. These tools create rectangles, circles, arcs, slots, lines, and patterns.

For this part, start by drawing the outside rectangle for the wood that will be cut.

---

## Step 3: Draw the Outer Rectangle

Use the rectangle tool.

Example:

```text
160 mm × 120 mm
```

This represents the flat plywood plate.

Make sure the rectangle is a closed shape.

---

## Step 4: Add the Pivot Hole

Add a circle for the pivot point.

The pivot hole is the center of rotation for the adjustable shooter channel.

Suggested clearance holes:

| Bolt size | Suggested CAD hole diameter |
|---|---:|
| M3 | 3.3–3.5 mm |
| M4 | 4.3–4.5 mm |
| M5 | 5.3–5.5 mm |
| M6 | 6.5–7.0 mm |
| 1/4 inch bolt | about 7.5–8.0 mm |

Important note:

> The pivot hole should fit the bolt that will act as the rotation point. The pivot should not be loose enough to wobble badly, but it must be large enough for the bolt to pass through.

---

## Step 5: Measure the Aluminum Channel

Choose two holes on the aluminum channel:

1. One hole for the pivot bolt.
2. One hole for the lock bolt.

Measure the center-to-center distance between those holes.

That measurement becomes the radius of the curved slot.

Example:

```text
Pivot-to-lock distance on channel = 64 mm
Slot radius in CAD = 64 mm
```

---

## Step 6: Create the Curved Slot

Use:

```text
Create → Slot → Center Point Arc Slot
```

Click in this order:

1. Click the center of the pivot hole.
2. Click where the slot should start.
3. Click where the slot should end.
4. Move the mouse to set the slot width, or type the slot width.

Suggested slot widths:

| Lock bolt size | Suggested slot width |
|---|---:|
| M4 | 4.5–5.0 mm |
| M5 | 5.5–6.0 mm |
| M6 | 6.8–7.2 mm |
| 1/4 inch bolt | about 7.5–8.0 mm |

The slot should be wider than the bolt so the bolt can slide smoothly.

Important note:

> The center of the slot must be the pivot hole. The slot radius must match the pivot-to-lock hole distance on the aluminum channel.

---

## Step 7: Choose the Angle Range

Decide how much launch-angle adjustment your team needs.

Possible starting range:

```text
50° to 75°
```

The exact range depends on the shooter design, goal height, distance to the target, and whether the hopper still lines up as the shooter rotates.

Design warning:

> When the shooter angle changes, the ball path may also change. Make sure the hopper can still feed the ball into the flywheel across the useful angle range.

---

## Step 8: Add Chassis Mounting Holes

Choose one mounting pattern.

### REV option

Use M3 clearance holes:

```text
Hole diameter: 3.3–3.5 mm
Hole spacing: 8 mm
```

### goBILDA option

Use M4 clearance holes:

```text
Hole diameter: 4.3–4.5 mm
Hole spacing: 8 mm grid or 16 mm structural spacing
```

Recommendation:

> Use at least two mounting holes. Four mounting holes are better for a shooter support plate.

Do not put mounting holes too close to the edge of the plywood.

---

## Step 9: Add Labels and Tick Marks

Use text or sketch lines for engraving.

Possible labels:

```text
PIVOT
ANGLE LOCK
50°
55°
60°
65°
70°
75°
```

These should be engraved, not cut all the way through.

Tick marks help the team record test data:

| Angle | Flywheel power | Distance | Result |
|---:|---:|---:|---|
| 55° | 0.7 | 36 in | short |
| 60° | 0.7 | 36 in | hit rim |
| 65° | 0.7 | 36 in | scored |

---

## Step 10: Check the Sketch

Before exporting, check:

- Is the outer rectangle closed?
- Is the pivot hole inside the plate?
- Is the slot a closed slot shape, not just an arc line?
- Is the slot fully inside the plate?
- Are mounting holes far enough from the edge?
- Is there enough space for washers around the pivot and lock bolt?
- Will the aluminum channel have room to rotate?
- Will the robot still fit inside the required size limit?
- Will the hopper still line up with the shooter?

---

## Step 11: Optional 3D Extrusion

You can extrude the sketch to visualize the part.

For 1/4 inch plywood:

```text
Extrusion thickness: 6.35 mm
```

This helps you check the shape, but the laser cutter usually needs the 2D sketch profile, not the 3D body.

---

## Step 12: Export for the Laser Cutter

The usual workflow is:

```text
Finish Sketch
Right-click the sketch
Save as DXF
Import the DXF into the laser cutter software
Assign cut and engrave settings
Cut a cardboard test first
Then cut plywood
```

Different laser cutters use different software. Ask which file type your school laser cutter prefers. Common formats include:

```text
DXF
SVG
PDF
AI
```

Fusion 360 commonly exports sketches as DXF.

---

## Step 13: Cut a Test Piece First

Do not cut a full class set first.

Test with cardboard or scrap plywood.

Check:

- Does the pivot bolt fit?
- Does the lock bolt slide in the curved slot?
- Does the aluminum channel rotate smoothly?
- Can the wing nut lock the angle?
- Are the mounting holes aligned?
- Does the shooter stay steady?
- Does the hopper still line up?
- Does the robot fit inside the size constraint?

Then revise the CAD file if needed.

---

## 3D Printing Option

A student could also add an extrusion and 3D print the part, but this should usually be treated as a prototype option, not the main support solution.

A 1/4 inch plastic body might work for a small or light test piece, but it may not be strong enough to support the flywheel, hopper, vibration, and adjustment forces unless it is carefully designed.

3D printed parts can fail because of:

- layer direction
- low infill
- weak material
- thin walls
- repeated vibration
- stress around holes
- heat or softening
- cracks near screws

For this course, a good rule is:

> Use plywood for flat adjustable side plates, aluminum channel for the main shooter structure, and 3D printing for small guides, spacers, servo brackets, or prototypes.

---

## Suggested First Version

Use this as a starting design:

```text
Units: millimeters
Plate: 160 mm × 120 mm
Material: 1/4 inch plywood, modeled as 6.35 mm
Pivot bolt: M5, M6, or 1/4 inch depending on team hardware
Slot radius: 64 mm or 80 mm if the channel geometry allows it
Angle range: 50°–75°
Slot width: bolt diameter + about 1 mm
Mounting pattern: REV M3 row or goBILDA M4 grid
```

The CAD challenge is to modify the template to fit your team’s actual channel and shooter geometry.

---

## Reflection Questions

1. What measurement controlled the radius of your curved slot?
2. How did geometry help you make a physical robot part?
3. What is one place where your design might fail or loosen?
4. What part of your CAD design feels more like math?
5. What part of your CAD design feels more like art?
6. If you had one more version, what would you improve?

---

## References

CareerExplorer. (n.d.-a). *Are architects happy?* CareerExplorer. https://www.careerexplorer.com/careers/architect/satisfaction/

CareerExplorer. (n.d.-b). *Are mechanical engineers happy?* CareerExplorer. https://www.careerexplorer.com/careers/mechanical-engineer/satisfaction/

Champlain College. (n.d.). *Game art degree: Bachelor of Fine Arts*. Champlain College. https://www.champlain.edu/academics/undergraduate-academics/degrees-programs/game-art/

Norwich University. (n.d.-a). *Architectural studies*. Norwich University. https://home.norwich.edu/on/academics/programs/architecture-art

Norwich University. (n.d.-b). *Design+Build Collaborative*. Norwich University. https://www.norwich.edu/academics/colleges-and-schools/college-professional-schools/designbuild-collaborative

University of Vermont. (n.d.-a). *Computer-Aided Engineering Technology undergraduate certificate*. University of Vermont Catalogue. https://catalogue.uvm.edu/undergraduate/engineeringandmathematicalsciences/interdisciplinaryengineeringprograms/computeraidedengineeringtechnologycertificate/

University of Vermont. (n.d.-b). *Engineering (ENGR) courses*. University of Vermont Catalogue. https://catalogue.uvm.edu/undergraduate/courses/courselist/engr/

U.S. Bureau of Labor Statistics. (2025a). *Mechanical engineers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/architecture-and-engineering/mechanical-engineers.htm

U.S. Bureau of Labor Statistics. (2025b). *Architects: Occupational Outlook Handbook*. https://www.bls.gov/ooh/architecture-and-engineering/architects.htm

U.S. Bureau of Labor Statistics. (2025c). *Drafters: Occupational Outlook Handbook*. https://www.bls.gov/ooh/architecture-and-engineering/drafters.htm

U.S. Bureau of Labor Statistics. (2025d). *Set and exhibit designers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/arts-and-design/set-and-exhibit-designers.htm

U.S. Bureau of Labor Statistics. (2025e). *Fashion designers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/arts-and-design/fashion-designers.htm

U.S. Bureau of Labor Statistics. (2025f). *Special effects artists and animators: Occupational Outlook Handbook*. https://www.bls.gov/ooh/arts-and-design/multimedia-artists-and-animators.htm

U.S. Bureau of Labor Statistics. (2025g). *Industrial designers: Occupational Outlook Handbook*. https://www.bls.gov/ooh/arts-and-design/industrial-designers.htm

Vermont State University. (n.d.-a). *Architectural Engineering Technology, A.S.* Vermont State University. https://vermontstate.edu/academic-programs/architectural-engineering-technology-as/

Vermont State University. (n.d.-b). *Architectural Engineering Technology, B.S.* Vermont State University. https://vermontstate.edu/academic-programs/architectural-engineering-technology-bs/
