#coding=utf-8
from page.register_page import RegisterPage
import sys
from util.get_code import GetCode
from log.user_log import UserLog

class RegisterHandle:
    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)
        get_user_Log = UserLog()
        self.logger = get_user_Log.get_log()


    def send_user_email(self, email):
        self.logger.info("输入邮箱值是"+email)
        self.register_p.get_email_element().send_keys(email)

    def send_user_name(self, username):
        self.logger.info("输入用户名是："+username)
        self.register_p.get_username_element().send_keys(username)

    def send_user_password(self, password):
        self.logger.info("输入密码是:"+ password)
        self.register_p.get_password_element()

    def send_user_code(self, file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)

    # 封装报错提示信息
    def get_user_text(self, info, user_info):
        try:
            if info == "user_email_error":
                text = self.register_p.get_email_error_element().text

            elif info == "user_name_error":
                text = self.register_p.get_username_element().text

            elif info == "password_error":
                text = self.register_p.get_password_error_element().text

            else:

                text = self.register_p.get_code_error_element().text

        except:

            text = None

        return text


    # 点击注册按钮，获取文字西信息
    def register_button_click(self):
        self.register_p.get_button_element().click()

    def register_text_info(self):
        return self.register_p.get_button_element()