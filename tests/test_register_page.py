import allure
import pytest

from MainPage import MainPage
from RegisterPage import RegisterPage
from TopPanel import TopPanel
from methods import scroll_to_elem


def test_search_registration(browser, get_url):
    url = get_url + "/index.php?route=account/register"
    with allure.step(f"Open {url} in {browser}"):
        registration_page = RegisterPage(browser, url)
        registration_page.open_page()

    with allure.step("Checking if Register label presented"):
        if registration_page.find_register_label() is False:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )

    assert registration_page.find_register_label() is True


def test_register_new_user(browser, get_url):
    url = get_url + "en-gb?route=account/register"

    with allure.step(f"Open {url} in {browser}"):
        main_page = MainPage(browser, get_url)
        main_page.open_page()

    register_page = RegisterPage(browser, url)

    top_panel = TopPanel(browser, get_url)
    top_panel.click_my_account_button()
    top_panel.click_register_button()

    register_page.find_register_label()
    register_page.fill_first_name()
    register_page.fill_last_name()
    register_page.fill_email()
    register_page.fill_password()

    scroll_to_elem(register_page.browser, register_page.get_agree_switch())
    register_page.click_agree()

    scroll_to_elem(register_page.browser, register_page.get_continue_button())
    register_page.click_continue_button()
