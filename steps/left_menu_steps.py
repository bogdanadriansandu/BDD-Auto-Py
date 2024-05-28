from pages.left_menu import LeftMenu
from behave import *


left_menu = LeftMenu()


@when('menu: I click on profile section')
def step_impl(context):
    left_menu.click_profile_section()
