import logging
import pytest

from Pages.loginPage import LoginPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider, configReader
from Utilities.credentials import get_credentials
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def reset_to_login(self):
        # Hard reset session so next test starts logged out
        self.driver.delete_all_cookies()

        loginPage = LoginPage(self.driver)
        loginPage.open()

        # Sanity wait: confirm we really are on login page
        loginPage.wait_for_visible("username_NAME", timeout=10)

    def test_loginSuccessful(self):
        username, password = get_credentials()

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

        assert "Invalid credentials" in loginPage.get_error_message()

        log.logger.info("Test - loginFailed ended")


