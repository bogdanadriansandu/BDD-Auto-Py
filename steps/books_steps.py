from pages.books_page import BooksPage
from behave import *


books_page = BooksPage()


@when('books: I click on login button')
def step_impl(context):
    books_page.click_login_button()


@when('books: I search for "{query}"')
def step_impl(context, query):
    books_page.fill_search_input(query)


@when('books: I add to collection the book with title "{title}"')
def step_impl(context, title):
    books_page.click_book_by_title(title)
    books_page.click_add_to_your_collection_button()
    # books_page.alert_ok()
    # books_page.click_back_to_bookstore_button()
    books_page.browser_back()


@when('books: I clear search input')
def step_impl(context):
    books_page.clear_search_input()


@then('books: I should land on books page')
def step_impl(context):
    books_page.validate_correct_url()


@then('books: I validate that 8 books are displayed')
def step_impl(context):
    books_page.validate_books_count(8)


@then('books: I validate that only "{title}" book is displayed')
def step_impl(context, title):
    books_page.validate_books_count(1)
    books_page.validate_book_title(title)
