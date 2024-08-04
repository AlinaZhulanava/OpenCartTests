from methods import get_elem_by_xpath, wait_elem_by_xpath, get_elem_by_id, wait_alert
from selenium.webdriver.common.by import By


class AdminPage:
    form_label_xpath = ("//div[text()="
                        "' Please enter your login details.']")
    email_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    user_email = "user"
    user_password = "bitnami"
    login_button_xpath = "//button[text()=' Login']"
    logout_button_xpath = "//span[text()='Logout']"
    avatar_xpath = "//img[@class='rounded-circle']"

    admin_menu_catalog_xpath = "//a[text()=' Catalog']"
    admin_menu_catalog_products_xpath = "//a[text()='Products']"

    add_product_button_xpath = "//a[@class='btn btn-primary']"
    save_product_button_xpath = "//button[@class='btn btn-primary']"
    new_product_name_id = "input-name-1"
    new_product_meta_tag_id = "input-meta-title-1"
    user_new_product_name = "product"
    user_new_product_meta_tag = "tag"
    new_product_data_xpath = "//a[text()='Data']"
    new_product_model_id = "input-model"
    user_new_product_model = "model"
    new_product_seo_xpath = "//a[text()='SEO']"
    new_product_seo_keyword_id = "input-keyword-0-1"
    user_new_product_seo_keyword = "1"

    alert_add_product_success_xpath = "//div[@class='alert alert-success alert-dismissible']"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def find_form_label(self):
        return wait_elem_by_xpath(self.browser, self.form_label_xpath)

    def get_email(self):
        return get_elem_by_xpath(self.browser, self.email_xpath)

    def fill_email(self):
        self.get_email().send_keys(self.user_email)

    def get_password(self):
        return get_elem_by_xpath(self.browser, self.password_xpath)

    def fill_password(self):
        self.get_password().send_keys(self.user_password)

    def get_login_button(self):
        return get_elem_by_xpath(self.browser, self.login_button_xpath)

    def click_login_button(self):
        self.get_login_button().click()

    def login(self):
        self.fill_email()
        self.fill_password()
        self.click_login_button()

    def get_logout_button(self):
        return get_elem_by_xpath(self.browser, self.logout_button_xpath)

    def click_logout_button(self):
        self.get_logout_button().click()

    def check_if_avatar_presented(self):
        return wait_elem_by_xpath(self.browser, self.avatar_xpath)

    def get_admin_menu_catalog(self):
        return get_elem_by_xpath(self.browser, self.admin_menu_catalog_xpath)

    def click_admin_menu_catalog(self):
        self.get_admin_menu_catalog().click()

    def find_admin_menu_catalog_products(self):
        return wait_elem_by_xpath(self.browser, self.admin_menu_catalog_products_xpath)

    def get_admin_menu_catalog_products_link(self):
        elem = get_elem_by_xpath(self.browser, self.admin_menu_catalog_products_xpath)
        return elem.get_attribute('href')

    def open_admin_menu_catalog_products(self):
        link = self.get_admin_menu_catalog_products_link()
        self.browser.get(link)

    def get_add_product_button(self):
        wait_elem_by_xpath(self.browser, self.add_product_button_xpath)
        return get_elem_by_xpath(self.browser, self.add_product_button_xpath)

    def click_add_product_button(self):
        self.get_add_product_button().click()

    def get_new_product_name(self):
        return get_elem_by_id(self.browser, self.new_product_name_id)

    def fill_new_product_name(self):
        self.get_new_product_name().send_keys(self.user_new_product_name)

    def get_new_product_meta_tag(self):
        return get_elem_by_id(self.browser, self.new_product_meta_tag_id)

    def fill_new_product_meta_tag(self):
        self.get_new_product_meta_tag().send_keys(self.user_new_product_meta_tag)

    def get_new_product_data(self):
        return get_elem_by_xpath(self.browser, self.new_product_data_xpath)

    def click_new_product_data(self):
        self.get_new_product_data().click()

    def get_new_product_seo(self):
        return get_elem_by_xpath(self.browser, self.new_product_seo_xpath)

    def click_new_product_seo(self):
        self.get_new_product_seo().click()

    def get_new_product_model(self):
        return get_elem_by_id(self.browser, self.new_product_model_id)

    def fill_new_product_model(self):
        self.get_new_product_model().send_keys(self.user_new_product_model)

    def get_new_product_seo_keyword(self):
        return get_elem_by_id(self.browser, self.new_product_seo_keyword_id)

    def fill_new_product_seo_keyword(self):
        self.get_new_product_seo_keyword().send_keys(self.user_new_product_seo_keyword)


    def get_save_product_button(self):
        return get_elem_by_xpath(self.browser, self.save_product_button_xpath)

    def click_save_product_button(self):
        self.get_save_product_button().click()

    def find_alert_add_product_success(self):
        return wait_elem_by_xpath(self.browser, self.alert_add_product_success_xpath)
