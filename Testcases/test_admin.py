import pytest
import logging

from Pages.adminPage import AdminPage
from Testcases.BaseTest import BaseTest
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

@pytest.mark.usefixtures("logged_in")
class TestAdmin(BaseTest):

    def test_search_for_user(self):
        log.logger.info("Test - search_for_user started")

        def test_search_for_user(self):
            admin = AdminPage(self.driver).open()
            admin.search_user("Admin")
            row = admin.find_user_row("Admin")
            assert row is not None

        log.logger.info("Test - search_for_user ended")

    # def test_record_found(self):
    #     row = self.wait_for_visible("user_row_XPATH", username="Admin")
    #     assert row is not None
    #
    #
    # def test_record_not_found(self):
    #     pass