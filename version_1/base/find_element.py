# coding=utf-8
import sys
from version_1.util.read_ini import ReadIni
from version_1.log.userlog import UserLog

class FindElement:

    def __init__(self, driver):
        self.driver = driver
        get_user_log = UserLog()
        self.logger = get_user_log.get_log()

    def get_element(self, key):
        """
        从配置文件中获取指定数据
        :param key:
        :return:
        """

        read_ini = ReadIni()
        data = read_ini.get_value(key)
        # 数值分割
        by = data.split(">")[0]
        value = data.split(">")[1]
        self.logger.info("定位方式："+by+"---------->定位值："+value)
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_id(value)
            elif by == "className":
                return self.driver.find_element_by_id(value)
        except:
            return None


