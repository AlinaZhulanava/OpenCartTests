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
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, elem_id))
        )
    except NoSuchElementException:
        return False
    return True

def wait_elem_by_xpath(browser, elem_xpath):
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, elem_xpath))
        )
    except NoSuchElementException:
        return False
    return True
