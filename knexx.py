import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

st.title("Housing Price Prediction using KNN")

# LOAD DATASET
df = pd.read_csv("c:/Users/Sanjana/Downloads/housing 1.csv")

st.subheader("Complete Dataset")
st.dataframe(df)

# SIMPLE DATA CLEANING
df = df.drop_duplicates()
df = df.dropna()          # removes the rows with missing total_bedrooms

st.subheader("Cleaned Dataset")
st.dataframe(df)

# CONVERT TEXT COLUMN TO NUMBERS
df = pd.get_dummies(df, columns=["ocean_proximity"], dtype=int)

# INPUT AND OUTPUT
X = df.drop("median_house_value", axis=1)
Y = df["median_house_value"]

# SPLIT DATA
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42
)

# SCALE DATA
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# TRAIN KNN MODEL (regression, because the target is a price)
model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, Y_train)

# EVALUATION
pred = model.predict(X_test)

r2 = r2_score(Y_test, pred)
mae = mean_absolute_error(Y_test, pred)
rmse = np.sqrt(mean_squared_error(Y_test, pred))

st.subheader("Model Performance")
st.write("R² Score:", round(r2, 3))
st.write("Mean Absolute Error: $", round(mae, 2))
st.write("RMSE: $", round(rmse, 2))

# PREDICTION INPUTS
st.subheader("Enter House Details")

income = st.number_input("Median Income (in $10,000s)", value=3.5)
age = st.number_input("Housing Median Age", value=28.0)
rooms = st.number_input("Total Rooms", value=2000.0)
population = st.number_input("Population", value=1200.0)
households = st.number_input("Households", value=500.0)
ocean = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
)

if st.button("Predict Price"):

    # USE MEDIAN VALUES FOR REMAINING FEATURES
    values = X.median()

    values["median_income"] = income
    values["housing_median_age"] = age
    values["total_rooms"] = rooms
    values["population"] = population
    values["households"] = households

    # SET THE SELECTED OCEAN CATEGORY
    for col in X.columns:
        if col.startswith("ocean_proximity_"):
            values[col] = 1 if col == "ocean_proximity_" + ocean else 0

    # SCALE INPUT (keep column order same as training)
    values = scaler.transform(pd.DataFrame([values], columns=X.columns))

    # PREDICT
    result = model.predict(values)

    st.success(f"Predicted Median House Value: ${result[0]:,.0f}")
