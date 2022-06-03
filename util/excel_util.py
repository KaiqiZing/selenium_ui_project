# coding=utf-8
"""
主要读取和写入Excel data
"""
import time

import xlrd
from xlutils import copy

class ExcelUtil:

    def __init__(self, excel_path=None, index=None):
        """
        :param excel_path:具体文件路径
        :param index: 读取指定的sheet
        """

        if excel_path == None:
            self.excel_path = ""
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0

        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

        # 获取Excel数据，按照每行一个list添加到大list
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取到excel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows > 1:
            return rows
        return None
    # 获取到Excel单元格数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None



    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)
        time.sleep(1)

if __name__ == '__main__':
    ex = ExcelUtil("/Users/kaiqi/PycharmProjects/selenium_ui_project/config/casedata.xls")
    # print(ex.get_col_value(1,2))
    print(ex.get_data())






