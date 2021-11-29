from fixtures.locators.guest_page import GuestLocators
from fixtures.pages.base_page import BasePage

class GuestPage(BasePage):
    def get_main_text(self):
        return self.get_text(locator=GuestLocators.TEST_MODULE)

    def find_exit_link(self):
        return self.get_text(locator=GuestLocators.EXIT_LINK)
