# coding=utf-8
from selenium import webdriver
import time
import pytesseract
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import ddddocr
#未封装代码前的一些操作

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(3)
# 获取到页面的文字元素
print(EC.title_contains("注册"))

email_element = driver.find_element_by_id("register_email")
email_element.send_keys("hello")
driver.find_element_by_id("captcha_code").send_keys("test")


# 验证码处理

driver.save_screenshot("")  # 保存截图后的位置
code_element = driver.find_element_by_id("getcode_num") # 获取到验证码的id
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
open_image = Image.open("/Volumes/DATAS2T/mooc_images/test.png")
crop_image = open_image.crop((left,top,right,height)) #截取验证码图片
crop_image.save("/Volumes/DATAS2T/mooc_images/test.png")  # 保存截取验证码后的图片


# 处理截图保存后的图片，注意电脑分辨率会导致截取图片出错，在这里我们使用第三方AI工具来处理验证码

code_image_ocr = ddddocr.DdddOcr(old=True)  # 开启old使用旧模型准确率更高，也可以关闭
with open("/Volumes/DATAS2T/mooc_images/test.png", "rb") as f:
    image_bytes = f.read()
res = code_image_ocr.classification(image_bytes)
print(res)
