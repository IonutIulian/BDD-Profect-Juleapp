from browser import Browser
from pages.basepage import Base_page
from pages.signin_page import Signin_page
from pages.signup_page import Signup_page



def before_all(context):
    context.browser = Browser()
    context.basepage = Base_page()
    context.signin_page_object = Signin_page()
    context.signup_page_object = Signup_page()

def after_all(context):
    context.browser.close()