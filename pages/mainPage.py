from lib.driverCommands import DriverCommands
from selenium.webdriver.common.by import By


class MainPage(DriverCommands):

    # LOCATORS
    # top menu locators
    register_link_loc = (By.LINK_TEXT, 'Register')
    log_in_link_loc = (By.LINK_TEXT, 'Log in')
    account_link_loc = (By.CLASS_NAME, 'ico-account')
    shopping_cart_loc = (By.LINK_TEXT, 'Shopping cart')

    # product menu locators
    electronics_loc = (By.LINK_TEXT, 'Electronics')
    cell_phones_loc = (By.LINK_TEXT, 'Cell phones')

    # other page elements locators
    search_loc = (By.ID, 'small-searchterms')

    def register_tab_click(self):
        self.click_element(self.register_link_loc)
        assert self.get_page_title() == 'nopCommerce demo store. Register', 'Wrong page title'
        self.log.logger('INFO', 'The registration page open')

    def log_in_tab_click(self):
        self.click_element(self.log_in_link_loc)
        assert self.get_page_title() == 'nopCommerce demo store. Login', 'Wrong page title'
        self.log.logger('INFO', 'The login page open')

    def shopping_cart_tab_click(self):
        self.click_element(self.shopping_cart_loc)
        assert self.get_page_title() == 'nopCommerce demo store. Shopping Cart', 'Wrong page title'
        self.log.logger('INFO', 'The shopping cart open')

    # PRODUCTS MENU ACTIONS
    def electronics_menu_click(self):
        self.click_element(self.electronics_loc)
        assert self.get_page_title() == 'nopCommerce demo store. Electronics', 'Wrong page title'
        self.log.logger('INFO', 'Electronic products page open')

    def cell_phones_menu_click(self):
        self.move_to_element(self.electronics_loc)
        self.click_element(self.cell_phones_loc)
        assert self.get_page_title() == 'nopCommerce demo store. Cell phones'
        self.log.logger('INFO', 'Cell phone products page open')



    def check_logged_user(self, user_email):
        logged_user = self.get_text_from_element(self.account_link_loc)
        assert logged_user == user_email, 'Wrong user account, should be %s, but logged is: %s' % (user_email, logged_user)

    def use_search(self, item):
        self.fill_in(self.search_loc, item, confirm=True)
        self.log.logger('INFO','Searching item: %s' % item)

