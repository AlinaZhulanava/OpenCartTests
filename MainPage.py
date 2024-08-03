from methods import wait_elem_by_xpath, get_elem_by_xpath
from selenium.webdriver.common.by import By


class MainPage:
    product_thumb_xpath = "//div[@class='product-thumb']"
    add_button_xpath = "//button[@type='submit']"
    elem_for_compare_xpath = "//div[@class='image']"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(url)

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
