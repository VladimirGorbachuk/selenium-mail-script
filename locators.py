from selenium.webdriver.common.by import By


class StartingPageLocators:
    '''
    page locators at mail.google.com
    it's necessary to add that if logged in this page automatically redirects
    to current google user's mail. So this is special case - it occurs in one of valid scenarios
    '''
    BUTTONS = (By.CLASS_NAME, "h-c-header__nav-li-link") 


class LoginPageLocators:
    '''
    Login page locators
    '''
    LOGIN_INPUT = (By.ID, 'identifierId')
    LOGIN_SUBMIT_BUTTON = None


class PasswordPageLocators:
    '''
    Password page locators
    '''
    PASSWORD_INPUT = (By.NAME, 'password')
    PASSWORD_SUBMIT_BUTTON = None


class MainMailPageLocators:
    '''
    locators at the main mail page
    '''
    SEARCH_MAIL_FIELD = (
        By.NAME, 'q')  

    ALL_BUTTONS = (By.CSS_SELECTOR, "[role=button]")


class MainMailPageSearchResultsLocators:
    '''
    locators at the main mail page with search results
    '''
    SPAN_LETTER_QUANTITY = (By.CLASS_NAME, 'ts')  # used to choose numbers corresponding to letters range and letters total (which is target)
    NEXT_BUTTON = (By.CSS_SELECTOR,
                   "[role=button][src='images/cleardot.gif']") # TODO: NotReadyYet for some cases we will need it to more accurately get number of letters



class WriteLetterWindowLocators:
    SEND_TO_ADDRESS_INPUT = (By.CSS_SELECTOR, "[rows='1'][name='to']")
    MAIL_THEME_INPUT = (By.CSS_SELECTOR, "[name='subjectbox']")
    MAIL_MAIN_TEXT = (By.CSS_SELECTOR, "[role='textbox'][g_editable='true']")