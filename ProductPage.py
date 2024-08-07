from methods import wait_elem_by_id
import logging
import allure


class ProductPage:
    product_info_id = "product-info"

    def __init__(self, browser, base_url, product_name):
        logging.info(f"create object of ProductPage")
        self.browser = browser
        self.url = base_url + "en-gb/product/" + product_name

    @allure.step("Opening the page")
    def open_page(self):
        self.browser.get(self.url)

    @allure.step("Find product info")
    def find_product_info(self):
        return wait_elem_by_id(self.browser, self.product_info_id)
