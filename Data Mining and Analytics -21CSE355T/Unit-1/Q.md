**Approximate Weightage Distribution** (based on topics and time allocation:  
- Introduction + Kinds of Data + Kinds of Patterns → ~20%  
- Data Objects and Attribute Types → ~25% (very important, frequent 10/16 mark questions)  
- Data Visualization → ~10–15%  
- Basic Statistical Descriptions → ~10%  
- Data Preprocessing (Cleaning, Integration, Transformation, Reduction) → **~35–40%** (highest weightage, most detailed topic)

**Question Types:**  
- Short answer (2/5 marks)  
- Descriptive (8/10/16 marks)  
- Differences/Comparisons  
- Explain with examples  

###  Question Bank – Unit-1

**Section A: Introduction & Basic Concepts**  
1. Define data mining. How is it different from traditional data analysis?  
2. What is Knowledge Discovery in Databases (KDD)? Explain the steps in KDD process.  
3. What are the different kinds of data on which data mining can be performed? Give examples for each.  
4. List and explain the various kinds of patterns that can be discovered in data mining.  
5. Differentiate between descriptive and predictive data mining tasks with suitable examples.  
6. What is the importance of data mining in the current era of big data? Give two real-world applications.  
7. Explain the challenges and issues in data mining.  

**Section B: Data Objects and Attribute Types** (High weightage)  
8. Define data object and attribute. Explain their role in a dataset with an example.  
9. Classify the different types of attributes in data mining with examples for each type.  
10. Explain nominal, ordinal, interval-scaled, and ratio-scaled attributes with suitable examples.  
11. What is the difference between symmetric and asymmetric binary attributes? Give examples.  
12. Why is it important to know the type of attribute before applying data mining techniques?  
13. Compare nominal and ordinal attributes. Can arithmetic operations be performed on them?  
14. Explain interval-scaled and ratio-scaled attributes. Why ratio-scaled is more powerful?  
15. Give examples of real-world datasets and classify at least 5 attributes in each according to their types.  

**Section C: Data Visualization**  
16. What is the role of data visualization in data preprocessing and exploratory data analysis?  
17. Explain histogram with an example. How does it help in understanding data distribution?  
18. Describe box plot (box-and-whisker plot). What information can be obtained from it?  
19. What is a quantile plot (Q-Q plot)? Explain its use in checking normality of data.  
20. Explain scatter plot and its importance in detecting correlation and clusters.  
21. Differentiate between histogram and box plot. When would you prefer one over the other?  

**Section D: Basic Statistical Descriptions**  
22. Explain the measures of central tendency (mean, median, mode) with examples.  
23. When would you prefer median over mean? Justify with an example.  
24. Define measures of dispersion. Explain range, variance, standard deviation, and IQR.  
25. What is skewness? Explain positive, negative, and zero skewness with sketches.  
26. Define kurtosis. Differentiate between leptokurtic, mesokurtic, and platykurtic distributions.  
27. How do basic statistical descriptions help in identifying noise and outliers in data?  

**Section E: Data Preprocessing** (Highest weightage – most questions)  
28. What is data preprocessing? Why is it considered the most important and time-consuming step in data mining?  
29. List and explain the major tasks in data preprocessing.  
30. Explain data cleaning in detail. What are the different ways to handle missing values?  
31. Describe binning methods for smoothing noisy data. Explain smoothing by bin means with an example.  
32. What are outliers? How can they be detected and handled during data cleaning?  
33. Explain data integration. What are the major issues in data integration?  
34. What is entity identification and redundancy detection in data integration?  
35. Define data transformation. Explain normalization techniques (min-max, z-score, decimal scaling) with formulas and examples.  
36. What is data discretization? Explain equal-width and equal-frequency binning with examples.  
37. Explain data reduction. Why is it necessary?  
38. Describe attribute subset selection in dimensionality reduction. What are filter and wrapper methods?  
39. Explain numerosity reduction techniques: histograms, clustering, sampling.  
40. What are the different types of sampling methods in data reduction? Explain stratified sampling with an example.  
41. Differentiate between data cleaning and data transformation.  
42. Compare data reduction and data transformation. Give situations where each is preferred.  
43. Explain the concept of concept hierarchy generation in data preprocessing.  
44. How does data preprocessing affect the performance of classification and clustering algorithms?  
45. Draw and explain the flowchart of major steps in data preprocessing.  

**Mixed / Important Long-Answer Type Questions**  
46. Explain data objects and attribute types in detail. Why is the knowledge of attribute types essential before mining? (16 marks)  
47. Discuss data visualization techniques in detail. How do they help in data understanding? (10/16 marks)  
48. What are the measures of central tendency and dispersion? Explain with examples and their significance in data mining. (10 marks)  
49. Describe data preprocessing in detail. Explain cleaning, integration, transformation, and reduction with techniques and examples. (16 marks – most repeated)  
50. Write a detailed note on data preprocessing tasks, challenges in real-world data, and how preprocessing improves mining results. (16 marks)
51. Explain the different kinds of data and patterns in data mining with examples.
52. Describe any four data preprocessing techniques with their purpose.
53. Differentiate between data discretization and data reduction. Give one method for each.
53. Explain the steps of the Apriori algorithm with a small example.
54. What is market basket analysis? Define support and confidence with formulas.
55. Describe the advantages of FP-growth over Apriori.
56. Discuss the complete data preprocessing process in detail, including cleaning, integration, transformation, and reduction techniques. Illustrate with suitable examples.
57. Explain attribute subset selection methods and data visualization techniques used in data preparation for mining. Provide examples of each.
58. Describe the Apriori algorithm in detail. Discuss its limitations and how mining frequent itemsets without candidate generation addresses them.
59. Explain multilevel and multidimensional association rules. Discuss constraint-based association mining with examples.




**Preparation Tips for Exam**  
- Focus maximum on **Data Preprocessing** (questions 28–50) – usually 1 full 16-mark question + many short ones.  
- **Data Objects & Attribute Types** (questions 8–15) – compulsory short + long.  
- Memorize **tables** (attribute types, preprocessing tasks) and **examples**.  
- Practice diagrams: Histogram, Box plot, Preprocessing flowchart, Attribute type hierarchy.  
- Use diagrams/tables for attributes, preprocessing steps, reduction techniques  
- Give real-life examples (market basket, customer data)  
- Write definitions first → explanation → example → advantages  
- Revise from **Han & Kamber** book – Chapter 2 & 3 (most questions come from there)

## Some other Questions 

**MCQ**

Which of the following is a nominal attribute type?  
   a) Age b) Temperature c) Gender d) Salary 

