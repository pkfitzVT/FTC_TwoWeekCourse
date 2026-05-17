# Using AI Wisely in This Robotics Course

AI tools such as ChatGPT, Claude, GitHub Copilot, and other coding assistants can be useful in robotics. They can help explain vocabulary, suggest code structure, debug error messages, organize ideas, and help you prepare presentations.

But AI is not a replacement for building, testing, measuring, and asking mentors for feedback. Robotics is physical. The robot has real parts, real wires, real friction, real weight, real size limits, and real problems that may not be obvious from a typed description.

The best robotics teams use AI as a helper, not as the engineer.

AI should help more students enter the work, not help one student take over. If AI helps you understand code, CAD, physics, or presentation writing, use that knowledge to explain ideas to your teammates and invite them into the process.

Using AI well should make your team more collaborative. It should help people ask better questions, try unfamiliar work, and understand the robot more clearly.

---

## What AI Can Help With

AI can be helpful when you need to:

- understand a new word or idea
- rewrite notes in clearer language
- brainstorm possible solutions
- organize code into methods
- explain a Java error message
- write sample code for a motor or servo
- make a testing checklist
- prepare a short presentation
- turn rough notes into a stronger engineering notebook entry
- compare two design ideas before testing them

For example, if your servo trigger is confusing, you might ask:

> Explain the difference between a standard servo and a continuous rotation servo in FTC robotics.

Or:

> Help me write Java methods called `shooterOn`, `shooterOff`, `triggerLoad`, and `triggerRelease`.

Those are good uses of AI because the tool is helping you think, write, organize, or learn.

---

## What AI Is Not Good At

AI is often weak when the problem depends on the exact physical shape of your robot.

AI may struggle with:

- making accurate technical drawings
- understanding your exact robot from a short description
- knowing whether two parts will collide
- knowing whether a bolt hole lines up
- seeing if your hopper will jam
- judging whether a servo will hit the frame
- knowing whether your robot fits in the 18-inch cube
- understanding the real spacing, stiffness, and weight of your parts
- drawing clear geometry diagrams without mistakes

AI is especially weak at showing precise geometry ideas. It may describe an arc slot, pivot hole, or mounting pattern in words, but still fail to draw it correctly. For geometry and CAD work, you should use real measurements, sketches, Fusion 360, cardboard prototypes, mentors, and test cuts.

A good rule:

> If the problem depends on exact size, shape, alignment, motion, or safety, AI can give ideas, but the team must verify with real measurements and real tests.

---

## Your Best Resources

Your best resources are still the people and materials around you:

- mentors
- coaches
- experienced students
- teammates
- official FTC documentation
- REV and goBILDA product pages and build guides
- manufacturer videos
- videos from experienced FTC teams
- examples of robots from past seasons
- “Robot in 24 Hours” style videos
- your own testing data

Videos can be especially useful because robotics is visual. Watching another team build a drivetrain, shooter, intake, or servo trigger can help you understand what the mechanism is supposed to look like and how it moves.

When you watch a video, do not just copy it. Ask:

- What problem is this team solving?
- What parts are they using?
- How does the mechanism move?
- What looks simple?
- What looks fragile?
- What could we build with the parts we have?
- What would we need to change for our robot?

---

## AI and Software Development

AI can be especially powerful for programming.

Advanced robotics teams and professional software developers may use AI inside their coding tools. For example, they may use AI as a command-line interface, coding assistant, or chat helper inside an IDE. An **IDE** is an **integrated development environment**, such as Android Studio, VS Code, WebStorm, or IntelliJ. These tools help programmers write, organize, run, and debug code.

For teams that keep going deeper with FTC Java, Android Studio is often used for larger programming projects. AI coding tools can help create classes, organize methods, explain errors, and suggest improvements.

In this course, we will mostly use **OnBot Java**, which is simpler and runs through the robot system. Some students may still use AI to help plan and organize code, then copy carefully tested code into OnBot Java.

A good AI-assisted programming workflow is:

1. Describe the robot behavior you want.
2. Ask AI for a simple version of the code.
3. Read the code carefully.
4. Check that hardware names match your robot configuration.
5. Test one part at a time.
6. Add telemetry so you can see what the code is doing.
7. Fix errors slowly and carefully.
8. Save the version that works.

Do not paste code into the robot without understanding it. A robot can move unexpectedly if the code is wrong.

---

## AI Is a Helper, Not a Builder

AI cannot tighten bolts.

AI cannot see that your battery is sliding.

AI cannot hear that your servo is buzzing.

AI cannot feel that a wheel is rubbing.

AI cannot notice that a wire is about to get pulled into the flywheel.

AI cannot know that your team changed the hopper angle unless you tell it.

Robotics requires your eyes, hands, measurements, judgment, and teamwork.

Use AI to think faster, not to stop thinking.

---

## Good Questions to Ask AI

Good AI questions are specific and include context.

Weak question:

> Why does my robot not work?

Better question:

> My FTC robot uses OnBot Java. The left motor is named `leftDrive` and the right motor is named `rightDrive`. When I press dpad up, the robot spins instead of driving forward. What should I check?

Weak question:

> Make me a shooter.

Better question:

> We are building a gravity-fed flywheel shooter for a light foam ball. The flywheel works, but two balls sometimes enter at once. What are some simple hopper or trigger ideas to feed one ball at a time?

Weak question:

> Draw my CAD part.

Better question:

> I am making a laser-cut plywood plate in Fusion 360. I need a pivot hole and a curved slot centered on that pivot. What Fusion 360 sketch tools should I use?

---

## Check AI Answers

Before you trust an AI answer, ask:

- Does this match our actual robot?
- Does this match our parts?
- Does this match our configuration names?
- Does this seem safe?
- Can we test this with the wheels off the ground?
- Can we test this with one ball first?
- Can a mentor or coach check this?
- Does the explanation make sense to us?

If the answer does not make sense, do not use it blindly.

---

## Using AI Ethically

Using AI is allowed when it helps you learn, design, debug, or explain. But you should be honest about how you used it.

Good uses:

- “We asked AI to explain servo positions.”
- “We used AI to help organize our code into methods.”
- “We used AI to improve our presentation script.”
- “We used AI to create a testing checklist, then we modified it for our robot.”

Not good:

- copying code you do not understand
- claiming AI-generated writing as your own thinking
- using AI instead of testing
- using AI to avoid contributing to the team
- using AI so one person controls the work while others watch
- ignoring mentors because AI gave a confident answer

A strong robotics student can say:

> I used AI for help, but I tested the idea, checked the result, and can explain what I learned.

---

## Final Reminder

AI is powerful, but robotics is real.

Your robot will teach you things that AI cannot predict. The best teams combine:

- human teamwork
- mentor feedback
- careful building
- good measurements
- reliable testing
- clear documentation
- smart use of AI

Use AI as one tool in your toolbox. Your team is still the engineer.
