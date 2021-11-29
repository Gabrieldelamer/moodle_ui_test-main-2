
from fixtures.locators.forgot_password import ForgotPasswordLocators

from fixtures.pages.base_page import BasePage

class ForgotPassPage(BasePage):
    def get_main_text(self):
        return self.get_text(locator=ForgotPasswordLocators.HAT_TEXT)

