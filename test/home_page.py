import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from pages.home_page import HomePage as HomePagePO
from pages.add_to_cart import Add_to_cart as AddToCartPO
from utils.config import BASE_URL
from utils.screenshot_util import capture_screenshot
from driver_setup import get_driver

class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.get(BASE_URL)

    def test_end_to_end_shopping_flow(self):
        driver = self.driver

        print(f"Navigated to: {BASE_URL}")

        home_page_po = HomePagePO(driver)
        add_to_cart_po = AddToCartPO(driver)

        home_page_po.continue_shop_link_linkedText()

        search_input = driver.find_element(*add_to_cart_po.SEARCH_INPUT_LOCATOR)
        search_input.send_keys("samsung s25")
        search_input.send_keys(Keys.ENTER)

        add_to_cart_po.search_product()
        add_to_cart_po.click_on_to_cart()
        add_to_cart_po.go_to_cart()
        add_to_cart_po.proceed_to_check_out()

        capture_screenshot(driver, "search_1")
        time.sleep(5)
        print("End-to-end shopping flow test completed.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
