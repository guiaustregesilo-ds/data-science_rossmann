**Rossmann Store Sales Prediction**

🚀 **Project Overview**
This project provides a robust Machine Learning solution to forecast the daily sales of 1,115 Rossmann drug stores across Europe. The main goal is to deliver accurate sales predictions for the immediate next week and up to six weeks ahead, enabling management to make strategic decisions regarding inventory, promotions, and logistics.

🎯 **Business Objective**
To accurately predict the daily sales for each store for a future period.

📊 **Performance Metric**
The model's performance was primarily evaluated using the Mean Absolute Percentage Error (MAPE). This metric is highly suitable for sales forecasting problems as it provides the average percentage error of the prediction relative to the actual value, which is easily interpretable for business stakeholders.

⚙️ **Solution Architecture**
The project follows a standard Data Science lifecycle, structured into distinct steps:

STEP 01: Data Description

Data Loading, merging datasets, and standardizing column names.

Handling data types and filling missing values for competition and promotion fields.

STEP 02: Feature Engineering & Hypotheses

Development of key temporal features such as the duration of the competition and promotion.

Creation of a Mind Map to list potential sales drivers.

STEP 03: Filtering

Removal of non-relevant data rows (stores that were closed and days with zero sales).

Exclusion of unnecessary columns for modeling.

STEP 04: Exploratory Data Analysis (EDA)

Validation of Business Hypotheses.

Univariate, bivariate, and multivariate analysis of variables.

STEP 05 - 09 (Inferred): Modeling and Feature Selection

Data preparation (Encoding and Scaling).

Feature Selection using the BorutaPy algorithm.

Model Training and Comparison (XGBoost was the top candidate).

Temporal Cross-Validation was used to ensure model robustness.

STEP 10: Deployment

The final model is serialized and deployed as a REST API using Flask for real-time inference.

🛠️ **Technologies and Libraries**
The project was developed in Python, leveraging the following libraries:

Language: Python

Data Analysis: Pandas, Numpy

Data Visualization: Matplotlib, Seaborn

Machine Learning: XGBoost, RandomForestRegressor, LinearRegression, Lasso

Feature Selection: BorutaPy

Preprocessing: Scikit-learn (RobustScaler, MinMaxScaler, LabelEncoder)

Deployment/API (Inferred): Flask
