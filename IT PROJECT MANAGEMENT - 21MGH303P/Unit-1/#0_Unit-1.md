# Unit-1: Introduction to Project Management  
**Course Code:** 21MGH303P  
**Primary Reference:** Software Engineering: A Practitioner's Approach (latest available edition)  

> Phases of project management – Initiation phases and contracting - Project Identification and selection – Project scope management - Planning phase - Project cost
estimation and capital budgeting - Software process Models - Traditional Models, Conventional models - Requirement Analysis - Requirement Engineering - Requirement elicitation - Market and Demand Analysis - Software project effort

**Practicals**  
1. Project requirement gathering and analysis  
2. Project identification process methodology and stakeholder description  
3. Project cost estimation and capital budgeting (using various software cost estimation models)  
4. Market demand analysis and demand planning  

---

### 1. What is Software Project Management? (Scope & Importance)
Software project management is the planning, organizing, directing, and controlling of resources to achieve specific software goals — while respecting constraints of scope, time, cost, and quality.

**Scope**  
- Deals with uncertainty and changing requirements  
- Manages team dynamics and stakeholder expectations  
- Reduces project failure rates (industry data shows only about 30% of projects succeed fully)  
- Critical for traditional, hybrid, and modern development approaches used in industry today  

### 2. Phases of Project Management (5-Phase Structure)
Project management overlays the entire software development life cycle and follows these five phases:

1. **Initiation / Project Definition**  
   - Identify the business need or opportunity  
   - Perform feasibility study (technical, economic, operational, schedule)  
   - Create project charter  
   - Identify stakeholders  
   - Define high-level scope and risks  
   - Key focus: Poor start → high chance of later failure  

2. **Planning**  
   - Define detailed scope  
   - Analyze and specify requirements  
   - Estimate size, effort, cost, and schedule  
   - Allocate resources and organize team  
   - Plan risks (identification, analysis, mitigation)  
   - Establish quality and metrics goals  
   - Set cost and budget baseline  
   - Principle: Realistic planning prevents major problems  

3. **Execution**  
   - Build the software (coding, integration)  
   - Manage team communication and motivation  
   - Apply chosen development process  
   - Conduct reviews and inspections  
   - Handle changes and configuration  

4. **Monitoring & Controlling**  
   - Track progress using metrics (earned value, performance indices)  
   - Monitor risks and apply corrections  
   - Manage changes formally  
   - Ensure quality through testing oversight  
   - Report status and take corrective actions  
   - Key idea: Continuous measurement is essential  

5. **Closing / Termination**  
   - Deliver product and gain acceptance  
   - Conduct final audits and reviews  
   - Hand over documentation  
   - Document lessons learned  
   - Release resources and formally close project  

---

### 3. What is an "Activity"?
A **process** is a collection of activities, actions, and tasks performed to create a work product.

An **activity** is a high-level group of work that achieves a broad objective (e.g. understanding requirements, building code).  
Each activity includes:  
- Software engineering actions (focused objectives)  
- Specific tasks  
- Work products (documents, models, code)  
- Milestones  
- Quality checkpoints  

> software engineering consists of two main types of activities: Framework Activities ,Umbrella activities

### 4. Framework Activities (Generic Process Framework)

These five core activities form the foundation of any software project. They apply to all projects — large or small — and can be used linearly or iteratively.

1. **Communication**  
   - Interact heavily with customers  
   - Understand objectives  
   - Gather initial requirements  
   - Negotiate scope  
   - Identify stakeholders  

2. **Planning**  
   - Create a roadmap  
   - Estimate effort, cost, schedule  
   - Identify risks  
   - Plan resources and work products  

3. **Modeling**  
   - Build models to understand requirements and design  
   - Analysis of requirements (what the system must do)  
   - Design (how it will be built — architecture, interfaces, components)  

4. **Construction**  
   - Generate code  
   - Perform testing (unit, integration, system)  
   - Implement and verify the design  

5. **Deployment**  
   - Deliver software to users  
   - Install and provide training  
   - Collect feedback  
   - Provide ongoing support  

