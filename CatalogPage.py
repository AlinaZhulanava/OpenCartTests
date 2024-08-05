from methods import get_prices_list, get_elem_by_id, wait_elem_by_id
from selenium.webdriver.common.by import By


class CatalogPage:
    catalog_product_list_id = "product-list"
    price_xpath = "//span[@class='price-new']"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def get_catalog_product_list(self):
        return get_elem_by_id(self.browser, self.catalog_product_list_id)

    def find_catalog_product_list(self):
        return wait_elem_by_id(self.browser, self.catalog_product_list_id)

    def get_list_of_all_prices_from_table(self):
        return get_prices_list(self.get_catalog_product_list()
                               .find_elements(By.XPATH, self.price_xpath))
