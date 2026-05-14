

from selenium.webdriver.common.by import By


def test_open_amazon(driver):
    driver.get("https://www.amazon.in")

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Laptop")

    assert "Amazon" in driver.title