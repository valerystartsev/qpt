import pytest


@pytest.mark.regression
def test_incorrect_pass(login_page):
    login_page.open()
    login_page.fill_login_form(login='user@mail.com', passw='qwqwqwqw')
    assert login_page.error_text == (
        'Epic sadface: Username and password do not match any user in this service'
    )

@pytest.mark.regression
def test_locked_pass(login_page):
    login_page.open()
    login_page.fill_login_form(login='locked_out_user1', passw='secret_sauce')
    assert login_page.error_text == (
        'Epic sadface: Sorry, this user has been locked out.'
    )


"""
Epic sadface: Username and password do not match any user in this service
"""