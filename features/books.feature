Feature: Books capability

  Background:
    Given home: I am a user on home page
    When home: I click on book store application card
    When books: I click on login button
    When login: I login with user_name "BogdanS" and password "Test123!"

  @regression
  Scenario: I validate the stock count
    Then books: I validate that 8 books are displayed

  @regression
  Scenario Outline: I validate that search is working
    When books: I search for "<query>"
    Then books: I validate that only "Git Pocket Guide" book is displayed

  Examples:
    | query   |
    | Git     |
    | Richard |

  @regression
  Scenario: I validate that clear search is working
    When books: I search for "test"
    When books: I clear search input
    Then books: I validate that 8 books are displayed