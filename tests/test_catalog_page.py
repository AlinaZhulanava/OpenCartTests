from CatalogPage import CatalogPage
from TopPanel import TopPanel


def test_search_for_product_list(browser, get_url):
    catalog_page = CatalogPage(browser, get_url + "en-gb/catalog/desktops")
    catalog_page.open_page()

    assert catalog_page.find_catalog_product_list() is True

def test_prices_change_in_catalog_when_change_currency(browser, get_url):
    catalog_page = CatalogPage(browser, get_url + "catalog/desktops")
    catalog_page.open_page()

    prices_list = catalog_page.get_list_of_all_prices_from_table()

    top_panel = TopPanel(browser)
    top_panel.click_currency_choose_button()
    top_panel.click_euro_button()

    prices_list_changed = catalog_page.get_list_of_all_prices_from_table()

    assert prices_list != prices_list_changed