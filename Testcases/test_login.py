import os
import logging

import pytest

from Pages.loginPage import LoginPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class TestLogin(BaseTest):

    def test_loginSuccessful(self):
        username = os.getenv("ORANGEHRM_USERNAME")
        password = os.getenv("ORANGEHRM_PASSWORD")

        log.logger.info("Test - loginSuccessful started")

        loginPage = LoginPage(self.driver)
        loginPage.login(username, password)

        title = loginPage.title()
        assert title.strip() == "Dashboard"

        log.logger.info("Test - loginSuccessful ended")

    @pytest.mark.parametrize("username,password", dataProvider.get_data("LoginTest"))
    def test_loginFailed(self, username, password):
        log.logger.info("Test - loginFailed started")

        loginPage = LoginPage(self.driver)
        loginPage.login(username, password)

        error_message = loginPage.get_error_message()
        assert "Invalid credentials" in error_message

        log.logger.info("Test - loginFailed ended")


