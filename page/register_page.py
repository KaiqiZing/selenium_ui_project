# coding=utf-8
from base.find_element import FindElement
class RegisterPage:
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取元素信息
    def get_email_element(self):
        return self.fd.get_element("user_email")  # self.driver.find_element_by_id(register_email)

    def get_username_element(self):
        return self.fd.get_element("user_name")

    def get_password_element(self):
        return self.fd.get_element("password")

    def get_code_element(self):
        return self.fd.get_element("code_text")

    # 操作类元素
    def get_button_element(self):
        return self.fd.get_element("register_button")

    # 获取报错文字信息
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")

    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")

    def get_password_error_element(self):
        return self.fd.get_element("password_error")

    def get_code_error_element(self):
        return self.fd.get_element("code_text_error")
