# Harkness Discussion Tool Student Data Compliance Planning Checklist

## Purpose

This document outlines a practical compliance planning checklist for a student-led discussion tool used in a Vermont school setting. The tool records student audio, transcribes speech, classifies student contributions, scores or evaluates discussion moves against a rubric, and displays a Harkness-style circle graph.

This document is not legal advice. It is a planning tool to help the teaching team, school technology staff, administrators, and district privacy/compliance personnel identify what needs to be reviewed before the tool is used with students.

## High-Level Recommendation

Because the tool records student voices, creates transcripts, analyzes student speech, and may produce rubric scores or feedback, treat the data as sensitive student education data.

Before regular classroom use, the team should complete a school/district review that includes:

1. Data inventory
2. Parent/student notice
3. Access controls
4. Retention/deletion plan
5. Security review
6. Vendor/DPA review if any third-party services are used
7. AI/transcription service review
8. Student-facing explanation of how the tool works
9. De-identification plan for admin-facing reports
10. Written approval from the appropriate school/district authority

## Would Code Names Help?

Yes, code names would help reduce risk, but they do not make the tool automatically compliant.

Code names are useful because they reduce direct identifiers in the tool display and may make classroom reflection safer. However, audio recordings, voiceprints, transcripts, timestamps, class membership, team membership, and teacher-held lookup tables can still make data identifiable.

Use code names as one layer in a broader privacy plan, not as the entire plan.

### Recommended Code Name Practice

Use code names or randomly assigned student IDs inside the tool interface.

Recommended:

- Display code names instead of legal names.
- Store the name-to-code lookup outside the tool, preferably in a school-controlled location.
- Limit access to the lookup table to the teacher and authorized school staff.
- Do not include student names in audio file names, transcript file names, exported reports, or AI prompts.
- Use team-level summaries for public or admin-facing examples whenever possible.

Not enough by itself:

- Code names alone do not anonymize audio.
- Code names alone do not anonymize transcripts if students mention names or personal details.
- Code names alone do not remove FERPA concerns if the school can connect the record back to a student.

## Data Map

Before using the tool, create a data map.

| Data Element | Collected? | Stored? | Where Stored? | Who Can Access? | Retention Period | Notes |
|---|---|---|---|---|---|---|
| Student legal name |  |  |  |  |  | Avoid if possible |
| Student code name / ID |  |  |  |  |  | Preferred display identifier |
| Audio recording |  |  |  |  |  | High sensitivity |
| Transcript |  |  |  |  |  | May include names/personal info |
| Speaker labels |  |  |  |  |  | May be identifiable |
| Rubric classification |  |  |  |  |  | Education record risk |
| Score / feedback |  |  |  |  |  | Education record risk |
| Harkness circle graph |  |  |  |  |  | Prefer team-level display |
| Teacher notes |  |  |  |  |  | Education record risk |
| Survey responses |  |  |  |  |  | Use separately from tool data |
| Parent/student consent or acknowledgment |  |  |  |  |  | Follow district guidance |

## Likely Legal/Policy Buckets to Review

### FERPA

FERPA protects the privacy of student education records at schools receiving U.S. Department of Education funds. Parents and eligible students have rights to inspect and review education records, request amendment in certain circumstances, and exercise some control over disclosure of personally identifiable information from education records.

Because this tool may generate records directly related to students and maintained by the school or a school-controlled system, assume FERPA may apply.

Planning questions:

- Are recordings, transcripts, rubric classifications, or scores education records?
- Who has access to the records?
- Are records disclosed to any third-party service?
- Is the disclosure covered by a FERPA exception, such as school official with legitimate educational interest?
- Are parents/students notified?
- What is the process if a parent requests access to records?

### COPPA

COPPA applies to operators of websites or online services directed to children under 13, and to operators with actual knowledge that they collect personal information from children under 13. If the tool is used with students under 13 or collects information online from under-13 students through a third-party service, COPPA review is needed.

For a high school course, COPPA may be less central if all students are 13 or older, but verify the student age range and any district policies.

Planning questions:

- Are any students under 13?
- Does the tool or any third-party service collect personal information online from students under 13?
- Is the tool used only for educational purposes?
- Has the school/district reviewed notice and consent requirements?

### PPRA

PPRA may be relevant if surveys ask about certain protected categories or sensitive personal information. The proposed course and discussion surveys should avoid protected/sensitive categories unless explicitly reviewed by the school.

Planning questions:

- Do surveys ask about political beliefs, religion, mental health, family relationships, illegal behavior, income, or other sensitive categories?
- If yes, does the school need additional notice or opt-out procedures?

### Vermont / District Student Data Privacy Requirements

Vermont schools commonly use student data privacy agreements and participate in student data privacy alliance processes for educational technology tools. Districts may require a Data Privacy Agreement or review before students use a web service that collects student data.

Planning questions:

- Is the school or supervisory union part of the Vermont Student Privacy Alliance or Student Data Privacy Alliance process?
- Is there a required district technology approval process?
- Is a National Data Privacy Agreement or equivalent DPA required?
- Does the district already have policies for recording student audio or using AI tools?
- Who in the district approves new educational technology tools?

