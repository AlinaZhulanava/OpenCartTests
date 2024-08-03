from methods import get_elem_by_xpath, wait_elem_by_xpath
import time

class TopPanel:
    shopping_cart_xpath = "//a[@title='Shopping Cart']"
    currency_choose_button_xpath = "//span[text()='Currency']"
    currency_euro_xpath = "//a[@href='EUR']"

    def __init__(self, browser):
        self.browser = browser

    def get_shopping_cart(self):
        return get_elem_by_xpath(self.browser, self.shopping_cart_xpath)


    def click_shopping_cart(self):
        get_elem_by_xpath(self.browser, self.shopping_cart_xpath).click()

    def get_currency_choose_button(self):
        return get_elem_by_xpath(self.browser, self.currency_choose_button_xpath)

    def click_currency_choose_button(self):
        get_elem_by_xpath(self.browser, self.currency_choose_button_xpath).click()

    def get_euro_button(self):
        return get_elem_by_xpath(self.browser, self.currency_euro_xpath)

    def click_euro_button(self):
        get_elem_by_xpath(self.browser, self.currency_euro_xpath).click()

    def change_currency_to_euro(self):
        time.sleep(10)
        self.click_currency_choose_button()
        time.sleep(10)
        self.click_euro_button()

