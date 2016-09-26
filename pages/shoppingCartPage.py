from lib.driverCommands import DriverCommands
from selenium.webdriver.common.by import By


class ShoppingCartPage(DriverCommands):

    #LOCATORS
    terms_conditions_loc = (By.ID, 'termsofservice')
    checkout_btn_loc = (By.ID, 'checkout')

    def confirm_terms_and_conditions(self):
        self.click_element(self.terms_conditions_loc)
        self.log.logger('INFO', 'Checkbox terms and conditions selected')

    def checkout_button_click(self):
        self.click_element(self.checkout_btn_loc)
        assert self.get_page_title() == 'nopCommerce demo store. Checkout', 'Wrong page title'
        self.log.logger('INFO', 'Checkout button clicked')

