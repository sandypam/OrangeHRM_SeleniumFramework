import pytest
import logging

from Pages.adminPage import AdminPage
from Testcases.BaseTest import BaseTest
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

@pytest.mark.usefixtures("logged_in")
class TestAdmin(BaseTest):

    def test_page_title(self, driver):
        log.logger.info("Test - page_title started")

        admin = AdminPage(driver).open()
        admin.assert_page_title("Admin")

        log.logger.info("Test - page_title ended")

    def test_search_for_user(self, driver):
        log.logger.info("Test - search_for_user started")

        admin = AdminPage(driver).open()
        admin.search_user("Admin")
        row = admin.find_user_row("Admin")

        assert row is not None, "Expected to find 'Admin' in Admin table results"

        log.logger.info("Test - search_for_user ended")