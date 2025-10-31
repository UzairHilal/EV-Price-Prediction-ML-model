import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
import path
import joblib

BASE_DIR = os.path.dirname(__file__)
data_file_path = os.path.join(BASE_DIR, "data/raw/EV_cars.csv")
print(BASE_DIR)
data_file = pd.read_csv(data_file_path)

encdr = joblib.load(os.path.join(BASE_DIR, "src/encoder.pkl"))
model = joblib.load(os.path.join(BASE_DIR, "models/ev_pricepred_model.pkl"))

st.title("EV Price Prediction")
st.write("Enter the details below to predict the price")

battery_capacity = st.number_input("Battery Capacity (kWh)", step=1.0, value=75.0)
car_name = st.selectbox("Choose EV", [name for name in data_file['Car_name']])
efficiency = st.number_input("Efficiency (Wh/km)",step=1.0, value=172.0)
charging_speed = st.number_input("Charging speed (km/h)",step=1.0, value=670.0)
ev_range = st.number_input("Range (km)",step=1.0, value=435.0)
top_speed = st.number_input("Top Speed (km/h)",step=1.0, value=217.0)
acceleration = st.number_input("Acceleration 0-100km/h (sec)",min_value=0.0, max_value=100.0, step=1.0, value=5.0)

car_name = encdr.transform([car_name])

button = st.button("Predict EV Price")
if button:
  input_data = pd.DataFrame([[battery_capacity, car_name, efficiency, charging_speed, ev_range, top_speed, acceleration]], columns= ['Battery', 'Car_name', 'Efficiency', 'Fast_charge', 'Range', 'Top_speed', 'acceleration..0.100.'])

  price_prediction = model.predict(input_data)
  st.markdown(f"Estimated EV Price: **${price_prediction * 1.16}**")