from selenium import webdriver
import time

class Tools:

    # 初始化函数 浏览器
    def __init__(self,browser):
        self.browser=browser

    # 访问
    def open(self,url):
        self.browser.get(url)

    # 元素定位
    def locator(self,loc):
        return self.browser.find_element(*loc)

    # 输入
    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def on_click(self,loc):
        self.locator(loc).click()

    # 等待
    def wait(self):
        time.sleep(3)

    # 关闭
    def quit(self):
        self.browser.quit()
