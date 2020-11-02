# coding=utf-8

import json

from Base.base_request import request
from Util.codition_data import get_data
from Util.handle_cookie import get_cookie_value
from Util.handle_excel import excel_data
from Util.handle_header import get_header
from Util.handle_result import handle_result, handle_result_json, get_result_json, get_value


class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            data = excel_data.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == 'yes':
                is_depend = data[3]
                data1 = json.loads(data[7])
                if is_depend:
                    '''
                    获取依赖数据
                    '''
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    # print(depend_data)
                    data1[depend_key] = depend_data

                method = data[6]
                url = data[5]
                is_header = data[9]
                excepect_method = data[10]
                excepect_result = data[11]
                cookie_method = data[8]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie = {"is_cookie": "app"}
                if is_header == 'yes':
                    header = get_header()
                res = request.run_main(method, url, data1, cookie, get_cookie, header)
                # print(res)
                code = str(res['errorCode'])
                message = res['errorDesc']
                if excepect_method == 'resultCode_errMsg':
                    config_message = handle_result(url, code)
                    if message == config_message:
                        excel_data.excel_write_data(i + 2, 13, "通过")
                    else:
                        excel_data.excel_write_data(i + 2, 13, "失败")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))
                if excepect_method == 'errMsg':
                    if excepect_result == code:
                        excel_data.excel_write_data(i + 2, 14, "通过")
                    else:
                        excel_data.excel_write_data(i + 2, 13, "失败")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))
                if excepect_method == 'json':
                    if code == 2000:
                        # status_str = 'sucess'
                        excepect_result = get_value(url, "../Config/result.json")[0]
                    else:
                        # status_str = 'error'
                        excepect_result = get_value(url, "../Config/result.json")[0]
                    # excepect_result = get_result_json(url, status_str)
                    excepect_result = get_result_json(url, excepect_result)
                    result = handle_result_json(res, excepect_result)
                    if result:
                        excel_data.excel_write_data(i + 2, 13, "通过")
                    else:
                        excel_data.excel_write_data(i + 2, 13, "失败")
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res))


if __name__ == "__main__":
    run = RunMain()
    run.run_case()
