from methods import get_elem_by_xpath, wait_elem_by_xpath


class AdminPage:
    email_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    user_email = "user"
    user_password = "bitnami"
    login_button_xpath = "//button[text()=' Login']"
    logout_button_xpath = "//span[text()='Logout']"
    avatar_xpath = "//img[@class='rounded-circle']"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(url)

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

    def check_if_avatar_presented(self):
        return wait_elem_by_xpath(self.browser, self.avatar_xpath)