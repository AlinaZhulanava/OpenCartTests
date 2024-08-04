from RegisterPage import RegisterPage


def test_search_registration(browser, get_url):
    registration_page = RegisterPage(browser, get_url + "/index.php?route=account/register")
    registration_page.open_page()

    assert registration_page.find_register_label() is True