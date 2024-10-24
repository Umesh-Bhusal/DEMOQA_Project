
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
website_url=driver.get("https://demoqa.com/automation-practice-form")  # Replace with your desired URL
driver.maximize_window()

# Username-----> First Name <-----------
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("umesh")

#usernale ----------> Last Name <---------

driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Bhusal")

#---------> Email <----------
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("anishbhusal30@gmail.com")

#---------> Gender (radio button) <---------
driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
#------> user mobile number <----------
driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("9821902575")

#---------->Date of birth<-----------------
driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[4]").click()


#---------->subject<-----------------------------

# driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div[2]/div/div/div[1]").send_keys("QA")
# time.sleep(3)

#---------->Hobbies<-----------------------
sports_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
reading_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']")
music_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3']")

# Select all checkboxes
sports_checkbox.click()
reading_checkbox.click()
music_checkbox.click()

# #---------->Upload Picture<------------------
driver.find_element(By.XPATH, "//input[@id='uploadPicture']").send_keys("/home/umesh/Desktop/fintech doc/u.JPG")


#----------->Current address<--------------------
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("maitidevi, kathmandu")



#------------->State and city<----------------------------


#--------------->dropdown<-------------------------------


#----------->submit button<-----------------------
driver.find_element(By.XPATH, "//button[@id='submit']").click()

