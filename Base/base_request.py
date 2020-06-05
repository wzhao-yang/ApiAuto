# coding:utf-8
import json
import os
import sys

import requests

from Util.handle_cookie import write_cookie
from Util.handle_init import handle_ini

base_path = os.getcwd()
sys.path.append(base_path)


class BaseRequest:
    # 发送post请求
    def send_post(self, url, data, header, cookie=None, get_cookie=None):
        response = requests.post(url=url, data=data, headers=header, cookies=cookie)
        if get_cookie is not None:
            # 如!=None,直接赋值{"is_cookie": "app"}
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    # 发送get请求
    def send_get(self, url, data, header=None, cookie=None, get_cookie=None):
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)
        if get_cookie is not None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])

        res = response.text
        return res

    # 执行方法，传递method、url、data参数
    def run_main(self, method, url, data, header=None, cookie=None, get_cookie=None):
        # 调用mock，直接返回json，key
        # return get_value("resultCode")
        base_url = handle_ini.get_value("host")
        if 'http' not in url:
            url = base_url + url
        # print(url)
        if method == 'get':
            res = self.send_get(url, data, header, cookie, get_cookie)
        else:
            res = self.send_post(url, data, header, cookie, get_cookie)
        # print(res)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res


request = BaseRequest()

if __name__ == '__main__':
    request = BaseRequest()
    # request.run_main('post', 'loain','sss')
    # request.run_main('get', 'logina', "{'username':'11111'}")
