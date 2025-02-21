# **Bank Marketing Campaign Analysis**

`Created by : Syafiq Basmallah`

## **Overview**
This project aims to analyze Bank Sigma's marketing campaign focused on promoting term deposit products. By utilizing historical data, we will identify customer characteristics that are more likely to participate in the campaign.

## **Table of Contents**

1. Business Problem
2. Data Understanding
3. Data Preparation
4. Modeling & Evaluation
5. Conclusion & Recommendation

## **1. Business Problem Understanding**

### **Context**
Bank Sigma periodically conducts direct marketing campaigns targeting potential customers. The objectives of this analysis are:
- Increasing efficiency in targeting relevant customers
- Optimizing campaign strategy effectiveness
- Minimizing marketing budget waste

### **Problem Statement**
Can we build a predictive model capable of identifying customers who are most likely to subscribe to the term deposit product?

### **Metrics**
- **Accuracy**: To assess how well the model can predict correctly
- **Precision & Recall**: To understand the balance between truly interested customers and those who are not
- **F1-score**: Combining precision and recall for a comprehensive evaluation

## **2. Data Understanding**
The dataset used comes from previous marketing campaigns containing customer demographic information, past interactions, and campaign outcomes.

Key features in the dataset:
- `age`: Customer age
- `job`: Customer's job type
- `marital`: Marital status
- `education`: Education level
- `default`: Credit default status
- `balance`: Average customer balance
- `contact`: Type of contact used
- `campaign`: Number of contacts made during the campaign
- `previous`: Number of previous contacts
- `y`: Target label (whether the customer subscribed to the term deposit or not)

## **3. Data Preparation**
Steps taken:
- Removing missing values
- Encoding categorical variables
- Normalizing numerical features
- Splitting the dataset into training and testing sets

## **4. Modeling & Evaluation**
Several machine learning models were tested:
- **Logistic Regression**
- **Random Forest Classifier**
- **Gradient Boosting**

Evaluation was performed using:
- Confusion Matrix
- ROC Curve
- Classification Report

## **5. Conclusion & Recommendation**
- The best model based on evaluation is `Logistic Regression`
- Bank Sigma can improve campaign effectiveness by targeting customers based on model analysis
- Further recommendations include testing with a larger dataset and exploring additional features

## **How to Run**
1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook
   ```bash
   jupyter notebook
   ```

## **Dependencies**
- Python 3.x
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

link streamlit: https://capstone3syafiq.streamlit.app/
