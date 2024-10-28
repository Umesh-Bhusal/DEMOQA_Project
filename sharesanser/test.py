from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website_url = "https://www.sharesansar.com/"
driver.get(website_url)
time.sleep(3)

# Maximize the window
driver.maximize_window()
time.sleep(3)

# Enter "NABIL" in the search field and press Enter
search_box = driver.find_element(By.XPATH, "/html/body/div[2]/div/header/div[1]/div/div[1]/div/div/div[2]/form/div/div/div[1]/input")
search_box.send_keys("NABIL", Keys.RETURN)

# Optional delay to observe results before quitting
time.sleep(5)

# Quit the driver
