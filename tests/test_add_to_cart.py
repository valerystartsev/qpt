import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@allure.epic(AllureEpic.ADD2CART)
@allure.feature(AllureFeature.feature1)
@allure.story(AllureStory.STORY_A)
@pytest.mark.smoke
@allure.title("Check Add to Card button is enabled ")
def test_e2e_add_to_cart(home_page, product_page, category_page, login_page):
    login_page.open()
    login_page.fill_login_form(login='standard_user', passw='secret_sauce')
    home_page.open()
    home_page.open_jackets_submenu()
    #category_page.open_first_product()
    assert product_page.add_to_cart_button_is_enabled(), '"Add to cart" button is not enabled'
