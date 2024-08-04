from ProductPage import ProductPage


def test_search_product_card(browser, get_url):
    product_page = ProductPage(browser, get_url, "iphone")
    product_page.open_page()

    assert product_page.find_product_info() is True