import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUsername()
    password = ReadConfig.getPassword()


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.close()
        assert True

