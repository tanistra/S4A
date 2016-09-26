from lib.driverCommands import DriverCommands
from selenium.webdriver.common.by import By


class RegistrationPage(DriverCommands):

    # LOCATORS
    gender_female_radio_loc = (By.ID,'gender-female')
    gender_male_radio_loc = (By.ID, 'gender-male')
    first_name_field_loc = (By.ID, 'FirstName')
    first_name_required_loc = (By.XPATH, '//form/div/div[2]/div[1]/div[2]/div[2]/span[2]')
    last_name_field_loc = (By.ID, 'LastName')
    last_name_required_loc = (By.XPATH, '//form/div/div[2]/div[1]/div[2]/div[3]/span[2]')
    birth_day_dd_loc = (By.NAME, 'DateOfBirthDay')
    birth_month_dd_loc = (By.NAME, 'DateOfBirthMonth')
    birth_year_dd_loc = (By.NAME, 'DateOfBirthYear')
    email_field_loc = (By.ID, 'Email')
    email_required_loc = (By.XPATH, '//form/div/div[2]/div[1]/div[2]/div[5]/span[2]')
    company_name_field_loc = (By.ID, 'Company')
    newsletter_checkbox_loc = (By.ID, 'Newsletter')
    password_field_loc = (By.ID, 'Password')
    password_required_loc = (By.XPATH, '//form/div/div[2]/div[4]/div[2]/div[1]/span[2]')
    confirm_password_field_loc = (By.ID, 'ConfirmPassword')
    confirm_password_required_loc = (By.XPATH, '//form/div/div[2]/div[4]/div[2]/div[2]/span[2]')
    register_button_loc = (By.ID, 'register-button')
    success_info_loc = (By.XPATH, '//form/div/div[2]/div[1]')

    def choose_gender(self, gender):
        if gender.lower() == 'male':
            self.click_element(self.gender_male_radio_loc)
        elif gender.lower() == 'female':
            self.click_element(self.gender_female_radio_loc)
        else:
            self.log.logger('WARNING', 'Incorrect gender, can by only male or female')
        self.log.logger('INFO','Selected gender: %s' % gender)

    def first_name_fill_in(self, first_name):
        self.fill_in(self.first_name_field_loc, first_name)
        self.log.logger('INFO', 'First name filled: %s' % first_name)

    def last_name_fill_in(self, last_name):
        self.fill_in(self.last_name_field_loc, last_name)
        self.log.logger('INFO', 'Last name filled: %s' % last_name)

    def birth_day_select(self, day):
        self.select_dd_element(self.birth_day_dd_loc, day)
        self.log.logger('INFO', 'Birth day selected: %s' % day)

    def birth_month_select(self, month):
        self.select_dd_element(self.birth_month_dd_loc, month)
        self.log.logger('INFO', 'Birth month selected: %s' % month)

    def birth_year_select(self, year):
        self.select_dd_element(self.birth_year_dd_loc, year)
        self.log.logger('INFO', 'Birth year selected: %s' % year)

    def email_fill_in(self, email):
        self.fill_in(self.email_field_loc, email)
        self.log.logger('INFO', 'Email filled: %s' % email)

    def company_name_fill_in(self, name):
        self.fill_in(self.company_name_field_loc, name)
        self.log.logger('INFO', 'Company name filled: %s' % name)

    def newsletter_checkbox_click(self):
        self.click_element(self.newsletter_checkbox_loc)
        self.log.logger('INFO', 'Newsletter checkbox unselected')

    def password_fill_in(self, password):
        self.fill_in(self.password_field_loc, password)
        self.log.logger('INFO', 'Password filled: %s' % password)

    def confirm_password_fill_in(self, password):
        self.fill_in(self.confirm_password_field_loc, password)
        self.log.logger('INFO', 'Confirm password filled: %s' % password)

    def register_button_click(self):
        self.click_element(self.register_button_loc)
        self.log.logger('INFO', 'Register button clicked')

    def register_user(self, gender=None, f_name=None, l_name=None, birth_day=None, birth_month=None,
                      birth_year=None, email=None, comp_name=None, newsletter=True, password=None, conf_pass=None):
        if gender is not None:
            self.choose_gender(gender)
        if f_name is not None:
            self.first_name_fill_in(f_name)
        if l_name is not None:
            self.last_name_fill_in(l_name)
        if birth_day is not None:
            self.birth_day_select(birth_day)
        if birth_month is not None:
            self.birth_month_select(birth_month)
        if birth_year is not None:
            self.birth_year_select(birth_year)
        if email is not None:
            self.email_fill_in(email)
        if not newsletter:
            self.newsletter_checkbox_click()
        if comp_name is not None:
            self.company_name_fill_in(comp_name)
        if password is not None:
            self.password_fill_in(password)
        if conf_pass is not None:
            self.confirm_password_fill_in(conf_pass)
        self.register_button_click()

    def first_name_check_required(self):
        alert = self.get_text_from_element(self.first_name_required_loc)
        assert alert == 'First name is required.', 'Field first name should be requied'

    def last_name_check_required(self):
        alert = self.get_text_from_element(self.last_name_required_loc)
        assert alert == 'Last name is required.', 'Field last name should be required'

    def email_required(self):
        alert = self.get_text_from_element(self.email_required_loc)
        assert alert == 'Email is required.', 'Filed email should be required'

    def password_required(self):
        alert = self.get_text_from_element(self.password_required_loc)
        assert alert == 'Password is required.', 'Field password should be required.'

    def confirm_password_required(self):
        alert = self.get_text_from_element(self.confirm_password_required_loc)
        assert alert == 'Password is required.', 'Filed confirm password should be required'

    def check_registration_success(self):
        success = 'Your registration completed'
        inf = self.get_text_from_element(self.success_info_loc)
        assert inf == success, 'Incorrect message, should be: %s, but is: %s ' % (success, inf)

