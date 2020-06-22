from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def wait_until_element_is_loaded(driver = None, locator = None):
    '''
    used strictly in cases when we don't need target element,
    but it indicates that page has been loaded and we may proceed
    '''
    WebDriverWait(driver, 100).until(
        presence_of_element_located(locator))

class BasePageElement(WebElement):
    """
    Copied directly from official manual on python/selenium
    modified to use locators in any form (not only by name)
    code was changed
    it is necessary to exclude repeating code
    sections with waiting for element to appear on page
    so I've changed it to property decorator, whenever we try to access it
    webdriver will wait untill it appears, and then we return it
    So basically:
    to initialize we need to call it as 
    element_instance = BasePageElement(driver=your_driver,locator=your_locator)
    then to access element we need to call its instance as element_instance.obj
    """
    def __init__(self,driver = None,locator = None):
        
        self.driver = driver
        self.locator = locator
        self.wait = WebDriverWait(self.driver, 100)

    @property
    def obj(self):
        self.wait.until(
            presence_of_element_located(self.locator))
        return self.driver.find_element(*self.locator)

class BasePageVisibleElements(WebElement):
    '''
    #TODO: current implementation is copy from BasePageElement,
    so possibly these two classes should have one parent class
    with abstract method, which will be overriden in each class
    However, I guess it is too early to decide what should these two classes have in common
    '''
    def __init__(self,driver= None, locator = None):

        self.driver = driver
        self.locator = locator
        self.wait = WebDriverWait(self.driver,100)

    @property
    def objs(self):
        self.wait.until(presence_of_element_located(self.locator))
        elements_visible = [element for element in self.driver.find_elements(*self.locator) if element.is_displayed()]
        return elements_visible


