import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from google import genai
import os
import path
import joblib

BASE_DIR = os.path.dirname(__file__)
data_file_path = os.path.join(BASE_DIR, "Week 1/data/raw/EV_cars.csv")
data_file = pd.read_csv(data_file_path)

encdr = joblib.load(os.path.join(BASE_DIR, "Week 1/src/encoder.pkl"))
model = joblib.load(os.path.join(
    BASE_DIR, "Week 2/models/ev_pricepred_model.pkl"))

col1, col2 = st.columns([0.6, 0.4], gap="small",border=True)

with col1:
    st.title("EV Price Prediction")
    st.write("Enter the details below to predict the price")
    battery_capacity = st.number_input(
        "Battery Capacity (kWh)", step=1.0, value=75.0)
    car_name = st.selectbox(
        "Choose EV", [name for name in data_file['Car_name']])
    efficiency = st.number_input("Efficiency (Wh/km)", step=1.0, value=172.0)
    charging_speed = st.number_input(
        "Charging speed (km/h)", step=1.0, value=670.0)
    ev_range = st.number_input("Range (km)", step=1.0, value=435.0)
    top_speed = st.number_input("Top Speed (km/h)", step=1.0, value=217.0)
    acceleration = st.number_input(
        "Acceleration 0-100km/h (sec)", min_value=0.0, max_value=100.0, step=1.0, value=5.0)

    car_name = encdr.transform([car_name])

    button = st.button("Predict EV Price")
    if button:
        input_data = pd.DataFrame([[battery_capacity, car_name, efficiency, charging_speed, ev_range, top_speed, acceleration]], columns=[
                                  'Battery', 'Car_name', 'Efficiency', 'Fast_charge', 'Range', 'Top_speed', 'acceleration..0.100.'])

        price_prediction = model.predict(input_data)
        st.markdown(f"Estimated EV Price: **${price_prediction * 1.16}**")


# chatbot
with col2:
  client = genai.Client(api_key="AIzaSyDIMgtfavxi3M3aZSEswXkXj9_GfMZdp1A")

  st.header("Chatbot")
  prompt_text = st.chat_input("Prompt")
  if prompt_text:
      response = client.models.generate_content(
          model="gemini-2.5-flash",
          contents=[
              '''SYSTEM: You are an advanced Electric Vehicle (EV) assistant.
              Your job is to:
              - guide users about EVs
              - compare EV models
              - explain battery types
              - recommend charging methods
              - calculate range, charging cost, and efficiency
              - answer only EV-related questions
              Keep the answers short, answer should be not more than 60 words''',
              f'''USER QUESTION: {prompt_text}'''
          ]
      )
      
      user_prompt = st.chat_message("user")
      user_prompt.write(prompt_text)
      message = st.chat_message("assistant")
      message.write(response.text)