**Important Characteristics**  
- These activities are not rigid — they can be sequential (traditional), iterative (incremental), or adaptive (modern approaches)  
- In iterative development, the cycle repeats → each pass creates a more complete software increment  

### 5. Umbrella activities  
   These are **supportive / cross-cutting activities** that are **applied continuously throughout the entire software project** — from beginning to end — **regardless of which phase** the project is in.

The word "umbrella" is used because these activities **cover / protect / support** all the other development work like an umbrella covers you in the rain.

> "Umbrella activities are applied throughout a software project and help a software team manage and control progress, quality, change, and risk."  

In other words:  
Umbrella activities are **not** tied to one specific phase — they run **parallel** and **continuously** to make sure the whole project stays on track, high quality, and under control.

### Common Umbrella Activities 

1. **Software Project Tracking and Control**  
   → Monitoring progress against the plan, taking corrective actions when things go off track.

2. **Risk Management**  
   → Identifying, analyzing, and mitigating risks throughout the project.

3. **Software Quality Assurance (SQA)**  
   → Ensuring the product meets quality standards (reviews, audits, standards compliance).

4. **Software Configuration Management (SCM)**  
   → Controlling changes to code, documents, and other work products (very important — GitHub is a practical example in your syllabus).

5. **Measurement**  
   → Collecting and analyzing metrics about the process, project, and product (size, effort, defects, etc.).

6. **Formal Technical Reviews**  
   → Conducting inspections and walkthroughs at various stages.


### Quick Summary Table

| Aspect                        | Framework Activities                  | Umbrella Activities                          |
|-------------------------------|----------------------------------------|----------------------------------------------|
| When applied                  | Mostly sequential / in phases          | Continuously, throughout the whole project   |
| Main purpose                  | Build the software (what & how)        | Manage, control, protect quality & progress  |
| Examples                      | Modeling, Construction, Deployment     | Risk management, SQA, SCM, Tracking & Control|
| Pressman Quote                | "Core process steps"                   | "Applied throughout... manage progress, quality, change, and risk" |

---

**Definition of Software Process Model**
A **software process model** (also called a **software development process model** or **process model**) is a structured representation that describes the sequence of activities, tasks, work products, and milestones used to develop, maintain, and deliver a software product.

In other words, it acts as a **roadmap** or **framework** that guides software engineers and project teams on **how** to build high-quality software in a systematic, repeatable, and manageable way.

### Key Characteristics of a Software Process Model
- It defines the **phases** or **activities** (such as requirements gathering, design, implementation, testing, deployment) and their logical order.
- It specifies **how** work flows from one stage to another (linear, iterative, risk-driven, etc.).
- It helps ensure the project is completed **on time**, **within budget**, and meets **quality** expectations.
- Different models suit different project types (small vs large, stable vs changing requirements, high-risk vs low-risk).

### 5. Traditional Software Process Models (Conventional)
Traditional software process models, like the Waterfall, V-Model, Incremental, and Spiral Models, are sequential, phase-based approaches to software development, emphasizing detailed upfront planning, distinct stages (requirements, design, implementation, testing, maintenance), and formal documentation, making them suitable for projects with stable requirements but less flexible for changes compared to modern methods like Agile. 

**Key Traditional Models**
   -> Waterfall Model: The classic linear, sequential model where each phase (Requirements, Design, Implementation, Testing, Deployment, Maintenance) must be fully completed before the next begins.
   -> V-Model (Verification & Validation Model): An extension of Waterfall that emphasizes testing by linking each development phase with a corresponding testing phase (e.g., design with integration testing).
   -> Incremental Model: Delivers software in small, functional increments, with each increment adding new features and building upon the last.
   ->Spiral Model: Combines elements of Waterfall and iterative development, focusing on risk assessment and prototyping in repetitive cycles.
Prototyping Model: Involves creating a working model (prototype) early on to gather user feedback and refine requirements before full development. 

