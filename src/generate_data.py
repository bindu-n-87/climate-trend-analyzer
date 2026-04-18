import pandas as pd
import numpy as np

# Step 1: Create date range
dates = pd.date_range(start="2010-01-01", end="2022-12-31")

# Step 2: Set seed (important for reproducibility)
np.random.seed(42)

# Step 3: Simulate temperature (with seasonality)
temperature = (
    25 
    + 10 * np.sin(2 * np.pi * dates.dayofyear / 365)   # seasonal pattern
    + np.random.normal(0, 2, len(dates))               # random noise
)

# Step 4: Simulate rainfall
rainfall = (
    5 
    + 5 * np.sin(2 * np.pi * dates.dayofyear / 365 + 1)
    + np.random.normal(0, 1.5, len(dates))
)

# Step 5: Simulate humidity
humidity = (
    60 
    + 20 * np.sin(2 * np.pi * dates.dayofyear / 365 + 2)
    + np.random.normal(0, 5, len(dates))
)

# Step 6: Create DataFrame
df = pd.DataFrame({
    "date": dates,
    "temperature": temperature,
    "rainfall": rainfall,
    "humidity": humidity
})

# Step 7: Inject anomalies (extreme values)
for _ in range(20):
    idx = np.random.randint(0, len(df))
    df.loc[idx, "temperature"] += np.random.choice([10, -10])  # heatwave or coldwave

# Step 8: Save dataset
df.to_csv("data/raw/climate_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())
