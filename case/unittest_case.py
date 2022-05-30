# coding=utf-8
import unittest
class FirstCase01(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("所有case的前置")
    # @classmethod
    # def tearDownClass(cls):
    #     print("所有case的后置条件")

    def setUp(self) -> None:
        print("这个是case的前置条件")

    def tearDown(self) -> None:
        print("这是case的后置条件")

    @unittest.skip("不执行第一条")
    def testfirst01(self):
        print("这是第一条case")

    def testfirst02(self):
        print("这是第二条case")

    def testfirst03(self):
        print("这是第三条case")

    def testfirst04(self):
        print("这是第四条case")
if __name__ == '__main__':

    """注意：默认情况下 addTest()不会起作用，pycharm中，引入了unittest 模块，会默认按照 unittest 模式执行。需要将 unittest 模式转换成普通模式
      Pycharm——View——appearance——toolbar——左上角工具条找到执行脚本的昵称——添加一个python新配置——配置命名，选择要执行的文件。之后就可在左上角工具条切换用刚才配置的方式运行
      参考：https://blog.csdn.net/sinat_34937826/article/details/108147722"""
    # 方法一： 逐个添加
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase01('testfirst02'))
    # suite.addTest(FirstCase01('testfirst03'))
    # unittest.TextTestRunner().run(suite)

    # 方法2 字符串嵌套列表--推荐使用
    suite = unittest.TestSuite()
    # 无效方法
    # suite.addTest([FirstCase01('testfirst02'),FirstCase01('testfirst04')])
    # 有效方法
    suite.addTests([FirstCase01('testfirst02'),FirstCase01('testfirst04')])
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
"""
1、注意区分addTest and addTests的区别；
2、verbosity 参数可以控制输出的错误报告详细程度，默认是1，则不输出，设为2输出详情数据
"""