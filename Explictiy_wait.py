#Run this cmd   pip install selenium webdriver-manager first
from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from trio import current_time
import time
from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button
from webdriver_manager.chrome import ChromeDriverManager


# Initialize the ChromeDriver service
service = Service(ChromeDriverManager().install())

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service)

mywait=WebDriverWait(driver,10)


website_url=driver.get("https://www.google.com/")  # Replace with your desired URL
driver.maximize_window()


searchbox= driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

searclink=mywait.until(EC.presence_of_element_to_be_clickable()

# time.sleep(3)

sele= driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")
sele.click()
# time.sleep(4)