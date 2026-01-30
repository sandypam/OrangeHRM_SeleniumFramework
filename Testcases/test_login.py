import os
import logging

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
        title = loginPage.login(username, password)
        assert title.strip() == "Dashboard"
        log.logger.info("Test - loginSuccessful ended")