# encoding: utf-8
#!/usr/bin/env python3
from datetime import datetime
import csv
import pandas as pd


def schedule_2_json():
    df = pd.read_csv("input.csv", encoding="utf-8")
    df = df.loc[df["aprovada"].isin(["ok"])]
    selected_headers = [
        "Data e Hora",
        "Título da Palestra:",
        "Duração (minutos)",
        "Link",
    ]
    df = df[selected_headers]
    df.columns = ["datetime", "title", "duration", "link"]
    df["datetime"] = df["datetime"].apply(lambda x: convert_date(x))
    df["embed_link"] = df["link"].apply(lambda x: convert_to_embed(x))

    df.to_json("output.json", orient="records", force_ascii=False)


def convert_date(date_str):
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
        return date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4]
    except Exception:
        return date_str


def convert_to_embed(url):
    return url.replace("watch?v=", "embed/")


if __name__ == "__main__":
    schedule_2_json()
