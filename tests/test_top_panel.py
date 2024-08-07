import allure
from TopPanel import TopPanel


def test_change_currency(browser, get_url):
    with allure.step(f"Open {get_url} in {browser}"):
        top_panel = TopPanel(browser, get_url)
        top_panel.open_page()

    chosen_currency = top_panel.get_displayed_currency()
    currency_change_chain = [chosen_currency]

    if chosen_currency == "USD":
        currency_change_chain.append("EUR")
        currency_change_chain.append("GBP")
    elif chosen_currency == "EUR":
        currency_change_chain.append("USD")
        currency_change_chain.append("GBP")
    elif chosen_currency == "GBP":
        currency_change_chain.append("USD")
        currency_change_chain.append("EUR")

    with allure.step("Checking the chain of switching all currencies"):
        top_panel.change_currency_to_another(currency_change_chain[1])
        assert top_panel.get_displayed_currency() == currency_change_chain[1]
        top_panel.change_currency_to_another(currency_change_chain[2])
        assert top_panel.get_displayed_currency() == currency_change_chain[2]
        top_panel.change_currency_to_another(currency_change_chain[0])
        assert top_panel.get_displayed_currency() == currency_change_chain[0]
        top_panel.change_currency_to_another(currency_change_chain[2])
        assert top_panel.get_displayed_currency() == currency_change_chain[2]
        top_panel.change_currency_to_another(currency_change_chain[1])
        assert top_panel.get_displayed_currency() == currency_change_chain[1]
        top_panel.change_currency_to_another(currency_change_chain[0])
        assert top_panel.get_displayed_currency() == currency_change_chain[0]
