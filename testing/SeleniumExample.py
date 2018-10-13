from selenium import webdriver

wd = webdriver.Chrome()

wd.get('http://www.google.com')
wd.find_element_by_id('lst-ib').send_keys("test search")
wd.find_element_by_name('btkK').click()
