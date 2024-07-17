import time
import pytest
from selenium import webdriver

def test_open(browser, get_url):
    browser = browser
    url = get_url

    browser.get(url)
    time.sleep(5)
