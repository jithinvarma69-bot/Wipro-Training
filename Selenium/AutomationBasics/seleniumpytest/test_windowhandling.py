import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_window_handling(driver):
    # Open initial page
    driver.get("https://example.com")
    original_window = driver.current_window_handle

    # Ensure only one window is open
    assert len(driver.window_handles) == 1

    # Open a new tab
    driver.switch_to.new_window(WindowTypes.TAB)
    driver.get("https://www.python.org")

    # Validate new tab opened
    assert len(driver.window_handles) == 2

    # Switch back to original window
    driver.switch_to.window(original_window)
    assert "Example Domain" in driver.title

    # Switch to second window
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    assert "Python" in driver.title

def test_multiple_windows(driver):
    driver.get("https://example.com")
    original_window = driver.current_window_handle

    # Open multiple windows
    for _ in range(2):
        driver.switch_to.new_window(WindowTypes.WINDOW)
        driver.get("https://www.wikipedia.org")

    assert len(driver.window_handles) == 3

    # Iterate through all windows
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        print(driver.title)

    # Close all except original
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            driver.close()

    driver.switch_to.window(original_window)
    assert len(driver.window_handles) == 1