# Project Overview

**Title:**  
A Comprehensive Analysis and Machine Learning Prediction of Life Expectancy with Deployment

**Objective:**  
This project aims to analyze global life expectancy trends and develop a machine learning model to predict life expectancy based on a range of socioeconomic and health indicators. The project covers the entire data science pipeline—from data cleaning and exploratory data analysis (EDA) to model building, evaluation, and eventual cloud deployment using Streamlit.

**Scope:**  
- **Data Cleaning and Preprocessing:** Address missing values, standardize column names, and ensure correct data types.
- **Exploratory Data Analysis (EDA):** Visualize trends and relationships among variables to understand factors influencing life expectancy.
- **Modeling:** Build and compare multiple regression models (e.g., Linear Regression, Decision Tree, Random Forest, and Gradient Boosting) to predict life expectancy.
- **Deployment:** Create an interactive web application using Streamlit to deploy the best performing model, allowing users to input feature values and obtain life expectancy predictions.

---

## Data Description

The dataset used in this project provides country-level health and socioeconomic indicators, which serve as predictors for life expectancy. Each row represents a country-year observation with multiple variables that describe various dimensions of health and social development.

## Methodology

1. **Data Cleaning and Imputation:** The project begins with cleaning the dataset by standardizing column names, converting data types, and imputing missing values both at the country level and overall using mean imputation.

2. **Exploratory Data Analysis (EDA):** Various plots (histograms, heatmaps, violin plots, and line charts) are used to understand the distribution of life expectancy and the relationships among the predictor variables.

3. **Feature Engineering:** Categorical variables such as **Status** are encoded. The **Year** variable is transformed into multiple binary columns via one-hot encoding. Other numeric variables are standardized to ensure that models perform optimally.

4. **Model Development:** Multiple regression models, including Random Forest (the primary model), are trained to predict life expectancy. Their performance is evaluated using metrics like Mean Squared Error (MSE) and R-squared.

5. **Deployment:** The final model is deployed using Streamlit, allowing end-users to interact with the model by inputting various health and socioeconomic indicators and receiving life expectancy predictions in real time.

---

## Deployed Streamlit App

Use the link below to navigate to the Streamlit application for real-time life expectancy predictions:

[Life Expectancy Prediction App](https://analysis-and-ml-prediction-of-life-expectancy-with-deployment.streamlit.app/)
