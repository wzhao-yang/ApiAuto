# coding:utf8
import os
import sys

import openpyxl

base_path = os.getcwd()
sys.path.append(base_path)


class HandExcel:

    # 加载excel
    def load_excel(self):
        open_excel = openpyxl.load_workbook("../Case/ApiAuto.xlsx")  # 首先对这个对象进行获取load本工程下得excel数据
        return open_excel

    # 加载所有sheet得内容
    def get_sheet_data(self, index=None):
        sheet_name = self.load_excel().sheetnames
        if index is None:
            index = 0
        data = self.load_excel()[sheet_name[index]]
        return data

    # 获取一个单元格得内容是由’行‘和‘列’决定
    def get_cell_value(self, row, cols):
        # get_sheet_data()使用默认值0
        data = self.get_sheet_data().cell(row=row, column=cols).value
        return data

    # 获取sheet页中得case行数
    def get_rows(self):
        row = self.get_sheet_data().max_row
        return row

    # 某一行得内容得list
    def get_rows_value(self, row):
        row_list = []
        for i in self.get_sheet_data()[row]:
            row_list.append(i.value)
        return row_list


if __name__ == "__main__":
    handle = HandExcel()
    print(handle.get_cell_value(2, 5))
    print(handle.get_rows_value(2))  # 打印第2行内所有内容
