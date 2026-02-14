import pytest
import logging

from Pages import adminPage
from Testcases.BaseTest import BaseTest
from Utilities.LogUtil import Logger
from Utilities.credentials import get_credentials

log = Logger(__name__, logging.INFO)

@pytest.mark.usefixtures("logged_in")
class TestAdmin(BaseTest):

    def test_search_for_user(self):
        pass

    def test_record_found(self):
        row = self.wait_for_visible("user_row_XPATH", username="Admin")
        assert row is not None


    def test_record_not_found(self):
        pass