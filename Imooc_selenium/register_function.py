# coding=utf-8
import sys
import ddddocr
from selenium import webdriver
import time
import random
from PIL import Image
from base.find_element import FindElement


class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url, i)

    #获取driver并且打开url
    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:

            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver
    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    
    #定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    #获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
        return user_info

    #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img.save(file_name)

        # 引入第三方包解析验证码
        oct = ddddocr.DdddOcr(old=True)
        with open(file_name, "rb") as f:
            image = f.read()
        res = oct.classification(image)
        return res



    def main(self):
        # 用户名
        user_name_info = self.get_range_user()
        # 邮箱
        user_email = user_name_info+"@163.com"
        # 截图地址
        file_name = "/Volumes/DATAS2T/mooc_images/est.png"
        code_text = self.get_code_image(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_info)
        self.send_user_info('password',"111111")
        self.send_user_info('code_text',code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print("注册成功")
        else:
            # 错误截图地址
            self.driver.save_screenshot("/Volumes/DATAS2T/mooc_images/error_element/test_error.png")
        time.sleep(5)
        self.driver.close()
    
if __name__ == '__main__':
    register_function = RegisterFunction('http://www.5itest.cn/register',1)
    register_function.main()