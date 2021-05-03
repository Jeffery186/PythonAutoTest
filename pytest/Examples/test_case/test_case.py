import pytest
import time
from selenium import webdriver
from page.login import LoginPage
from page.choice import ChoicePage
from config.yamlload import loadyaml

class TestCase:

    # 用例执行前要做的事情
    def setup_class(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.lp = LoginPage(cls.browser)
        cls.cp = ChoicePage(cls.browser)

    # 用例执行后要做的事情
    def teardown_class(cls) -> None:
        cls.browser.quit()

    # 用例 写test_ 一个test方法代表一条用例 如：登录
    @pytest.mark.parametrize('utxt', loadyaml('./data/login.yaml'))
    def test_01(self, utxt):
        self.lp.login(utxt['uname'], utxt['pwd'])
        time.sleep(3)

    def test_02(self):
        self.cp.search('')

if __name__ == '__main__':
    pytest.main(['-s', 'test_case.py'])
