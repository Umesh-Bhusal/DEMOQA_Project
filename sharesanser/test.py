from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
driver.maximize_window()

share= driver.find_element(By.NAME, "q")
share.send_keys("sharesansar")
share.submit()

submit_share= driver.find_element(By.XPATH, "//a[@href='https://www.sharesansar.com/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='ShareSansar']")
submit_share.click()

insidesite = driver.find_element(By.XPATH,"//input[@id='company_search']")
insidesite.send_keys("Nabil")
insidesite.submit()
time.sleep(4)



# #######################################################################
#You can use both option  down or above both code work fine
##########################################################################








# website_url = "https://www.sharesansar.com/"
# driver.get(website_url)
# time.sleep(3)
#
# # Maximize the window
# driver.maximize_window()
# time.sleep(3)

# # Enter "NABIL" in the search field and press Enter
# search_box = driver.find_element(By.XPATH, "/html/body/div[2]/div/header/div[1]/div/div[1]/div/div/div[2]/form/div/div/div[1]/input")
# search_box.send_keys("NABIL", Keys.RETURN)
# # Optional delay to observe results before quitting
# time.sleep(5)

# Quit the driver





