import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import page
import locators
import time
from private_information import GMAIL_PASSWORD, GMAIL_USERNAME, EXECUTOR_HUB, EMAIL_AUTHOR_TO_FIND, MY_SURNAME, EMAIL_SEND_TO

import pytest
import allure

class GMailLettersCounting(unittest.TestCase):

    def setUp(self):
        #self.driver=webdriver.Chrome()#TODO:delete this line
        self.driver = webdriver.Remote(
            command_executor=EXECUTOR_HUB,
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        self.driver.get('https://mail.google.com')
        self.wait = WebDriverWait(self.driver, 100)

    @allure.testcase("login, count letters from specific person and send him a letter")
    def test_enter_login_proceed(self):
        self.login()
        self.search_count_letters_from()
        self.write_letters_to()
        

    def tearDown(self):
        self.driver.close()

    @allure.step('login')
    def login(self):
        
        login_page = page.LoginPage(self.driver)
        login_page.enter_login_and_press_enter(GMAIL_USERNAME)
        
        password_page = page.PasswordPage(self.driver)
        password_page.enter_password_and_press_enter(GMAIL_PASSWORD)
        time.sleep(5)  # for two-factor authentication

    @allure.step('search and count letters from specific person')
    def search_count_letters_from(self):
        main_mail_page = page.MainMailPage(self.driver)
        main_mail_page.enter_search_from_query_and_press_enter(
            f'from: {EMAIL_AUTHOR_TO_FIND}')
        self.num_of_letters = main_mail_page.get_num_of_letters()
        print(self.num_of_letters) #TODO:used only before using test reporting, only without grid DELETEIT!
    
    @allure.step('write a letter to specific person with quantity of letters')
    def write_letters_to(self):
        main_mail_page = page.MainMailPage(self.driver)
        main_mail_page.open_write_letter_window()
        write_letter_window = page.WriteLetterWindow(self.driver)
        write_letter_window.write_letter(surname = MY_SURNAME, send_to = EMAIL_SEND_TO, num_of_letters=self.num_of_letters)



if __name__ == "__main__":
    unittest.main()
