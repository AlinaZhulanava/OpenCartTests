from methods import get_elem_by_xpath, wait_elem_by_xpath


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
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)


    def get_email(self):
        return get_elem_by_xpath(self.browser, self.email_xpath)

    def fill_email(self):
        self.get_email().send_keys(self.user_email)

    def get_password(self):
        return get_elem_by_xpath(self.browser, self.password_xpath)

    def fill_password(self):
        self.get_password().send_keys(self.user_password)

    def get_login_button(self):
        return get_elem_by_xpath(self.browser, self.login_button_xpath)

    def click_login_button(self):
        self.get_login_button().click()

    def get_logout_button(self):
        return get_elem_by_xpath(self.browser, self.logout_button_xpath)

    def click_logout_button(self):
        self.get_logout_button().click()

    def find_my_account_label(self):
        return wait_elem_by_xpath(self.browser, self.label_my_account_xpath)

    def find_account_logout_label(self):
        return wait_elem_by_xpath(self.browser, self.label_account_logout)

