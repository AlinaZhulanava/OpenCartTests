import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="choose a browser")
    parser.addoption("--url", action="store", default="http://localhost/", help="url for OpenCart")

@pytest.fixture
def get_browser(request):
    browser_chosen = request.config.getoption("--browser")
    return browser_chosen

@pytest.fixture
def get_url(request):
    url = request.config.getoption("--url")
    return url

@pytest.fixture
def browser(get_browser):
    browser_name = get_browser

    if browser_name == 'Chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'Firefox':
        browser = webdriver.Firefox()
    elif browser_name == 'Edge':
        browser = webdriver.Edge()
    else:
        raise ValueError("Wrong browser name entered")
    browser.maximize_window()

    yield browser

    browser.close()