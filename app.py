import streamlit as st
import pickle
import numpy as np

# Load the saved model (ensure rf_model.pkl exists in your working directory)
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

st.title("Life Expectancy Prediction App")
st.write("Provide the required inputs to predict Life Expectancy.")

# Input for categorical feature 'Status'
status = st.selectbox("Status", ["Developed", "Developing"])
status_val = 1 if status == "Developed" else 0

# Inputs for numeric features
adult_mortality = st.number_input("Adult Mortality", min_value=0.0, value=100.0)
infant_deaths = st.number_input("Infant Deaths", min_value=0.0, value=50.0)
alcohol = st.number_input("Alcohol", min_value=0.0, value=0.0, step=0.1)
percentage_expenditure = st.number_input("Percentage Expenditure", min_value=0.0, value=5.0, step=0.1)
hepatitis_b = st.number_input("Hepatitis B", min_value=0.0, value=90.0, step=0.1)
measles = st.number_input("Measles", min_value=0.0, value=0.0, step=1.0)
bmi = st.number_input("BMI", min_value=0.0, value=25.0, step=0.1)
under_five_deaths = st.number_input("Under-Five Deaths", min_value=0.0, value=10.0)
polio = st.number_input("Polio", min_value=0.0, value=90.0, step=0.1)
total_expenditure = st.number_input("Total Expenditure", min_value=0.0, value=5.0, step=0.1)
diphtheria = st.number_input("Diphtheria", min_value=0.0, value=90.0, step=0.1)
hiv_aids = st.number_input("HIV/AIDS", min_value=0.0, value=0.0, step=0.1)
gdp = st.number_input("GDP", min_value=0.0, value=5000.0, step=100.0)
population = st.number_input("Population", min_value=0.0, value=1000000.0, step=1000.0)
thinness_1_19 = st.number_input("Thinness (1-19 years)", min_value=0.0, value=5.0, step=0.1)
thinness_5_9 = st.number_input("Thinness (5-9 years)", min_value=0.0, value=5.0, step=0.1)
income_composition = st.number_input("Income Composition", min_value=0.0, value=0.5, step=0.1)
schooling = st.number_input("Schooling", min_value=0.0, value=10.0, step=0.1)

# Input for Year (one-hot encoded)
year = st.selectbox("Year", [str(y) for y in range(2001, 2016)])

# Create one-hot encoding for the year columns
year_columns = ['Year_2001', 'Year_2002', 'Year_2003', 'Year_2004', 'Year_2005',
                'Year_2006', 'Year_2007', 'Year_2008', 'Year_2009', 'Year_2010',
                'Year_2011', 'Year_2012', 'Year_2013', 'Year_2014', 'Year_2015']
# Initialize all year columns to 0
year_inputs = {col: 0 for col in year_columns}
# Set the selected year to 1
selected_year_col = f"Year_{year}"
if selected_year_col in year_inputs:
    year_inputs[selected_year_col] = 1

# Combine all inputs into a feature vector in the correct order
# Ensure this order matches exactly how your model was trained!
input_features_list = [
    status_val, adult_mortality, infant_deaths, alcohol, percentage_expenditure,
    hepatitis_b, measles, bmi, under_five_deaths, polio, total_expenditure,
    diphtheria, hiv_aids, gdp, population, thinness_1_19, thinness_5_9,
    income_composition, schooling
]
# Append the one-hot encoded year features in the order of year_columns
input_features_list += [year_inputs[col] for col in year_columns]

# Convert to a 2D numpy array for prediction
input_features = np.array([input_features_list])

if st.button("Predict Life Expectancy"):
    prediction = rf_model.predict(input_features)
    st.write(f"Predicted Life Expectancy: {prediction[0]:.2f} years")
