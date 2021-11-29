import pytest

from fixtures.constants import Errors
from fixtures.constants import Objects
from fixtures.models.login import LoginData


class TestLogin:
    def test_login_with_valid_data(self, app, user_data):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        app.open_login_page()
        app.login.auth(data=user_data, is_submit=True)
        text = app.guest.find_exit_link()
        assert text == Objects.EXIT_LINK

    def test_login_with_invalid_data(self, app):
        """
        Steps:
        1. Open login page
        2. Auth with invalid data
        3. Check result
        """
        app.open_login_page()
        data = LoginData.random()
        app.login.auth(data)
        errormessage = app.login._get_error_text()
        assert errormessage == Errors.ERROR_LOGOPASS


    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_with_password(self, app, field):
      """
     Steps:
     1. Open login page
     2. Auth with invalid data
     3. Check result
     """
      app.open_login_page()
      data = LoginData.random()
      setattr(data, field, None)
      data = LoginData(login=data.login, password=None)
      app.login.auth(data)
      errorbox = app.login._get_error_text()
      assert errorbox == Errors.ERROR_LOGOPASS


    def test_forgot_password(self, app):
      """
      Steps:
      1. Open Login page
      2. Click Забыли пароль
      3. Check Result
      """
      app.open_login_page()
      app.login.click_forgot_pass()
      hat_text = app.forgotpass.get_main_text()
      assert Objects.HAT_TEXT == hat_text


    def test_guest_login(self, app):
      """
      Steps:
      1. Open Login page
      2. Click Зайти гостем
      3. Check Result
      """
      app.open_login_page()
      app.login.click_guest_login()
      text = app.guest.get_main_text()
      assert text == Objects.ENTER_LINK


    def test_create_user_button(self, app):
     """
     Steps:
     1. Open Login page
     2. Click Зайти гостем
     3. Check Result
     """
     app.open_login_page()
     app.login.click_create_user()
     text = app.register.get_page_exist()
     assert text == Objects.HAT_TEXT
