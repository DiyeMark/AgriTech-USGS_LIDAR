import json
import laspy
import pandas as pd


def read_csv(file_name: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        pass


def read_txt(file_name: str) -> list:
    try:
        with open(file_name, "r") as f:
            text_file = f.read().splitlines()
        return text_file
    except FileNotFoundError:
        pass


def read_json(file_name: str) -> dict:
    try:
        with open(file_name, 'r') as json_file:
            json_obj = json.load(json_file)
        return json_obj
    except FileNotFoundError:
        pass


def read_point_data(file_name: str):
    try:
        las = laspy.read(file_name)
        return las
    except FileNotFoundError:
        pass


def write_csv(df: pd.DataFrame, file_name: str):
    try:
        df.to_csv(file_name, index=False)
    except Exception:
        pass
