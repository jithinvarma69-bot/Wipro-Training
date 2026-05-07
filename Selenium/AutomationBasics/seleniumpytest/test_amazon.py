import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def open_amazon(driver):
    driver.get("https://www.amazon.in/")

    wait = WebDriverWait(driver, 20)

    # Handle possible location popup
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))).click()
    except:
        pass

    # Wait for search box properly (VISIBLE, not just present)
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    return search_box

def test_amazon_search(driver):
    search_box = open_amazon(driver)

    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 20)

    results = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")
        )
    )

    assert len(results) > 0


def test_amazon_product_click(driver):
    search_box = open_amazon(driver)

    search_box.send_keys("headphones")
    search_box.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 20)

    first_product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "h2 a"))
    )
    first_product.click()

    # Switch to new tab if opened
    driver.switch_to.window(driver.window_handles[-1])

    title = wait.until(
        EC.visibility_of_element_located((By.ID, "productTitle"))
    )

    assert title.text.strip() != ""