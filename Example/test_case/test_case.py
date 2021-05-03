import unittest
import time
from selenium import webdriver
from page.login import LoginPage
from page.choice import ChoicePage

from ddt import ddt, file_data


@ddt
# 必须要继承unittest.TestCase
class TestCase(unittest.TestCase):

    # 用例执行前要做的事情
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.lp = LoginPage(cls.browser)
        cls.cp = ChoicePage(cls.browser)

    # 用例执行后要做的事情 关闭浏览器
    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    # ..相对路径 ../当前文件
    @file_data('../data/login.yaml')
    # 用例 写test_ 一个test方法代表一条用例 如：登录
    def test_01(self, uname, pwd):
        self.lp.login(uname, pwd)

    time.sleep(3)  # 等待3秒

    def test_02(self):
        self.cp.search('')


# 测试这个过程
if __name__ == '__main__':
    unittest.main()
