from selenium.webdriver.common.action_chains import ActionChains


from MainPage import MainPage
from ShoppingCartPage import ShoppingCartPage
from TopPanel import TopPanel
from methods import scroll_to_elem

import allure


def test_search_for_carousel(browser, get_url):
    with allure.step(f"Opening {get_url} in {browser}"):
        main_page = MainPage(browser, get_url)
        main_page.open_page()

    with allure.step("Checking if carousel presented"):
        if main_page.find_carousel() is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )

    assert main_page.find_carousel() is True


def test_add_to_cart(browser, get_url):
    with allure.step(f"Opening {get_url} in {browser}"):
        main_page = MainPage(browser, get_url)
        main_page.open_page()

    main_page.find_first_product()

    scroll_to_elem(main_page.browser, main_page.get_add_button())
    (ActionChains(main_page.browser)
     .move_to_element(main_page.get_add_button()).perform())
    main_page.click_add_button()

    scroll_to_elem(main_page.browser, main_page.get_elem_for_compare())
    xpath_to_compare = main_page.get_xpath_to_compare()

    top_panel = TopPanel(browser, get_url)
    scroll_to_elem(top_panel.browser, top_panel.get_shopping_cart())
    top_panel.click_shopping_cart()

    shopping_cart_page = ShoppingCartPage(main_page.browser)

    with allure.step("Checking if chosen product and product in cart are equal"):
        if shopping_cart_page.find_elem_with_xpath(xpath_to_compare) is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )

    assert shopping_cart_page.find_elem_with_xpath(xpath_to_compare) is True


def test_prices_change_when_change_currency(browser, get_url):
    with allure.step(f"Opening {get_url} in {browser}"):
        main_page = MainPage(browser, get_url)
        main_page.open_page()

    prices_list = main_page.get_list_of_all_prices_from_table()

    top_panel = TopPanel(browser, get_url)
    top_panel.change_currency_to_another("EUR")

    prices_list_changed = main_page.get_list_of_all_prices_from_table()

    with allure.step("Checking prices changed with currency"):
        if prices_list == prices_list_changed:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )

    assert prices_list != prices_list_changed
