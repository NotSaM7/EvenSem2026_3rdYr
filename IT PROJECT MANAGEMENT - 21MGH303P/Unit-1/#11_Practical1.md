# Practical 1: Project Requirement Gathering and Analysis

## Objective
To understand and practice the process of gathering and analyzing requirements for a software project. This helps in identifying user needs, ensuring the project aligns with stakeholder expectations, and preventing scope creep.

## Tools/Materials Needed
- Word processor or requirements management tool (e.g., Microsoft Word, Google Docs, Jira, or Trello).
- Interview/survey templates (can be created in Google Forms).
- Access to stakeholders (simulate with classmates or fictional users).

## Theoretical Background
Requirement gathering involves collecting information from stakeholders using techniques like interviews, surveys, and workshops. Analysis refines these into functional (what the system does) and non-functional (performance, security) requirements. This is part of the initiation and planning phases in software project management.

## Procedure
1. **Identify Stakeholders:** List all parties involved (e.g., users, clients, developers).
2. **Elicit Requirements:** Use techniques such as:
   - Interviews: Ask open-ended questions.
   - Surveys: Distribute questionnaires.
   - Brainstorming: Group discussions.
3. **Document Requirements:** Categorize into functional and non-functional.
4. **Analyze and Prioritize:** Check for completeness, feasibility, and conflicts. Use MoSCoW method (Must-have, Should-have, Could-have, Won't-have).
5. **Validate:** Get feedback from stakeholders and refine.

## Sample Project Example
Let's use a hypothetical project: Developing a "TaskMaster" mobile app for personal task management.

### Step-by-Step Solution
1. **Stakeholder Identification:**
   - End-users: Busy professionals and students.
   - Clients: App development company.
   - Developers: Team of 3 programmers.

2. **Elicitation Techniques Applied:**
   - Conducted interviews with 5 potential users: Questions like "What features do you need in a task app?" Responses: Add tasks, set reminders, prioritize.
   - Sent surveys to 10 people: 80% wanted mobile notifications, 60% wanted cloud sync.

3. **Documented Requirements:**
   - **Functional Requirements:**
     - Users can create, edit, and delete tasks.
     - Set due dates and reminders.
     - Categorize tasks (e.g., work, personal).
   - **Non-Functional Requirements:**
     - App should load in under 2 seconds.
     - Support Android and iOS.
     - Secure data with encryption.

4. **Analysis and Prioritization:**
   - Conflicts: One user wanted complex AI prioritization; deemed too advanced for MVP (Minimum Viable Product) – moved to "Could-have".
   - Prioritized using MoSCoW:
     - Must-have: Task creation and reminders.
     - Should-have: Categorization.
     - Could-have: Cloud sync.
     - Won't-have: Social sharing (for now).

5. **Validation:**
   - Shared document with stakeholders; received feedback to add offline mode (added as Should-have).

## Output/Results
Create a Requirements Specification Document (RSD) as a table:

| Requirement ID | Type | Description | Priority |
|---------------|------|-------------|----------|
| REQ-001 | Functional | Create new task with title, description, due date | Must-have |
| REQ-002 | Functional | Set reminders via notifications | Must-have |
| REQ-003 | Non-Functional | App response time < 2 seconds | Must-have |
| REQ-004 | Functional | Offline access to tasks | Should-have |

## Conclusion
This practical demonstrates how proper requirement gathering prevents misunderstandings. In real projects, tools like Jira can track changes. Potential improvements: Use prototyping for better feedback.

## References
- Roger S. Pressman, Software Engineering – A Practitioner Approach (from course resources).