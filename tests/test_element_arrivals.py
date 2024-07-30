import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_for_carousel(browser, get_url):
    browser = browser
    url = get_url
    browser.get(url)

    try:
        element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "carousel-banner-0"))
    )
    except NoSuchElementException:
        assert False
    assert True

def test_search_for_product_list(browser, get_url):
    browser = browser
    url = get_url + "en-gb/catalog/desktops"
    browser.get(url)

    try:
        element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "product-list"))
    )
    except NoSuchElementException:
        assert False
    assert True

def test_search_product_card(browser, get_url):
    browser = browser
    url = get_url + "en-gb/product/iphone"
    browser.get(url)

    try:
        element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "product-info"))
    )
    except NoSuchElementException:
        assert False
    assert True

def test_search_administration(browser, get_url):
    browser = browser
    url = get_url + "administration/"
    browser.get(url)

    try:
        element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()=' Please enter your login details.']"))
    )
    except NoSuchElementException:
        assert False
    assert True

def test_search_registration(browser, get_url):
    browser = browser
    url = get_url + "/index.php?route=account/register"
    browser.get(url)

    try:
        element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Register Account']"))
    )
    except NoSuchElementException:
        assert False
    assert True

def test_user_login(browser, get_url):
    browser = browser
    url = get_url + "/en-gb?route=account/login"
    browser.get(url)

    try:
        email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        email.send_keys("ali.zhulanova@gmail.com")
        password = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password.send_keys("password")
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
        )
        button.click()
    except NoSuchElementException:
        assert False

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='My Account']"))
        )
        dropdown = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa-solid fa-user']"))
        )
        dropdown.click()
    except NoSuchElementException:
        assert False

    try:
        logout = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']"))
        )
        logout.click()
    except NoSuchElementException:
        assert False
    assert True