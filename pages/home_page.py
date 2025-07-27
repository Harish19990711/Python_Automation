from selenium.webdriver.common.by import By
from self import driver
from Locators import locators
from Locators.locators import Locators
from utils.screenshot_util import capture_screenshot


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.CONTINUE_SHOP_LINK = Locators.CONTINUE_SHOP_LINK


    def continue_shop_link_linkedText(self):
        self.driver.find_element(*self.CONTINUE_SHOP_LINK).click()



# class HomePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.CONTINUE_SHOP_LINK = (By.LINK_TEXT, "Continue shopping")
#
#     def continue_shop_link_linkedText(self):
#         self.driver.find_element(*self.CONTINUE_SHOP_LINK).click()