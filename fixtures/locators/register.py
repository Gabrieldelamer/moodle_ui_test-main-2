from selenium.webdriver.common.by import By


class RegisterLocators:
    LOGIN_INPUT = (By.ID, "id_username")
    PASSWORD_INPUT = (By.ID, "id_password")
    EMAIL_1 = (By.ID, "id_email")
    EMAIL_2 = (By.ID, "id_email2")
    NAME = (By.ID, "id_firstname")
    SURNAME = (By.ID, "id_lastname")
    CITY = (By.ID, "id_city")
    SUBMIT_BTN = (By.ID, "id_submitbutton")
    ERROR_FIRST_NAME = (By.ID, "id_error_firstname")
    ERROR_PASSWORD = (By.ID, "id_error_password")
    ERROR_LOGIN = (By.ID, "id_error_username")

    ERROR_FIELD = (By.CLASS_NAME, "form-control-feedback invalid-feedback")




    HAT_TEXT = (By.XPATH, "//h2[contains(.,'test_moodle_2021')]")