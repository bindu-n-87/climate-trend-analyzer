import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def load_data():
    df = pd.read_csv("data/processed/cleaned_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

def prepare_data(df):
    # Convert dates to numeric format (important for ML)
    df['day_index'] = (df['date'] - df['date'].min()).dt.days
    return df

def train_model(df):
    X = df[['day_index']]
    y = df['temperature']

    model = LinearRegression()
    model.fit(X, y)

    print("Model trained successfully!")
    return model

def forecast_future(df, model, days=365):
    last_day = df['day_index'].max()

    future_days = np.arange(last_day, last_day + days).reshape(-1, 1)

    predictions = model.predict(future_days)

    future_dates = pd.date_range(
        start=df['date'].max(),
        periods=days
    )

    future_df = pd.DataFrame({
        "date": future_dates,
        "forecast_temp": predictions
    })

    return future_df

def plot_forecast(df, future_df):
    plt.figure(figsize=(12,5))

    plt.plot(df['date'], df['temperature'], label="Historical Data", alpha=0.6)

    plt.plot(future_df['date'], future_df['forecast_temp'], 
             color='orange', label="Forecast (Next 1 Year)")

    plt.title("Climate Temperature Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()

    plt.savefig("outputs/graphs/temperature_forecast.png")
    plt.show()

if __name__ == "__main__":
    df = load_data()
    df = prepare_data(df)

    model = train_model(df)

    future_df = forecast_future(df, model)

    print("\nFuture Prediction Sample:")
    print(future_df.head())

    plot_forecast(df, future_df)
