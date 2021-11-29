import logging

from fixtures.locators.login import LoginLocators
from fixtures.models.login import LoginData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def auth(self, data: LoginData, is_submit: bool = True):
        """
        Auth func
        Если мы не login  → login
        Если мы login → logout → login
        """
        logger.info(f"Login with user {data.login} and password {data.password}")
        self.fill_element(data=data.login, locator=LoginLocators.LOGIN_INPUT)
        self.fill_element(data=data.password, locator=LoginLocators.PASSWORD_INPUT)
        if is_submit:
            self.click_element(locator=LoginLocators.LOGIN_BTN)

    def _get_error_text(self) -> str:
        """
        Пример получения текста элемента!!!!
        """
        return self.get_text(locator=LoginLocators.ERROR_MESSAGE)

    def _popup_open(self):
        """Open popUp coockies"""
        self.click_element(locator=LoginLocators.POPUP_CLICK)

    def _popup_text(self):
        self.get_text(LoginLocators.POPUP_TEXT_WINDOW)

    def click_guest_login(self):
        self.click_element(LoginLocators.GUEST_LOGIN)

    def click_create_user(self):
        self.click_element(LoginLocators.CREATE_BTN)

    def click_forgot_pass(self):
        self.click_element(LoginLocators.FORGOT_LOG)