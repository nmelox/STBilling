import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import keys

class LoginSTBilling (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login (self):
        driver = self.driver
        driver.get("http://tl-stbilling12:8080/")
        self.assertIn("ShopperTrak Billing", driver.title)
        userName = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/form/table/tbody/tr[1]/td[2]/input')
        userName.send_keys("nmelo@shoppertrak.com")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()