# encoding: utf-8
#!/usr/bin/env python3
from datetime import datetime
import csv
import pandas as pd


def schedule_2_json():
    df = pd.read_csv("input.csv", encoding="utf-8")
    df = df.loc[df["aprovada"].isin(["ok"])]
    selected_headers = [
        "Carimbo de data/hora",
        "Título da Palestra:",
        "Duração (minutos)",
        "Link",
    ]
    df = df[selected_headers]
    df.columns = ["datetime", "title", "duration", "link"]
    df["datetime"] = df["datetime"].apply(lambda x: convert_date(x))

    df.to_json("output.json", orient="records", force_ascii=False)


def convert_date(date_str):
    date = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
    return str(date)


if __name__ == "__main__":
    schedule_2_json()
