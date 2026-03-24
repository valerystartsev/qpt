from pages.base_page import BasePage
from pages.locators import sale_page_loc as loc



class SalePage(BasePage):
    page_url = '/inventory.html'

    @property
    def page_title_text(self):
        return self.find(loc.page_title).text
