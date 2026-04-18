import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    df = load_data("data/raw/climate_data.csv")
    print(df.head())
    print(df.info())