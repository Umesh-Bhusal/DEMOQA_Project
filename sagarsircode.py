#Import necessary modules from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from trio import current_time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set up the chrome driver using webdriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desired url:

website_url="https://demoqa.com/alerts"

#open the website as:
driver.get(website_url)
time.sleep(3)

#maximize the windows size:
driver.maximize_window()
time.sleep(3)

#locate the alert button
click_me=driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
click_me.click()
time.sleep(5)

#-----switch to alert
alert=driver.switch_to.alert

#--close the alert
alert.accept()

#close the driver instance
driver.quit()
print("Alert message is execute successfully!!!!")