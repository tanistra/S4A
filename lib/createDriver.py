from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lib.configurationReader import load_configuration_from_file
from lib.logger import Logger

CONFIG = load_configuration_from_file('config.json')

log = Logger()


def create_driver(browser=CONFIG["BROWSER"]):
    """
    Function creates selenium webdriver
    :param browser: specify web browser. Can be:
    * "FF" for firefox browser
    * "CHROME" for chrome,
    * "OPERA" for opera browser
    * "IE" for internet explorer
    * "EDGE" for edge browser
    * "SAFARI" for safari browser
    Default browser is load from config.json file
    :return: driver
    """
    if browser.upper() == "FF":
        d = DesiredCapabilities.FIREFOX
        d['loggingPrefs'] = {'browser': 'ALL'}
        driver = webdriver.Firefox(capabilities=d)
        driver.maximize_window()
    elif browser.upper() == "CHROME":
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        driver = webdriver.Chrome(desired_capabilities=d)
        driver.set_window_size('1680', '1050')
        driver.maximize_window()
    elif browser.upper() == "OPERA":
        driver = webdriver.Opera()
    elif browser.upper() == "IE":
        driver = webdriver.Ie()
        driver.maximize_window()
    elif browser.upper() == "EDGE":
        driver = webdriver.Edge()
    elif browser.upper() == "SAFARI":
        driver = webdriver.Safari()
    else:
        raise Exception("""
        ERROR! Please check browser in config.json file. BROWSER should = 'FF',
        'CHROME', 'OPERA' 'IE', 'EDGE' or 'SAFARI'
        """)
    driver.implicitly_wait(15)
    log.logger('INFO', '%s selenium driver started' % browser)
    return driver