### AI / Transcription Service Review

If audio or transcripts are sent to a third-party AI, transcription, or LLM service, review the service carefully.

Planning questions:

- What third-party service receives audio, transcripts, or student data?
- Is data used to train models?
- Is data retained by the vendor?
- Can data be deleted?
- Where is data stored?
- Is the service covered by a DPA?
- Does the vendor prohibit advertising, profiling, resale, or non-educational secondary use?
- Is encryption used in transit and at rest?
- Are access logs available?

## Minimum Privacy Design Principles

### 1. Data Minimization

Collect only what is needed.

Recommended:

- Do not collect legal names inside the tool if code names will work.
- Do not collect email addresses unless needed.
- Do not retain raw audio longer than necessary.
- Prefer short discussion samples over full-period recordings during pilots.
- Avoid collecting sensitive personal information.

### 2. Purpose Limitation

Use the data only for the educational purpose explained to students and families.

Recommended purpose statement:

> The discussion tool is used to help students reflect on discussion patterns, participation, listening, questioning, evidence use, and collaborative decision-making during class activities.

Avoid:

- Using student discussion data for unrelated research without approval
- Using audio/transcripts for product marketing
- Using data to train public models unless explicitly approved and legally reviewed
- Sharing identifiable examples outside the school

### 3. Access Control

Limit access to the smallest reasonable group.

Recommended:

- Student sees their own feedback and/or team-level feedback.
- Teacher sees class/team/student data.
- Co-teacher sees course data.
- Administrator sees aggregated/de-identified summaries unless student-level access is educationally necessary.
- Developer sees only test data or de-identified data unless specifically approved by the school/district.

Important:

If the developer is not a school employee or approved school official, do not give access to identifiable student data without district review and an appropriate agreement.

### 4. Retention and Deletion

Define exactly how long data is kept.

Possible pilot retention model:

- Raw audio: delete within 7 to 14 days after transcription/verification.
- Transcripts: keep only through the end of the course unless needed for a documented educational purpose.
- Rubric scores/classifications: keep through the end of the course or grading period.
- De-identified aggregate results: may be kept longer for program evaluation.
- Name-to-code lookup: delete when no longer needed.

Use district policy if it requires a different retention period.

### 5. Student Transparency

Students should know:

- What is recorded
- Why it is recorded
- What is transcribed
- What is scored or classified
- Who can see the results
- Whether the results affect grades
- How long data is kept
- How to ask questions or report concerns

### 6. Parent/Guardian Transparency

For a pilot, provide parents/guardians with a plain-language notice if required or recommended by the district.

The notice should explain:

- Educational purpose
- Data collected
- How code names are used
- Who can access data
- Whether any third-party services are used
- Retention/deletion
- Whether participation is required
- Who to contact with questions

### 7. Use for Reflection Before Grading

For early use, the tool should be reflection-focused rather than grade-focused.

Recommended:

- Do not grade students directly on AI classification during the pilot.
- Use teacher judgment and student reflection.
- Allow students to comment on or challenge classifications.
- Use team-level data to support better discussions.

### 8. Bias and Accuracy Review

AI transcription and classification can make mistakes.

Planning questions:

- Does transcription accuracy vary by accent, speech pattern, background noise, or English language proficiency?
- Are multilingual students disadvantaged?
- Does the rubric classification misread short comments or informal speech?
- Are students able to review and correct transcripts?
- Are scores treated as suggestions rather than final truth?

## Student-Facing Explanation

Suggested language:

> We are testing a discussion reflection tool. The goal is to help teams see patterns in conversation that are hard to notice in the moment: who is speaking, who is listening, who is building on ideas, who is asking questions, and how the group makes decisions. The tool is not here to catch you or rank you as people. It is here to help us improve discussion and teamwork.

## Parent/Guardian Notice Draft

This is a rough internal draft. Have school/district leadership review before sending.

> Dear families,
>
> In our robotics course, students may use a discussion reflection tool designed to support student-led conversations and collaborative decision-making. During selected class discussions, the tool may record classroom discussion audio, create a transcript, classify discussion moves using a rubric, and generate a Harkness-style circle graph to help students reflect on participation and collaboration.
>
> The purpose of the tool is educational: to help students improve listening, questioning, evidence use, equitable participation, and team decision-making. The tool is not intended to publicly rank students or replace teacher judgment.
>
> To reduce the use of personally identifying information, students may use code names or assigned identifiers in the tool. Access to identifiable data will be limited to authorized school staff. Data will be retained only as long as needed for the course or as required by school policy.
>
> Please contact [teacher/school contact] with questions.

## Compliance Checklist Before Classroom Use

### Internal Review

- [ ] Identify all data collected by the tool.
- [ ] Identify where each data type is stored.
- [ ] Identify all third-party services involved.
- [ ] Confirm whether any third-party service receives audio, transcripts, or student identifiers.
- [ ] Determine whether the developer can access identifiable student data.
- [ ] Review school/district policies on student recordings.
- [ ] Review school/district policies on AI tools.
- [ ] Review school/district policies on student data privacy agreements.

