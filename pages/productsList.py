from lib.driverCommands import DriverCommands
from selenium.webdriver.common.by import By


class ProductsList(DriverCommands):
    # LOCATORS
    product_title_loc = (By.CLASS_NAME, 'product-item')

    def get_all_items(self):
        items = self.find_elements(self.product_title_loc)
        self.log.logger('INFO', 'Found %s items' % len(items))
        return items

    def open_product_details(self, product):
        self.log.logger('INFO', 'Searching for item: %s' % product)
        items = self.get_all_items()
        for item in items:
            product_title = item.text
            if product in product_title:
                self.log.logger('INFO', '%s. Found it!' % product_title)
                item.click()
                break
            else:
                self.log.logger('INFO', 'Found item: %s' % product_title)
        else:
            raise Exception('Cannot find searched item on the list')
