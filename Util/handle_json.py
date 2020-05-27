# coding=utf-8
import json


def read_json():
    with open("../Config/user_data.json") as f:
        data = json.load(f)
    return data


def get_value(key):
    data = read_json()
    return data[key]
