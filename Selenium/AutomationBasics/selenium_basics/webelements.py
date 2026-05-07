from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium WebElements")
search_box.send_keys(Keys.RETURN)

time.sleep(2)

results = driver.find_elements(By.CSS_SELECTOR, "h3")

for result in results[:5]:
    print(result.text)

driver.get("https://www.wikipedia.org")

input_box = driver.find_element(By.ID, "searchInput")
input_box.send_keys("Automation")
input_box.submit()

time.sleep(2)

title = driver.find_element(By.ID, "firstHeading")
print(title.text)

driver.quit()