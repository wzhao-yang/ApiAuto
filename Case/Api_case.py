import json
import mock
import HTMLTestRunner
from Base.base_request import request

def read_json():
    with open("../Config/user_data.json") as f:
        data = json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]

if __name__ == '__main__':
    read_json()