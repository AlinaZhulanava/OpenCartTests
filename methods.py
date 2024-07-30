from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_elem_by_id(browser, elem_id):
    try:
        element = WebDriverWait(browser, 10).until(
            # EC.visibility_of_element_located((By.ID, elem_id))
            EC.presence_of_element_located((By.ID, elem_id))
        )
    except NoSuchElementException:
        return None
    return element


def get_elem_by_xpath(browser, elem_xpath):
    try:
        element = WebDriverWait(browser, 10).until(
            # EC.visibility_of_element_located((By.XPATH, elem_xpath))
            EC.presence_of_element_located((By.XPATH, elem_xpath))
        )
    except NoSuchElementException:
        return None
    return element


def wait_elem_by_id(browser, elem_id):
    try:
        WebDriverWait(browser, 10).until(
            # EC.visibility_of_element_located((By.XPATH, elem_id))
            EC.presence_of_element_located((By.ID, elem_id))
        )
    except NoSuchElementException:
        return False
    return True


def wait_elem_by_xpath(browser, elem_xpath):
    try:
        WebDriverWait(browser, 10).until(
            # EC.visibility_of_element_located((By.XPATH, elem_xpath))
            EC.presence_of_element_located((By.XPATH, elem_xpath))
        )
    except NoSuchElementException:
        return False
    return True


def wait_elem_clickable_by_xpath(browser, elem_xpath):
    try:
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, elem_xpath))
        )
    except NoSuchElementException:
        return False
    return True


def scroll_to_elem(browser, element):
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
