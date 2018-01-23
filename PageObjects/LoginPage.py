from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import  By
import json
import datetime


class LoginPage ():

    userNameField = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/form/table/tbody/tr[1]/td[2]/input')
    passwordField = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/form/table/tbody/tr[2]/td[2]/input')
    businessUnitSelector = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/form/table/tbody/tr[3]/td[2]/select')
    submitButton = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/form/button')

    def __init__(self, driver):
        with open('Data.json') as data_file:
            data = json.load(data_file)
        self.driver = driver
        self.userName = data["User"]["userName"]
        self.password = data["User"]["password"]
        self.businessUnit = data["BusinessUnit"]["Name"]


    def enterUserName (self):
        self.driver.find_element(*self.userNameField).send_keys(self.userName)

    def enterPassword (self):
        self.driver.find_element(*self.passwordField).send_keys(self.password )

    def selectBusinessUnit(self):
        Select(self.driver.find_element(*self.businessUnitSelector)).select_by_visible_text(self.businessUnit)

    def loginUser(self):
        self.enterUserName()
        self.enterPassword()
        self.selectBusinessUnit()
        self.driver.get_screenshot_as_file(
            'C:\Automation\STBilling\Screenshots\Login_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M") + '.png')