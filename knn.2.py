import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,mean_squared_error,r2_score
from data_cleaning import clean_data

st.title("Survival Prediction Of Titanic")

upload_file = st.file_uploader("Upload Titanic CSV Dataset",type=["csv"])

df = pd.read_csv("upload_file")

tab1,tab2,tab3,tab4,tab5,tab6= st.tabs(["Complete Data","Describe","Clean Data","Top 5 rows","Bottom 5 rows","Analysis of Data"])

with tab1:
    st.write("Dataset")
    st.dataframe(df)

with tab2:
    st.write("Describe")
    st.dataframe(df.describe())


with tab3:
    st.write("Clean Data")
    cleaned_df = clean_data(df.copy())
    st.dataframe(cleaned_df,use_container_width=True)


with tab4:
    st.write("Top 5 rows")
    st.dataframe(cleaned_df.head())

with tab5:
    st.write("Bottom 5 rows")
    st.dataframe(cleaned_df.tail())

X =  df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]

Y = df[["Survived"]]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

st.write("pred")
st.write("proba")