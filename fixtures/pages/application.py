from fixtures.pages.login import LoginPage
from fixtures.pages.register import RegisterPage
from fixtures.pages.guest_page import GuestPage
from fixtures.pages.forgot_password import ForgotPassPage

class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.register = RegisterPage(self)
        self.forgotpass = ForgotPassPage(self)
        self.guest = GuestPage(self)

    def quit(self):
        self.driver.quit()

    def open_login_page(self):
        self.driver.get(self.url)

    def open_register_page(self):
        self.driver.get("https://qacoursemoodle.innopolis.university/login/signup.php?")

