# we import selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# we initialize chrome
chrome = webdriver.Chrome()

# we maximize the window
chrome.maximize_window()

# we navigate to an url
chrome.get('https://the-internet.herokuapp.com/login')

# with "sleep" we can pause for a few seconds so that we can wait in order to see something
sleep(2)

# we fill in the username
chrome.find_element(By.ID, 'username').send_keys('tomsmith')

# we fill in the password
chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')

# we click on login button
chrome.find_element(By.XPATH, '//i[text()=" Login"]').click()

# we check that you have reached the correct page
expected_page = 'https://the-internet.herokuapp.com/secure'
actual_page = chrome.current_url
assert expected_page == actual_page, f'Incorrect url, was expecting {expected_page}'

# we close chrome
chrome.quit()

# if the test passed, we print a success message in the console
print('SUCCESS - TEST PASSED')
