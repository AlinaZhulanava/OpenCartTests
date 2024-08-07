from methods import get_elem_by_xpath, wait_elem_by_xpath
import logging
import allure


class TopPanel:
    shopping_cart_xpath = "//a[@title='Shopping Cart']"
    my_account_button_xpath = "//i[@class='fa-solid fa-user']"
    register_button_xpath = "//a[text()='Register']"
    logout_button_xpath = "//a[text()='Logout']"
    currency_choose_button_xpath = "//span[text()='Currency']"

    currency_sign_euro_xpath = "//strong[text()='€']"
    currency_sign_pound_xpath = "//strong[text()='£']"
    currency_sign_dollar_xpath = "//strong[text()='$']"

    currency_euro_xpath = "//a[@href='EUR']"
    currency_pound_xpath = "//a[@href='GBP']"
    currency_dollar_xpath = "//a[@href='USD']"

    def __init__(self, browser, url):
        logging.info(f"create object of TopPanel")
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def get_shopping_cart(self):
        return get_elem_by_xpath(self.browser, self.shopping_cart_xpath)

    @allure.step("Click shopping cart on the top panel")
    def click_shopping_cart(self):
        self.get_shopping_cart().click()

    def get_my_account_button(self):
        return get_elem_by_xpath(self.browser, self.my_account_button_xpath)

    @allure.step("Click My Account button on the top panel")
    def click_my_account_button(self):
        self.get_my_account_button().click()

    def get_register_button(self):
        return get_elem_by_xpath(self.browser, self.register_button_xpath)

    @allure.step("Click Register button on the top panel")
    def click_register_button(self):
        self.get_register_button().click()

    def get_logout_button(self):
        return get_elem_by_xpath(self.browser, self.logout_button_xpath)

    @allure.step("Logout")
    def click_logout_button(self):
        self.get_logout_button().click()

    def get_displayed_currency(self):
        if wait_elem_by_xpath(self.browser, self.currency_sign_dollar_xpath):
            return "USD"
        elif wait_elem_by_xpath(self.browser, self.currency_sign_euro_xpath):
            return "EUR"
        elif wait_elem_by_xpath(self.browser, self.currency_sign_pound_xpath):
            return "GBP"

    def get_currency_choose_button(self):
        return get_elem_by_xpath(self.browser,
                                 self.currency_choose_button_xpath)

    @allure.step("Click Currency button to choose currency")
    def click_currency_choose_button(self):
        self.get_currency_choose_button().click()

    def get_currency_option_button(self, currency):
        logging.info(f"define currency {currency}")
        if currency == "EUR":
            return get_elem_by_xpath(self.browser, self.currency_euro_xpath)
        elif currency == "USD":
            return get_elem_by_xpath(self.browser, self.currency_dollar_xpath)
        elif currency == "GBP":
            return get_elem_by_xpath(self.browser, self.currency_pound_xpath)

    @allure.step("Choose currency as {currency}")
    def click_currency_option_button(self, currency):
        self.get_currency_option_button(currency).click()

    def change_currency_to_another(self, currency):
        self.click_currency_choose_button()
        self.click_currency_option_button(currency)
