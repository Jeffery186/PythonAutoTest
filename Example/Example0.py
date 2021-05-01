# open a new Firefox browser
# load the page at the given URL

from selenium import webdriver

brower = webdriver.Chrome()
brower.get('http://seleniumhq.org/')
