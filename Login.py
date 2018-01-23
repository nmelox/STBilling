import unittest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class LoginSTBilling (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login (self):
        driver = self.driver
        driver.get("http://tl-stbilling12:8080/")
        #self.assertIn("ShopperTrak Billing", driver.title)
        login = LoginPage(driver)
        login.loginUser()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()