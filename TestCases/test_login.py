import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test001Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepage_title(self, setup):
        self.logger.info("************************** Test_001_Login **********************")
        self.logger.info("************************** Homepage verify title **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("************************** Homepage Test Title Verification returns OK **********************")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.info("************************** Homepage Test Title Verification returns false **********************")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************************** Test_001_Login **********************")
        self.logger.info("************************** Login verify title **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************************** Login Test Title Verification returns OK **********************")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_loginTitle.png")
            self.driver.close()
            self.logger.info("************************** Login Test Title Verification returns false **********************")
            assert False
