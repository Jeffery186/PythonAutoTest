from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import Tools

class LoginPage(Tools):

    # 页面地址
    url='https://github.com/login'

    # 页面元素
    username=(By.NAME,'login')
    password=(By.NAME,'password')
    loginbtn=(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[12]')

    # 页面流程
    def login(self,usr,pwd):
        self.open(self.url)
        self.input(self.username,usr)
        self.input(self.password,pwd)
        self.on_click(self.loginbtn)

# 测试
'''
if __name__ == '__main__':
    browser=LoginPage(webdriver.Chrome())
    browser.login('','')
'''