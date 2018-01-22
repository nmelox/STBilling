from selenium.webdriver.support.select import Select


class LoginPage (object):

    userNameField = ('//*[@id="root"]/div/div[2]/div/div/form/table/tbody/tr[1]/td[2]/input')
    passwordField = ('//*[@id="root"]/div/div[2]/div/div/form/table/tbody/tr[2]/td[2]/input')
    businessUnitSelector = ('//*[@id="root"]/div/div[2]/div/div/form/table/tbody/tr[3]/td[2]/select')
    businessUnitText = 'ShopperTrak Ltd (UK)'
    businessUnitId = '300000003692534'
    submitButton = ('//*[@id="root"]/div/div[2]/div/div/form/button')
    userName = "nmelo@shoppertrak.com"
    password = "test"

    def __init__(self, driver):
        self.driver = driver


    def enterUserName (self):
        self.driver.find_element_by_xpath(self.userNameField).send_keys(self.userName)

    def enterPassword (self):
        self.driver.find_element_by_xpath(self.passwordField).send_keys(self.password)

    def selectBusinessUnit(self):
        Select(self.driver.find_element_by_xpath(self.businessUnitSelector)).select_by_visible_text(self.businessUnitText)

    def login(self):
        self.enterUserName()
        self.enterPassword()
        self.selectBusinessUnit()