**Core Characteristics**
   -> Sequential Flow: Development moves in one direction, from one phase to the next.
   -> Upfront Planning: Detailed requirements and designs are established at the start.
   -> Documentation-Heavy: Emphasizes formal, detailed documentation for each phase.
   -> Fixed Requirements: Best for projects where requirements are well-understood and unlikely to change. 

**Advantages of Traditional Software Development**
   -> Well-Established Methodology: Traditional software development follows a well-established methodology that is widely understood and documented.
   -> Clear Requirements: Traditional software development relies on clear and detailed requirements, which helps to ensure that the final product meets the customer's needs.
   -> Structured Approach: Traditional software development follows a structured approach, with clear phases and milestones, which helps to ensure that the project stays on track.
   -> Proven Success: Traditional software development has a proven track record of success and is widely used in many industries.
   -> Quality Control: Traditional software development typically includes extensive testing and quality control processes, which helps to ensure that the final product is of high quality.

**Disadvantages of Traditional Software Development**
   -> Slow Process: Traditional software development can be a slow process, with lengthy planning and design phases.
   -> Lack of Flexibility: Traditional software development can be inflexible, with changes to requirements or design difficult to implement once development has begun.
   -> High Cost: Traditional software development can be expensive, particularly if the project is large or complex.
   -> Limited Customer Involvement: Traditional software development often limits customer involvement to the planning and design phases, which can result in a product that does not fully meet their needs.
   ->Limited Innovation: Traditional software development can be conservative and risk-averse, which can limit innovation and the development of new ideas.

### Common Types of Software Process Models 
1. **Waterfall Model**  
   - Linear and sequential  
   - Phases: Requirements → Design → Implementation → Testing → Deployment → Maintenance  
   - Best for projects with **well-understood**, **stable requirements** (e.g., regulated domains like banking or defense)

2. **Incremental Model**  
   - Delivers the software in small, usable **increments**  
   - Combines waterfall elements but allows partial delivery early  
   - Good when you need **early feedback** or partial functionality quickly

3. **Spiral Model**  
   - Risk-driven and iterative  
   - Each spiral loop includes planning, risk analysis, engineering, and evaluation  
   - Ideal for **large, complex, high-risk** projects (e.g., mission-critical systems)

4. **V-Model**  
   - Extension of waterfall with strong emphasis on **testing**  
   - Each development phase has a corresponding verification/validation phase (V shape)  
   - Used in **safety-critical** systems (medical, aerospace, automotive)

**Modern/Adaptive models** (covered in later units of your syllabus)  
- Agile approaches  
- Scrum  
- Extreme Programming (XP)  
- These are iterative and flexible, responding to change rather than following a rigid plan

### Why Software Process Models Are Important 
- Provide a clear **structure** to avoid chaos in development  
- Help in **estimation**, **planning**, and **risk management**  
- Improve **communication** between team and stakeholders  
- Reduce the chance of project failure (industry data shows many projects fail due to poor process choice)

### Quick Summary Table

| Model Type          | Flow Style     | Best For                              | Flexibility | Risk Handling |
|---------------------|----------------|---------------------------------------|-------------|---------------|
| Waterfall           | Linear         | Stable, well-defined requirements     | Low         | Late          |
| Incremental         | Iterative partial delivery | Need early working versions           | Medium      | Medium        |
| Spiral              | Risk-driven cycles | High-risk, large projects             | High        | Early & strong|
| V-Model             | Sequential + testing focus | Safety-critical systems               | Low         | Good testing  |

---

| Model          | Characteristics                          | Best Used When                              | Advantages                        | Disadvantages                     |
|----------------|------------------------------------------|---------------------------------------------|-----------------------------------|-----------------------------------|
| Waterfall      | Linear, sequential                       | Requirements are clear and stable           | Simple, well-documented           | Very little flexibility           |
| Incremental    | Deliver in small usable parts            | Need early partial delivery                 | Early feedback                    | Integration can be complex        |
| Spiral         | Risk-focused, iterative prototypes       | High-risk or large projects                 | Early risk handling               | More expensive, complex           |
| V-Model        | Strong emphasis on testing               | Safety-critical systems                     | Excellent verification & validation | Remains rigid                     |

