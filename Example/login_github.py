from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://github.com/login')
browser.find_element_by_name('login').send_keys('')
browser.find_element_by_name('password').send_keys('')
browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

browser.quit()
