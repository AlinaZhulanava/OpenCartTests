import time
from selenium.webdriver.common.by import By

from methods import wait_elem_by_id, wait_elem_by_xpath, get_elem_by_xpath, wait_elem_clickable_by_xpath, \
    get_elem_by_id, scroll_to_elem, get_prices_list, change_currency


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

    assert wait_elem_by_xpath(browser, "//div[text()=' Please enter your login details.']") is True


def test_search_registration(browser, get_url):
    browser = browser
    url = get_url + "/index.php?route=account/register"
    browser.get(url)

    assert wait_elem_by_xpath(browser, "//h1[text()='Register Account']") is True


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


def test_add_to_cart(browser, get_url):
    browser = browser
    url = get_url
    browser.get(url)

    shopping_cart = get_elem_by_xpath(browser, "//a[@title='Shopping Cart']")
    wait_elem_by_xpath(browser, "//div[@class='product-thumb']")
    add_button = get_elem_by_xpath(browser, "//button[@type='submit']")

    elem_for_compare = get_elem_by_xpath(browser, "//div[@class='image']")

    scroll_to_elem(browser, add_button)
    time.sleep(10)
    add_button.click()

    scroll_to_elem(browser, elem_for_compare)
    time.sleep(10)
    elem_link = elem_for_compare.find_element(By.XPATH, "//a[contains(@href, 'product')]")
    str_href = elem_link.get_attribute("href")

    scroll_to_elem(browser, shopping_cart)
    time.sleep(10)
    shopping_cart.click()

    xpath = "//a[@href=\'" + str_href + "\']"

    assert wait_elem_by_xpath(browser, xpath) is True


def test_prices_change_when_change_currency(browser, get_url):
    browser = browser
    url = get_url
    browser.get(url)

    table_elem = get_elem_by_xpath(browser, "//div[@class='row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4']")
    all_prices_elems = table_elem.find_elements(By.XPATH, "//span[@class='price-new']")
    prices_list = get_prices_list(all_prices_elems)

    change_currency(browser)

    table_elem = get_elem_by_xpath(browser, "//div[@class='row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4']")
    all_prices_elems = table_elem.find_elements(By.XPATH, "//span[@class='price-new']")
    prices_list_changed = get_prices_list(all_prices_elems)

    assert prices_list != prices_list_changed


def test_prices_change_in_catalog_when_change_currency(browser, get_url):
    browser = browser
    url = get_url
    browser.get(url+"catalog/desktops")

    catalog_product_list = get_elem_by_id(browser, "product-list")

    all_prices_elems = catalog_product_list.find_elements(By.XPATH, "//span[@class='price-new']")
    prices_list = get_prices_list(all_prices_elems)

    change_currency(browser)

    catalog_product_list = get_elem_by_id(browser, "product-list")

    all_prices_elems = catalog_product_list.find_elements(By.XPATH, "//span[@class='price-new']")
    prices_list_changed = get_prices_list(all_prices_elems)

    assert prices_list != prices_list_changed
