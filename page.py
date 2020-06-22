from locators import (LoginPageLocators,
                      PasswordPageLocators,
                      MainMailPageLocators,
                      MainMailPageSearchResultsLocators,
                      WriteLetterWindowLocators)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from elements import BasePageElement, BasePageVisibleElements, wait_until_element_is_loaded
import time #TODO: time module and lines using it should be replaced with wait_until_element_is_loaded, I use them only because of 2-factor authentification



class BasePage(object):
    '''Base class, which is just inherited by all page classes,
    as far as I understand, it is used to provide common interface to
    initialize page instances with webdriver'''

    def __init__(self, driver):
        self.driver = driver
        


class LoginPage(BasePage):
    '''the first page, to which we are redirected by link 'mail.google.com' '''

    def __init__(self, driver):
        super().__init__(driver)
        self.login_enter_text_element = BasePageElement(
            driver=self.driver,
            locator=LoginPageLocators.LOGIN_INPUT
        )

    def enter_login_and_press_enter(self, login):
        self.login_enter_text_element.obj.send_keys(login,Keys.ENTER)


class PasswordPage(BasePage):
    '''if we've entered the login successfully we are redirected to enter password page'''

    def __init__(self, driver):
        super().__init__(driver)
        self.password_enter_text_element = BasePageElement(
            driver=self.driver,
            locator=PasswordPageLocators.PASSWORD_INPUT
        )

    def enter_password_and_press_enter(self, password):
        self.password_enter_text_element.obj.send_keys(password, Keys.ENTER)

class MainMailPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_mail_field_element = BasePageElement(
            driver=self.driver,
            locator = MainMailPageLocators.SEARCH_MAIL_FIELD
        )

        self.span_letter_quantities = BasePageVisibleElements(
            driver = self.driver,
            locator = MainMailPageSearchResultsLocators.SPAN_LETTER_QUANTITY
        )

        self.buttons = BasePageVisibleElements(
            driver=self.driver,
            locator=MainMailPageLocators.ALL_BUTTONS
        )

    def enter_search_from_query_and_press_enter(self, query):
        self.search_mail_field_element.obj.send_keys(query, Keys.ENTER)

    def get_num_of_letters(self):
        
        time.sleep(5) #TODO: should be replaced with wait_until_element_is_loaded()
        try:
            text = self.span_letter_quantities.objs[2].get_attribute("textContent")
            self.num_of_letters = int(text)
        except IndexError:
            self.num_of_letters = 0 #this issue found prior to acquiring emails from Valiakhmetov Farit
        return self.num_of_letters

    def open_write_letter_window(self):
        '''opens window where we can write letter'''
        self.buttons.objs[7].click()

class WriteLetterWindow(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.send_to_address_input = BasePageElement(driver=self.driver,
                                                     locator=WriteLetterWindowLocators.SEND_TO_ADDRESS_INPUT)
        self.mail_theme_input = BasePageElement(driver=self.driver,
                                                locator=WriteLetterWindowLocators.MAIL_THEME_INPUT)
        self.mail_main_text = BasePageElement(driver=self.driver,
                                              locator=WriteLetterWindowLocators.MAIL_MAIN_TEXT)

    def write_letter(self,surname = None,send_to=None, num_of_letters=None):
        self.send_to_address_input.obj.send_keys(send_to,Keys.ENTER)
        self.mail_theme_input.obj.send_keys(f'Тестовое задание. {surname}')
        self.mail_main_text.obj.send_keys(num_of_letters)
        ActionChains(self.driver).key_down(Keys.CONTROL).key_down(Keys.ENTER).key_up(Keys.CONTROL).key_up(Keys.CONTROL).perform()



