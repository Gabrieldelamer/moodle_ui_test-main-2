from logging import Logger
from time import sleep

from fixtures.constants import Errors, Objects
from fixtures.models.register import RegisterData
import pytest
import logging

logger: Logger = logging.getLogger("moodle")

class TestRegistration:
    def test_registration_with_valid_data(self, app, user_data):
        """
        Steps:
        1. Open register page
        2. Add valid data
        3. Check result
        """
        app.open_register_page()
        data = RegisterData.random()
        app.register.add_new_user(data, 0)

        assert 1 == 1

    def test_registration_with_empty_name(self, app, user_data):
        """
        Steps:
        1. Open register page
        2. Add data with empty name
        3. Check result
        """
        app.open_register_page()
        data = RegisterData.random()
        setattr(data, "login", None)
        app.register.add_new_user(data)
        text  = app.register.get_error_name()
        assert text == Errors.ERROR_FIRST_NAME, "Check error first name"

    @pytest.mark.parametrize("field", ["password", "email_2", "name", "surname"])
    def test_empty_val(self, app, user_data, field):
        app.open_register_page()
        data = RegisterData.random()
        setattr(data, field, None)
        app.register.add_new_user(data)
        text = app.register.get_error_appear()
        assert text == Objects.NEW_USER
