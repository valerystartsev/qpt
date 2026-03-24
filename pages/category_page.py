from pages.base_page import BasePage
from pages.locators import category_page_loc as loc


class CategoryPage(BasePage):
    page_url = None

    def __init__(self, driver, category_url=None):
        super().__init__(driver)
        self.category_url = category_url

    def open(self,):
        if self.category_url:
            self.driver.get(f'{self.base_url}{self.category_url}')
        else:
            raise NotImplementedError('Category URL should be passed to object be able to open the page by URL')

    def open_first_product(self):
        self.find(loc.first_product).click()
