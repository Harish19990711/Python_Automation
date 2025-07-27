from selenium.webdriver import Keys
from Locators.locators import Locators

class Add_to_cart:

    def __init__(self, driver):
        self.driver = driver
        self.SEARCH_INPUT_LOCATOR = Locators.SEARCH_INPUT_LOCATOR
        self.SEARCH_BUTTON_LOCATOR = Locators.SEARCH_BUTTON_LOCATOR
        self.ADD_TO_CART_BUTTON_LOCATOR = Locators.ADD_TO_CART_BUTTON_LOCATOR #(By.ID,"a-autoid-1-announce")
        self.GO_TO_CART_BUTTON_LOCATOR = Locators.GO_TO_CART_BUTTON_LOCATOR #(By.LINK_TEXT, "Go to Cart")
        self.PROCEED_TO_CHECKOUT_BUTTON_LOCATOR = Locators.PROCEED_TO_CHECKOUT_BUTTON_LOCATOR #(By.NAME, "proceedToRetailCheckout")

    def search_1(self, product_name=None):
        search_box = self.driver.find_element(*self.SEARCH_INPUT_LOCATOR)
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

    def search_product(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON_LOCATOR)
        search_button.click()

    def click_on_to_cart(self):
        click_cart_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON_LOCATOR)
        click_cart_button.click()

    def go_to_cart(self):
        go_to_cart_button = self.driver.find_element(*self.GO_TO_CART_BUTTON_LOCATOR)
        go_to_cart_button.click()

    def proceed_to_check_out(self):
        check_out = self.driver.find_element(*self.PROCEED_TO_CHECKOUT_BUTTON_LOCATOR)
        check_out.click()




