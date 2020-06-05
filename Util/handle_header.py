# coding:utf-8
"""
1、通过read_json,读取所有json文件，
{
  "header": {
    "Content-Type": "application/json",
    "Accept": "application/json,*/*",
    "x-device-info": "1.0/nil/1/1.0"
  }
}
"""
from Util.handle_json import read_json, write_value


# 读取json文件，获取header
def get_header(header_key):
    data = read_json("../Config/header.json")
    return data[header_key]


# 写入cookie
def write_cookie(data, cookie_key):
    new_data = read_json("../Config/cookie.json")
    new_data[cookie_key] = data
    write_value(new_data)


if __name__ == '__main__':
    print(get_header("header"))

