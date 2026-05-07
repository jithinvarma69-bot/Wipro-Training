from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_homepage():
    driver = webdriver.Edge(executable_path="C:/path/to/your/msedgedriver.exe")  # Specify path to Edge WebDriver

    try:
        driver.get("https://www.google.com")

        assert "Google" in driver.title

        search_box = driver.find_element(By.NAME, "q")

        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)

        assert "Selenium Python" in driver.title

    finally:
        driver.quit()