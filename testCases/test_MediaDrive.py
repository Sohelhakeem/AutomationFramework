import os
import time
import unittest
import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.randomGen import randomGen
from pageObjects.LoginPage import LoginPage
from pageObjects.mediaDrivePage import mediaDrivePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass


class TestMediaDrive(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    first_name = randomGen.random_first_name()
    # relative_folder = "Files/five.png"
    file_name = "Files/five.png"
    file_path = os.path.abspath(os.path.join(os.getcwd(), file_name))
    # absolute_folder = os.path.abspath(relative_folder)
    workbook = load_workbook("TestData/LoginData.xlsx")
    worksheet = workbook.active
    username = worksheet["I10"].value
    password = ReadConfig.getPassword()
    workbook.close()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.skip("created a common method")
    @pytest.mark.run(order=1)
    def test_MediaDrive(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.md = mediaDrivePage(self.driver)
        self.md.clickMediaDrive()

    @pytest.mark.regression
    @pytest.mark.skip("created a common method")
    @pytest.mark.run(order=2)
    def test_MediaDriveVerify(self):
        self.test_MediaDrive()

        xpath = "//span[text()='There are no items']"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_MediaDriveVerify.png")
            assert False
    @pytest.mark.regression
    @pytest.mark.run(order=3)
    def test_MediaDriveCreationAndUpload(self):
        self.test_MediaDrive()
        # self.md.clickButtonNew()
        # self.md.clickCreateFolder()
        # self.md.setinputFolderName(self.first_name)
        # self.md.clickbuttonCreate()
        # xpath = "//div[contains(text(),'Folder created successfully')]"
        # try:
        #     # Use WebDriverWait to wait for the element to be present
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, xpath))
        #     )
        #     self.logger.info(f"Text Found : {element.text}")
        #     assert True
        # except:
        #     self.logger.info(f"Text Not Found")
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_MediaDriveVerify.png")
        #     assert False
        self.md.clickButtonNew()

        self.md.setUploadFiles(self.file_path)

        # xpath = "//div[contains(text(),'File uploaded successfully')]"
        # try:
        #     # Use WebDriverWait to wait for the element to be present
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, xpath))
        #     )
        #     self.logger.info(f"Text Found : {element.text}")
        #     assert True
        # except:
        #     self.logger.info(f"Text Not Found")
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_MediaDriveCreationAndUpload.png")
        #     assert False

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_MediaDriveCreationAndUpload.png")
                assert False



if __name__ == "__main__":
    unittest.main()
