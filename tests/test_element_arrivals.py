from methods import wait_elem_by_id, wait_elem_by_xpath, get_elem_by_xpath


def test_search_for_carousel(browser, get_url):
    browser = browser
    url = get_url
    browser.get(url)

    assert wait_elem_by_id(browser, "carousel-banner-0") == True


def test_search_for_product_list(browser, get_url):
    browser = browser
    url = get_url + "en-gb/catalog/desktops"
    browser.get(url)

    assert wait_elem_by_id(browser, "product-list") == True


def test_search_product_card(browser, get_url):
    browser = browser
    url = get_url + "en-gb/product/iphone"
    browser.get(url)

    assert wait_elem_by_id(browser, "product-info") == True


def test_search_administration(browser, get_url):
    browser = browser
    url = get_url + "administration/"
    browser.get(url)

    assert wait_elem_by_xpath(browser, "//div[text()=' Please enter your login details.']") == True


def test_search_registration(browser, get_url):
    browser = browser
    url = get_url + "/index.php?route=account/register"
    browser.get(url)

    assert wait_elem_by_xpath(browser, "//h1[text()='Register Account']") == True


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

    assert wait_elem_by_xpath(browser, "//h1[text()='Account Logout']") == True
