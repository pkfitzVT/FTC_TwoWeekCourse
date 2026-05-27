# Performance Testing Postmortem SLD Template

## Use This When

Use this SLD after a performance test, practice run, subsystem test, driving challenge, autonomous challenge, practice match, qualification round, elimination round, or whole-robot integration test.

This template can support:

- drive reliability challenge
- autonomous straight-line challenge
- flywheel / shooter testing
- hopper testing
- trigger / servo testing
- whole-robot scoring loop testing
- TeleOp practice
- autonomous practice
- qualification-round reflection
- between-round repair and strategy decisions
- pit repair decisions

## Required Framing

A postmortem is not about blame. A postmortem is about understanding what happened so the team can improve.

Robot performance comes from a system: human operation, mechanical design, software/controls, and strategy/communication.

The same result may involve more than one category. The goal is to identify the most useful next change.

Do not change everything at once. Choose one or two evidence-based changes, assign responsibility, and retest.

SLD is the discussion process. The Performance Postmortem Record is the work product.

## Main Discussion Question

What did this test or match reveal, what type of issue did we observe, and what should we change before the next run?

Simpler student version:

What happened, why did it happen, and what is the next change we should make?

## Four Standard Categories

Use these four categories in every postmortem:

```text
Human Operation
Mechanical System
Software / Controls
Strategy / Communication
```

Categories may overlap, but teams should still choose one main issue category for the next revision.

## Category Guidance

### Human Operation

Examples:

- overcorrecting
- panic under pressure
- poor field awareness
- missed timing
- not listening to partner
- driver/operator confusion
- needing more practice
- weak communication between driver and operator
- driver loses orientation when the robot turns around

Driving becomes harder when the robot turns around because the robot's front may no longer face the same direction as the driver. Forward, backward, left, and right may feel different depending on robot orientation.

Possible changes:

- set a driver practice target
- drive more slowly in turns
- add a visual front marker
- add coach/spotter callouts
- practice with the robot facing different directions
- revise driver/operator communication

### Mechanical System

Examples:

- loose wheel
- rubbing part
- frame flex
- battery shifting
- wire snagging
- poor traction
- wheel slip
- uneven weight distribution
- loose connector
- hopper jam
- trigger sticking
- flywheel mount moving
- ball path blocked
- mechanism hard to repair or reload

Possible changes:

- tighten fasteners
- improve wire management
- move battery
- reinforce frame
- reduce rubbing
- adjust hopper angle
- improve trigger clearance
- add guide rails or supports

### Software / Controls

Examples:

- speed too high
- turning too sensitive
- no slow mode
- confusing button mapping
- motor direction mismatch
- servo range too large or too small
- autonomous target wrong
- encoder conversion inaccurate
- code does not match configuration name
- flywheel power not consistent
- trigger timing not reliable

Possible changes:

- reduce drive power
- add slow mode
- revise controller mapping
- change servo positions
- adjust motor power
- update autonomous target
- retest encoder model
- fix configuration names

### Strategy / Communication

Examples:

- unclear role plan
- no recovery plan
- poor driver/operator communication
- no passing/waiting plan
- trying to do too much
- changing too many things at once
- unclear strategy
- no backup driver/operator
- not knowing when to abandon a plan
- pit/field communication issue
- team made a change but did not tell the driver/operator

Possible changes:

- revise role plan
- set a recovery plan
- simplify strategy
- assign a coach/spotter
- write pit-to-field checklist
- change one thing at a time
- create backup role plan
- update team communication norms

## Discussion Roles

| Role | Job |
|---|---|
| Facilitator | Keeps the team focused on evidence and next action. |
| Tally keeper | Uses the SLD tally sheet. |
| Recorder | Writes the postmortem record. |
| Evidence checker | Asks what evidence supports each claim. |
| Category checker | Asks whether each issue is human, mechanical, software/control, or strategy/communication. |
| Action checker | Asks whether the next change is specific and testable. |

For smaller teams, one student may hold more than one role.

## Sentence Stems

```text
The evidence from the test shows ___.
This looks like a human operation issue because ___.
This looks like a mechanical issue because ___.
This looks like a software/control issue because ___.
This looks like a strategy/communication issue because ___.
The robot turned around and the driver orientation changed when ___.
The issue may overlap categories because ___.
One change we should make next is ___.
We should not change ___ yet because ___.
The person responsible for this fix should be ___ because ___.
We will know the change worked if ___.
```

## Test / Match Summary

| Field | Team Response |
|---|---|
| Test or match reviewed | |
| Date / session | |
| Subsystem or whole robot tested | |
| Goal of the test | |
| Result / score / time | |
| Best evidence from the test | |

## Category Classification Table

| Category | Evidence / What We Observed | Possible Change |
|---|---|---|
| Human Operation | | |
| Mechanical System | | |
| Software / Controls | | |
| Strategy / Communication | | |

## Postmortem Decision Table

| Postmortem Decision | Team Response |
|---|---|
| What worked well? | |
| What did not work? | |
| Main issue category | Human / Mechanical / Software / Strategy |
| One change we will make before the next run | |
| Who owns this change? | |
| How will we retest? | |
| What evidence belongs in the portfolio? | |

## Change Log

| Test / Run | Change Made | Reason for Change | Result |
|---|---|---|---|
| After Run 1 | | | |
| After Run 2 | | | |
| After Run 3 | | | |

## 2-Minute Pit Postmortem

Use this fast version for quick between-round decisions.

1. What happened?
2. What category was the main issue?
   - Human Operation
   - Mechanical System
   - Software / Controls
   - Strategy / Communication
3. What is the one change we can make before the next run?
4. Who owns it?
5. Can we test it before the next match?

Use the full version for classroom reflection or portfolio work.

## Tally Sheet Connection

Use `90_templates/student_led_discussion_tally_sheet_template.md`.

Use the SLD tally sheet to track discussion moves: Q, C, E, B, O, D, X.

At the end, record one discussion strength and one target for the next test or match discussion.

## Portfolio Connection

Students should add the Performance Postmortem Record to the engineering portfolio.

Portfolio evidence should include:

- test or match result
- photo/video if available
- data table, score, time, or observation
- issue classification
- change made
- person responsible
- retest result
- revision note
