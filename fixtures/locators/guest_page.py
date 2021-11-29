from selenium.webdriver.common.by import By

from fixtures.constants import Objects


class GuestLocators:
    TEST_MODULE = (By.LINK_TEXT, Objects.ENTER_LINK)
    EXIT_LINK = (By.LINK_TEXT, Objects.EXIT_LINK)