from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup Edge WebDriver
service = Service(EdgeDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://www.example.com")
time.sleep(2)

# Locate an element by ID and print its text
element = driver.find_element(By.ID, "elementID")
print(element.text)

# Locate an input field by name and send keys to it
input_field = driver.find_element(By.NAME, "inputFieldName")
input_field.send_keys("Hello, World!")
input_field.send_keys(Keys.RETURN)

time.sleep(3)

# Close the browser
driver.quit()