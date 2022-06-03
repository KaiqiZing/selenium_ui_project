# coding=utf-8
"""
数据驱动实现UI自动化
"""
import ddt
from selenium import webdriver
from util.excel_util import ExcelUtil
import os
from log.user_log import UserLog
import time
import unittest
from business.register_business import RegisterBusiness

#邮箱 用户名 密码 验证码 错误信息定位元素  错误提示信息
@ddt.ddt
class FirsrDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        time.sleep(1)

        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(1)
        for method_name, error in self._outcome.errors:
            #  封装报错截图：
            if error:
                case_name = self._testMethodName
                file_path = "/Users/kaiqi/PycharmProjects/selenium_ui_project/report/"+case_name+".png"
                self.driver.save_screenshot(file_path)
        self.driver.close()


    @ddt.data(
        ['12', 'Mushishi01', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        ['@qq.com', 'Mushishi01', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        ['12@qq.com', 'Mushishi01', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址']
    )

    @ddt.unpack
    # 数据驱动执行过程
    def test_register_case(self, email, username, password, code, assertCode, assertText):
        email_error = self.login.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(email_error, "测试失败")

if __name__ == '__main__':

    # 数据驱动执行方法
    unittest.main()


    # file_path = "/Users/kaiqi/PycharmProjects/selenium_ui_project/report/" + "first_case1.html"
    # f = open(file_path, "wb")
    # suite = unittest.TestSuite()
    # suite.addTest(FirsrDdtCase('test_register_case'))
    # unittest.TextTestRunner().run(suite)

