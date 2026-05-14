from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")

    def enter_search(self, text):
        self.driver.find_element(*self.search_box).send_keys(text)