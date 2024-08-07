import allure
from ProductPage import ProductPage


def test_search_product_card(browser, get_url):
    with allure.step(f"Opening {get_url} in {browser}"):
        product_page = ProductPage(browser, get_url, "iphone")
        product_page.open_page()

    with allure.step("Checking if product info presented"):
        if product_page.find_product_info() is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )

    assert product_page.find_product_info() is True
