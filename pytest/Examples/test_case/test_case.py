import pytest
from selenium import webdriver
from page.login import LoginPage
from page.choice import ChoicePage

# 必须要继承unittest.TestCase
class TestCase

    # 用例执行前要做的事情
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser=webdriver.Chrome()
        cls.lp=LoginPage(cls.browser)
        cls.cp=ChoicePage(cls.browser)

    # 用例执行后要做的事情
    @classmethod
    def tearDownClass(cls) -> None:

    # 用例 写test_ 一个test方法代表一条用例 如：登录
    def test_01(self):

    def test_02(self):