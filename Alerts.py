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
website_url=driver.get("https://demoqa.com/alerts")  # Replace with your desired URL
driver.maximize_window()

#Alertsbutton
driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
alert=driver.switch_to.alert
#--close the alert
alert.accept()
time.sleep(4)

#On button click, alert will appear after 5 seconds
driver.find_element(By.XPATH, "//button[@id='timerAlertButton']").click()
time.sleep(8)
alert=driver.switch_to.alert
alert.accept()


#On button click, confirm box will appear
driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
alert=driver.switch_to.alert
alert.accept()
time.sleep(3)

# #On button click, prompt box will appear
# driver.find_element(By.XPATH, "//button[@id='promtButton']").click()

#frames
driver.find_element(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-2']").click()
time.sleep(4)



