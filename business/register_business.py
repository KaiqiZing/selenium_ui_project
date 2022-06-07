# coding=utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.register_h = RegisterHandle(self.driver)

    # 执行基类，执行注册页面完整操作
    def user_base(self, email, name, password, file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.register_button_click()

    # 获取注册页面点击按钮的提示信息是否存在
    def register_success(self):

        if self.register_h.register_text_info() == None:
            return True
        else:
            return False

    def login_email_error(self, email, name, password, file_name):

        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("email_error", "请输入有效的电子邮件地址") == None:
            return True
        else:
            return False


    # ddt 数据驱动使用函数,Notice:该方法必须放在user_base下方，不然无法执行
    # def register_function(self, email, username, password, code, assertCode, assertText):
    #     self.user_base(email, username, password, code)
    #     if self.register_h.get_user_text(assertCode, assertText) == None:
    #         # print("邮箱检验不成功")
    #         return True
    #     else:
    #         return False

    def register_function(self, email, username, password, file_name, assertCode, assertText):
        self.user_base(email, username, password, file_name)
        if self.register_h.get_user_text(assertCode, assertText) == None:
            # print("邮箱检验不成功")
            return True
        else:
            return False


    def login_name_error(self, email, name, password, file_name):

        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text('user_name_error', "字符长度必须大于等于4，一个中文字算2个字符") == None:
            # print("用户名检验不成功")
            return True
        else:
            return False

    def login_password_error(self, email, name, password, file_name):

        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text('password_error', "最少需要输入 5 个字符") == None:
            # print("密码检验不成功")
            return True
        else:
            return False


    def login_code_error(self, email, name, password, file_name):

        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text('code_text_error', "验证码错误") == None:
            # print("验证码检验不成功")
            return True
        else:
            return False
