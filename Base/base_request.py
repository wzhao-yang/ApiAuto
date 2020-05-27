# coding:utf-8
import json
import os
import sys

import requests
from Util.handle_init import handle_ini
from Util.handle_json import get_value
base_path = os.getcwd()
sys.path.append(base_path)


class BaseRequest:

    # 发送post请求
    def send_post(self, url, data):
        res = requests.post(url=url, data=data)
        return res.json()

    # 发送get请求
    def send_get(self, url, data):
        res = requests.get(url=url, params=data).text
        return res

    # 执行方法，传递method、url、data参数
    def run_main(self, method, url, data):
        # return get_value("resultCode")
        base_url = handle_ini.get_value("host")
        if 'http' not in url:
            url = base_url + url
        # print(url)

        if method == 'get':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)

        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res


request = BaseRequest()


if __name__ == '__main__':
    request = BaseRequest()
    # request.run_main('get', 'http://www.baidu.com', "{'username':'11111'}")
    # request.run_main('get', 'logina', "{'username':'11111'}")
