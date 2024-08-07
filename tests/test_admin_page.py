import allure

from AdminPage import AdminPage


def test_search_administration(browser, get_url):
    url = get_url + "administration/"
    with allure.step(f"Opening {url} in {browser}"):
        admin_page = AdminPage(browser, url)
        admin_page.open_page()

    with allure.step("Finding form label"):
        if admin_page.find_form_label() is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
    assert admin_page.find_form_label() is True


def test_admin_login(browser, get_url):
    url = get_url + "administration"
    with allure.step(f"Opening {url} in {browser}"):
        admin_page = AdminPage(browser, url)
        admin_page.open_page()

    admin_page.login()

    avatar_flag = admin_page.check_if_avatar_presented()
    admin_page.click_logout_button()

    with allure.step("Checking if avatar found"):
        if avatar_flag is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
    assert avatar_flag is True


def test_add_new_product(browser, get_url):
    url = get_url + "administration"
    with allure.step(f"Opening {url} in {browser}"):
        admin_page = AdminPage(browser, url)
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

    with allure.step("Checking if product added alert presented"):
        if admin_page.find_alert_add_product_success() is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
    assert admin_page.find_alert_add_product_success()


def test_delete_product(browser, get_url):
    url = get_url + "administration"
    with allure.step(f"Opening {url} in {browser}"):
        admin_page = AdminPage(browser, url)
        admin_page.open_page()

    admin_page.login()
    admin_page.click_admin_menu_catalog()
    admin_page.open_admin_menu_catalog_products()

    # admin_page.choose_product_to_delete()

    admin_page.click_delete_product_button()
    admin_page.submit_alert()

    with allure.step("Checking if product deleted alert presented"):
        if admin_page.find_alert_add_product_success() is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
    assert admin_page.find_alert_add_product_success()
