import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import LoginPage

class LoginSTBilling (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login (self):
        driver = self.driver
        driver.get("http://tl-stbilling12:8080/")
        self.assertIn("ShopperTrak Billing", driver.title)
        login = LoginPage(driver)
        login.login()
        driver.get_screenshot_as_file('C:\Automation\STBilling\Screenshots\Login_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M") + '.png')

    def tearDown(self):

        self.driver.close()
        self.driver.quit()