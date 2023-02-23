from behave import *


@given ("Home page: I am on jules app homepage")
def step_impl(context):
    context.signin_page_object.navigate_to_signinpage()

@when ('Sign in: Input "{email}" leave password text box empty')
def step_impl(context, email):
    context.signin_page_object.input_email_no_pass(email)

@then ("Sign in: Verify error ‘Please enter your password!’ is displayed")
def step_impl(context):
    context.signin_page_object.verify_error_smg()

@then ("Sign in: Verify Log in button is enabled")
def step_impl(context):
    context.signin_page_object.login_enabled()

@when ("Sign in: Click sign up button")
def step_impl(context):
    context.signin_page_object.signup_button()

@then ("Sign in: Verify url of the sign in page")
def step_impl(context):
    context.basepage.verify_url("https://jules.app/sign-in")
