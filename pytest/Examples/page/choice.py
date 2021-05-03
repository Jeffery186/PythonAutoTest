from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import Tools

class ChoicePage(Tools):
    # 页面地址
    url = 'http://www.baidu.com'

    # 页面元素
    search_input = (By.ID, 'kw')
    search_btn = (By.ID, 'su')

    # 流程
    def search(self, txt_search):
        self.open(self.url)
        self.input(self.search_input, txt_search)
        self.on_click(self.search_btn)
# 测试
if __name__ == '__main__':
    browser = ChoicePage(webdriver.Chrome())
    browser.search('test')