## Waterfall vs V-Model Comparison

| Aspect                          | Waterfall Model                                      | V-Model (Verification & Validation Model)                  |
|---------------------------------|------------------------------------------------------|-------------------------------------------------------------|
| **Structure**                   | Linear & sequential phases                           | Sequential but V-shaped (development on left, testing on right) |
| **Key Phases**                  | Requirements → Design → Implementation → Testing → Deployment → Maintenance | Requirements ↔ Acceptance Testing<br>High-level Design ↔ System Testing<br>Low-level Design ↔ Integration Testing<br>Coding (bottom) ↔ Unit Testing |
| **Testing Approach**            | Testing only after full development is complete      | Testing planned & executed in parallel with each corresponding development phase |
| **When Testing Starts**         | Late in the lifecycle                                | Early – verification & validation integrated from the start |
| **Flexibility to Change**       | Very low – changes costly & difficult late           | Very low – similar to Waterfall, rigid structure            |
| **Risk Handling**               | Poor – risks discovered late (mostly in testing)     | Better than Waterfall – early defect detection via paired testing |
| **First Working Software**      | Very late (end of project)                           | Late (similar to Waterfall)                                 |
| **Customer Involvement**        | Low – mainly requirements & final acceptance         | Low – similar to Waterfall                                  |
| **Documentation**               | Very high (heavy upfront)                            | Very high (detailed test plans & traceability)              |
| **Best Suited For**             | Small/medium projects with fixed, well-understood requirements | Safety-critical, quality-focused projects (medical, aerospace, automotive, defense) |
| **Main Strength**               | Simple, structured, easy to manage & understand      | Strong emphasis on quality, verification, & early defect finding |
| **Main Weakness**               | Inflexible, late feedback, high risk of late failures | Inflexible, no early working product, expensive late changes |
| **Real-World Use**              | Government contracts, simple internal tools          | Regulated industries requiring traceability & high reliability |

---

## Incremental vs Spiral Model Comparison

| Aspect                          | Incremental Model                                    | Spiral Model                                                |
|---------------------------------|------------------------------------------------------|-------------------------------------------------------------|
| **Structure**                   | Iterative with small, cumulative increments          | Iterative spirals (loops) with strong risk focus            |
| **Key Phases per Iteration**    | Requirements → Design → Code → Test → Integrate → Deploy (per increment) | Objectives → Risk Analysis → Development & Test → Review & Plan next spiral |
| **Requirements Handling**       | Partially upfront; refined & added per increment     | Evolving; gathered/refined in each spiral                   |
| **Flexibility to Change**       | Medium – easier in later increments                  | High – changes incorporated via new spirals                 |
| **Risk Handling**               | Good – risks addressed incrementally                 | Excellent – risk analysis is the core of every spiral       |
| **First Working Software**      | Early – after first increment (partial functionality)| Early prototypes in initial spirals                         |
| **Customer Involvement**        | Medium to High – feedback after each increment       | High – reviews & feedback after every spiral                |
| **Prototyping**                 | Built-in – each increment is a working mini-product  | Heavy – prototyping common in early spirals                 |
| **Cost of Changes**             | Moderate – lower than sequential models              | Moderate to high (but reduced by early risk mitigation)     |
| **Best Suited For**             | Projects needing early delivery & evolving requirements (e.g., web/apps, e-commerce MVPs) | Large, complex, high-risk, uncertain projects (enterprise systems, new platforms) |
| **Main Strength**               | Early value delivery, handles change well, reduces overall risk | Best-in-class risk management, flexible for uncertainty     |
| **Main Weakness**               | Potential integration issues between increments, needs good upfront architecture | Complex to manage, higher overhead from risk analysis & prototyping |
| **Real-World Use**              | E-commerce (catalog → cart → payments increments), mobile apps | High-stakes enterprise software, defense, banking platforms with uncertainty |