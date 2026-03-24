import pytest


@pytest.mark.extended
def test_sale_title(sale_page, login_page):
    login_page.open()
    login_page.fill_login_form(login='standard_user', passw='secret_sauce')
    sale_page.open()
    assert sale_page.page_title_text == 'Swag Labs'
