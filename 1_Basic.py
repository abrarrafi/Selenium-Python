from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')

# Web title, url and source code
print(driver.title)
print(driver.current_url)
print(driver.page_source)

# window maximize
driver.maximize_window()
