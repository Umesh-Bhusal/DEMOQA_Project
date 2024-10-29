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

website_url="https://merolagani.com/"

#open the website as:
driver.get(website_url)
time.sleep(3)

#maximize the windows size:
driver.maximize_window()
time.sleep(3)
market=driver.find_element(By.XPATH,"//a[normalize-space()='Market']")
market.click()
time.sleep(3)
visible_text=driver.find_element(By.LINK_TEXT,"Live Trading")
visible_text.click()
time.sleep(7)
#close the driver instance
driver.quit()