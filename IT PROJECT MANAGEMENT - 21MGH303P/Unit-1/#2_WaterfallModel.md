The **Waterfall Model** is a traditional software development methodology that follows a linear and sequential approach. Each phase such as requirements, design, implementation, testing, and maintenance must be completed before moving to the next, making the process structured and easy to manage.
SDLC Waterfall Model

The Waterfall Model is a traditional and sequential software development approach best suited for large and well-defined projects where requirements remain stable.
🟢Follows a linear phase-by-phase development process.
🟢Ideal for projects with clear requirements and minimal changes.
🟢Provides strong structure, documentation, and predictability.

**Phases of Waterfall Model**
Classical Waterfall Model divides the life cycle into a set of phases. The development process can be considered as a sequential flow in the waterfall. 
![Waterfall](https://github.com/anirudhagaikwad/EvenSem2026_3rdYr/blob/main/IT%20PROJECT%20MANAGEMENT%20-%2021MGH303P/Unit-1/imgs/WaterFall.png)

**1. Requirements Analysis and Specification**
Requirement Analysis and specification phase aims to understand the exact requirements of the customer and document them properly. This phase consists of two different activities. 
 🟢Requirement Gathering and Analysis: Software requirements are collected from the customer and analyzed to eliminate incompleteness and inconsistencies, ensuring clarity and accuracy.
🟢Requirement Specification: The validated requirements are documented in the Software Requirement Specification document, which acts as a formal agreement between the customer and the development team.

**2. Design**
The goal of this Software Design Phase is to convert the requirements acquired in the **Software Requirements Specification**(SRS) into a format that can be coded in a programming language. It includes high-level and detailed design as well as the overall software architecture. A **Software Design Document** is used to document all of this effort (SDD).
🟢High-Level Design (HLD): This phase focuses on outlining the broad structure of the system. It highlights the key components and how they interact with each other, giving a clear overview of the system’s architecture.
🟢Low-Level Design (LLD): Once the high-level design is in place, this phase zooms into the details. It breaks down each component into smaller parts and provides specifics about how each part will function, guiding the actual coding process.

**3. Development**
In the Development Phase software design is translated into source code using any suitable programming language. Thus each designed module is coded. The unit testing phase aims to check whether each module is working properly or not. 
🟢In this phase, developers begin writing the actual source code based on the designs created earlier.
🟢The goal is to transform the design into working code using the most suitable programming languages.
🟢Unit tests are often performed during this phase to make sure that each component functions correctly on its own.

**4. Testing and Deployment**
This phase ensures that the integrated software functions correctly and is successfully delivered for real world use.
🟢Testing: After unit testing, software modules are integrated incrementally and tested at each stage. Once all modules are successfully integrated, full system testing is performed to ensure the system functions as expected.
🟢Alpha testing: Alpha testing is the system testing performed by the development team.
🟢Beta testing: Beta testing is the system testing performed by a friendly set of customers.
🟢Acceptance testing: Acceptance testing is performed by the customer after software delivery to verify that the system meets requirements and to decide whether the software should be accepted or rejected.

**5. Deployment**
After successful testing, the software is deployed to a live environment for end users. This phase includes environment setup, user training, and final checks to ensure smooth operation in real world conditions.

6. Maintenance
In Maintenance Phase is the most important phase of a software life cycle. The effort spent on maintenance is 60% of the total effort spent to develop a full software. There are three types of maintenance.
🟢Corrective Maintenance: This type of maintenance is carried out to correct errors that were not discovered during the product development phase.
🟢Perfective Maintenance: This type of maintenance is carried out to enhance the functionalities of the system based on the customer’s request.
🟢Adaptive Maintenance: Adaptive maintenance is usually required for porting the software to work in a new environment such as working on a new computer platform or with a new operating system.

---

**Features of Waterfall Model**
Following are the features of the waterfall model:
🟢Sequential Approach: The waterfall model involves a sequential approach to software development, where each phase of the project is completed before moving on to the next one.
🟢Document-Driven: The waterfall model depended on documentation to ensure that the project is well-defined and the project team is working towards a clear set of goals.
🟢Quality Control: The waterfall model places a high emphasis on quality control and testing at each phase of the project, to ensure that the final product meets the requirements and expectations of the stakeholders.
🟢Rigorous Planning: The waterfall model involves a careful planning process, where the project scope, timelines, and deliverables are carefully defined and monitored throughout the project lifecycle.

---

## **Example of Waterfall Model**
Here is a clear example of how the **Waterfall model** can be applied to developing an **e-commerce website** (such as an online fashion store or electronics shop), using the commonly accepted **6 phases** version of the Waterfall model.

These 6 phases are:

1. **Requirements Gathering & Analysis**
2. **System & Software Design**
3. **Implementation (Coding)**
4. **Testing / Verification**
5. **Deployment**
6. **Maintenance**

In the Waterfall model, each phase must be 100% completed and approved before moving to the next one — no going back easily.

### 1. Requirements Gathering & Analysis
**Goal**: Collect and document every requirement in detail.

**Activities for E-commerce website**:
- Meet stakeholders (business owner, marketing team, logistics team)
- Define functional requirements:
  - User registration/login (customer + admin)
  - Product catalog with categories, search, filters
  - Shopping cart & checkout process
  - Multiple payment gateways (UPI, cards, COD, wallets)
  - Order tracking & email/SMS notifications
  - Admin dashboard for product management, orders, users
  - Wishlist, reviews/ratings
- Non-functional requirements:
  - Must load pages in <3 seconds
  - Support 10,000 concurrent users
  - Mobile-responsive design
  - PCI-DSS compliant for payments
  - Multi-language & multi-currency (optional)
- Create detailed **Software Requirements Specification (SRS)** document.
**Deliverable**: Signed-off SRS document

### 2. System & Software Design
**Goal**: Convert requirements into technical blueprints.

**Activities for E-commerce website**:
- High-level design (architecture):
  - Frontend: React.js / Next.js
  - Backend: Node.js + Express / Laravel / Django
  - Database: MySQL / PostgreSQL + Redis for caching
  - Cloud: AWS (EC2, S3, RDS, CloudFront)
  - Microservices or monolithic?
- Low-level design:
  - Database schema (ER diagram): tables for users, products, orders, payments, reviews
  - API endpoints (e.g. GET /api/products, POST /api/cart/add)
  - UI/UX wireframes & final designs (Figma files)
  - Security design: JWT authentication, HTTPS, input validation, rate limiting
  - Payment flow sequence diagrams

**Deliverable**: System Design Document (SDD), database schema, wireframes, API documentation

### 3. Implementation (Coding)
**Goal**: Write actual code based on design documents.

**Activities for E-commerce website**:
- Frontend developers build UI pages (home, product listing, PDP, cart, checkout)
- Backend developers implement APIs, business logic, payment integrations (Razorpay/Stripe/PayU)
- Database setup & data population (sample products)
- Integrate third-party services (email: SendGrid, SMS: Twilio, shipping: Shiprocket)
- Write unit tests for critical functions

**Important**: No changes to requirements/design allowed here — only coding as per approved documents.

**Deliverable**: Fully coded & unit-tested application (source code in Git)

### 4. Testing / Verification
**Goal**: Verify the system works as specified and is bug-free.

**Activities for E-commerce website**:
- Functional testing: Does checkout work end-to-end?
- Integration testing: Payment gateway + order creation + email
- Performance testing: Load test with 5,000–10,000 users
- Security testing: OWASP Top 10 checks, penetration testing
- Cross-browser & mobile testing
- Usability testing with sample users
- Fix all critical & high-priority bugs

**Deliverable**: Test reports, bug-free (or accepted level) system, sign-off on quality

### 5. Deployment
**Goal**: Make the website live for real users.

**Activities for E-commerce website**:
- Set up production environment (AWS / Azure / VPS)
- Deploy code via CI/CD pipeline
- Migrate final database
- Configure domain, SSL certificate
- Set up monitoring (New Relic / Datadog)
- Final smoke tests in production
- Go-live with soft launch (limited users first)

**Deliverable**: Live e-commerce website (e.g., www.yourshop.com)

### 6. Maintenance
**Goal**: Support the live system long-term.

**Activities for E-commerce website**:
- Fix bugs reported by users
- Apply security patches
- Add minor features (e.g., new payment method)
- Scale servers during sales (Diwali / Black Friday)
- Monitor uptime, performance, errors
- Release version updates (v1.1, v1.2…)

**Deliverable**: Ongoing support, updated system, SLA compliance

### Summary Table – Waterfall for E-commerce Website

| Phase              | Key Deliverables                          | Typical Duration (small-medium project) | E-commerce Specific Example                     |
|--------------------|-------------------------------------------|------------------------------------------|-------------------------------------------------|
| 1. Requirements    | SRS document                              | 3–6 weeks                               | Full list of features + payment modes           |
| 2. Design          | SDD, ERD, wireframes, API docs            | 4–8 weeks                               | Database schema + checkout flow diagram         |
| 3. Implementation  | Source code, unit tests                   | 8–14 weeks                              | Working cart, payment integration               |
| 4. Testing         | Test cases, bug reports, quality sign-off | 4–8 weeks                               | End-to-end payment + load testing               |
| 5. Deployment      | Live website                              | 1–2 weeks                               | Go-live on production domain                    |
| 6. Maintenance     | Support tickets, patches, updates         | Ongoing (years)                         | Festival sale scaling + bug fixes               |


> *Waterfall model is **sequential**, meaning each phase must be completed before the next phase begins.*

---

**Advantages of Waterfall Model**
The classical waterfall model is an idealistic model for software development. It is very simple, so it can be considered the basis for other software development life cycle models. Below are some of the major advantages of this SDLC model.
🟢Easy to Understand: The Classical Waterfall Model is very simple and easy to understand.
🟢Individual Processing: Phases in the Classical Waterfall model are processed one at a time.
🟢Properly Defined: In the classical waterfall model, each stage in the model is clearly defined.
🟢Clear Milestones: The classical Waterfall model has very clear and well-understood milestones.
🟢Properly Documented: Processes, actions, and results are very well documented.
🟢Reinforces Good Habits: The Classical Waterfall Model reinforces good habits like define-before-design and design-before-code.
🟢Working: Classical Waterfall Model works well for smaller projects and projects where requirements are well understood.

The **Classical Waterfall Model** is indeed simple and structured, as you listed in its advantages. However, in practice, it has several significant **limitations** and disadvantages, especially in today's dynamic software projects (including e-commerce websites). These drawbacks are why many teams have moved toward iterative, Agile, or hybrid approaches.

**Limitations of the Waterfall Model**:
🟡 **Inflexibility / No room for changes**  
Once a phase is completed and signed off, going back to fix or change anything (e.g., requirements or design) is extremely difficult and expensive.  
Customer requirements often evolve during development, but Waterfall assumes they are 100% correct and fixed from day 1 — which is rarely true in real life.
🟡 **Late discovery of problems & risks**  
Testing happens only after implementation is fully done → bugs, design flaws, wrong assumptions, or missing features are usually found very late (sometimes months after coding starts).  
Fixing them often requires restarting large parts of the project → high cost, delays, and sometimes complete failure.
🟡 **No working software until very late**  
The customer or end-user sees a working, testable product only after coding + testing (often 60–80% into the project timeline).  
This increases risk — if the delivered product doesn't meet expectations, massive rework is needed.
🟡 **Limited / late customer & user involvement**  
Users or stakeholders are mainly involved at the beginning (requirements) and end (acceptance testing).  
There is almost no feedback loop during design, coding, or early testing → higher chance of building the wrong thing.
🟡 **Not suitable for complex, long, or uncertain projects**  
Works best only for **small projects** with **very clear, stable, unchanging requirements** (e.g., embedded systems, regulated industries like defense or certain government projects).  
For most modern software (apps, websites, e-commerce, SaaS), requirements change frequently due to market, user feedback, competition, or technology → Waterfall becomes risky and inefficient.
🟡 **High risk & uncertainty accumulation**  
All risk is pushed to the end.  
If major issues appear in testing or deployment, the entire schedule and budget can explode.
🟡 **Poor risk management**  
No built-in mechanism for early risk identification, prototyping, or mitigation → surprises are common and costly.

#### Quick Comparison Table – Advantages vs Limitations

| Aspect                        | Advantage (as you listed)                  | Limitation / Disadvantage                              |
|-------------------------------|--------------------------------------------|-----------------------------------------------------------------|
| Understanding & Structure     | Very simple & easy to understand           | Too rigid — doesn't match real-world changing needs             |
| Phase handling                | One phase at a time                        | Can't easily go back → costly rework                            |
| Milestones & Documentation    | Clear milestones & well-documented         | Documentation becomes outdated if requirements change           |
| Customer involvement          | —                                          | Very limited until the end → risk of building wrong product     |
| Working product visibility    | —                                          | No usable software until late in the cycle                      |
| Suitability                   | Good for small, well-understood projects   | Poor for complex, long, or uncertain projects                   |
| Risk & Testing                | —                                          | Problems found very late → expensive & time-consuming fixes     |

---
**When to Use Waterfall Model?**
Here are some cases where the use of the Waterfall Model is best suited:
🟢Well-understood Requirements: Before beginning development, there are precise, reliable, and thoroughly documented requirements available.
🟢Very Little Changes Expected: During development, very little adjustments or expansions to the project's scope are anticipated.
🟢Small to Medium-Sized Projects: Ideal for more manageable projects with a clear development path and little complexity.
🟢Predictable: Projects that are predictable, low-risk, and able to be addressed early in the development life cycle are those that have known, controllable risks.
🟢Regulatory Compliance is Critical: Circumstances in which paperwork is of utmost importance and stringent regulatory compliance is required.
🟢Client Prefers a Linear and Sequential Approach: This situation describes the client's preference for a linear and sequential approach to project development.
🟢Limited Resources: Projects with limited resources can benefit from a set-up strategy, which enables targeted resource allocation.    