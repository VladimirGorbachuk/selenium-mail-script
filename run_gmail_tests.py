import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import page
import locators
import time
import dotenv
from private_information import GMAIL_PASSWORD, GMAIL_USERNAME, EXECUTOR_HUB

class GMailLettersCounting(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Remote(
        #    command_executor=EXECUTOR_HUB,
        #    desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.google.com')
        self.wait = WebDriverWait(self.driver, 100)

    def test_enter_login_proceed(self):
        
        self.login()
        self.search_count_letters_from()
        

    def tearDown(self):
        self.driver.close()

    def login(self):
        
        login_page = page.LoginPage(self.driver)
        login_page.enter_login_and_press_enter(GMAIL_USERNAME)
        
        password_page = page.PasswordPage(self.driver)
        password_page.enter_password_and_press_enter(GMAIL_PASSWORD)
        time.sleep(5)  # for two-factor authentication


    def search_count_letters_from(self):
        main_mail_page = page.MainMailPage(self.driver)
        main_mail_page.enter_search_from_query_and_press_enter(
            'from: blizzard')
        self.num_of_letters = main_mail_page.get_num_of_letters()
        print(self.num_of_letters)


if __name__ == "__main__":
    unittest.main()
