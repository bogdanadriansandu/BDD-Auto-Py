Feature: Login capability

  Background:
    Given home: I am a user on home page
    When home: I click on book store application card
    When books: I click on login button

  @smoke
  Scenario: I login with valid credentials
    When login: I login with user_name "BogdanS" and password "Test123!"
    Then books: I should land on books page

  @regression
  Scenario Outline: I login with invalid credentials
    When login: I login with user_name "<user_name>" and password "<password>"
    Then login: I validate that error message is displayed

  Examples:
    | user_name | password |
    | BogdanS   | Test123  |
    | BgdS      | Test1234 |
