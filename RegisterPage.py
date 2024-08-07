from methods import wait_elem_by_xpath, get_elem_by_xpath
import logging
import allure


class RegisterPage:
    register_label_xpath = "//h1[text()='Register Account']"

    first_name_xpath = "//input[@name='firstname']"
    last_name_xpath = "//input[@name='lastname']"
    email_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    continue_button_xpath = "//button[text()='Continue']"
    agree_switch_xpath = "//input[@name='agree']"

    user_first_name = "CharlieA"
    user_last_name = "BrownA"
    user_email = "charlibrowm1@gmail.com"
    user_password = "password"

    account_created_label_xpath = \
        "//h1[text()='Your Account Has Been Created!']"

    def __init__(self, browser, url):
        logging.info(f"create object of RegisterPage")
        self.browser = browser
        self.url = url

    @allure.step("Opening the page")
    def open_page(self):
        self.browser.get(self.url)

    @allure.step("Find Account Created label to check if registered")
    def find_account_created_label(self):
        wait_elem_by_xpath(self.browser, self.account_created_label_xpath)

    @allure.step("Find Register label to check Registration page shown")
    def find_register_label(self):
        return wait_elem_by_xpath(self.browser, self.register_label_xpath)

    def get_first_name(self):
        return get_elem_by_xpath(self.browser, self.first_name_xpath)

    @allure.step("Fill the user's first name")
    def fill_first_name(self):
        self.get_first_name().send_keys(self.user_first_name)

    def get_last_name(self):
        return get_elem_by_xpath(self.browser, self.last_name_xpath)

    @allure.step("Fill the user's last name")
    def fill_last_name(self):
        self.get_last_name().send_keys(self.user_last_name)

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

    def get_agree_switch(self):
        return get_elem_by_xpath(self.browser, self.agree_switch_xpath)

    @allure.step("Agree with politics")
    def click_agree(self):
        self.get_agree_switch().click()

    def get_continue_button(self):
        return get_elem_by_xpath(self.browser, self.continue_button_xpath)

    @allure.step("Click Continue button")
    def click_continue_button(self):
        self.get_continue_button().click()
