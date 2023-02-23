Feature:Test the jules app webpage

  Background:
    Given Home page: I am on jules app homepage


  @t1
  Scenario:Check Sign in page functionality
    When Sign in: Input "good.email@yahoo.com" leave password text box empty
    Then Sign in: Verify error ‘Please enter your password!’ is displayed
    Then Sign in: Verify Log in button is enabled

  @t2
  Scenario: Check the urls of sign in and sign up page
    When Sign in: Click sign up button
    Then Sign up: Verify ulr of the sign up page
    When Sign up: Click log in button
    Then Sign in: Verify url of the sign in page

  @t3
  Scenario Outline: Check the Sign up  page functionality
    When Sign in: Click sign up button
    When Sign up: Click personal and click Continue button
    When Sign up: Input "<first_name>" and click Continue button
    When Sign up: Input "<last_name>" and  Continue
    When Sign up: Input "<wrong_email>"
    Then Sign up: Verify that error message is displayed
    Then Sign up: Write a "<correct_email>" address
    Examples:
      | first_name | last_name | wrong_email | correct_email      |
      |Ilie        |Moromete   |bad_email    |good_email@gmail.com|
      |John        |Kennedy    |ken          |kennedy@yahoo.com   |
      |Margaret    |Tacher     |margi        |tacher@gmail.com    |





