import pytest
import allure
from allure_commons.types import Severity

from tools.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


from pages.login_page import LoginPage


@allure.epic(AllureEpic.SALE)
@allure.feature(AllureFeature.feature2)
@allure.story(AllureStory.STORY_A)
@pytest.mark.extended
@allure.tag( AllureTag.SMOKE, AllureTag.REGRESSION)
@allure.title("Check Sale page is visible")
@allure.severity(Severity.TRIVIAL)
def test_sale_title(sale_page, login_page):
    login_page.open()
    login_page.fill_login_form(login='standard_user', passw='secret_sauce')
    sale_page.open()
    assert sale_page.page_title_text == 'Swag Labs'
