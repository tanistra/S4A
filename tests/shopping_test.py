from tests.baseTest import BaseTest
from lib.logger import whoami
from pages.mainPage import MainPage
from pages.registrationPage import RegistrationPage
from pages.loginPage import LoginPage
from pages.productsList import ProductsList
from pages.productDetailsPage import ProductDetailsPage
from pages.shoppingCartPage import ShoppingCartPage
from pages.checkoutPage import CheckoutPage
from faker import Factory


class ShoppingTestSuite(BaseTest):

    # TEST DATA
    # **********************************************************
    f = Factory.create()
    name = f.first_name_female()
    last_name = f.last_name_female()
    email = f.email()
    password = 'alamakota'
    phone = f.phone_number()
    country = 'Poland',
    city = f.city()
    address1 = f.street_address()
    zip_code = f.postcode()
    card_type = 'Visa'
    cardholder = f.credit_card_provider(card_type.lower())
    card_number = f.credit_card_number(card_type.lower())
    exp_month = f.credit_card_expire(date_format="%m")
    exp_year = f.credit_card_expire(end='+5y', date_format='%Y')
    card_code = f.credit_card_security_code(card_type.lower())
    # **********************************************************

    def setUp(self):
        BaseTest.setUp(self)
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.products_list = ProductsList(self.driver)
        self.prod_details = ProductDetailsPage(self.driver)
        self.cart = ShoppingCartPage(self.driver)
        self.checkout = CheckoutPage(self.driver)

    def test_01_register_new_user(self):
        whoami()
        self.main_page.register_tab_click()
        reg_page = RegistrationPage(self.driver)
        reg_page.register_user(gender='female', f_name=self.name, l_name=self.last_name, email=self.email,
                               password=self.password, conf_pass=self.password)
        reg_page.check_registration_success()
        self.testResult = True

    def test_02_add_product_to_cart(self):
        whoami()
        self.main_page.log_in_tab_click()
        self.login_page.log_in_to_shop(email=self.email, password=self.password)
        self.main_page.check_logged_user(self.email)
        self.main_page.cell_phones_menu_click()
        self.products_list.open_product_details('HTC One Mini Blue')
        self.prod_details.add_to_cart_click()
        self.testResult = True

    def test_03_checkout_order(self):
        whoami()
        self.main_page.log_in_tab_click()
        self.login_page.log_in_to_shop(email=self.email, password=self.password)
        self.main_page.shopping_cart_tab_click()
        self.cart.confirm_terms_and_conditions()
        self.cart.checkout_button_click()
        self.checkout.biling_data_fill_in(f_name=self.name, l_name=self.last_name, email=self.email, country='Poland',
                                          city=self.city, address1=self.address1, zip_code=self.zip_code,
                                          phone=self.phone)
        self.checkout.select_shipping_method(None)
        self.checkout.select_payment_method(method='credit card')
        self.checkout.payment_credit_card_info_fill_in(card_type=self.card_type, cardholder=self.cardholder,
                                                       card_number=self.card_number, exp_month=self.exp_month,
                                                       exp_year=self.exp_year, card_code=self.card_code)
        self.checkout.confim_btn_click()
        self.checkout.check_confirmation_info('Your order has been successfully processed!')
        self.testResult = True
