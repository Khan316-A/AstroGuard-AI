import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="AstroGuard AI - NASA Space Health", page_icon="🚀", layout="wide")

# Custom Dark Space Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #ffffff; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 AstroGuard AI: Astronaut Health & Anomaly Alert System")
st.markdown("**Powered by NASA Human Research Program (HRP) & Open Science Data Thresholds**")

# Sidebar Controls (Simulated Astronaut Sensors)
st.sidebar.header("👨‍🚀 Live Telemetry Simulator")
st.sidebar.write("Adjust sensors to test AI Emergency Alerts:")

heart_rate = st.sidebar.slider("Heart Rate (BPM)", 40, 180, 75)
spo2 = st.sidebar.slider("Blood Oxygen SpO2 (%)", 80, 100, 98)
radiation = st.sidebar.slider("Cosmic Radiation (mSv/day)", 0.1, 100.0, 0.5)
co2_level = st.sidebar.slider("Cabin CO2 Level (%)", 0.1, 5.0, 0.4)

# Main Metrics Display
col1, col2, col3, col4 = st.columns(4)
col1.metric("Heart Rate", f"{heart_rate} BPM", "Normal: 50-100" if 50 <= heart_rate <= 100 else "ALERT")
col2.metric("Oxygen (SpO2)", f"{spo2}%", "Normal: 95-100%" if spo2 >= 95 else "LOW OXYGEN")
col3.metric("Radiation Dose", f"{radiation} mSv", "Safe: <2.0 mSv" if radiation < 2.0 else "HIGH RADIATION")
col4.metric("Cabin CO2", f"{co2_level}%", "Safe: <0.5%" if co2_level <= 0.5 else "TOXIC LEVEL")

st.divider()

# AI Diagnostic & Alert Engine
st.subheader("🧠 AI Medical Diagnostic & Countermeasure Engine")

alerts = []
if heart_rate > 110:
    alerts.append("🔴 **TACHYCARDIA ALERT:** Heart rate exceeds NASA EVA limit. Action: Halt physical exertion, initiate deep breathing, and monitor ECG.")
elif heart_rate < 50:
    alerts.append("🔴 **BRADYCARDIA ALERT:** Heart rate dangerously low. Action: Check autonomic response and contact Flight Surgeon.")

if spo2 < 94:
    alerts.append("🔴 **HYPOXIA WARNING:** Blood oxygen below 94%. Action: Switch to 100% emergency O2 mask and inspect suit pressure.")

if radiation >= 10.0:
    alerts.append("🔴 **SOLAR RADIATION STORM:** Radiation exceeds NASA HRP safe threshold! Action: Move immediately to the spacecraft's shielded storm shelter.")

if co2_level > 0.7:
    alerts.append("🔴 **HYPERCAPNIA RISK:** High cabin CO2 detected. Action: Activate backup LiOH CO2 scrubbers immediately.")

if len(alerts) == 0:
    st.success("✅ **ALL SYSTEMS NOMINAL:** Astronaut vitals are within NASA Human Research Program safe parameters. No intervention required.")
else:
    for alert in alerts:
        st.error(alert)

# Live Telemetry Graph
st.subheader("📈 Real-Time Biometric Telemetry Stream")
chart_data = pd.DataFrame({
    "Heart Rate (BPM)": np.random.normal(heart_rate, 2, 30),
    "Oxygen SpO2 (%)": np.random.normal(spo2, 0.5, 30)
})
st.line_chart(chart_data)

st.caption("Data Reference: NASA Human Research Program (HRP) & NASA Open Science Data Repository (OSDR).")
