from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.login_page import LoginPage
from pages.sale_page import SalePage
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from time import sleep
import random
import allure
from allure_commons.types import AttachmentType


@pytest.fixture()
def driver():
    options = Options()

    #options = ChromiumOptions()
    # Set preferences
    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False  # Important preference
    }
    options.add_experimental_option('prefs', chrome_prefs)

    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,800')


    chrome_driver = webdriver.Chrome(options=options)
    # sleep(3)
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    # filename = f'{str(random.randint(100, 10000))}.png'
    # chrome_driver.save_screenshot(filename)
    # Check if the test failed, then take a screenshot
    #if request.node.rep_call.failed:
    #    allure.attach(chrome_driver.get_screenshot_as_png(),
    #                  name="Screenshot",
    #                  attachment_type=AttachmentType.PNG)

    chrome_driver.quit()

def pytest_runtest_makereport(item, call):
    """ Capture the result of the test (pass/fail) after it runs """
    if call.when == 'call' and call.excinfo is not None:
        # Test failed, take a screenshot
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=AttachmentType.PNG
            )

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def category_page(driver):
    return CategoryPage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)
