# Fraud Detection using Machine Learning

## Overview
This project focuses on detecting fraudulent transactions in financial systems using machine learning techniques. With the rise of sophisticated fraud schemes, traditional rule-based detection methods often fall short. By utilizing advanced machine learning models, we aim to accurately identify and prevent fraudulent transactions, thereby enhancing security in financial sectors.

The key models used in this project are:
- **Random Forest Classifier**
- **XGBoost Classifier**

We compared their performance to determine the most effective approach for detecting fraud.

## Table of Contents
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Dataset Overview](#dataset-overview)
4. [Approach](#approach)
5. [Results](#results)
6. [Installation and Usage](#installation-and-usage)
7. [Screenshots](#screenshots)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction
Fraud detection is a critical component in finance, healthcare, and many other industries. It involves identifying suspicious activities to prevent financial losses and protect users' assets. In this project, machine learning introduces a dynamic approach, allowing the detection model to learn and adapt to new fraud patterns that traditional methods might miss.

## Problem Statement
The main objective of this project is to improve fraud detection using machine learning models to:
- Accurately identify fraudulent transactions.
- Minimize false positives while maximizing recall.

We hypothesize that machine learning models like **Random Forest** and **XGBoost** can significantly improve fraud detection by finding subtle patterns that rule-based systems cannot.

## Dataset Overview
We used a dataset from Kaggle, consisting of transactional records with key features like:
- **Transaction Amount**
- **Original and New Balances**
- **Transaction Type**

The data was preprocessed, with features like transaction types numerically encoded, and balance differences calculated to help in fraud detection.

## Approach
The project workflow includes:
1. **Data Preprocessing**: Normalizing features for better performance, removing irrelevant features, and creating derived features.
2. **Model Training**: Training two machine learning models—**Random Forest** and **XGBoost**—on the dataset.
3. **Evaluation**: Evaluating model performance using confusion matrices, recall, and precision metrics.

**Model Comparison**:
- **Random Forest Classifier**: Achieved recall of 0.824 and precision of 0.925.
- **XGBoost Classifier**: Achieved recall of 0.787 and precision of 0.903.

The Random Forest Classifier outperformed XGBoost in this context.

## Results
The **Random Forest Classifier** provided better results for both recall and precision compared to **XGBoost**. Below is a summary:
- **Confusion Matrix for Random Forest**:
  - **Recall**: 0.824
  - **Precision**: 0.925
- **Confusion Matrix for XGBoost**:
  - **Recall**: 0.787
  - **Precision**: 0.903

### Key Insights:
- **Higher Recall** with Random Forest suggests better detection of fraud cases.
- **Higher Precision** indicates fewer false positives, enhancing the reliability of fraud alerts.

## Installation and Usage
### Requirements
- Python 3.8+
- Jupyter Notebook
- Required Python Libraries: `numpy`, `pandas`, `scikit-learn`, `xgboost`, `matplotlib`

### Setup
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/fraud-detection-ml.git
    cd fraud-detection-ml
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Notebook**:
    Open the Jupyter Notebook and execute the cells to see the data preprocessing steps, training, and evaluation of the models.

## Screenshots
Add your screenshots here to illustrate the project steps and model performance.

Example:
- **Figure 1**: Confusion Matrix of Random Forest Model
- **Figure 2**: Model Comparison Chart

## Contributing
Contributions are welcome! Please feel free to raise issues, suggest improvements, or submit pull requests.

### Contributors
- **Abhishek Panta** (pantaa@uwindsor.ca)
- **Ajay Charan** (charan2@uwindsor.ca)
- **Divy Patel** (patel3ma@uwindsor.ca)

## License
This project is licensed under the MIT License.
