import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Climate Trend Analyzer", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

st.title("Climate Trend Analyzer Dashboard")
st.write("Interactive analysis of climate patterns, trends, and anomalies")

# Sidebar
option = st.sidebar.selectbox(
    "Choose Analysis",
    ["Overview", "Temperature Trend", "Rainfall Trend", "Humidity Trend"]
)

# ---------------- OVERVIEW ----------------
if option == "Overview":
    st.subheader("Dataset Overview")
    st.write(df.head())

    st.subheader("Basic Statistics")
    st.write(df.describe())

# ---------------- TEMPERATURE ----------------
elif option == "Temperature Trend":
    st.subheader("Temperature Analysis")

    fig, ax = plt.subplots()
    ax.plot(df['date'], df['temperature'], color='red')
    ax.set_title("Temperature Over Time")

    st.pyplot(fig)

# ---------------- RAINFALL ----------------
elif option == "Rainfall Trend":
    st.subheader("Rainfall Analysis")

    fig, ax = plt.subplots()
    ax.plot(df['date'], df['rainfall'], color='blue')
    ax.set_title("Rainfall Over Time")

    st.pyplot(fig)

# ---------------- HUMIDITY ----------------
elif option == "Humidity Trend":
    st.subheader("Humidity Analysis")

    fig, ax = plt.subplots()
    ax.plot(df['date'], df['humidity'], color='green')
    ax.set_title("Humidity Over Time")

    st.pyplot(fig)