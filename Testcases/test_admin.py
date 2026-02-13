import pytest
import logging
import os

from Pages import adminPage
from Testcases.BaseTest import BaseTest
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

@pytest.mark.usefixtures("logged_in")
class TestAdmin(BaseTest):

    def test_search_for_user(username):
        username = os.getenv("ORANGEHRM_USERNAME")
        password = os.getenv("ORANGEHRM_PASSWORD")

        log.logger.info("Test - search for user started")

    def test_record_found(user):
        row = adminPage.find_user_row("Admin")
        assert row is not None


    def test_record_not_found(user):
        pass