# 💰 Adult Census Income Prediction

A Machine Learning project that predicts whether a person's annual income is **<=50K or >50K** based on demographic, education, employment, and financial attributes.

The project uses a **Random Forest Classifier** with Scikit-learn preprocessing and provides an interactive **Streamlit web application** for making predictions.

---

## 📌 Project Overview

The goal of this project is to build a classification model that predicts an individual's income category using information such as:

- Age
- Workclass
- Education
- Marital Status
- Occupation
- Relationship
- Race
- Sex
- Capital Gain
- Capital Loss
- Hours per Week
- Native Country

The trained model is integrated into a Streamlit application where users can enter these details and receive an income prediction.

---

## 🎯 Target Variable

The model predicts two classes:

| Class | Meaning |
|---|---|
| `<=50K` | Annual income is less than or equal to 50K |
| `>50K` | Annual income is greater than 50K |

---

## 🧠 Machine Learning Workflow

The project follows a complete Machine Learning workflow:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Data Preprocessing
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Model Saving
      ↓
Streamlit Deployment
