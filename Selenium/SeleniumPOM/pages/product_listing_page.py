from selenium.webdriver.common.by import By


class ProductListingPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_links = (By.CSS_SELECTOR, "h2.a-size-mini a.a-link-normal")

    def click_first_product(self):
        products = self.driver.find_elements(*self.product_links)
        if products:
            products[0].click()