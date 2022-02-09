from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox(executable_path = "C:\geckodriver-v0.30.0-win64\geckodriver")
browser.get('http://automationpractice.com/index.php')
browser.find_element_by_class_name("login").send_keys(Keys.ENTER)
time.sleep(5)
browser.find_element_by_id("email_create").send_keys("ushabm999@gmail.com")
browser.find_element_by_name("SubmitCreate").send_keys(Keys.ENTER)
time.sleep(5)
browser.find_element_by_name("submitAccount").send_keys(Keys.ENTER)
time.sleep(5)