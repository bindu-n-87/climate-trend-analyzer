import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

def load_data():
    df = pd.read_csv("data/processed/cleaned_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

def plot_temperature(df):
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['temperature'], color='red', label='Temperature')
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.savefig("outputs/graphs/temperature_trend.png")
    plt.show()

def plot_rainfall(df):
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['rainfall'], color='blue', label='Rainfall')
    plt.title("Rainfall Over Time")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.legend()
    plt.savefig("outputs/graphs/rainfall_trend.png")
    plt.show()

def plot_humidity(df):
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['humidity'], color='green', label='Humidity')
    plt.title("Humidity Over Time")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.legend()
    plt.savefig("outputs/graphs/humidity_trend.png")
    plt.show()

def seasonal_analysis(df):
    df['month'] = df['date'].dt.month

    monthly_avg = df.groupby('month')[['temperature', 'rainfall', 'humidity']].mean()

    monthly_avg.plot(kind='bar', figsize=(12,6))
    plt.title("Monthly Climate Pattern")
    plt.savefig("outputs/graphs/seasonal_pattern.png")
    plt.show()

if __name__ == "__main__":
    df = load_data()

    print("Generating EDA graphs...")

    plot_temperature(df)
    plot_rainfall(df)
    plot_humidity(df)
    seasonal_analysis(df)

    print("EDA completed successfully!")
