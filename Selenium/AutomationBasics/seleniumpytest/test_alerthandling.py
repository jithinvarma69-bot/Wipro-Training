import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_simple_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert"
    alert.accept()

    result = driver.find_element(By.ID, "result").text
    assert result == "You successfully clicked an alert"


def test_confirm_alert_accept(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    alert = driver.switch_to.alert
    assert "I am a JS Confirm" in alert.text
    alert.accept()

    result = driver.find_element(By.ID, "result").text
    assert result == "You clicked: Ok"


def test_confirm_alert_dismiss(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    alert = driver.switch_to.alert
    alert.dismiss()

    result = driver.find_element(By.ID, "result").text
    assert result == "You clicked: Cancel"


def test_prompt_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

    alert = driver.switch_to.alert
    alert.send_keys("Hello Alert")
    alert.accept()

    result = driver.find_element(By.ID, "result").text
    assert result == "You entered: Hello Alert"


def test_alert_absence_handling(driver):
    driver.get("https://the-internet.herokuapp.com/")

    with pytest.raises(NoAlertPresentException):
        driver.switch_to.alert.accept()