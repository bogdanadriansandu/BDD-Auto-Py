from time import sleep
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class BasePage(Browser, unittest.TestCase):

    def wait_for_elem(self, xpath_selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_selector)))

    def browser_back(self):
        self.driver.back()

    def alert_ok(self):
        sleep(1)
        self.driver.switch_to.alert.accept()

    def refresh_page(self):
        self.driver.refresh()

