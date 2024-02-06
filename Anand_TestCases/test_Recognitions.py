import time
import pytest


from openpyxl.reader.excel import load_workbook

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from Anand_PageObjects.RecognitionPage import Recognitions


class Test_Create_Recognition:
    baseURL = ReadConfig.getApplicationURL()

    # RelationName = "Test Dealer"
    # RelationDescription = "Test Dealer Software Testing"
    # EditRelationDescription = " Edited Description for relation"
    addemployee="kris"
    addtitle="Best Employee of the Year"
    adddescription="The Best Employee of the Year is recognized for exceptional performance, innovation, teamwork, leadership, adaptability, initiative, reliability, positivity, customer focus, and continuous learning."


    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["B7"].value
    username1=worksheet["E7"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()

    # @pytest.mark.anand
    @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        time.sleep(2)
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")
            print(self,'--self')

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.rcp.closepopup()
        time.sleep(3)
        self.lp.clickLogout()

    @pytest.mark.skip(reason="skipping this Test")
    def test_UnpublishedRecognition(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        time.sleep(2)
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.savetemplate()
        time.sleep(1)
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)

        if "Krishna" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
        # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickLogout()

    @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.anand
    def test_UnpublishedtoPunlishRecognition(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        time.sleep(2)
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.savetemplate()
        time.sleep(1)
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)

        if "Krishna" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        time.sleep(2)
        self.rcp.unpublishedtab()
        time.sleep(2)
        self.rcp.clickonthreedots()
        time.sleep(1)
        self.rcp.clickonpublish()
        self.rcp.publishconfirm()
        time.sleep(2)
        if "Employee Recognition has been published successfully" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(2)
        self.rcp.closepopup()
        time.sleep(1)
        self.lp.clickLogout()
        time.sleep(2)


    # @pytest.mark.pspk
    def test_EditRecognition(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()

        self.rcp.clicknewrecognition()
        time.sleep(2)
        self.rcp.selecttemplate()
        self.rcp.selectbadge()
        self.rcp.clicknext()
        time.sleep(2)
        self.rcp.setaddemployee(self.addemployee)
        self.rcp.clickemployee()
        self.rcp.setaddtitle(self.addtitle)
        self.rcp.setadddescription(self.adddescription)
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.savetemplate()
        time.sleep(1)
        if "Employee recognition has been saved in unpublished" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)

        if "Krishna" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        self.rcp = Recognitions(self.driver)
        self.rcp.clickrecognition()
        time.sleep(2)
        self.rcp.unpublishedtab()
        time.sleep(2)
        self.rcp.clickonthreedots()
        time.sleep(1)
        self.rcp.clickonedit()
        time.sleep(1)
        self.rcp.clcikonback()
        time.sleep(1)
        self.rcp.selecttemplatetwo()
        self.rcp.selectbannertwo()
        time.sleep(1)
        self.rcp.clicknext()
        time.sleep(1)
        self.rcp.clickonpreview()
        time.sleep(1)
        self.rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(2)
        self.lp.setUserName1(self.username1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in self.driver.page_source:
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** content creation test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.rcp.closepopup()
        time.sleep(3)
        self.lp.clickLogout()



