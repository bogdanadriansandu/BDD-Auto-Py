from pages.login_page import LoginPage
from behave import *

login_page = LoginPage()


@when('login: I login with user_name "{user_name}" and password "{password}"')
def step_impl(context, user_name, password):
    login_page.fill_username_input(user_name)
    login_page.fill_password_input(password)
    login_page.click_login_button()


@then('login: I validate that error message is displayed')
def step_impl(context):
    login_page.validate_error_message()
