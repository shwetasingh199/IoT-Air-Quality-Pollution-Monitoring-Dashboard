import pandas as pd

df = pd.read_csv(
    "../data/sensor_logs.csv"
)

report = f"""
Total Records:
{len(df)}

Maximum AQI:
{df['aqi'].max()}

Average AQI:
{df['aqi'].mean()}
"""

with open(
    "../reports/summary.txt",
    "w"
) as f:

    f.write(report)