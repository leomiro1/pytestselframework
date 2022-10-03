import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.readProperties import ReadConfig
from pageObjects.loginPage import LoginPage
from utilities.customlogger import LogGen
from utilities import ExcelUtils


class Test002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = "./TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("**************************Test_002_login_ddt test**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("number of rows in Excel:", self.rows)
        # empty list variable
        list_status=[]

        for r in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(10)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***test pass***")
                    self.lp.clicklogout()
                    list_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("***test failed***")
                    self.lp.clicklogout();
                    list_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == "Pass":
                    self.logger.info("***test failed***")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("***passed***")
                    list_status.append("Pass")
                print(list_status)
        if "Fail" not in list_status:
            self.logger.info("********Login ddt test passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********Login ddt test failed*********")
            self.driver.close()
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");