import pandas as pd

def load_data():
    df = pd.read_csv("data/raw/climate_data.csv")
    print("Data loaded successfully")
    return df


def clean_data(df):
    # FIXED DATE PARSING
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)

    # Sort
    df = df.sort_values(by='date')

    # Missing values check
    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    # Fill missing values
    df = df.fillna(method='ffill')

    # Remove duplicates
    df = df.drop_duplicates()

    print("\nData cleaned successfully!")
    return df


def save_cleaned_data(df):
    df.to_csv("data/processed/cleaned_climate_data.csv", index=False)
    print("Cleaned data saved!")


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    save_cleaned_data(df)

    print("\nPreview:")
    print(df.head())