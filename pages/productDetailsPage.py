from selenium.webdriver.common.by import By
from lib.driverCommands import DriverCommands


class ProductDetailsPage(DriverCommands):
    # LOCATORS
    add_to_cart_btn_loc = (By.XPATH, '//div/input[2]')

    def add_to_cart_click(self):
        self.click_element(self.add_to_cart_btn_loc)
        self.log.logger('INFO', 'Add to cart btn clicked')
