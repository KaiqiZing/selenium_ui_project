# coding=utf-8
import pytesseract
from PIL import Image
import ddddocr
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()

def readimage(save_path):

    driver.save_screenshot(save_path)  # 保存截图后的位置
    code_element = driver.find_element_by_id("getcode_num") # 获取到验证码的id

    #处理截图
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    open_image = Image.open(save_path)
    crop_image = open_image.crop((left,top,right,height)) #截取验证码图片
    crop_image.save(save_path)  # 保存截取验证码后的图片

    code_image_ocr = ddddocr.DdddOcr(old=True)  # 开启old使用旧模型准确率更高，也可以关闭
    with open(save_path, "rb") as f:
        image_bytes = f.read()
    code_image = code_image_ocr.classification(image_bytes)
    return code_image
if __name__ == '__main__':
    result = readimage("D:/mooc_images/test.png")
    print(result)
