import time
import unittest

import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin(unittest.TestCase):
    baseURL = ReadConfig.getApplicationURL()
    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()

    def setUp(self):
        self.logger = LogGen.loggen()
        self.driver = webdriver.Chrome()  # Change to the appropriate driver
        self.driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.regression
    def test_homePageTitle(self):
        self.logger.info("****Started Home page title test ****")
        act_title=self.driver.title

        if act_title=="InLynk - Business Digital Eco System":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login_inValid_Password(self):

        self.logger.info("****Started invalid Password Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword("InLINK@!@#$")
        self.lp.clickLogin()

        act_Text = self.lp.IncorrectLoginText()

        if act_Text == "Incorrect username or password.":
            assert True
            self.logger.info("********* ivalid Login password Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.logger.error("********* ivalid Login password Test is Failed ***********")
            self.driver.close()
            assert False

    @pytest.mark.run
    def test_login_inValid_Username(self):

        self.logger.info("****Started invalid Username Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName("sohel@gmailxyz.com")
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_Text = self.lp.IncorrectLoginText()

        if act_Text == "Incorrect username or password.":
            assert True
            self.logger.info("********* ivalid Login Username Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.logger.error("********* ivalid Login Username Test is Failed ***********")
            self.driver.close()
            assert False



    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_login_Valid_UsernamePassword(self):

        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickcreatePost()
        act_Text = self.lp.newsFeedText()

        if act_Text == "Create News Feed":
            assert True
            self.logger.info("********* Login Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.logger.error("********* Login Test is Failed ***********")
            self.driver.close()
            assert False

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[@class='flexAutoRow alignCntr pdngHXS']").click()
        self.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)