import json


def read_json():
    with open("../Config/user_data.json") as f:
        data = json.load(f)
    return data


def get_value(key):
    data = read_json()
    return data[key]


if __name__ == '__main__':
    data = read_json()
    print(data)
