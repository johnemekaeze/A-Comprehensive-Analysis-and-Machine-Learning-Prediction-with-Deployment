# Project Overview

**Title:**  
A Comprehensive Analysis and Machine Learning Prediction of Life Expectancy with Deployment

**Objective:**  
This project aims to analyze global life expectancy trends and develop a machine learning model to predict life expectancy based on a range of socioeconomic and health indicators. The project covers the entire data science pipeline—from data cleaning and exploratory data analysis (EDA) to model building, evaluation, and eventual cloud deployment using Streamlit.

**Scope:**  
- **Data Cleaning and Preprocessing:**  
  Address missing values, standardize column names, and ensure correct data types.
- **Exploratory Data Analysis (EDA):**  
  Visualize trends and relationships among variables to understand factors influencing life expectancy.
- **Modeling:**  
  Build and compare multiple regression models (e.g., Linear Regression, Decision Tree, Random Forest, and Gradient Boosting) to predict life expectancy.
- **Deployment:**  
  Create an interactive web application using Streamlit to deploy the best performing model, allowing users to input feature values and obtain life expectancy predictions.

---

## Data Description

The dataset used in this project provides country-level health and socioeconomic indicators, which serve as predictors for life expectancy. Each row represents a country-year observation with multiple variables that describe various dimensions of health and social development.

### Key Variables and Their Descriptions

- **Status:**  
  Indicates whether a country is classified as "Developed" or "Developing." This categorical variable often reflects differences in healthcare, economic stability, and infrastructure.

- **Adult Mortality:**  
  The number of adult deaths per 1,000 individuals. This variable is a key indicator of overall health conditions and healthcare quality.

- **Infant Deaths:**  
  The number of infant deaths per 1,000 live births. High infant mortality rates are typically associated with inadequate healthcare services and poor living conditions.

- **Alcohol:**  
  Per capita alcohol consumption, which can have significant effects on public health, including life expectancy.

- **Percentage Expenditure:**  
  The percentage of GDP that a country spends on health expenditure. This provides insight into the level of investment in public health.

- **Hepatitis B:**  
  Vaccination coverage for Hepatitis B, reflecting preventive healthcare measures in place.

- **Measles:**  
  Number of reported measles cases, which can indicate the strength of public health systems and vaccination programs.

- **BMI (Body Mass Index):**  
  A measure used to evaluate whether a population has a healthy weight, which is linked to overall health and longevity.

- **Under-Five Deaths:**  
  The number of deaths among children under the age of five. Similar to infant deaths, this variable highlights the effectiveness of maternal and child healthcare.

- **Polio:**  
  Vaccination coverage for polio, serving as an indicator of a country's immunization efforts.

- **Total Expenditure:**  
  Total health expenditure per capita, providing a broader picture of investment in healthcare services.

- **Diphtheria:**  
  Vaccination coverage for diphtheria, another marker of preventive healthcare practices.

- **HIV/AIDS:**  
  Prevalence of HIV/AIDS, an important health variable that can significantly impact life expectancy.

- **GDP:**  
  Gross Domestic Product, reflecting the economic strength of a country. Economic resources often correlate with better healthcare and longer life expectancy.

- **Population:**  
  The total population of the country, which can sometimes influence the availability and quality of healthcare services.

- **Thinness (1-19 years) and Thinness (5-9 years):**  
  Indicators of malnutrition in children and adolescents, which can affect overall health and development.

- **Income Composition:**  
  A composite measure representing the income distribution within a country. Income inequality can have substantial implications for public health.

- **Schooling:**  
  Average years of schooling, a proxy for the level of education in a population. Higher education levels often correlate with better health awareness and outcomes.

- **Year:**  
  The year when the data was collected. In this project, the year is one-hot encoded into separate binary columns (e.g., `Year_2001`, `Year_2002`, ..., `Year_2015`) to capture temporal trends without implying an ordinal relationship.

---

## Methodology

1. **Data Cleaning and Imputation:**  
   The project begins with cleaning the dataset by standardizing column names, converting data types, and imputing missing values both at the country level and overall using mean imputation.

2. **Exploratory Data Analysis (EDA):**  
   Various plots (histograms, heatmaps, violin plots, and line charts) are used to understand the distribution of life expectancy and the relationships among the predictor variables.

3. **Feature Engineering:**  
   - Categorical variables such as **Status** are encoded.
   - The **Year** variable is transformed into multiple binary columns via one-hot encoding.
   - Other numeric variables are standardized to ensure that models perform optimally.

4. **Model Development:**  
   Multiple regression models, including Random Forest (the primary model), are trained to predict life expectancy. Their performance is evaluated using metrics like Mean Squared Error (MSE) and R-squared.

5. **Deployment:**  
   The final model is deployed using Streamlit, allowing end-users to interact with the model by inputting various health and socioeconomic indicators and receiving life expectancy predictions in real time.
