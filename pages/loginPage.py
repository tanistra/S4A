from lib.driverCommands import DriverCommands
from selenium.webdriver.common.by import By


class LoginPage(DriverCommands):
    email_field_loc = (By.ID, 'Email')
    password_field_loc = (By.ID, 'Password')
    login_btn_loc = (By.CSS_SELECTOR, 'input.button-1.login-button')

    def email_fill_in(self, email):
        self.fill_in(self.email_field_loc, email)
        self.log.logger('INFO', 'Email entered: %s' % email)

    def password_fill_in(self, password):
        self.fill_in(self.password_field_loc, password)
        self.log.logger('INFO', 'Password entered: %s' % password)

    def login_btn_click(self):
        self.click_element(self.login_btn_loc)
        self.log.logger('INFO', 'Login button clicked')

    def log_in_to_shop(self, email=None, password=None):
        if email is not None:
            self.fill_in(self.email_field_loc, email)
        if password is not None:
            self.fill_in(self.password_field_loc, password)
        self.login_btn_click()
