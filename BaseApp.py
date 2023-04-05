from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import logging
import pytest


class SeleniumActions:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://health-fitness.io/'

    def wait_until(self, locator=None, expectation=None, timeout=5):
        if locator is None or expectation is None:
            return logging.getLogger().info("[wait][until] No all the parameters specified.")

        return WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        ).until(
            expectation(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_element_clickable(self, locator, timeout=10):
        return self.wait_until(locator, EC.element_to_be_clickable, timeout)

    def find_elements(self, locator, timeout=70):
        return self.wait_until(locator, EC.presence_of_all_elements_located, timeout)

    def loadUrl(self, url=''):
        return self.driver.get(self.base_url + url)



