# Unit-1: Data Mining Introduction – 
**Topic Focus: What is a Pattern? Its Types in Data Mining (Kinds of Patterns / Functionalities)**  
**Course: 21CSE355T - Data Mining and Analytics**  
**Reference:** Jiawei Han, Micheline Kamber – "Data Mining: Concepts and Techniques" (3rd Edition), Chapter 1 & 2  

## 1. What is a Pattern in Data Mining?

**Simple Definition :**  
A **pattern** in data mining is a **regularity**, **relationship**, **trend**, **association**, or **structure** that exists in the data and is **interesting**, **non-trivial**, **previously unknown**, and **potentially useful** for decision-making.

**More Formal Definition (for exams):**  
A pattern is a **representation of knowledge** discovered from data that describes **frequent occurrences**, **correlations**, **deviations**, or **structures** in large datasets. Patterns help transform raw data into **actionable insights**.

**Key Characteristics of Interesting Patterns:**  
- **Novel** → Not obvious or already known  
- **Useful** → Can lead to business decisions, predictions, etc.  
- **Valid** → Holds on new/unseen data  
- **Understandable** → Easy for humans to interpret  
- **Unexpected** (sometimes) → Surprising insights

**Why Patterns Matter?**  
- Data is huge → We can't look at everything manually.  
- Patterns = Hidden knowledge → Helps in **decision support**, **prediction**, **optimization**, **fraud detection**, etc.  
- Real-life analogy: "Finding gold nuggets in a river of sand" – patterns are the gold!

**Quick Class Question:**  
"Think of your daily life – what patterns do you notice without realizing? (e.g., You always buy chips when buying cola → that's an association pattern!)"

## 2. Classification of Patterns – Overview 

Data mining patterns are broadly classified into two categories (as per syllabus & standard books):

| Category          | Task Type      | Learning Type       | Goal                                      | Main Techniques                     |
|-------------------|----------------|---------------------|-------------------------------------------|-------------------------------------|
| Descriptive       | Descriptive    | Unsupervised        | Summarize & describe data structure       | Clustering, Association, Outliers   |
| Predictive        | Predictive     | Supervised          | Forecast future or unknown values         | Classification, Prediction (Regression) |

**Exam Tip:** Always remember:  
**Descriptive** → What is happening? (No target label needed)  
**Predictive** → What will happen? (Needs labeled training data)

## 3. Detailed Types of Patterns in Data Mining 
(Explain each with: Definition → How it works → Supervised/Unsupervised → Example → Real-world application → Why useful)

### 3.1 Classification  
**Definition:** Predicts the **categorical class label** of new data objects based on the training data with known labels.  
**Type:** Predictive + Supervised  
**How it works:** Learn a model from labeled examples → Use model to assign class to new instances.  
**Algorithms (later units):** Decision Trees (ID3, CART), Naive Bayes, SVM, KNN, Neural Networks  

**Example:**  
**Customer Churn Prediction**  
Dataset: Past customers (features: age, plan type, usage, complaints) + label (Churned = Yes/No)  
Model learns → For a new customer: "This customer has high chance of churning → Offer discount!"  

**Real-world Application:** Telecom companies (Airtel, Jio) predict who will switch to competitors and take preventive actions.

### 3.2 Clustering  
**Definition:** Groups similar data objects into **clusters** without any predefined labels. Objects in same cluster are similar; different clusters are dissimilar.  
**Type:** Descriptive + Unsupervised  
**How it works:** Maximize intra-cluster similarity & minimize inter-cluster similarity.  
**Algorithms (Unit-4):** K-Means, Hierarchical, DBSCAN, BIRCH  

**Example:**  
**Customer Segmentation**  
Dataset: Customer data (age, income, spending score)  
Result: Cluster 1 = Young & High spenders, Cluster 2 = Middle-age & Low spenders  
→ Company targets ads differently for each group.

**Real-world Application:** E-commerce (Amazon, Flipkart) creates customer groups for personalized marketing.

