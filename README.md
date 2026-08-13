# Customer Churn Prediction

> Machine Learning based customer churn prediction and risk analysis system.

## 🚀 Live Demo

👉 [Try the Customer Churn Prediction App](https://customer-churn-ml-0.streamlit.app/)

# Customer Churn Prediction

A machine learning project for predicting customer churn probability, identifying important churn factors, and segmenting customers according to their churn risk.

The project focuses not only on prediction performance but also on transforming machine learning results into actionable customer retention insights.

---

## 📌 Project Overview

Customer churn is an important problem for subscription-based businesses.

The main objectives of this project are:

- Predict whether a customer is likely to churn.
- Estimate individual customer churn probability.
- Identify the most important factors associated with churn.
- Compare different machine learning models.
- Optimize the classification threshold.
- Segment customers into Low, Medium, and High risk groups.
- Analyze the characteristics of high-risk customers.
- Provide actionable customer retention recommendations.

---

## 📊 Dataset

The project uses the **Telco Customer Churn** dataset.

The dataset contains:

- **7,043 customers**
- **21 features**
- Customer demographic information
- Contract information
- Internet service information
- Payment information
- Customer support services
- Monthly and total charges
- Customer churn status

### Target Distribution

| Churn | Customers | Percentage |
|---|---:|---:|
| No | 5,174 | 73.5% |
| Yes | 1,869 | 26.5% |

Target encoding:

- `0` → No Churn
- `1` → Churn

---

## 🔎 Exploratory Data Analysis

Exploratory data analysis was performed to understand the main factors associated with customer churn.

One of the strongest relationships was observed between **contract type and churn**.

### Churn Rate by Contract Type

| Contract | Churn Rate |
|---|---:|
| Month-to-month | 42.7% |
| One year | 11.3% |
| Two year | 2.8% |

Customers with month-to-month contracts have a substantially higher churn rate compared with customers with longer-term contracts.

---

## ⚙️ Data Preprocessing

The following preprocessing steps were applied:

- Missing value analysis
- Conversion of `TotalCharges` to numerical format
- Handling missing `TotalCharges` values
- Feature engineering
- Numerical and categorical feature separation
- One-hot encoding of categorical variables
- Numerical feature scaling
- Train/test split

Additional features were created:

- `EstimatedLifetimeValue`
- `IsNewCustomer`

### Dataset Split

- Training set: **5,634 customers**
- Test set: **1,409 customers**

---

## 🤖 Machine Learning Models

Three classification algorithms were evaluated:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting

### Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 0.762 | 0.536 | 0.772 | 0.633 | 0.846 |
| Logistic Regression | 0.751 | 0.520 | 0.800 | 0.630 | 0.847 |
| Gradient Boosting | 0.797 | 0.643 | 0.528 | 0.579 | 0.840 |

Although Gradient Boosting achieved higher accuracy and precision, its recall was significantly lower.

Since identifying customers who are likely to churn is important for customer retention, Logistic Regression and Random Forest provide a better balance for this business problem.

---

## 📈 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Average Precision
- Confusion Matrix
- ROC Curve
- Precision-Recall Curve

### ROC-AUC

The best ROC-AUC score was obtained by Logistic Regression:

**ROC-AUC = 0.847**

The three models showed similar ROC curve performance.

---

## 🎯 Threshold Optimization

Different classification thresholds were evaluated.

| Threshold | Precision | Recall | F1 Score | Detected Churn | Missed Churn | False Alarm |
|---|---:|---:|---:|---:|---:|---:|
| 0.50 | 0.505 | 0.794 | 0.617 | 297 | 77 | 291 |
| 0.45 | 0.492 | 0.829 | 0.618 | 310 | 64 | 320 |
| 0.40 | 0.466 | 0.877 | 0.609 | 328 | 46 | 376 |

Lowering the threshold increases recall and allows the model to detect more potential churn customers.

However, lower thresholds also increase false alarms.

For a customer retention scenario, a threshold around **0.45** can be considered because it improves churn detection while maintaining a similar F1 score.

---

## 🔬 Feature Importance

Random Forest feature importance was used to identify the most influential variables.

The most important features included:

1. Contract — Month-to-month
2. Tenure
3. Total Charges
4. Estimated Lifetime Value
5. Online Security — No
6. Monthly Charges
7. Contract — Two year
8. Internet Service — Fiber optic
9. Tech Support — No
10. Payment Method — Electronic check

### Logistic Regression Coefficients

Logistic Regression was also used to analyze the direction of the relationship between features and churn.

### Features Associated with Higher Churn Probability

- Fiber optic internet service
- Month-to-month contracts
- New customer status
- Streaming Movies
- Streaming TV
- Higher total charges
- Electronic check payment
- No Online Security
- Multiple Lines
- No Tech Support

### Features Associated with Lower Churn Probability

- Two-year contracts
- DSL internet service
- Longer tenure
- Customers without internet service

---

## 🚨 Customer Risk Segmentation

Customers were segmented according to their predicted churn probability.

| Risk Level | Customers | Percentage | Actual Churn Rate |
|---|---:|---:|---:|
| Low | 635 | 45.07% | 5.98% |
| Medium | 337 | 23.92% | 25.52% |
| High | 437 | 31.01% | 57.21% |

### High-Risk Customers

There are **437 high-risk customers**.

Among these:

- **250 customers actually churned**
- **187 customers did not churn**
- Actual churn rate: **57.21%**

This shows that the risk segmentation can distinguish customers with substantially different churn rates.

---

## 👤 High-Risk Customer Profile

The high-risk customer group has the following characteristics:

- Average tenure: **10.76 months**
- Average monthly charges: **75.82**
- **100%** have month-to-month contracts
- **80.4%** use Fiber optic internet
- **66.8%** use Electronic check
- **92.0%** have no Online Security
- Approximately **89%** have no Tech Support
- **80.0%** use Paperless Billing

These characteristics can be used to identify customers who may benefit from proactive retention campaigns.

---

## 💡 Business Insights

Based on the analysis, several customer retention strategies can be considered.

### 1. Encourage Longer Contracts

Month-to-month customers have the highest churn rate.

Businesses could offer discounts or incentives for customers who switch to one-year or two-year contracts.

### 2. Focus on New Customers

Customers with short tenure have a higher churn risk.

Early-stage customers could receive personalized onboarding and support.

### 3. Target High Monthly Charges

Customers with relatively high monthly charges could be targeted with personalized pricing or service offers.

### 4. Promote Support Services

Customers without Online Security or Tech Support are frequently observed among high-risk customers.

Bundled service offers could potentially improve customer retention.

### 5. Monitor Electronic Check Customers

Electronic check users are overrepresented among high-risk customers.

This group can be monitored using targeted retention campaigns.

### 6. Prioritize High-Risk Customers

The risk segmentation allows customer success teams to prioritize their limited retention resources.

Instead of contacting every customer, businesses can focus first on customers with the highest predicted churn probability.

---

## 📁 Project Structure

```text
customer-churn-ml/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
├── results/
│   ├── output.png
│   ├── output1.png
│   ├── output2.png
│   ├── output3.png
│   ├── output4.png
│   ├── output5.png
│   ├── output6.png
│   ├── output7.png
│   ├── output8.png
│   └── output9.png
│
├── src/
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## ▶️ How to Run

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Navigate to the project:

```bash
cd customer-churn-ml
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Open the notebook:

```bash
jupyter notebook
```

Then open:

```text
notebooks/customer_churn_analysis.ipynb
```

---

## 📌 Key Results

- Dataset size: **7,043 customers**
- Churn rate: **26.5%**
- Best ROC-AUC: **0.847**
- High-risk customers: **437**
- High-risk actual churn rate: **57.21%**
- High-risk customers who actually churned: **250**
- Best recall among tested thresholds: **87.7% at threshold 0.40**

---

## 📚 Conclusion

This project demonstrates an end-to-end customer churn prediction workflow, from data preprocessing and exploratory analysis to machine learning, model evaluation, threshold optimization, and customer risk segmentation.

The main objective is not only to predict churn but also to transform machine learning predictions into actionable business insights.

The analysis indicates that contract type, customer tenure, internet service, monthly charges, and additional support services are important factors associated with customer churn.

The risk segmentation approach provides a practical framework for prioritizing customer retention efforts.

---

## 👩‍💻 Author

**Simge Altun**

Machine Learning & Data Analysis Project