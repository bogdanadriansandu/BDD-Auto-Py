from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(5)
    driver.maximize_window()

    def close(self):
        self.driver.quit()
        