# Practical 3: Project Cost Estimation and Capital Budgeting (Software Cost Estimation Models Using Various Techniques)

## Objective
To estimate project costs using models like COCOMO and Function Point Analysis, and apply capital budgeting techniques to evaluate financial viability.

## Tools/Materials Needed
- Spreadsheet software (Excel or Google Sheets) for calculations.
- Python or calculator for model computations.
- Historical project data (simulate if needed).

## Theoretical Background
Cost estimation predicts effort, time, and resources. Models: COCOMO (basic, intermediate), Function Point (measures functionality). Capital budgeting: NPV (Net Present Value), ROI to decide if project is worth funding.

## Procedure
1. **Gather Data:** Project size (e.g., in KLOC – thousands of lines of code).
2. **Apply Estimation Models:** Use COCOMO for effort, Function Point for size.
3. **Calculate Costs:** Include labor, tools.
4. **Capital Budgeting:** Compute NPV, payback period.
5. **Analyze:** Compare techniques and recommend.

## Sample Project Example
"TaskMaster" app from Practical 1. Assume size: 5 KLOC, organic mode (simple project).

### Step-by-Step Solution
1. **Technique 1: COCOMO Model (Basic)**
   - Formula: Effort (PM) = a * (KLOC)^b; Time (months) = c * (Effort)^d
   - For Organic: a=2.4, b=1.05, c=2.5, d=0.38
   - Calculation: Effort = 2.4 * (5)^1.05 ≈ 2.4 * 5.26 ≈ 12.62 Person-Months
   - Time = 2.5 * (12.62)^0.38 ≈ 2.5 * 3.04 ≈ 7.6 months
   - Cost: Assume $5,000/month/person → Total Cost ≈ 12.62 * 5,000 = $63,100

2. **Technique 2: Function Point Analysis**
   - Count: Inputs (4), Outputs (5), Inquiries (3), Files (2), Interfaces (1) – Adjust for complexity.
   - Unadjusted FP = (4*4) + (5*5) + (3*4) + (2*10) + (1*7) = 16+25+12+20+7 = 80
   - Adjust (VAF=1.1 for complexity): Adjusted FP = 80 * 1.1 = 88
   - Effort: Assume 5 hours/FP → 88 * 5 = 440 hours (≈ 2.5 Person-Months at 176 hours/month)
   - Cost: $5,000/month → ≈ $12,500 (lower estimate due to different focus)

3. **Capital Budgeting:**
   - Initial Investment: $10,000 (tools/setup).
   - Cash Flows: Year 1: $20,000 revenue; Year 2: $30,000.
   - NPV (discount rate 10%): NPV = -10,000 + (20,000/1.1) + (30,000/1.21) ≈ -10,000 + 18,182 + 24,793 ≈ $32,975 (positive → viable)
   - ROI: (Net Profit / Investment) * 100 = (40,000 / 10,000) * 100 = 400%

## Output/Results
Estimation Comparison Table:

| Model | Effort (Person-Months) | Time (Months) | Total Cost |
|-------|------------------------|---------------|------------|
| COCOMO | 12.62 | 7.6 | $63,100 |
| Function Point | 2.5 | ~3 | $12,500 |

Budgeting: Project approved as NPV > 0.

## Python Code for COCOMO Calculation (Optional)
```python
kloc = 5
a, b = 2.4, 1.05  # Organic
effort = a * (kloc ** b)
print(f"Effort: {effort:.2f} Person-Months")