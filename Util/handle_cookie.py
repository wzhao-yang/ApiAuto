# coding=utf-8

from Util.handle_json import read_json, write_value


def get_cookie_value(cookie_key):
    """

    :param cookie_key:
    :return: 获取cookie
    """
    data = read_json("../Config/cookie.json")
    return data[cookie_key]


def write_cookie(data, cookie_key):
    """
    :param data:
    :param cookie_key:
    :return: 写入cookie
    """
    data1 = read_json("../Config/cookie.json")
    data1[cookie_key] = data
    write_value(data1)


if __name__ == "__main__":
    data = {
        "aaaa": "1111111111111111"
    }
    print(write_cookie("23423423423423",'cookies'))
