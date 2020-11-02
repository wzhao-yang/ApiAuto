# coding:utf8
# 导入handle_excel，拿到excel的数据
from __future__ import unicode_literals

import ast
import json
import os
import sys

from Base.base_request import request
from Util.handle_cookie import get_cookie_value
from Util.handle_header import get_header
from Util.handle_excel import excel_data
from Util.handle_send_email import SendEmail
from Util.codition_data import get_data
from Util.handle_init import handle_ini
from Util.handle_result import handle_result, handle_result_json, get_result_json, get_value

# 执行测试用例
class RunMain:
    def __init__(self):
        self.sen_Email = SendEmail()

    def run_case(self):
        rows = excel_data.get_rows()  # 获取excel中所有行数
        for i in range(rows):  # 循环遍历rows
            pass_count = []  # 通过
            fail_count = []  # 失败
            cookie = None
            get_cookie =None
            header =None
            depend_data = None
            # header = handle_ini.get_value("header") # 不从配置文件中拿header
            # headers = eval(header)
            # headers = json.loads(header)
            # headers = ast.literal_eval(header)
            data = excel_data.get_rows_value(i + 2)  # 获取excel中得行
            case_id = excel_data.get_cell_value(i + 2, 1)  # 获取case_id
            is_run = data[2]
            if is_run == 'yes':
                print(case_id + '--------------->第{}个执行完毕'.format(i + 1))
                # method = handle_ini.get_value('method')
                is_depend = data[3]
                # data1 = json.loads(data7)
                # if is_depend:
                #     depend_data = get_data(is_depend)  # 获取依赖数据
                #     print(depend_data)
                url = data[4]  # 获取URL
                method = data[5]  # 获取method名
                data1 = data[6]  # 获取请求数据
                excepect_method = data[8]  # 预期执行判断方法
                excepect_result = data[9]  # 预期结果
                cookie_method = data[7]  # 是否需要携带cookie
                is_header = data[12]  # 获取是否需要携带header
                if cookie_method == 'yes':
                    cookie = get_cookie_value("app")
                # 获取登录成功后得cookie值
                if cookie_method == 'write':
                    get_cookie = {"is_cookie": "app"}
                if is_header == 'yes':
                    header = get_header("header")
                res = request.run_main(method, url, data1, header, cookie, get_cookie)
                # print(res)
                code = (res['resultCode'])
                message = res['errMsg']
                if excepect_method == 'resultCode_errMsg':
                    config_message = handle_result(url, code)
                    if message == config_message:
                        excel_data.excel_write_data(i + 2, 11, "测试通过")
                        pass_count.append(i)  # 统计测试成功得case
                        # print("测试通过------>", pass_count.append(i))  # 统计测试成功得case
                        print(case_id, "case测试通过", res)
                    else:
                        excel_data.excel_write_data(i + 2, 11, "测试失败")
                        excel_data.excel_write_data(i + 2, 12, json.dumps(res))  # 失败得case，数据写入excel中
                        print("测试失败------>", fail_count.append(i))  # 测试失败case
                        print(case_id, "case测试失败", res)
                if excepect_method == 'errMsg':
                    if excepect_result == code:
                        excel_data.excel_write_data(i + 2, 11, "测试通过")
                        pass_count.append(i)  # 统计测试成功得case
                        # print(code, "-----errMsg")
                        print(case_id, "case测试通过", res)
                    else:
                        excel_data.excel_write_data(i + 2, 11, "测试失败")
                        # 失败得case，数据写入excel中,注意res对象利用json.dumps(ensure_ascii=False)，不知直接存入
                        excel_data.excel_write_data(i + 2, 12, json.dumps(res, ensure_ascii=False))
                        fail_count.append(i)  # 测试失败case
                        print(case_id, "case测试失败", res)
                if excepect_method == 'json':
                    if code == 2000:
                        # status_str = "content"
                        # 拿result.json文件中key相对应得预期结果
                        excepect_result = get_value(url, "../Config/result.json")[0]

                    else:
                        # status_str = 'content'
                        excepect_result = get_value(url, "../Config/result.json")[0]
                    # excepect_result = get_result_json(url, status_str)
                    # result = handle_result_json(res['content'], excepect_result)
                    # response比对结果
                    result = handle_result_json(res, excepect_result)
                    print(res)
                    # print(type(excepect_result))
                    if result:
                        excel_data.excel_write_data(i + 2, 11, "测试通过")
                        pass_count.append(i)  # 统计测试成功得case
                        print(case_id, "case测试通过", res)
                    else:
                        excel_data.excel_write_data(i + 2, 11, "测试失败")
                        excel_data.excel_write_data(i + 2, 12, json.dumps(res, ensure_ascii=False))
                        fail_count.append(i)  # 测试失败case
                        print(case_id, "case测试失败", res)
            # print(len(pass_count))  # 打印通过了多少
            # print(len(fail_count))  # 打印失败了多少
            # self.sen_Email.send_main(pass_count, fail_count)


if __name__ == "__main__":
    run = RunMain()
    run.run_case()
