from selenium.webdriver.common.by import By


class ProductDetailPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_title = (By.ID, "productTitle")

    def get_product_title(self):
        return self.driver.find_element(*self.product_title).text