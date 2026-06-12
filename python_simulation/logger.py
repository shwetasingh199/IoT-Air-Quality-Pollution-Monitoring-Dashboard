import pandas as pd
import os

LOG_FILE = "data/sensor_logs.csv"

def save_record(record):

    df = pd.DataFrame([record])

    if not os.path.exists(LOG_FILE):

        df.to_csv(
            LOG_FILE,
            index=False
        )

    else:

        df.to_csv(
            LOG_FILE,
            mode="a",
            header=False,
            index=False
        )