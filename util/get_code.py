from PIL import Image
import time
import ddddocr
class GetCode:
    """
    封装图片验证码接口，以备使用
    """

    def __init__(self, driver):
        self.driver = driver

    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img.save(file_name)
        time.sleep(1)

        # 引入第三方包解析验证码
    def code_online(self, file_name):
        # 获取图片地址
        self.get_code_image(file_name)
        # 引入第三方解析包
        oct = ddddocr.DdddOcr(old=True)
        with open(file_name, "rb") as f:
            image = f.read()
        code = oct.classification(image)
        return code