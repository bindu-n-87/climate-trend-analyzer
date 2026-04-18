import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("data/processed/cleaned_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df


def add_trend_lines(df):
    # Rolling mean = smoothens noise (VERY IMPORTANT in real data science)
    df['temp_trend'] = df['temperature'].rolling(window=30).mean()
    df['rain_trend'] = df['rainfall'].rolling(window=30).mean()
    df['humidity_trend'] = df['humidity'].rolling(window=30).mean()
    return df


def plot_temperature_trend(df):
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['temperature'], alpha=0.4, label="Raw Temperature")
    plt.plot(df['date'], df['temp_trend'], color='red', label="Trend (30-day avg)")
    plt.title("Temperature Trend Analysis")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.savefig("outputs/graphs/temperature_trend_analysis.png")
    plt.show()


def plot_rainfall_trend(df):
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['rainfall'], alpha=0.4, label="Raw Rainfall")
    plt.plot(df['date'], df['rain_trend'], color='blue', label="Trend (30-day avg)")
    plt.title("Rainfall Trend Analysis")
    plt.legend()
    plt.savefig("outputs/graphs/rainfall_trend_analysis.png")
    plt.show()


def plot_humidity_trend(df):
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['humidity'], alpha=0.4, label="Raw Humidity")
    plt.plot(df['date'], df['humidity_trend'], color='green', label="Trend (30-day avg)")
    plt.title("Humidity Trend Analysis")
    plt.legend()
    plt.savefig("outputs/graphs/humidity_trend_analysis.png")
    plt.show()


if __name__ == "__main__":
    df = load_data()
    df = add_trend_lines(df)

    print("Generating trend analysis graphs...")

    plot_temperature_trend(df)
    plot_rainfall_trend(df)
    plot_humidity_trend(df)

    print("Trend analysis completed successfully!")