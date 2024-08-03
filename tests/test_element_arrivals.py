import time

from selenium.webdriver.common.action_chains import ActionChains

from AdminPage import AdminPage
from CatalogPage import CatalogPage
from LoginPage import LoginPage
from MainPage import MainPage
from ProductPage import ProductPage
from RegisterPage import RegisterPage
from ShoppingCartPage import ShoppingCartPage
from TopPanel import TopPanel
from methods import (wait_elem_by_id, wait_elem_by_xpath, get_elem_by_xpath,
                     get_elem_by_id, scroll_to_elem,
                     get_prices_list)


def test_search_for_carousel(browser, get_url):
    main_page = MainPage(browser, get_url)
    main_page.open_page()

    assert main_page.find_carousel() is True


def test_search_for_product_list(browser, get_url):
    catalog_page = CatalogPage(browser, get_url + "en-gb/catalog/desktops")
    catalog_page.open_page()

    assert catalog_page.find_catalog_product_list() is True


def test_search_product_card(browser, get_url):
    product_page = ProductPage(browser, get_url, "iphone")
    product_page.open_page()

    assert product_page.find_product_info() is True


def test_search_administration(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration/")
    admin_page.open_page()

    assert admin_page.find_form_label() is True


def test_search_registration(browser, get_url):
    registration_page = RegisterPage(browser, get_url + "/index.php?route=account/register")
    registration_page.open_page()

    assert registration_page.find_register_label() is True


def test_user_login(browser, get_url):
    login_page = LoginPage(browser, get_url + "en-gb?route=account/login")
    login_page.open_page()

    login_page.fill_email()
    login_page.fill_password()
    login_page.click_login_button()

    login_page.find_my_account_label()

    top_panel = TopPanel(browser)
    top_panel.click_my_account_button()
    top_panel.click_logout_button()

    assert login_page.find_account_logout_label() is True


def test_admin_login(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration")
    admin_page.open_page()

    admin_page.fill_email()
    admin_page.fill_password()
    admin_page.click_login_button()
    avatar_flag = admin_page.check_if_avatar_presented()
    admin_page.click_logout_button()
    assert avatar_flag is True


def test_add_to_cart(browser, get_url):
    main_page = MainPage(browser, get_url)
    main_page.open_page()

    main_page.find_first_product()

    scroll_to_elem(main_page.browser, main_page.get_add_button())
    ActionChains(main_page.browser).move_to_element(main_page.get_add_button()).perform()
    main_page.click_add_button()

    scroll_to_elem(main_page.browser, main_page.get_elem_for_compare())
    xpath_to_compare = main_page.get_xpath_to_compare()

    top_panel = TopPanel(browser)
    scroll_to_elem(top_panel.browser, top_panel.get_shopping_cart())
    top_panel.click_shopping_cart()

    shopping_cart_page = ShoppingCartPage(main_page.browser)
    assert shopping_cart_page.find_elem_with_xpath(xpath_to_compare) is True


def test_prices_change_when_change_currency(browser, get_url):
    main_page = MainPage(browser, get_url)
    main_page.open_page()

    prices_list = main_page.get_list_of_all_prices_from_table()

    top_panel = TopPanel(browser)
    top_panel.click_currency_choose_button()
    top_panel.click_euro_button()

    prices_list_changed = main_page.get_list_of_all_prices_from_table()

    assert prices_list != prices_list_changed


def test_prices_change_in_catalog_when_change_currency(browser, get_url):
    catalog_page = CatalogPage(browser, get_url + "catalog/desktops")
    catalog_page.open_page()

    prices_list = catalog_page.get_list_of_all_prices_from_table()

    top_panel = TopPanel(browser)
    top_panel.click_currency_choose_button()
    top_panel.click_euro_button()

    prices_list_changed = catalog_page.get_list_of_all_prices_from_table()

    assert prices_list != prices_list_changed
