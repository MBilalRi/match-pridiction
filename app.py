import streamlit as st
from predict import predict_match
import matplotlib.pyplot as plt

st.set_page_config(page_title="PlayWise AI", page_icon="🏏", layout="wide")

st.title("🏏 PlayWise AI - Match Decision System")

st.markdown("### Select Match Conditions")

col1, col2 = st.columns(2)

with col1:
    sport = st.selectbox("Sport", ["Cricket", "Hockey"])
    weather = st.selectbox("Weather", ["Sunny", "Rainy", "Cloudy"])
    wind = st.selectbox("Wind", ["Low", "Strong"])
    humidity = st.selectbox("Humidity", ["Low", "Medium", "High"])
    rain = st.selectbox("Rain Chance", ["Yes", "No"])

with col2:
    sky = st.selectbox("Sky", ["Clear", "Cloudy"])
    time = st.selectbox("Time", ["Afternoon", "Evening"])
    temp = st.selectbox("Temperature", ["Low", "Medium", "High"])
    ground = st.selectbox("Ground", ["Dry", "Wet"])
    visibility = st.selectbox("Visibility", ["Clear", "Foggy"])

if st.button("🔍 Predict"):
    data = {
        "Sport": sport,
        "Weather": weather,
        "Wind": wind,
        "Humidity": humidity,
        "RainChance": rain,
        "Sky": sky,
        "Time": time,
        "Temperature": temp,
        "Ground": ground,
        "Visibility": visibility
    }

    result = predict_match(data)

    if result == "Yes":
        st.success("✅ Match Should Be Played")
    else:
        st.error("❌ Match Should NOT Be Played")

    # Graph
    st.subheader("📊 Condition Overview")

    labels = ["Weather", "Wind", "Humidity", "Rain", "Ground"]
    values = [
        1 if weather == "Sunny" else 0,
        1 if wind == "Low" else 0,
        1 if humidity == "Low" else 0,
        0 if rain == "Yes" else 1,
        1 if ground == "Dry" else 0
    ]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    st.pyplot(fig)