from methods import wait_elem_by_xpath


class RegisterPage:
    register_label_xpath = "//h1[text()='Register Account']"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(self.url)

    def open_page(self):
        self.browser.get(self.url)

    def find_register_label(self):
        return wait_elem_by_xpath(self.browser, self.register_label_xpath)