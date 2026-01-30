from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import configReader
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _by(self, locator_key: str):
        """Infer By strategy from key suffix like name_CSS, submit_XPATH, etc."""
        key = str(locator_key)
        if key.endswith("_XPATH"):
            return By.XPATH
        if key.endswith("_CSS"):
            return By.CSS_SELECTOR
        if key.endswith("_ID"):
            return By.ID
        if key.endswith("_NAME"):
            return By.NAME
        raise ValueError(f"Unsupported locator key suffix: {locator_key}")

    def _locator_value(self, locator_key: str) -> str:
        """Read the locator value from config.ini using the provided key."""
        return configReader.readConfig("Locators", locator_key)

    def click(self, locator_key, timeout=10):
        by = self._by(locator_key)
        value = self._locator_value(locator_key)
        log.logger.debug(f"Attempting click: {locator_key} -> {value}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        log.logger.info(f"Clicked locator: {locator_key}")

    def type(self, locator_key, text, timeout=10, clear=True):
        by = self._by(locator_key)
        value = self._locator_value(locator_key)
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        if clear:
            element.clear()
        element.send_keys(str(text))
        log.logger.info(f"Typed into locator: {locator_key}")

    def select(self, locator_key, visible_text, timeout=10):
        by = self._by(locator_key)
        value = self._locator_value(locator_key)

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

        Select(element).select_by_visible_text(visible_text)
        log.logger.info(f"Selected '{visible_text}' from dropdown: {locator_key}")

    def moveTo(self, locator_key, context=None, timeout=10):
        by = self._by(locator_key)
        value = self._locator_value(locator_key)

        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info(f"Move to locator: {locator_key} ({context})")

    def wait_for_visible(self, locator_key, timeout=10):
        by = self._by(locator_key)
        value = self._locator_value(locator_key)
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def get_text(self, locator_key, timeout=10):
        el = self.wait_for_visible(locator_key, timeout)
        return el.text