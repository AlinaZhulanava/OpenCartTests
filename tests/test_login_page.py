from LoginPage import LoginPage
from TopPanel import TopPanel
import allure


def test_user_login(browser, get_url):
    url = get_url + "en-gb?route=account/login"
    with allure.step(f"Opening {url} in {browser}"):
        login_page = LoginPage(browser, url)
        login_page.open_page()

    login_page.fill_email()
    login_page.fill_password()
    login_page.click_login_button()

    login_page.find_my_account_label()

    top_panel = TopPanel(browser, get_url)
    top_panel.click_my_account_button()
    top_panel.click_logout_button()

    assert login_page.find_account_logout_label() is True
