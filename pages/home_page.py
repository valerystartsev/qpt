from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from pages.locators import home_page_loc as loc


class HomePage(BasePage):
    page_url = '/inventory.html'

    def open_second_tier_menu_item(self, menu_item, first_tier_item, target_item):
        actions = ActionChains(self.driver)

    def open_jackets_submenu(self):
        # women = self.find(loc.women)
        # tops = self.find(loc.tops)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find(loc.women))
        actions.move_to_element(self.find(loc.tops))
        actions.click(self.find(loc.jackets))
        actions.perform()

