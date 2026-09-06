import csv
import random
from datetime import datetime, timedelta
import pandas as pd

# Generating Time Series Synthetic Data
# every day per hour traffic data for 30 days starting from 2026-01-01 00:00:00 to
#     2026-01-30 23:00:00
random.seed(42)

start = datetime(2026, 1, 1, 0, 0, 0)
hours = 24 * 30
rows = []

for i in range(hours):
    ts = start + timedelta(hours=i)
    weekday = ts.weekday()

    base = 120
    if weekday >= 5:
        base = 80

    hour = ts.hour
    if 8 <= hour <= 11:
        base += 60
    elif 18 <= hour <= 21:
        base += 40
    elif 0 <= hour <= 5:
        base -= 30

    visits = max(0, int(random.gauss(base, 15)))

    rows.append({
        "timestamp": ts.isoformat(),
        "visits": visits
    })

pd.DataFrame(rows).to_csv(r'D:\python_data_genaration_script\time_series_data\traffic_timeseries.csv', index=False)
print("Saved traffic_timeseries.csv")