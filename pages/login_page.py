from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # selectors
    USERNAME_INPUT = '//input[@id="userName"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//button[@id="login"]'
    INVALID_CREDENTIALS_ERROR = '//p[@id="name"]'

    # actions
    def fill_username_input(self, user_name):
        self.wait_for_elem(self.USERNAME_INPUT)
        self.driver.find_element(By.XPATH, self.USERNAME_INPUT).send_keys(user_name)

    def fill_password_input(self, password):
        self.wait_for_elem(self.PASSWORD_INPUT)
        self.driver.find_element(By.XPATH, self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    # validations
    def validate_error_message(self):
        sleep(1)
        self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = 'Invalid username or password!'
        actual = self.driver.find_element(By.XPATH, self.INVALID_CREDENTIALS_ERROR).text
        self.assertEqual(expected, actual, 'Error message is incorrect!')
