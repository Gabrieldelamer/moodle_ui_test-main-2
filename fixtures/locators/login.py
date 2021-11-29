from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginbtn")
    ERROR_MESSAGE = (By.ID, "loginerrormessage")
    GUEST_LOGIN = (By.XPATH, "//form[@id='guestlogin']/button")
    REMEMBER_LOGIN = (By.ID, "rememberusername")
    FORGOT_LOG = (By.LINK_TEXT, "Забыли логин или пароль?")
    CREATE_BTN = (By.XPATH, "//button[contains(.,'Создать учетную запись')]")
