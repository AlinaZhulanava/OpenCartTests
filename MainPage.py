from methods import (wait_elem_by_xpath, get_elem_by_xpath,
                     get_prices_list, wait_elem_by_id)
from selenium.webdriver.common.by import By


class MainPage:
    product_thumb_xpath = "//div[@class='product-thumb']"
    add_button_xpath = "//button[@type='submit']"
    elem_for_compare_xpath = "//div[@class='image']"
    catalog_table_xpath = ("//div[@class='row row-cols-1 "
                           "row-cols-sm-2 row-cols-md-3 "
                           "row-cols-xl-4']")
    price_xpath = "//span[@class='price-new']"
    carousel_id = "carousel-banner-0"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def find_first_product(self):
        return wait_elem_by_xpath(self.browser, self.product_thumb_xpath)

    def get_add_button(self):
        return get_elem_by_xpath(self.browser, self.add_button_xpath)

    def click_add_button(self):
        self.get_add_button().click()

    def get_elem_for_compare(self):
        return get_elem_by_xpath(self.browser, self.elem_for_compare_xpath)

    def get_xpath_to_compare(self):
        elem = self.get_elem_for_compare().find_element(By.XPATH,
                                                        "//a[contains(@href, "
                                                        "'product')]")
        str_href = elem.get_attribute("href")
        xpath = "//a[@href=\'" + str_href + "\']"
        return xpath

    def get_catalog_table(self):
        return get_elem_by_xpath(self.browser, self.catalog_table_xpath)

    def get_list_of_all_prices_from_table(self):
        return get_prices_list(self.get_catalog_table()
                               .find_elements(By.XPATH, self.price_xpath))

    def find_carousel(self):
        return wait_elem_by_id(self.browser, self.carousel_id)
