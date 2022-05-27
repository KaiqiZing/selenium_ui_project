# coding=utf-8
# 对register_code进一步封装
import string
import ddddocr
from selenium import webdriver
import time
import random
from PIL import Image

class RegisterFunction:

    def __init__(self, url, i):
        """
        初始化浏览器，并创建可选择浏览器类型
        :param url:
        :param i:
        """
        self.driver = self.get_driver(url, i)

    #浏览器初始化，拓展多个浏览器种类的适用范围
    def get_driver(self, url, i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()

        driver.get(url)
        driver.maximize_window()
        time.sleep(2)

    # 输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self, key):
        pass
    # 获取随机数
    def get_range_user(self):

        user_info = random.randint(0,9999)
        test_user_info = string.ascii_letters
        return test_user_info
    # def create_string_number(n):
    #     """生成一串指定位数的字符+数组混合的字符串"""
    #     m = random.randint(1, n)
    #     a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    #     b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    #     return ''.join(random.sample(list(a + b), n))

    # 获取图片并解析
    # 获取图片并处理保存
    def readimage(self, save_path):

        self.driver.save_screenshot(save_path)  # 保存截图后的位置
        code_element = self.driver.find_element_by_id("getcode_num") # 获取到验证码的id

        #处理截图
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        open_image = Image.open("save_path")
        crop_image = open_image.crop((left,top,right,height)) #截取验证码图片
        crop_image.save("save_path")  # 保存截取验证码后的图片

        code_image_ocr = ddddocr.DdddOcr(old=True)  # 开启old使用旧模型准确率更高，也可以关闭
        with open("save_path", "rb") as f:
            image_bytes = f.read()
        code_image = code_image_ocr.classification(image_bytes)
        return code_image
    # 主程序
    def run_main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info+"@163.com"
        file_name = "save_path"

        self.send_user_info("user_email",user_email)
        self.send_user_info("user_name", user_name_info)
        self.send_user_info("passwprd", "111111")
        self.send_user_info("code_text", "111111")
        self.get_user_element("register_button").click()
        code_error = self.get_user_element("code_text_error")
        if code_error ==None:
            print("注册成功")
        else:
            self.driver.save_screenshot("save_error_path")
        # # 发送验证码
        # result_image = readimage(file_name)
        # get_element("captcha_code").send_keys(result_image)
        # get_element("register-btn").click()
        # driver.close()


if __name__ == '__main__':
    for i in range(3):
        register_fucntion = RegisterFunction('http://www.5itest.cn/register',i)
        register_fucntion.run_main()

