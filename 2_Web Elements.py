from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.google.com')

search = driver.find_element_by_name('q')

search.send_keys('python')

time.sleep(3)

search.submit()
