from selenium.webdriver.common.by import By


class Locators:

    def __init__(self, driver):
        self.driver = driver

    #HomePage
    CONTINUE_SHOP_LINK = (By.XPATH, "//button[@alt='Continue shopping']")

    #add_to_cart
    SEARCH_INPUT_LOCATOR = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON_LOCATOR = (By.ID, "nav-search-submit-button")
    ADD_TO_CART_BUTTON_LOCATOR = (By.ID, "a-autoid-1-announce")
    GO_TO_CART_BUTTON_LOCATOR = (By.LINK_TEXT, "Go to Cart")
    PROCEED_TO_CHECKOUT_BUTTON_LOCATOR = (By.NAME, "proceedToRetailCheckout")