import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.basepage import Base_page



class Signup_page(Base_page):

    LOGIN_BUTTON = (By.XPATH,"//button[@data-test-id='go-to-login-btn']")
    PERSONAL_CHECKBOX = (By.XPATH,"//input[@value='personal']")
    CONTINUE_BUTTON = (By.XPATH,"//button[@data-test-id='select-account-continue-btn']")
    TEXT_BOX = (By.XPATH,"//input[@aria-invalid='false']")
    VERIFICATION_MESSAGE = (By.XPATH,"//p[text()='Please enter a valid email address.']")
    CONTINUE_BUTTON1 = (By.XPATH,"//button[@data-test-id='first-name-continue-btn']")
    CONTINUE_BUTTON2 = (By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button')

    def login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def personal_check_continue(self):
        time.sleep(2)
        self.wait_and_click_element_by_selector(*self.PERSONAL_CHECKBOX)
        time.sleep(2)
        self.wait_and_click_element_by_selector(*self.CONTINUE_BUTTON)

    def first_name_continue(self, first_name):
        self.driver.find_element(*self.TEXT_BOX).send_keys(first_name)
        self.wait_and_click_element_by_selector(*self.CONTINUE_BUTTON1)


    def last_name_continue(self, last_name):
        time.sleep(2)
        self.driver.find_element(*self.TEXT_BOX).send_keys(last_name)
        self.wait_and_click_element_by_selector(*self.CONTINUE_BUTTON2)



    def wrong_email(self, wrong_email):
        time.sleep(2)
        self.driver.find_element(*self.TEXT_BOX).send_keys(wrong_email)



    def verify_message(self):

        assert self.driver.find_element(*self.VERIFICATION_MESSAGE).is_displayed(),"Please enter a valid email address."
        time.sleep(1)
        self.driver.find_element(*self.TEXT_BOX).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*self.TEXT_BOX).send_keys(Keys.BACK_SPACE)

    def correct_email(self,correct_email):
        time.sleep(2)
        self.driver.find_element(*self.TEXT_BOX).send_keys(correct_email)


