url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_button_add_to_busket(browser):
    browser.get(url)
    add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket').is_displayed()

    assert add_to_basket, 'The "Add to basket" button is not visible'
