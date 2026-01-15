# Unit 2: Project Scheduling

## Overview of Unit 2
- **Duration:** 9 Hours (Theory + Discussion)
- **Key Focus:** Scheduling tools and techniques to organize tasks, resources, and timelines. This is part of the planning and execution phases in project management.
- **Why It Matters:** Poor scheduling leads to delays (e.g., software releases missing deadlines). Tools like PERT and CPM help predict and optimize.
- **Practicals:** Hands-on with PERT, CPM, resource leveling, and crashing—perfect for tools like Microsoft Project or Excel.

## 1. Work Breakdown Structure (WBS)
**What is it?**  
WBS is like chopping a big pizza into slices—it's a hierarchical breakdown of the project into smaller, manageable tasks. It decomposes the entire project scope into deliverables and work packages (smallest units of work).

**Why is it important?**  
- Defines "what" needs to be done clearly.
- Helps in estimating time, cost, and resources.
- Basis for scheduling tools like Gantt charts.

**How to Create a WBS:**
- **Level 1:** Project name (e.g., "Develop TaskMaster App").
- **Level 2:** Major phases (e.g., Requirements, Design, Coding, Testing).
- **Level 3+:** Sub-tasks (e.g., Under Coding: Frontend, Backend).
- Use tools: Mind maps or numbered lists (e.g., 1.1.1 for sub-sub-task).

**Types:**
- **Phase-Oriented:** Based on project lifecycle.
- **Deliverable-Oriented:** Focused on outputs (e.g., app modules).

**Example:**  
For a mobile app project:
- 1.0 Initiation
  - 1.1 Gather Requirements
  - 1.2 Define Scope
- 2.0 Development
  - 2.1 UI Design
  - 2.2 Database Setup

**Practical Tip:** In your labs, start every schedule with a WBS. Use Excel to create a tree structure.

## 2. Program Evaluation Review Technique (PERT)
**What is it?**  
PERT is a probabilistic scheduling tool for projects with uncertainty. It uses three time estimates per task: Optimistic (O), Most Likely (M), Pessimistic (P). Great for R&D or software projects where times vary.

**Key Formula:**  
- Expected Time (TE) = (O + 4M + P) / 6
- Variance = [(P - O)/6]^2 (for risk analysis)

**Steps in PERT:**
1. Identify tasks and dependencies (network diagram).
2. Estimate O, M, P for each.
3. Calculate TE and plot on a diagram (arrows for tasks, nodes for events).
4. Find Critical Path: Longest path determining project duration.
5. Calculate slack (float): Time a task can delay without affecting the project.

**Example:**  
Task: Code Module – O=4 days, M=6 days, P=10 days.  
TE = (4 + 4*6 + 10)/6 = (4+24+10)/6 = 38/6 ≈ 6.33 days.  
If this is on the critical path, delays here push the whole project.

**Advantages:** Handles uncertainty; shows probabilities (e.g., 95% chance of finishing on time).  
**Disadvantages:** Time-consuming to estimate three times.

**Practical Tip:** In Practical 1: PERT Analysis, use software like Primavera or draw on paper. Calculate probabilities for fun—e.g., use normal distribution for completion odds.

## 3. Critical Path Method (CPM)
**What is it?**  
CPM is a deterministic tool (fixed times) to identify the longest sequence of dependent tasks (critical path). Similar to PERT but uses single time estimates.

**Key Concepts:**
- **Forward Pass:** Calculate earliest start/finish times.
- **Backward Pass:** Calculate latest start/finish times.
- **Slack:** LS - ES (or LF - EF). Zero slack = critical task.
- Critical Path: Path with zero slack; shortest project time.

**Steps:**
1. List tasks, durations, dependencies.
2. Draw network diagram.
3. Compute forward/backward passes.
4. Identify critical path and total duration.

**Example:**  
Tasks: A (2 days) → B (3 days) → C (4 days). Parallel: D (5 days).  
Critical Path: A-B-C (9 days). D has slack of 4 days.

**Advantages:** Simple for known durations; helps in crashing (shortening).  
**Disadvantages:** Ignores uncertainty.

**Practical Tip:** For Practical 2: CPM Analysis, use Excel formulas for passes. Compare with PERT for the same project to see differences.

