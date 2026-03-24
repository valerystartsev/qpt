from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement


def sdfds(locator, elt):
    return elt.find_element(*locator)


class BasePage:
    base_url = 'https://www.saucedemo.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('This page can not be opened by URL')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @staticmethod
    def find_in_elt(locator, elt: WebElement):
        return elt.find_element(*locator)

    @staticmethod
    def find_all_in_elt(locator, elt: WebElement):
        return elt.find_elements(*locator)

    def scroll_page(self, pixel=None):
        if pixel:
            self.driver.execute_script(f'window.scrollTo(0, {pixel});')
        else:
            self.driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight);')

