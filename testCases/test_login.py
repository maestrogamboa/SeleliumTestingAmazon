import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
<<<<<<< HEAD
=======
from utilities.customLogger import LogGen
>>>>>>> d523123 (Changes1)

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
<<<<<<< HEAD


    def test_login(self, setup):
=======
    logger = LogGen.loggen()


    def test_login(self, setup):
        self.logger.info("*******Test_001_Login*******")
        self.logger.info("*******Verifying Login*******")
>>>>>>> d523123 (Changes1)
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.close()
        assert True
<<<<<<< HEAD
=======
        self.logger.info("*******Loging test passed *******")
>>>>>>> d523123 (Changes1)

