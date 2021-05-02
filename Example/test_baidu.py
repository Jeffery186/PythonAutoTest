from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import Tools

browser=Tools(webdriver.Chrome())
browser.open("http://www.baidu.com")
browser.input((By.ID,'kw'),'test')