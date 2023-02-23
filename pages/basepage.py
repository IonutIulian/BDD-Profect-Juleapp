from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser






class Base_page(Browser):

    def verify_url(self,url):
        actual_url = self.driver.current_url
        assert actual_url == url,f"Wrong url, actual:{actual_url}, expected:{url}"

    def wait_and_click_element_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
        self.driver.find_element(by, selector).click()