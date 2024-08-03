import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from AdminPage import AdminPage
from MainPage import MainPage
from ShoppingCartPage import ShoppingCartPage
from TopPanel import TopPanel
from methods import (wait_elem_by_id, wait_elem_by_xpath, get_elem_by_xpath,
                     get_elem_by_id, scroll_to_elem,
                     get_prices_list, change_currency)


def test_search_for_carousel(browser, get_url):
    browser = browser
    url = get_url
    browser.get(url)

    assert wait_elem_by_id(browser, "carousel-banner-0") is True


def test_search_for_product_list(browser, get_url):
    browser = browser
    url = get_url + "en-gb/catalog/desktops"
    browser.get(url)

    assert wait_elem_by_id(browser, "product-list") is True


def test_search_product_card(browser, get_url):
    browser = browser
    url = get_url + "en-gb/product/iphone"
    browser.get(url)

    assert wait_elem_by_id(browser, "product-info") is True


def test_search_administration(browser, get_url):
    browser = browser
    url = get_url + "administration/"
    browser.get(url)

    assert wait_elem_by_xpath(browser,
                              "//div[text()="
                              "' Please enter your login details.']") is True


def test_search_registration(browser, get_url):
    browser = browser
    url = get_url + "/index.php?route=account/register"
    browser.get(url)

    assert wait_elem_by_xpath(browser,
                              "//h1[text()='Register Account']") is True


def test_user_login(browser, get_url):
    browser = browser
    url = get_url + "/en-gb?route=account/login"
    browser.get(url)

    email = get_elem_by_xpath(browser, "//input[@name='email']")
    email.send_keys("ali.zhulanova@gmail.com")
    password = get_elem_by_xpath(browser, "//input[@name='password']")
    password.send_keys("password")
    button = get_elem_by_xpath(browser, "//button[text()='Login']")
    button.click()

    wait_elem_by_xpath(browser, "//h2[text()='My Account']")
    dropdown = get_elem_by_xpath(browser, "//i[@class='fa-solid fa-user']")
    dropdown.click()
    logout = get_elem_by_xpath(browser, "//a[text()='Logout']")
    logout.click()

    assert wait_elem_by_xpath(browser, "//h1[text()='Account Logout']") is True


def test_admin_login(browser, get_url):
    browser = browser
    url = get_url + "administration"
    admin_page = AdminPage(browser, url)

    admin_page.fill_email()
    admin_page.fill_password()
    admin_page.click_login_button()
    avatar_flag = admin_page.check_if_avatar_presented()
    admin_page.click_logout_button()
    assert avatar_flag is True


def test_add_to_cart(browser, get_url):
    browser = browser
    url = get_url
    main_page = MainPage(browser, url)

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
    browser = browser
    url = get_url
    browser.get(url)

    table_elem = get_elem_by_xpath(browser,
                                   "//div[@class='row row-cols-1 "
                                   "row-cols-sm-2 row-cols-md-3 "
                                   "row-cols-xl-4']")
    all_prices_elems = table_elem.find_elements(By.XPATH,
                                                "//span[@class='price-new']")
    prices_list = get_prices_list(all_prices_elems)

    #change_currency(browser)
    top_panel = TopPanel(browser)
    top_panel.click_currency_choose_button()
    top_panel.click_euro_button()

    table_elem = get_elem_by_xpath(browser,
                                   "//div[@class='row row-cols-1 "
                                   "row-cols-sm-2 row-cols-md-3 "
                                   "row-cols-xl-4']")
    all_prices_elems = table_elem.find_elements(By.XPATH,
                                                "//span[@class='price-new']")
    prices_list_changed = get_prices_list(all_prices_elems)

    assert prices_list != prices_list_changed


def test_prices_change_in_catalog_when_change_currency(browser, get_url):
    browser = browser
    url = get_url
    browser.get(url + "catalog/desktops")

    catalog_product_list = get_elem_by_id(browser, "product-list")

    all_prices_elems = (catalog_product_list
                        .find_elements(By.XPATH, "//span[@class='price-new']"))
    prices_list = get_prices_list(all_prices_elems)

    #change_currency(browser)
    top_panel = TopPanel(browser)
    top_panel.click_currency_choose_button()
    top_panel.click_euro_button()

    catalog_product_list = get_elem_by_id(browser, "product-list")

    all_prices_elems = (catalog_product_list
                        .find_elements(By.XPATH, "//span[@class='price-new']"))
    prices_list_changed = get_prices_list(all_prices_elems)

    assert prices_list != prices_list_changed
