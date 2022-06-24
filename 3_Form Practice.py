from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="RESULT_TextField-1"]').send_keys("Rafi")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-2"]').send_keys("Abrar")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-3"]').send_keys("01709683060")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-4"]').send_keys("Bangladesh")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-5"]').send_keys("Dhaka")
driver.find_element_by_xpath('//*[@id="RESULT_TextField-6"]').send_keys("abrarrafi174@gmail.com")



# search.send_keys('python')
#
# time.sleep(3)
#
# search.submit()
