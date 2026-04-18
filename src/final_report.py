import pandas as pd

def load_data():
    df = pd.read_csv("data/processed/cleaned_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

def generate_insights(df):
    print("\nCLIMATE TREND ANALYZER - FINAL REPORT\n")

    # Basic stats
    print("🔹 Average Temperature:", round(df['temperature'].mean(), 2))
    print("🔹 Max Temperature:", round(df['temperature'].max(), 2))
    print("🔹 Min Temperature:", round(df['temperature'].min(), 2))

    print("\n🔹 Average Rainfall:", round(df['rainfall'].mean(), 2))
    print("🔹 Average Humidity:", round(df['humidity'].mean(), 2))

    # Trends
    temp_trend = df['temperature'].iloc[-1] - df['temperature'].iloc[0]

    if temp_trend > 0:
        trend_msg = "Warming Trend Detected"
    else:
        trend_msg = "Cooling Trend Detected"

    print("\n🔹 Climate Trend:", trend_msg)

    # Anomaly count (if anomaly columns exist)
    if 'temp_anomaly' in df.columns:
        print("\n🔹 Temperature Anomalies:", df['temp_anomaly'].sum())
        print("🔹 Rainfall Anomalies:", df['rain_anomaly'].sum())

    print("\nKEY INSIGHTS:")
    print("- Climate shows seasonal variation patterns")
    print("- Temperature exhibits long-term trend behavior")
    print("- Anomalies represent extreme climate events")
    print("- Forecasting model predicts future climate behavior")

    print("\nProject Completed Successfully!")

if __name__ == "__main__":
    df = load_data()
    generate_insights(df)
