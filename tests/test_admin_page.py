import time

from AdminPage import AdminPage


def test_search_administration(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration/")
    admin_page.open_page()

    assert admin_page.find_form_label() is True


def test_admin_login(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration")
    admin_page.open_page()

    admin_page.login()

    avatar_flag = admin_page.check_if_avatar_presented()
    admin_page.click_logout_button()
    assert avatar_flag is True


def test_add_new_product(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration")
    admin_page.open_page()

    admin_page.login()
    admin_page.click_admin_menu_catalog()
    admin_page.open_admin_menu_catalog_products()
    admin_page.click_add_product_button()

    admin_page.fill_new_product_name()
    admin_page.fill_new_product_meta_tag()
    admin_page.click_new_product_data()
    admin_page.fill_new_product_model()
    admin_page.click_new_product_seo()
    admin_page.fill_new_product_seo_keyword()
    admin_page.click_save_product_button()

    assert admin_page.find_alert_add_product_success()


def test_delete_product(browser, get_url):
    admin_page = AdminPage(browser, get_url + "administration")
    admin_page.open_page()

    admin_page.login()
    admin_page.click_admin_menu_catalog()
    admin_page.open_admin_menu_catalog_products()

    admin_page.choose_product_to_delete()
    #admin_page.choose_product_to_delete()

    admin_page.click_delete_product_button()
    admin_page.submit_alert()

    assert admin_page.find_alert_add_product_success()