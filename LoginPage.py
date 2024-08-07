from methods import get_elem_by_xpath, wait_elem_by_xpath
import logging
import allure


class LoginPage:
    email_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    user_email = "ali.zhulanova@gmail.com"
    user_password = "password"
    login_button_xpath = "//button[text()='Login']"
    logout_button_xpath = "//a[text()='Logout']"

    label_my_account_xpath = "//h2[text()='My Account']"
    label_account_logout = "//h1[text()='Account Logout']"

    def __init__(self, browser, url):
        logging.info(f"create object of LoginPage")
        self.browser = browser
        self.url = url

    @allure.step("Opening the page")
    def open_page(self):
        self.browser.get(self.url)

    def get_email(self):
        return get_elem_by_xpath(self.browser, self.email_xpath)

    @allure.step("Fill the user's email")
    def fill_email(self):
        self.get_email().send_keys(self.user_email)

    def get_password(self):
        return get_elem_by_xpath(self.browser, self.password_xpath)

    @allure.step("Fill the user's password")
    def fill_password(self):
        self.get_password().send_keys(self.user_password)

    def get_login_button(self):
        return get_elem_by_xpath(self.browser, self.login_button_xpath)

    @allure.step("Click Login button")
    def click_login_button(self):
        self.get_login_button().click()

    def get_logout_button(self):
        return get_elem_by_xpath(self.browser, self.logout_button_xpath)

    @allure.step("Logout")
    def click_logout_button(self):
        self.get_logout_button().click()

    @allure.step("Find My Account label to check whether logged in")
    def find_my_account_label(self):
        return wait_elem_by_xpath(self.browser, self.label_my_account_xpath)

    @allure.step("Find Logout label to check whether logged out")
    def find_account_logout_label(self):
        return wait_elem_by_xpath(self.browser, self.label_account_logout)