### 6. Requirement Engineering & Elicitation

**Requirement Engineering** — Complete process to discover, document, validate, and manage requirements.

**Elicitation Techniques**  
- Interviews & questionnaires  
- Use cases / scenarios  
- Prototyping  
- Observation  
- Workshops  
- Document analysis  

**Requirement Analysis**  
- Categorize functional & non-functional  
- Prioritize (e.g., MoSCoW method)  
- Resolve conflicts  

### 7. Project Cost Estimation & Capital Budgeting

**Main Techniques**  
- Lines of Code (LOC/KLOC) based  
- Function Point Analysis  
- COCOMO (Constructive Cost Model)  

**Basic COCOMO Formula**  
Effort (person-months) = a × (KLOC)^b  

| Project Type   | a    | b    |
|----------------|------|------|
| Organic        | 2.4  | 1.05 |
| Semi-detached  | 3.0  | 1.12 |
| Embedded       | 3.6  | 1.20 |

**Capital Budgeting**  
- Payback period  
- Net Present Value (NPV)  
- Return on Investment (ROI)  

- **LOC** = **Lines of Code**  
  It refers to the total number of lines written in the source code of a software program (including comments, blank lines, or sometimes only executable statements — depending on the counting method used).

- **KLOC** = **Kilo Lines of Code** (or **Thousands of Lines of Code**)  
  It means **1,000 lines of code** (K = Kilo = 1,000).  
  This is the most commonly used unit in software project estimation, especially in traditional models like COCOMO, because software projects are usually much larger than just a few hundred lines.

### Quick Examples (from your syllabus & Unit-1 – Project Cost Estimation)

- A small program with 500 lines → **0.5 KLOC**  
- A medium-sized application with 50,000 lines → **50 KLOC**  
- A large enterprise system with 200,000 lines → **200 KLOC**

### Why LOC/KLOC is Important 

In **Unit-1** (Project cost estimation and capital budgeting), LOC/KLOC is one of the primary **size metrics** used for effort and cost estimation.

Common estimation models that use LOC/KLOC:
- **Basic COCOMO** (Constructive Cost Model)  
  Effort (person-months) = a × (KLOC)^b  
  (a and b values change based on project type: Organic, Semi-detached, Embedded)

- **LOC-based Effort Estimation**  
  Effort = a × (KLOC)^b (where a and b are constants derived from historical data)

**Advantages** of using LOC/KLOC (as per traditional approaches):
- Simple to count (especially with tools)
- Widely used in early estimation

**Disadvantages**:
- Language-dependent (Java vs Python → different lines for same functionality)
- Doesn't measure complexity or quality
- Encourages bad practices (e.g., writing more lines for same result)

This is why modern approaches (like Agile/Scrum in Units 4 & 5) prefer **function points**, **story points**, or **use case points** instead of pure LOC/KLOC.

**Key Models (Pressman detailed explanation)**:

1. **LOC-based Estimation** → Effort = a × (KLOC)^b  
2. **Function Point Estimation** → Count inputs, outputs, inquiries, files, interfaces → Adjust complexity → Convert to effort  
3. **COCOMO (Constructive Cost Model)** – Boehm model explained in Pressman  

   **Basic COCOMO** (Pressman):  
   Effort (PM) = a × (KLOC)^b  

   | Mode          | a    | b    | Application Type                     |
   |---------------|------|------|--------------------------------------|
   | Organic       | 2.4  | 1.05 | Small, familiar team                 |
   | Semi-detached | 3.0  | 1.12 | Medium, mixed experience             |
   | Embedded      | 3.6  | 1.20 | Complex, tight constraints           |

   **Intermediate COCOMO** (Pressman):  
   Effort = a × (KLOC)^b × EAF (Effort Adjustment Factor from 15 cost drivers)  

   **Detailed COCOMO** → Applies multipliers per phase (planning, design, coding, testing).

**Capital Budgeting** (Pressman context):  
- NPV, ROI, Payback period → Used to justify project investment  

 

