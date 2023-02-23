from behave import *


@then ("sign up: Verify ulr of the sign up page")
def step_impl(context):
    context.basepage.verify_url("https://jules.app/sign-up")

@when ("Sign up: Click log in button")
def step_impl(context):
    context.signup_page_object.login_button()

@when ("Sign up: Click personal and click Continue button")
def step_impl(context):
    context.signup_page_object.personal_check_continue()

@when ('Sign up: Input "{first_name}" and click Continue button')
def step_impl(context, first_name):
    context.signup_page_object.first_name_continue(first_name)

@when ('Sign up: Input "{last_name}" and  Continue')
def step_impl(context, last_name):
    context.signup_page_object.last_name_continue(last_name)

@when ('Sign up: Input "{wrong_email}"')
def step_impl(context, wrong_email):
    context.signup_page_object.wrong_email(wrong_email)

@then ("Sign up: Verify that error message is displayed")
def step_impl(context):
    context.signup_page_object.verify_message()

@then ('Sign up: Write a "{correct_email}" address')
def step_impl(context, correct_email):
    context.signup_page_object.correct_email(correct_email)