Data visualization is primarily used to:  
   a) Clean data b) Discover patterns c) Reduce dimensions d) Transform values 

Which step in data preprocessing handles missing values?  
   a) Data integration b) Data cleaning c) Data discretization d) Sampling 

Histogram is a technique used in:  
   a) Data cleaning b) Data reduction c) Data transformation d) Attribute selection  

Clustering for data reduction belongs to:  
   a) Numerosity reduction b) Dimensionality reduction c) Data integration d) Discretization

In market basket analysis, support of an itemset is defined as:  
   a) Confidence / Lift b) Frequency of occurrence / Total transactions c) Probability of co-occurrence d) Correlation coefficient

The Apriori algorithm uses which property to prune candidates?  
   a) Downward closure b) Upward closure c) Monotonicity d) Apriori property

FP-growth algorithm avoids:  
   a) Candidate generation b) Support counting c) Tree construction d) Pattern mining

Correlation analysis in association mining is used to:  
   a) Find frequent itemsets b) Identify interesting rules c) Generate candidates d) Prune rules 

Multidimensional association rules involve:  
    a) Single dimension b) Multiple dimensions c) Binary attributes only d) Transactional data only 


**Short Notes:**  
1. Kinds of Data in Data Mining  
2. Types of Attributes with examples  
3. Data Preprocessing – Need & Tasks  
4. Data Visualization Techniques  
5. Attribute Subset Selection  
6. Sampling Methods in Data Reduction  

**Long Answers :**  
1. Explain Data Preprocessing in detail with techniques for Cleaning, Integration, Transformation & Reduction.  
2. Discuss Data Reduction strategies with focus on Histograms, Clustering & Sampling.  
3. What are kinds of patterns in data mining? Explain with examples.  
4. Describe Data Objects & Attribute Types in detail.

