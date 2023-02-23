from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.basepage import Base_page


class Signin_page(Base_page):
    EMAIL_TEXTBOX = (By.XPATH,"//input[@placeholder='Enter your email']")
    PASSS_TEXTBOX = (By.XPATH,"//input[@placeholder='Enter your password']")
    ERROR_MSG = (By.XPATH,"//*[@id='root']/div/div[2]/form/div/div[2]/div/p")
    LOGIN_BUTTON = (By.XPATH,"//button[@data-test-id='login-button']")
    SIGNUP_BUTTON = (By.XPATH,"//a[@data-test-id='sign-up-link']")


    def navigate_to_signinpage(self):
        self.driver.get("https://jules.app/sign-in")

    def input_email_no_pass(self,email):
        self.driver.find_element(*self.EMAIL_TEXTBOX).send_keys(email)
        self.driver.find_element(*self.PASSS_TEXTBOX).send_keys("a")
        self.driver.find_element(*self.PASSS_TEXTBOX).send_keys(Keys.BACKSPACE)

    def verify_error_smg(self):
        assert self.driver.find_element(*self.ERROR_MSG).is_displayed(),"Error message not displayed"

    def login_enabled(self):
        assert  not self.driver.find_element(*self.LOGIN_BUTTON).is_enabled(),"Login button enabled"

    def signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()




