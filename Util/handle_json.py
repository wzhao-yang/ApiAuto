# coding=utf-8
import json
import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)


def read_json(file_name=None):
    if file_name == None:
        file_path = "../Config/user_data.json"
    else:
        file_path = file_name
    # with open("../Config/code_message.json", encoding='utf-8') as f:
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    return data


# 获取json文件中得key值
def get_value(key, file_name=None):
    data = read_json(file_name)
    return data.get(key)
    # return data[key]


# 定义获取cookie.json文件，便于查看，放在了handle_cookie.py文件内了

# 写入cookie或者写入其他数据
def write_value(data):
    data_value = json.dumps(data)
    with open("../Config/cookie.json", "w") as f:
        f.write(data_value)


if __name__ == '__main__':
    data = {"cookies": "aaaaa"}
    write_value(data)
    # print(get_value("api/v1/order/myOrderList?", "../Config/result.json"))
    music_dict_list = get_value("api/v1/goods/getGoodsDetail/18404?", "../Config/result.json")[0]
    # music_dict_list = get_value("api/v1/order/myOrderList?", "../Config/result.json")[0]
    print(music_dict_list)
    print(type(music_dict_list))
