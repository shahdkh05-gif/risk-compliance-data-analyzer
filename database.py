import sqlite3
from pathlib import Path

import pandas as pd


def save_to_database(data: pd.DataFrame, db_path: Path):
    with sqlite3.connect(db_path) as connection:
        data.to_sql("processed_incidents", connection, if_exists="replace", index=False)
