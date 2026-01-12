### Four Major Tasks in Data Preprocessing: Manual Steps with Examples

Data preprocessing is a crucial step in data mining and machine learning to prepare raw data for analysis. The **four major tasks** are **Data Cleaning**, **Data Integration**, **Data Transformation**, and **Data Reduction**. These help improve data quality, consistency, and efficiency.

a consistent **example dataset** throughout: A small table of student exam records (raw data with common issues like missing values, duplicates, inconsistencies, etc.).

**Raw Dataset** (imagine this as a table in a spreadsheet or on paper):

| Student ID | Name       | Age | Score | Department    |
|------------|------------|-----|-------|---------------|
| 101        | Anirudha      | 20  | 85    | CS            |
| 102        | Bablu        |     | 92    | EE            |
| 101        | Anirudha      | 20  | 85    | Computer Sci  |
| 103        | Chetan    | 22  | ABC   | CS            |
| 104        | Dayma      | 21  | 78    | EE            |
| 105        | Eve        | 19  | 88    | CS            |

Issues: Missing age for Bablu, duplicate row for Anirudha, inconsistent department names ("CS" vs "Computer Sci"), noisy score ("ABC" instead of number).

Now, **manual steps** for each task (as if doing it by hand in a spreadsheet like Excel or on paper).

#### 1. Data Cleaning: Filling in missing values, smoothing noisy data, resolving inconsistencies, and removing duplicates.
   - **Purpose**: Handle incomplete, noisy, or inconsistent data to make it reliable.
   - **Manual Steps**:
     1. Identify issues: Scan the dataset for blanks, duplicates, wrong formats (e.g., text in numeric fields), or inconsistencies (e.g., varying abbreviations).
     2. Handle missing values: Decide on a strategy—delete row, fill with mean/median/mode, or estimate based on similar rows.
     3. Smooth noisy data: Replace invalid entries with valid ones (e.g., mean of column or nearest valid value).
     4. Resolve inconsistencies: Standardize formats (e.g., unify abbreviations).
     5. Remove duplicates: Compare rows and delete identical or near-identical ones.
     6. Verify: Recheck the cleaned data.

   - **Example with Dataset**:
     - Missing age for Bablu (ID 102): Fill with average age ( (20+20+22+21+19)/5 = 20.4 ≈ 20 ).
     - Noisy score for Chetan (ID 103): "ABC" is invalid—replace with mean score of others ( (85+92+85+78+88)/5 = 85.6 ≈ 86 ).
     - Inconsistent department: Change "Computer Sci" to "CS".
     - Duplicate row (ID 101 repeated): Delete the second row.
     - **Cleaned Dataset**:
       
       | Student ID | Name       | Age | Score | Department |
       |------------|------------|-----|-------|------------|
       | 101        | Anirudha      | 20  | 85    | CS         |
       | 102        | Bablu        | 20  | 92    | EE         |
       | 103        | Chetan    | 22  | 86    | CS         |
       | 104        | Dayma      | 21  | 78    | EE         |
       | 105        | Eve        | 19  | 88    | CS         |

#### 2. Data Integration: Combining data from multiple sources into a coherent store.
   - **Purpose**: Merge heterogeneous data (e.g., from different files/databases) while handling redundancies and conflicts.
   - **Manual Steps**:
     1. Identify sources: Gather all datasets (e.g., two spreadsheets).
     2. Schema integration: Align columns (e.g., match "Dept" in one to "Department" in another).
     3. Entity identification: Match records (e.g., using IDs to avoid duplicates).
     4. Detect redundancies/conflicts: Check for overlapping data and resolve (e.g., average conflicting values or choose one).
     5. Merge: Copy data into a single table.
     6. Verify: Ensure no data loss or new errors.

   - **Example with Dataset**:
     - Suppose a second dataset (from another source): 
       
       | ID | Attendance | Grade |
       |----|------------|-------|
       | 101| 95%        | A     |
       | 102| 88%        | B     |
       | 103|            | C     |
       | 104| 92%        | B     |
       | 105| 97%        | A     |
     
     - Align schemas: Match "ID" to "Student ID".
     - Resolve conflict: Missing attendance for Chetan—fill with average ( (95+88+92+97)/4 = 93% ).
     - Merge by ID.
     - **Integrated Dataset** (from cleaned original + second):
       
       | Student ID | Name     | Age | Score | Department | Attendance | Grade |
       |------------|----------|-----|-------|------------|------------|-------|
       | 101        | Anirudha    | 20  | 85    | CS         | 95%        | A     |
       | 102        | Bablu      | 20  | 92    | EE         | 88%        | B     |
       | 103        | Chetan  | 22  | 86    | CS         | 93%        | C     |
       | 104        | Dayma    | 21  | 78    | EE         | 92%        | B     |
       | 105        | Eve      | 19  | 88    | CS         | 97%        | A     |

