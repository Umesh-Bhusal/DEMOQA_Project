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
website_url=driver.get("https://opensource-demo.orangehrmlive.com/")# Replace with your desired URL
time.sleep(4)
driver.maximize_window()

# Login Page of OrangeHRM

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(4)

#Admin Page
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()

# driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
time.sleep(4)

#PIM

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
time.sleep(4)

# element= driver.find_element(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item']")
# drp = Select(element)
# drp.select_by_index(2)
# driver.find_element(By.XPATH, "//li[@class='--active oxd-topbar-body-nav-tab --parent --visited']//li[2]").click()

# time.sleep(3)





# driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
# alert=driver.switch_to.alert
# #--close the alert
# alert.accept()

# Dashboard Homepage admin
# driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
# driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
# time.sleep(6)
