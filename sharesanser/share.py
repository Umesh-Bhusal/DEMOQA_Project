
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
website_url=driver.get("https://www.sharesansar.com/company/nabil")  # Replace with your desired URL
driver.maximize_window()

#calculate the height of the page using javascripts
page_height=driver.execute_script("return document.body.scrollHeight")

#scroll down the page using the scripts
scroll_speed=1200

scroll_iterations=int(page_height/scroll_speed)

#loop to perform the iterations:
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(4)

driver.find_element(By.XPATH, "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div[2]/div/div[1]/div[1]/ul/li[8]/a").click()
time.sleep(3)

# Loop to click the "Next" button 65 times
for _ in range(155):
   # try:
        # Find and click the "Next" button
        next_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div/div[8]/div/div/div[5]/a[2]")
        next_button.click()
        time.sleep(1)  # Pause to allow the page to load after each click
    # except Exception as e:
    #     print(f"Error clicking Next button: {e}")
    #     break