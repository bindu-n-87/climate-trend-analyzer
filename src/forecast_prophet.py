import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

def load_data():
    df = pd.read_csv("data/processed/cleaned_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df


def prepare_data(df):
    # Prophet requires specific column names
    prophet_df = df[['date', 'temperature']].rename(
        columns={'date': 'ds', 'temperature': 'y'}
    )
    return prophet_df


def train_model(prophet_df):
    model = Prophet(
        yearly_seasonality=True,
        daily_seasonality=False,
        weekly_seasonality=False
    )

    model.fit(prophet_df)
    print("Prophet model trained successfully!")
    return model


def forecast(model, periods=365):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


def plot_forecast(model, forecast):
    fig = model.plot(forecast)
    plt.title("Climate Forecast using Prophet (Seasonal Model)")
    plt.savefig("outputs/graphs/prophet_forecast.png")
    plt.show()

    fig2 = model.plot_components(forecast)
    plt.savefig("outputs/graphs/prophet_components.png")
    plt.show()


if __name__ == "__main__":
    df = load_data()
    prophet_df = prepare_data(df)

    model = train_model(prophet_df)

    forecast_data = forecast(model)

    print(forecast_data[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())

    plot_forecast(model, forecast_data)