from locators import LoginPageLocators, PasswordPageLocators, MainMailPageLocators, MainMailPageSearchResultsLocators
from selenium.webdriver.common.keys import Keys
from elements import BasePageElement, BasePageVisibleElements, wait_until_element_is_loaded
import time #TODO: time module and lines using it should be replaced with wait_until_element_is_loaded



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

    def enter_search_from_query_and_press_enter(self, query):
        self.search_mail_field_element.obj.send_keys(query, Keys.ENTER)

    def get_num_of_letters(self):
        
        time.sleep(5) #TODO: should be replaced with wait_until_element_is_loaded()
        text = self.span_letter_quantities.objs[2].get_attribute("textContent")
        return text


