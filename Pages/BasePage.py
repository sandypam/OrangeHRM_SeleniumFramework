from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Utilities import configReader
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    LOCATOR_MAP = {
        "_XPATH": By.XPATH,
        "_CSS": By.CSS_SELECTOR,
        "_ID": By.ID,
        "_NAME": By.NAME,
        "_CLASS": By.CLASS_NAME,
    }

    def _by(self, locator_key: str):
        """Infer Selenium By strategy from locator key suffix."""
        key = str(locator_key)

        for suffix, by in self.LOCATOR_MAP.items():
            if key.endswith(suffix):
                return by

        raise ValueError(
            f"Unsupported locator key suffix '{locator_key}'. "
            f"Supported suffixes: {list(self.LOCATOR_MAP.keys())}"
        )

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

    def move_to(self, locator_key, context=None, timeout=10):
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

    def is_visible(self, locator_key, timeout=10):
        try:
            self.wait_for_visible(locator_key, timeout)
            return True
        except TimeoutException:
            log.logger.info(f"Element not visible: {locator_key}")
            return False

    def get_text(self, locator_key, timeout=10, strip=True):
        text = self.wait_for_visible(locator_key, timeout).text
        return text.strip() if strip else text

    def wait_for_clickable(self, locator_key, timeout=10):
        """Wait until the element located by the key is clickable and return it."""
        by = self._by(locator_key)
        value = self._locator_value(locator_key)
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )






