from AdminPage import AdminPage


def test_search_administration(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration/")
    admin_page.open_page()

    assert admin_page.find_form_label() is True


def test_admin_login(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration")
    admin_page.open_page()

    admin_page.fill_email()
    admin_page.fill_password()
    admin_page.click_login_button()
    avatar_flag = admin_page.check_if_avatar_presented()
    admin_page.click_logout_button()
    assert avatar_flag is True
