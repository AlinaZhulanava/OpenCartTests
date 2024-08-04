from LoginPage import LoginPage
from TopPanel import TopPanel


def test_user_login(browser, get_url):
    login_page = LoginPage(browser, get_url + "en-gb?route=account/login")
    login_page.open_page()

    login_page.fill_email()
    login_page.fill_password()
    login_page.click_login_button()

    login_page.find_my_account_label()

    top_panel = TopPanel(browser)
    top_panel.click_my_account_button()
    top_panel.click_logout_button()

    assert login_page.find_account_logout_label() is True