# coding:utf8
# 导入handle_excel，拿到excel的数据
import os
import sys

import request

from Base.base_request import request
from Util.handle_excel import excel_data

base_path = os.getcwd()
sys.path.append(base_path)


# 执行测试用例
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()  # 获取excel中所有行数
        for i in range(rows):  # 循环遍历rows

            data = excel_data.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[4]
                url = data[3]
                data1 = data[5]

                res = request.run_main(method, url, data1)
                print(res)


if __name__ == "__main__":
    run = RunMain()
    run.run_case()
