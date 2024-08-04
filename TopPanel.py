from methods import get_elem_by_xpath, wait_elem_by_xpath
import time

class TopPanel:
    shopping_cart_xpath = "//a[@title='Shopping Cart']"
    my_account_button_xpath = "//i[@class='fa-solid fa-user']"
    register_button_xpath = "//a[text()='Register']"
    logout_button_xpath = "//a[text()='Logout']"
    currency_choose_button_xpath = "//span[text()='Currency']"
    currency_euro_xpath = "//a[@href='EUR']"

    def __init__(self, browser):
        self.browser = browser

    def get_shopping_cart(self):
        return get_elem_by_xpath(self.browser, self.shopping_cart_xpath)


    def click_shopping_cart(self):
        self.get_shopping_cart().click()

    def get_my_account_button(self):
        return get_elem_by_xpath(self.browser, self.my_account_button_xpath)

    def click_my_account_button(self):
        self.get_my_account_button().click()

    def get_register_button(self):
        return get_elem_by_xpath(self.browser, self.register_button_xpath)

    def click_register_button(self):
        self.get_register_button().click()

    def get_logout_button(self):
        return get_elem_by_xpath(self.browser, self.logout_button_xpath)

    def click_logout_button(self):
        self.get_logout_button().click()

    def get_currency_choose_button(self):
        return get_elem_by_xpath(self.browser, self.currency_choose_button_xpath)

    def click_currency_choose_button(self):
        self.get_currency_choose_button().click()

    def get_euro_button(self):
        return get_elem_by_xpath(self.browser, self.currency_euro_xpath)

    def click_euro_button(self):
        self.get_euro_button().click()

    def change_currency_to_euro(self):
        time.sleep(10)
        self.click_currency_choose_button()
        time.sleep(10)
        self.click_euro_button()

