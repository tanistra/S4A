from lib.driverCommands import DriverCommands
from selenium.webdriver.common.by import By


class CheckoutPage(DriverCommands):
    # LOCATORS
    # biling address
    first_name_loc = (By.ID, 'BillingNewAddress_FirstName')
    last_name_loc = (By.ID, 'BillingNewAddress_FirstName')
    email_loc = (By.ID, 'BillingNewAddress_Email')
    company_loc = (By.ID, 'BillingNewAddress_Company')
    country_dd_loc = (By.ID, 'BillingNewAddress_CountryId')
    state_dd_loc = (By.ID, 'BillingNewAddress_StateProvinceId')
    city_loc = (By.ID, 'BillingNewAddress_City')
    address_1_loc = (By.ID, 'BillingNewAddress_Address1')
    address_2_loc = (By.ID, 'BillingNewAddress_Address2')
    zip_code_loc = (By.ID, 'BillingNewAddress_ZipPostalCode')
    phone_number_loc = (By.ID, 'BillingNewAddress_PhoneNumber')
    fax_loc = (By.ID, 'BillingNewAddress_FaxNumber')
    biling_continue_btn_loc = (By.ID, 'billing-buttons-container')

    # shipping method
    shipping_continue_btn_loc = (By.XPATH, '//form/div[2]/input')

    # payment method
    credit_card = (By.ID, 'paymentmethod_1')
    payment_continue_btn_loc = (By.XPATH, "(//input[@value='Continue'])[4]")

    # payment information
    credit_card_type_dd_loc = (By.ID, 'CreditCardType')
    cardholder_name_loc = (By.ID, 'CardholderName')
    card_number_loc = (By.ID, 'CardNumber')
    expiration_month_dd_loc = (By.ID, 'ExpireMonth')
    expiration_year_dd_loc = (By.ID, 'ExpireYear')
    card_code_loc = (By.ID, 'CardCode')
    payment_info_continue_btn_loc = (By.XPATH, '//li[5]/div[2]/div/input')

    # confirm order
    confirm_btn_loc = (By.XPATH, '//*[@id="confirm-order-buttons-container"]/input')
    confirmation_info = (By.XPATH, '//div[2]/div/div[1]/strong')

    # billing tab actions
    def first_name_fill_in(self, name):
        self.fill_in(self.first_name_loc, name)
        self.log.logger('INFO', 'First name entered: %s' % name)

    def last_name_fill_in(self, name):
        self.fill_in(self.last_name_loc, name)
        self.log.logger('INFO', 'Last name entered: %s' % name)

    def email_fill_in(self, email):
        self.fill_in(self.email_loc, email)
        self.log.logger('INFO', 'Email entered: %s' % email)

    def company_fill_in(self, name):
        self.fill_in(self.company_loc, name)
        self.log.logger('INFO', 'Company name entered: %s' % name)

    def select_country(self, country):
        self.select_dd_element(self.country_dd_loc, country)
        self.log.logger('INFO', 'Selected country %s' % country)

    def select_state(self, state):
        pass

    def city_fill_in(self, city):
        self.fill_in(self.city_loc, city)
        self.log.logger('INFO', 'City entered')

    def address_1_fill_in(self, address):
        self.fill_in(self.address_1_loc, address)
        self.log.logger('INFO', 'Address 1 entered')

    def address_2_fill_in(self, address):
        self.fill_in(self.address_2_loc, address)
        self.log.logger('INFO', 'Address 2 entered')

    def zip_fill_in(self, zip_code):
        self.fill_in(self.zip_code_loc, zip_code)
        self.log.logger('INFO', 'Zip entered')

    def phone_number_fill_in(self, number):
        self.fill_in(self.phone_number_loc, number)
        self.log.logger('INFO', 'Phone number entered')

    def fax_number_fill_in(self, fax):
        pass

    def biling_continue_btn_click(self):
        self.click_element(self.biling_continue_btn_loc)

    def biling_data_fill_in(self, f_name=None, l_name=None, email=None, company=None, country=None, state=None,
                            city=None,
                            address1=None, address2=None, zip_code=None, phone=None, fax=None):
        if f_name is not None:
            self.first_name_fill_in(f_name)
        if l_name is not None:
            self.last_name_fill_in(l_name)
        if email is not None:
            self.email_fill_in(email)
        if company is not None:
            self.company_fill_in(company)
        if country is not None:
            self.select_country(country)
        if state is not None:
            self.select_state(state)
        if city is not None:
            self.city_fill_in(city)
        if address1 is not None:
            self.address_1_fill_in(address1)
        if address2 is not None:
            self.address_2_fill_in(address2)
        if zip_code is not None:
            self.zip_fill_in(zip_code)
        if phone is not None:
            self.phone_number_fill_in(phone)
        if fax is not None:
            self.fax_number_fill_in(fax)
        self.biling_continue_btn_click()

    # shipping tab actions
    def shipping_method_continue_btn_click(self):
        self.click_element(self.shipping_continue_btn_loc)

    def select_shipping_method(self, method):
        self.find_element(self.shipping_continue_btn_loc)
        self.shipping_method_continue_btn_click()

    # payment tab actions
    def payment_method_continue_btn_click(self):
        self.click_element(self.payment_continue_btn_loc)

    def select_payment_method(self, method):
        if method.lower() == 'credit card':
            self.click_element(self.credit_card)
        elif method.lower() == 'money':
            pass
        elif method.lower() == 'purchase':
            pass
        self.payment_method_continue_btn_click()

    # payment info actions
    def select_credit_card_type(self, card_type):
        self.select_dd_element(self.credit_card_type_dd_loc, card_type)
        self.log.logger('INFO', 'Credit card type selected: %s' % card_type)

    def cardholder_fill_in(self, name):
        self.fill_in(self.cardholder_name_loc, name)
        self.log.logger('INFO', 'Cardholder name entered: %s' % name)

    def card_number_fill_in(self, number):
        self.fill_in(self.card_number_loc, number)
        self.log.logger('INFO', 'Entered card number: %s' % number)

    def select_exp_month(self, month):
        self.select_dd_element(self.expiration_month_dd_loc, month)
        self.log.logger('INFO', 'Selected expiration month: %s' % month)

    def select_exp_year(self, year):
        self.select_dd_element(self.expiration_year_dd_loc, year)
        self.log.logger('INFO', 'Selected expiration year: %s' % year)

    def card_code_fill_in(self, code):
        self.fill_in(self.card_code_loc, code)
        self.log.logger('INFO', 'Entered card code: %s' % code)

    def payment_info_continue_btn_click(self):
        self.click_element(self.payment_info_continue_btn_loc)
        self.log.logger('INFO', 'Continue button clicked')

    def payment_credit_card_info_fill_in(self, card_type=None, cardholder=None, card_number=None, exp_month=None,
                                         exp_year=None, card_code=None):
        if card_type is not None:
            self.select_credit_card_type(card_type)
        if cardholder is not None:
            self.cardholder_fill_in(cardholder)
        if card_number is not None:
            self.card_number_fill_in(card_number)
        if exp_month is not None:
            self.select_exp_month(exp_month)
        if exp_year is not None:
            self.select_exp_year(exp_year)
        if card_code is not None:
            self.card_code_fill_in(card_code)
        self.payment_info_continue_btn_click()

    def confim_btn_click(self):
        self.click_element(self.confirm_btn_loc)
        self.log.logger('INFO', 'Confirm order button clicked')

    def check_confirmation_info(self, expected):
        info = self.get_text_from_element(self.confirmation_info)
        assert info == expected, 'Wrong message, should be: %s, but is %s' % (expected, info)
