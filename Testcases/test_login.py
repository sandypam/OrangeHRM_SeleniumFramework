import logging
import pytest

from Pages.loginPage import LoginPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.credentials import get_credentials
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def reset_to_login(self, driver):
        # Hard reset session so next test starts logged out
        driver.delete_all_cookies()

        loginPage = LoginPage(driver)
        loginPage.open()

        # Sanity wait: confirm we really are on login page
        loginPage.wait_for_visible("username_NAME", timeout=10)

    def test_loginSuccessful(self, driver):
        username, password = get_credentials()

        log.logger.info("Test - loginSuccessful started")

        loginPage = LoginPage(driver)
        loginPage.login(username, password)

        title = loginPage.get_page_title()
        assert title.strip() == "Dashboard"

        log.logger.info("Test - loginSuccessful ended")

    @pytest.mark.parametrize("username,password", dataProvider.get_data("LoginTest"))
    def test_loginFailed(self, driver, username, password):
        log.logger.info("Test - loginFailed started")

        loginPage = LoginPage(driver)
        loginPage.login(username, password)

        assert "Invalid credentials" in loginPage.get_error_message()

        log.logger.info("Test - loginFailed ended")

    def test_page_title(self, driver):
        username, password = get_credentials()

        log.logger.info("Test - page_title started")

        loginPage = LoginPage(driver)
        loginPage.login(username, password)

        loginPage.assert_page_title("Dashboard")

        log.logger.info("Test - page_title ended")