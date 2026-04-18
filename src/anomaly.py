import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("data/processed/cleaned_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

def detect_anomalies(df):
    # Z-score method (standard in data science)
    def zscore(series):
        return (series - series.mean()) / series.std()

    df['temp_z'] = zscore(df['temperature'])
    df['rain_z'] = zscore(df['rainfall'])
    df['hum_z'] = zscore(df['humidity'])

    # anomaly condition: |z| > 2
    df['temp_anomaly'] = df['temp_z'].apply(lambda x: 1 if abs(x) > 2 else 0)
    df['rain_anomaly'] = df['rain_z'].apply(lambda x: 1 if abs(x) > 2 else 0)
    df['hum_anomaly'] = df['hum_z'].apply(lambda x: 1 if abs(x) > 2 else 0)

    print("\nAnomalies detected!")
    return df

def plot_temperature_anomalies(df):
    plt.figure(figsize=(12,5))

    plt.plot(df['date'], df['temperature'], label="Temperature", alpha=0.5)

    anomalies = df[df['temp_anomaly'] == 1]

    plt.scatter(anomalies['date'], anomalies['temperature'], 
                color='red', label="Anomaly")

    plt.title("Temperature Anomalies Detection")
    plt.legend()
    plt.savefig("outputs/graphs/temp_anomalies.png")
    plt.show()

def plot_rainfall_anomalies(df):
    plt.figure(figsize=(12,5))

    plt.plot(df['date'], df['rainfall'], label="Rainfall", alpha=0.5)

    anomalies = df[df['rain_anomaly'] == 1]

    plt.scatter(anomalies['date'], anomalies['rainfall'], 
                color='blue', label="Anomaly")

    plt.title("Rainfall Anomalies Detection")
    plt.legend()
    plt.savefig("outputs/graphs/rain_anomalies.png")
    plt.show()

if __name__ == "__main__":
    df = load_data()
    df = detect_anomalies(df)

    print("\nSample anomalies:")
    print(df[df['temp_anomaly'] == 1].head())

    plot_temperature_anomalies(df)
    plot_rainfall_anomalies(df)
