import pytest
import allure
from allure_commons.types import Severity

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.parametrize(
    "email, password",
    [
        ("user@mail.com", "qwqwqwqw"),
        ("problem_user", "secret_sauce" ),
        ("another@mail.com", "qwqwqwqw")
    ]
)

@allure.epic(AllureEpic.LOGIN)
@allure.feature(AllureFeature.feature3)
@allure.story(AllureStory.STORY_C)
@pytest.mark.regression
@allure.title('Login with wrong password')
@allure.description('Login with wrong password')
@allure.severity(Severity.BLOCKER)
def test_incorrect_pass(login_page, email: str, password: str ):
    #allure.dynamic.title(f"Login with wrong password: {email}, {password}")
    login_page.open()
    login_page.fill_login_form(login=email, passw=password)
    assert login_page.error_text == (
        'Epic sadface: Username and password do not match any user in this service'
    )

@allure.epic(AllureEpic.LOGIN)
@allure.feature(AllureFeature.feature3)
@allure.story(AllureStory.STORY_A)

@pytest.mark.regression
@allure.title('Login with locked user')
@allure.description('Attempt to login with locked user, should show correct message')
@allure.severity(Severity.CRITICAL)
def test_locked_pass(login_page):
    login_page.open()
    login_page.fill_login_form(login='locked_out_user', passw='secret_sauce')
    assert login_page.error_text == (
        'Epic sadface: Sorry, this user has been locked out.'
    )


"""
Epic sadface: Username and password do not match any user in this service
"""