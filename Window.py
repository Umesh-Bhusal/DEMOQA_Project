
#Run this cmd   pip install selenium webdriver-manager first
from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from trio import current_time
import time
from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button
from webdriver_manager.chrome import ChromeDriverManager


# Initialize the ChromeDriver service
service = Service(ChromeDriverManager().install())

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to a specific URL
website_url=driver.get("https://demoqa.com/browser-windows")  # Replace with your desired URL
driver.maximize_window()

#Browser Window
driver.find_element(By.XPATH, "//button[@id='tabButton']").click()
time.sleep(4)

#New Window page
driver.find_element(By.XPATH, "//button[@id='windowButton']").click()
time.sleep(3)

#//button[@id='messageWindowButton']
driver.find_element(By.XPATH, "//button[@id='messageWindowButton']").click()
time.sleep(4)



