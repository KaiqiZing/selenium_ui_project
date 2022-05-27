# coding=utf-8
import string
import ddddocr
from selenium import webdriver
import time
import random
from PIL import Image
driver = webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(2)

# 获取到element information
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取到随机数
def get_range_user():
    user_info = random.randint(0,9999)
    test_user_info = string.ascii_letters
    return test_user_info



def create_string_number(n):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))

# 获取图片并解析

def readimage(save_path):

    driver.save_screenshot(save_path)  # 保存截图后的位置
    code_element = driver.find_element_by_id("getcode_num") # 获取到验证码的id

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
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"@163.com"
    file_name = "save_path"
    driver_init()
    # 发送用户名
    get_element("register_email").send_keys(user_email)

    # 发送验证码
    result_image = readimage(file_name)
    get_element("captcha_code").send_keys(result_image)
    get_element("register-btn").click()
    driver.close()


run_main()

