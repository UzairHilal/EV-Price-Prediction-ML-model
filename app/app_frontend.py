import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# from utils import wrangle
import pickle
import sys
import path
import joblib

data_file = pd.read_csv("../data/raw/EV_cars.csv")

encdr = joblib.load("../src/encoder.pkl")
model = joblib.load("../models/ev_pricepred_model.pkl")

st.title("EV Price Prediction")
st.write("Enter the details below to predict the price")

battery_capacity = st.number_input("Battery Capacity (kWh)", step=1.0)
car_name = st.selectbox("Choose EV", [name for name in data_file['Car_name']])
efficiency = st.number_input("Efficiency (Wh/km)",step=1.0)
charging_speed = st.number_input("Charging speed (km/h)",step=1.0)
ev_range = st.number_input("Range (km)",step=1.0)
top_speed = st.number_input("Top Speed (km/h)",step=1.0)
acceleration = st.number_input("Acceleration 0-100km/h (sec)",min_value=0.0, max_value=100.0, step=1.0)

car_name = encdr.transform([car_name])

button = st.button("Predict Price")
if button:
  input_data = pd.DataFrame([[battery_capacity, car_name, efficiency, charging_speed, ev_range, top_speed, acceleration]], columns= ['Battery', 'Car_name', 'Efficiency', 'Fast_charge', 'Range', 'Top_speed', 'acceleration..0.100.'])

  price_prediction = model.predict(input_data)
  st.write(f"Estimated EV Price: {price_prediction}")