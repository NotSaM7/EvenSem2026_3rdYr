import pandas as pd
from sklearn.preprocessing import MinMaxScaler  # For normalization
from sklearn.decomposition import PCA  # For dimensionality reduction (example)
# pip install pandas scikit-learn
# Step 0: Create raw dataset as DataFrame
data = {
    'Student ID': [101, 102, 101, 103, 104, 105],
    'Name': ['Anirudha', 'Bablu', 'Anirudha', 'Chetan', 'Dayma', 'Eve'],
    'Age': [20, None, 20, 22, 21, 19],
    'Score': [85, 92, 85, 'ABC', 78, 88],
    'Department': ['CS', 'EE', 'Computer Sci', 'CS', 'EE', 'CS']
}
df = pd.DataFrame(data)
print("Raw Data:\n", df)

# 1. Data Cleaning
# Handle missing values (fill Age with mean)
df['Age'] = df['Age'].fillna(df['Age'].mean())
# Handle noisy data (replace 'ABC' with mean Score after converting to numeric)
df['Score'] = pd.to_numeric(df['Score'], errors='coerce')  # Convert to numeric, invalid to NaN
df['Score'] = df['Score'].fillna(df['Score'].mean())
# Resolve inconsistencies (standardize Department)
df['Department'] = df['Department'].replace('Computer Sci', 'CS')
# Remove duplicates
df = df.drop_duplicates()
print("\nCleaned Data:\n", df)

# 2. Data Integration (merge with another DataFrame)
second_data = {
    'Student ID': [101, 102, 103, 104, 105],
    'Attendance': ['95%', '88%', None, '92%', '97%'],
    'Grade': ['A', 'B', 'C', 'B', 'A']
}
df2 = pd.DataFrame(second_data)
# Fill missing in second data
df2['Attendance'] = df2['Attendance'].fillna('93%')  # Example fill
# Merge on 'Student ID'
integrated_df = pd.merge(df, df2, on='Student ID', how='inner')
print("\nIntegrated Data:\n", integrated_df)

# 3. Data Transformation
# Normalize Score (0-1 scale)
scaler = MinMaxScaler()
integrated_df['Normalized Score'] = scaler.fit_transform(integrated_df[['Score']])
# Generalize Age to categories
def generalize_age(age):
    if age < 20: return 'Teen'
    elif 20 <= age <= 21: return 'Young Adult'
    else: return 'Adult'
integrated_df['Age Category'] = integrated_df['Age'].apply(generalize_age)
# Aggregate: Average by Department
agg_df = integrated_df.groupby('Department').agg({'Normalized Score': 'mean', 'Score': 'mean'}).reset_index()
print("\nTransformed Data (with Aggregation):\n", integrated_df)
print("\nAggregated Summary:\n", agg_df)

# 4. Data Reduction
# Remove irrelevant column (e.g., Name)
reduced_df = integrated_df.drop(columns=['Name'])
# Numerosity reduction: Sample 3 rows
sampled_df = reduced_df.sample(n=3, random_state=42)
# Dimensionality reduction: Example PCA on numeric columns (reduce to 1 component)
numeric_cols = reduced_df.select_dtypes(include='number').dropna(axis=1)  # Select numerics
pca = PCA(n_components=1)
reduced_df['PCA_Component'] = pca.fit_transform(numeric_cols)
# Final reduced (keep key columns + PCA)
final_reduced = reduced_df[['Department', 'PCA_Component']]
print("\nReduced Data (Sampled):\n", sampled_df)
print("\nFurther Reduced with PCA:\n", final_reduced)
