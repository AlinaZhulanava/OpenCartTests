import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_elem_by_id(browser, elem_id):
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, elem_id))
        )
    except NoSuchElementException:
        return None
    return element


def get_elem_by_xpath(browser, elem_xpath):
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, elem_xpath))
        )
    except NoSuchElementException:
        return None
    return element


def wait_elem_by_id(browser, elem_id):
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, elem_id))
        )
    except NoSuchElementException:
        return False
    return True


def wait_elem_by_xpath(browser, elem_xpath):
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, elem_xpath))
        )
    except NoSuchElementException:
        return False
    return True


def scroll_to_elem(browser, element):
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(3)


def get_prices_list(all_prices_elems):
    prices_list = []
    for price_elem in all_prices_elems:
        prices_list.append(price_elem.text)
    return prices_list


def change_currency(browser):
    currency_choose_button = get_elem_by_xpath(browser,
                                               "//span[text()='Currency']")
    time.sleep(10)
    currency_choose_button.click()
    currency_button = get_elem_by_xpath(browser, "//a[@href='EUR']")
    time.sleep(10)
    currency_button.click()
