# utils/storage.py

import json
import csv
import pandas as pd
import os


# Create data folder automatically
os.makedirs("data", exist_ok=True)


def save_json(data, filename="data/scraped_data.json"):

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def save_csv(data, filename="data/scraped_data.csv"):

    if not data:
        return

    # Get all unique keys from all dictionaries
    keys = set()

    for item in data:
        keys.update(item.keys())

    keys = list(keys)

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=keys,
            extrasaction="ignore"
        )

        writer.writeheader()
        writer.writerows(data)


def save_excel(data, filename="data/scraped_data.xlsx"):

    df = pd.DataFrame(data)

    df.to_excel(filename, index=False)