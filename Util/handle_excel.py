# coding:utf8
import os
import sys

import openpyxl

base_path = os.getcwd()
sys.path.append(base_path)
#  整个对象 open_excel
open_excel = openpyxl.load_workbook("../Case/ApiAuto.xlsx")  # 首先对这个对象进行获取load本工程下得excel数据
# open_excel = openpyxl.load_workbook(base_path+"/Case/ApiAuto.xlsx")  # 首先对这个对象进行获取load本工程下得excel数据
sheet_name = open_excel.sheetnames  # 获取整个excel下得sheet页得内容
excel_value = open_excel[sheet_name[0]]  # 获取第[0]个sheet页下所有数据
print(excel_value)
print(base_path)
print(excel_value.cell(1, 3))
print(excel_value.cell(1, 3).value)  # 利用cell获取坐标下数据，第1行，第3列
print(excel_value.max_row)  # 利用max_row获取excel中有数据得行数,

'''
底层，获取数据得阀值
min_row = MinMax(min=1, max=1000000, expected_type=int)
max_row = MinMax(min=1, max=1000000, expected_type=int)
min_col = MinMax(min=1, max=16384, expected_type=int)
max_col = MinMax(min=1, max=16384, expected_type=int)
'''

