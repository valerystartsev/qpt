from pages.locators import login_page_loc as loc
from pages.base_page import BasePage


class LoginPage(BasePage):
    page_url = ' '

    def fill_login_form(self, login, passw):
        self.find(loc.email).send_keys(login)
        self.find(loc.password).send_keys(passw)
        self.find(loc.send_button).click()

    @property
    def error_text(self):
        return self.find(loc.error_panel).text
