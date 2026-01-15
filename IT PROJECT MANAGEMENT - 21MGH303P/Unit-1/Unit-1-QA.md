### Typical Questions & Answers

1. **List the phases of software project management.**  
   **Answer:**  
   phases of software project management are:  
   1. Initiation/Project Definition  
   2. Planning  
   3. Execution  
   4. Monitoring & Controlling  
   5. Closing/Termination  

2. **What is the importance of the Initiation phase in software project management?**  
   **Answer:**  
   The Initiation phase establishes project feasibility, defines high-level scope, identifies stakeholders, and creates the project charter. Pressman states that weak initiation is a major cause of project failure, as it leads to unclear objectives and unrealistic expectations.

3. **Explain the phases of project management in detail with reference to Roger S. Pressman.**  
   **Answer:**  
   Roger S. Pressman in *Software Engineering: A Practitioner's Approach* describes project management as an umbrella activity with five key phases:  

   1. **Initiation**: Focuses on project justification through feasibility studies and charter creation.  
   2. **Planning**: Develops detailed scope, schedule, cost estimates, risk plans, and resource allocation.  
   3. **Execution**: Implements the plan through development activities, team management, and process execution.  
   4. **Monitoring & Controlling**: Tracks progress using metrics, manages changes, and applies corrective actions.  
   5. **Closing**: Delivers the product, conducts audits, documents lessons learned, and formally closes the project.  

   Pressman emphasizes that these phases apply across any software process model and require continuous metrics and risk management.

4. **Differentiate between Project Management phases and Software Development Life Cycle (SDLC) as per Pressman.**  
   **Answer:**  
   Pressman clearly distinguishes:  
   - **SDLC** (software process models like Waterfall, Spiral) focuses on **how** the software is built (technical activities: requirements → design → code → test).  
   - **Project Management phases** are management-oriented activities that **overlay** any SDLC — they focus on **when, by whom, at what cost, and with what risk** the work is done.  
   Example: Planning phase includes estimation and scheduling, which apply regardless of whether the underlying process is Waterfall or Incremental.

5. **Discuss the role of Monitoring & Controlling phase in successful software project management.** (Pressman)  
   **Answer:**  
   In Pressman’s framework, the Monitoring & Controlling phase ensures the project stays on track. Key activities include:  
   - Measuring performance using earned value analysis, schedule performance index (SPI), cost performance index (CPI).  
   - Monitoring risks and implementing mitigation.  
   - Controlling changes through formal change control.  
   - Reporting status to stakeholders.  
   Pressman stresses that this phase is continuous and metrics-driven — without it, deviations from plan go unnoticed, leading to cost/time overruns.

6. **Q.** What is meant by the term "umbrella activity" in software engineering? (Pressman)  
**A.** Umbrella activities are those that are applied continuously throughout the software project (not limited to one phase) to help manage progress, quality, change, and risk. Examples include software project tracking & control, risk management, SQA, and configuration management. (Pressman, Software Engineering: A Practitioner's Approach)

7. **Q.** Explain umbrella activities as described by Roger S. Pressman with examples.  
**A.** According to Roger S. Pressman, umbrella activities are supportive activities that run parallel to the main framework activities of software development. They are applied throughout the entire project lifecycle to ensure effective management and control.  
Key umbrella activities include:  
1. Software project tracking and control – assessing progress and taking corrective actions.  
2. Risk management – identifying and mitigating risks continuously.  
3. Software quality assurance – ensuring quality standards.  
4. Software configuration management – controlling changes to artifacts.  
5. Measurement – collecting metrics for better decision-making.  
These activities help the team deliver high-quality software on time and within budget.
---
1. List the five framework activities.  
2. Name four requirement elicitation techniques.  
3. What is the difference between basic and intermediate COCOMO?  
4. Explain the five phases of project management with focus on Initiation.  
5. Describe the generic process framework activities in detail.  
6. Discuss requirement engineering process.  

**Numerical Example (Common)**  
A project has 100 KLOC in organic mode. Calculate effort using basic COCOMO.  
**Answer:** Effort ≈ 2.4 × (100)^1.05 ≈ 2.4 × 120.2 ≈ 288 person-months  

**Q.** What do LOC and KLOC stand for? Explain their use in software project estimation.  
**Ans:**  
LOC stands for **Lines of Code** and KLOC stands for **Kilo Lines of Code** (1 KLOC = 1000 lines).  
They are used as size metrics in traditional cost estimation models like COCOMO to calculate effort, development time, and staffing needs. For example: Effort = a × (KLOC)^b, where a and b depend on project type.

**What is the difference between basic and intermediate COCOMO?**  
   **Ans:** Basic COCOMO uses only size (KLOC) and mode. Intermediate adds 15 cost drivers (EAF) for better accuracy.

6. **Explain COCOMO model in detail with formulas and examples.** (Pressman Ch 23)  
   **Ans:** [Explain Basic, Intermediate, Detailed]  
   **Example (Basic COCOMO):** Organic mode, 60 KLOC  
   Effort = 2.4 × (60)^1.05 ≈ 2.4 × 74.3 ≈ 178 PM  
   Development time ≈ 2.5 × (178)^0.38 ≈ 12 months  
   Staff = 178/12 ≈ 15 persons

8. **Explain function point analysis with counting rules.** (Pressman Ch 23)  
   **Ans:** Count 5 components (ILF, EIF, EI, EO, EQ) → Apply weights → Adjust by 14 general system characteristics → FP = UFP × (0.65 + 0.01 × ΣGSC)