## 4. Gantt Chart
**What is it?**  
A bar chart showing tasks over time—horizontal bars for duration, with dependencies as arrows. Invented by Henry Gantt; visual timeline.

**How to Use:**
- X-axis: Time (days/weeks).
- Y-axis: Tasks from WBS.
- Bars: Start/end dates; colors for phases.

**Example:**  
- Task A: Bar from Day 1-3.
- Task B: Starts after A, Day 4-7.
- Milestones: Diamonds for key events (e.g., "App Prototype Ready").

**Advantages:** Easy to understand; tracks progress (shade completed parts).  
**Disadvantages:** Doesn't show dependencies well without software.

**Practical Tip:** Create in Microsoft Project or Google Sheets. Update weekly to show actual vs. planned.

## 5. Project Team Formation Methods and Structure
**What is it?**  
Building the right team: Methods (e.g., matrix, functional) and structures (hierarchical, flat).

**Methods:**
- **Functional:** Team from one department (e.g., all devs).
- **Projectized:** Dedicated team for project.
- **Matrix:** Mix—borrow from departments (common in IT).

**Structure:**
- Hierarchical: PM at top, devs below.
- Flat: Collaborative, less layers (Agile-friendly).

**Example:** In software, a matrix team: PM, devs, testers from different units.

**Practical Tip:** Discuss pros/cons—matrix is flexible but can cause conflicts.

## 6. Selection of Project Manager
**What is it?**  
Choosing a PM based on skills: Leadership, communication, technical knowledge.

**Criteria:**
- Experience in similar projects.
- Soft skills: Motivation, conflict resolution.
- Certifications: PMP (Project Management Professional).

**Example:** For a Gurugram startup app project, select someone with Agile experience in local tech scene.

## 7. Roles and Responsibilities of Project Manager
**What is it?**  
PM is the captain: Plans, executes, monitors, closes.

**Key Roles:**
- Planning: Scope, schedule, budget.
- Leading: Motivate team, resolve issues.
- Controlling: Track progress, manage risks.
- Communicating: With stakeholders.

**Example:** In execution, PM assigns tasks and holds daily stand-ups.

## 8. Project Execution
**What is it?**  
Doing the work: Directing team, managing quality, acquiring resources.

**Phases:** Kick-off meetings, task assignment, progress tracking.

**Example:** Weekly reviews to ensure coding is on track.

## 9. Project Resource Allocation and Leveling Techniques
**What is it?**  
Assigning resources (people, tools) without overload. Leveling: Smoothing peaks/valleys in resource use.

**Techniques:**
- **Allocation:** Match skills to tasks (e.g., senior dev for complex code).
- **Leveling:** Delay non-critical tasks to balance workload.

**Example:** If two tasks need the same dev, level by shifting one.

**Practical Tip:** Practical 3: Resource Leveling—Use histograms in Excel to visualize overloads.

## 10. Project Crashing Methods
**What is it?**  
Shortening project duration by adding resources or overtime—at extra cost.

**Steps:**
1. Identify critical path.
2. Crash cheapest tasks first (cost/time saved).
3. Recalculate path.

**Example:** Add a dev to a 10-day task, reduce to 7 days for $500 extra.

**Practical Tip:** Practical 4: Crashing Techniques—Calculate cost-time trade-offs.

## Connections to Course and Practicals
- **Links to COs:** CO-3 (Project management features like scheduling). Builds on Unit 1's planning.
- **Practicals Summary:**
  1. PERT: Build network, calculate TE.
  2. CPM: Find critical path.
  3. Leveling: Balance resources.
  4. Crashing: Optimize for time.
- **Real-World Tie-In:** In Gurugram's IT hubs (like Cyber City), tools like Jira use Gantt and CPM for app development.

## Study Tips
- **Visualize:** Draw diagrams for PERT/CPM—practice on paper.
- **Tools:** Free: Trello for Gantt; Excel for calculations.
- **Quiz Yourself:** What's the difference between PERT and CPM? (Uncertainty vs. fixed times).
- **Pro Tip:** Relate to Agile (Unit 4)—scheduling is more iterative there.
- **Current Relevance (Jan 2026):** With AI tools booming, use ChatGPT for mock PERT calcs, but understand manually!
