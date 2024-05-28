from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    # selectors
    CONFIRM_DELETE_BUTTON = '//button[@id="closeSmallModal-ok"]'

    # actions
    def click_delete_by_book_title(self, title):
        self.driver.find_element(By.XPATH, '//a[text()="' + title + '"]/parent::span/parent::div/parent::div/parent::div//span[@id="delete-record-undefined"]').click()

    def click_confirm_delete_button(self):
        self.wait_for_elem(self.CONFIRM_DELETE_BUTTON)
        self.driver.find_element(By.XPATH, self.CONFIRM_DELETE_BUTTON).click()

    # validations
    def validate_book_displayed(self, title):
        books_list = self.driver.find_elements(By.XPATH, '//a[text()="' + title + '"]')
        self.assertEqual(1, len(books_list), 'Book is not present')

    def validate_book_not_displayed(self, title):
        sleep(1)
        self.driver.implicitly_wait(2)
        books_list = self.driver.find_elements(By.XPATH, '//a[text()="' + title + '"]')
        self.assertEqual(0, len(books_list), 'Book is present')
        self.driver.implicitly_wait(5)