### 3.3 Association Rules  
**Definition:** Discovers interesting **relationships** (affinities) between items/attributes that occur together frequently.  
**Type:** Descriptive + Unsupervised  
**How it works:** Find frequent itemsets → Generate rules like X → Y (support & confidence)  
**Algorithm:** Apriori (Unit-2)  

**Example:**  
**Market Basket Analysis**  
Rule: **Bread → Butter** (Support=40%, Confidence=85%)  
→ If customer buys bread, 85% chance they also buy butter.  

**Real-world Application:** Supermarkets (Big Bazaar) place butter near bread → increases sales by cross-selling.

### 3.4 Sequential Patterns  
**Definition:** Finds **frequently occurring sequences** or ordered events over time.  
**Type:** Descriptive + Unsupervised  
**How it works:** Extend association rules to consider order/timing.  
**Example:**  
**Customer Buying Sequence**  
Pattern: Laptop → External Hard Disk → Antivirus Software  
→ Customer buys laptop first, then backup device, then security software.

**Real-world Application:** Online stores suggest next product in sequence (e.g., "People who bought laptop also bought...").

### 3.5 Outlier / Anomaly Detection  
**Definition:** Identifies **rare/unusual data objects** that do not follow the general pattern (deviations).  
**Type:** Descriptive + Mostly Unsupervised (can be supervised too)  
**How it works:** Find data points far from clusters or normal distribution.  
**Algorithms (Unit-5):** Statistical, Distance-based, Clustering-based  

**Example:**  
**Fraud Detection**  
Transaction data: 99% normal purchases → One sudden ₹5 lakh purchase in foreign country.  
→ Detected as outlier → Bank blocks card & alerts customer.

**Real-world Application:** Credit card companies (Visa, Mastercard) detect fraud in real-time.

### 3.6 Prediction (Regression / Numeric Prediction)  
**Definition:** Predicts **continuous numeric values** (future trends/values) based on historical data.  
**Type:** Predictive + Supervised  
**How it works:** Fit a model (equation) to data → Use to forecast.  
**Algorithms:** Linear Regression, Neural Networks  

**Example:**  
**Stock Price Prediction**  
Input: Past prices, volume, news sentiment  
Output: Predicted price tomorrow = ₹1250  

**Real-world Application:** Finance companies predict sales, stock trends, housing prices.

## 4. Summary Table – Quick Revision 

| Pattern Type              | Task Type     | Learning Type   | Key Goal                              | One Strong Real-world Example                  |
|---------------------------|---------------|-----------------|---------------------------------------|------------------------------------------------|
| Classification            | Predictive    | Supervised      | Predict category/class                | Customer churn in telecom                      |
| Clustering                | Descriptive   | Unsupervised    | Group similar objects                 | Customer segmentation in e-commerce            |
| Association Rules         | Descriptive   | Unsupervised    | Find item relationships               | Market basket (Bread → Butter)                 |
| Sequential Patterns       | Descriptive   | Unsupervised    | Discover ordered sequences            | Buying sequence: Laptop → Accessories          |
| Outlier Detection         | Descriptive   | Mostly Unsupervised | Find unusual/anomalous points     | Credit card fraud detection                    |
| Prediction                | Predictive    | Supervised      | Forecast numeric values               | Stock price or sales forecasting               |

**Important Exam Differences to Remember:**  
- **Classification vs Clustering** → Labels known vs unknown  
- **Predictive vs Descriptive** → Forecast future vs summarize current  
- **Supervised vs Unsupervised** → Training with target vs without target

## 5. Class Activity & Discussion 
- Think of one more real-life example for **each** pattern type.  
- Which pattern would you use for:  
  a) Finding fake news spreaders?  
  b) Grouping similar diseases?  
  c) Predicting rainfall?  
- Discuss in pairs → Share 2–3 answers.

## 6. Q&A + Motivation   
- Clear doubts.  
- Remember: **Understanding patterns is the heart of data mining!**   
- **Homework:** Find 1 real-world example for each pattern type from news/internet (submit next class).

