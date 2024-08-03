from methods import wait_elem_by_xpath


class ShoppingCartPage:
    def __init__(self, browser):
        self.browser = browser


    def find_elem_with_xpath(self, xpath):
        return wait_elem_by_xpath(self.browser, xpath)