### FERPA / Education Records

- [ ] Determine whether recordings, transcripts, and scores are education records.
- [ ] Determine who has legitimate educational interest.
- [ ] Document who can access records.
- [ ] Create process for parent/eligible-student access requests.
- [ ] Avoid disclosing identifiable records outside school-approved channels.

### COPPA / Age Review

- [ ] Confirm whether any students are under 13.
- [ ] If yes, complete COPPA review.
- [ ] Verify that any operator collecting under-13 data provides required notices and uses data only for educational purposes.

### Consent / Notice

- [ ] Decide whether parent consent, parent notice, student assent, or district approval is required.
- [ ] Prepare plain-language student explanation.
- [ ] Prepare parent/guardian notice if needed.
- [ ] Provide alternative activity if required by school policy.

### Security

- [ ] Use HTTPS.
- [ ] Encrypt data in transit.
- [ ] Encrypt sensitive stored data where possible.
- [ ] Use strong authentication for teacher/admin access.
- [ ] Restrict access by role.
- [ ] Avoid storing secrets in code.
- [ ] Keep audit logs for admin/teacher access if feasible.
- [ ] Back up data securely if backups are needed.
- [ ] Delete data from backups according to retention policy if feasible.

### Data Retention

- [ ] Define retention period for raw audio.
- [ ] Define retention period for transcripts.
- [ ] Define retention period for rubric scores/classifications.
- [ ] Define retention period for de-identified aggregate results.
- [ ] Create deletion procedure.
- [ ] Test deletion procedure.

### AI/Transcription

- [ ] Confirm whether data is used for model training.
- [ ] Confirm vendor retention period.
- [ ] Confirm whether vendor supports deletion.
- [ ] Confirm whether vendor permits educational use with student data.
- [ ] Confirm whether vendor terms allow use by schools.
- [ ] Confirm whether a DPA is needed or already exists.

### Reporting / Admin Pitch

- [ ] Use de-identified or aggregated data in reports.
- [ ] Do not include student names.
- [ ] Do not include raw transcripts unless de-identified and approved.
- [ ] Use student quotes only with permission or after de-identification.
- [ ] Avoid sharing audio externally.
- [ ] Use team-level or class-level trends when possible.

## Pilot Recommendation

For the first pilot, use a conservative model:

1. Use code names.
2. Record only short structured discussions.
3. Do not use the tool for grades.
4. Display team-level data first.
5. Store raw audio temporarily.
6. Delete raw audio quickly after transcription.
7. Keep transcripts only through the course unless needed.
8. Use de-identified aggregate results for admin-facing evidence.
9. Do not give outside developers access to identifiable data.
10. Get school/district approval before using real student data.

## Questions for School/District Review

1. May teachers record student discussion audio for instructional reflection?
2. Is parent/guardian notice required?
3. Is parent/guardian consent required?
4. Can students opt out of recording?
5. Does the tool need to go through the district's edtech approval process?
6. Is a Data Privacy Agreement required?
7. Can third-party transcription or AI services process the audio/transcripts?
8. Are code names sufficient for the pilot display?
9. What retention period should be used?
10. Can de-identified aggregate results be used in an admin-facing proposal for a FIRST program?
11. What language should be used in parent and student notices?

## Suggested Technical Safeguards

- Use school-controlled accounts when possible.
- Separate code-name identifiers from real student identities.
- Store lookup table separately.
- Use least-privilege access.
- Avoid putting student names in prompts sent to AI services.
- Strip names from transcripts where possible.
- Do not use student audio or transcripts for model training.
- Create export controls.
- Create deletion tools.
- Keep a simple data dictionary.
- Keep a log of data flows and third-party services.

## Suggested Repo Location

Recommended location:

`docs/impact_study/discussion_tool_compliance_planning_checklist.md`

## Suggested Related Files

- `docs/impact_study/discussion_tool_impact_study_plan.md`
- `docs/impact_study/robotics_course_impact_study_plan.md`
- `docs/privacy/discussion_tool_data_map.md`
- `docs/privacy/discussion_tool_parent_notice_draft.md`
- `docs/privacy/discussion_tool_retention_policy.md`

## Suggested Git Branch

```bash
git checkout -b feature/discussion-tool-compliance-plan
```

Suggested commit:

```bash
git add docs/impact_study/discussion_tool_compliance_planning_checklist.md
git commit -m "Add discussion tool student data compliance checklist"
git push -u origin feature/discussion-tool-compliance-plan
```

## References

- U.S. Department of Education, Student Privacy Policy Office. FERPA resources.
- Federal Trade Commission. Children's Online Privacy Protection Rule (COPPA).
- FTC business guidance for edtech companies and schools.
- Vermont Student Privacy Alliance / Student Data Privacy Alliance resources.
- District student data privacy policies and technology approval procedures.