#### 3. Data Transformation: Converting data into a suitable form for mining (e.g., normalization, aggregation).
   - **Purpose**: Improve data mining efficiency by smoothing, aggregating, or normalizing.
   - **Manual Steps**:
     1. Identify needs: Decide on techniques like normalization (scale to 0-1), aggregation (group and summarize), or generalization (replace specifics with categories).
     2. Apply normalization: For each value, use formula like (value - min) / (max - min).
     3. Aggregate if needed: Group data (e.g., average by department).
     4. Generalize: Replace values with higher-level concepts (e.g., age to "Young/Adult").
     5. Discretize: Bin continuous values into categories.
     6. Verify: Check if transformed data makes sense.

   - **Example with Dataset** (using integrated data):
     - Normalize scores (0-1 scale): Min score=78, Max=92. Formula: (score - 78)/(92-78).
       - Anirudha: (85-78)/14 ≈ 0.50
       - Bablu: (92-78)/14 ≈ 1.00
       - Chetan: (86-78)/14 ≈ 0.57
       - Dayma: (78-78)/14 = 0.00
       - Eve: (88-78)/14 ≈ 0.71
     - Generalize age: <20="Teen", 20-21="Young Adult", >21="Adult".
     - Aggregate: Add a row for average score per department (CS: (85+86+88)/3 ≈ 86.3; EE: (92+78)/2=85).
     - **Transformed Dataset** (partial—focus on normalized score and generalized age):
       
       | Student ID | Name     | Age Category | Normalized Score | Department |
       |------------|----------|--------------|------------------|------------|
       | 101        | Anirudha    | Young Adult  | 0.50             | CS         |
       | 102        | Bablu      | Young Adult  | 1.00             | EE         |
       | 103        | Chetan  | Adult        | 0.57             | CS         |
       | 104        | Dayma    | Young Adult  | 0.00             | EE         |
       | 105        | Eve      | Teen         | 0.71             | CS         |
       | Avg CS     | -        | -            | 0.59             | CS         |
       | Avg EE     | -        | -            | 0.50             | EE         |

#### 4. Data Reduction: Obtaining a reduced representation of data that produces similar analytical results.
   - **Purpose**: Reduce data volume for faster processing without losing key information.
   - **Manual Steps**:
     1. Identify redundancy: Look for irrelevant attributes or high-dimensional data.
     2. Attribute subset selection: Remove unnecessary columns.
     3. Dimensionality reduction: Use techniques like averaging or principal component analysis (manual approximation: combine columns).
     4. Numerosity reduction: Sample rows or bin data.
     5. Data compression: Summarize (e.g., histograms).
     6. Verify: Ensure reduced data still represents original.

   - **Example with Dataset** (using transformed data):
     - Remove irrelevant: Drop "Name" if not needed for analysis.
     - Sample: If dataset was larger, keep every other row; here, reduce to 3 rows by sampling (e.g., keep IDs 101, 103, 105).
     - Bin ages: Instead of categories, bin into "18-20", "21-23".
     - Aggregate further: Reduce to department-level summary.
     - **Reduced Dataset** (summary-focused):
       
       | Department | Avg Age | Avg Normalized Score | Student Count |
       |------------|---------|----------------------|---------------|
       | CS         | 20.3    | 0.59                 | 3             |
       | EE         | 20.5    | 0.50                 | 2             |


