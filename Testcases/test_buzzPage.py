import logging
import pytest

from Pages.buzzPage import BuzzPage
from Testcases.BaseTest import BaseTest
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

@pytest.mark.usefixtures("logged_in")
class TestBuzzPage(BaseTest):

    def test_page_title(self, driver):
        log.logger.info("Test - page_title started")

        buzz = BuzzPage(driver)
        buzz.open_buzz()
        buzz.assert_page_title("Buzz")

        log.logger.info("Test - page_title ended")