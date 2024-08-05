from methods import wait_elem_by_id


class ProductPage:
    product_info_id = "product-info"

    def __init__(self, browser, base_url, product_name):
        self.browser = browser
        self.url = base_url + "en-gb/product/" + product_name

    def open_page(self):
        self.browser.get(self.url)

    def find_product_info(self):
        return wait_elem_by_id(self.browser, self.product_info_id)
