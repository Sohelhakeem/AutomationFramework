import os

import pytest
import time


from pageObjects.LoginPage import LoginPage
from krishnapageObjects.CertificationPage import Certification
from pageObjects.randomGen import randomGen
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Certification:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    enterquestion = "who  is the cm of Telangana"
    firstanswer = "KCR"
    secondanswer = "Revanth Reddy"


    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_acronymcreation(self, setup):
        self.logger.info("************* Test_001_Certification **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")
        acronym1 = randomGen.random_acronym1()
        acronym2 = randomGen.random_acronym2()

        self.logger.info("******* Starting acronym Test **********")
        self.cp = Certification(self.driver)
        self.cp.clickoncertificationprogramme()
        # self.cp.clickonmarkingsystem()
        # self.cp.clickonmarkingsystemnew()
        # self.cp.setacronym1(acronym1)
        # self.cp.clickonaddanotherfield()
        # self.cp.setacronym2(acronym2)
        #
        # self.cp.clickonsave()
        # time.sleep(3)
        # if "Acronym created and unpublished successfully" in self.driver.page_source:
        #     self.logger.info("********** Acronym creation test is passed *********")
        #
        # else:
        #     # Log and take a screenshot
        #     self.logger.error("************** Acronym creation test is failed **********")
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
        #     assert False
        # time.sleep(3)
        # self.cp.setsearch(acronym1)
        # self.cp.clickonacronymedit()
        # self.cp.clickonacronympublish()
        # time.sleep(3)
        # if "Acronym updated and published successfully" in self.driver.page_source:
        #     self.logger.info("********** Acronym creation test is passed *********")
        #
        # else:
        #     # Log and take a screenshot
        #     self.logger.error("************** Acronym creation test is failed **********")
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
        #     assert False
        # time.sleep(3)
        # self.cp.clickonquestionbank()
        # self.cp.clickonmarkingsystemnew()
        # self.cp.setenterquestion(self.enterquestion)
        # self.cp.setfirstanswer(self.firstanswer)
        # self.cp.clickonadd()
        # self.cp.setsecondanswer(self.secondanswer)
        # self.cp.clickonselectanswer()
        # self.cp.clickoncategoryselect()
        # self.cp.clickonselectmarkingsystem()
        # self.cp.clickonselectmarkingsystemoption()
        # self.cp.clickonselectacronym()
        # self.cp.clickonquestionsave()
        # time.sleep(3)
        # if "Question created and unpublished successfully" in self.driver.page_source:
        #     self.logger.info("********** Acronym creation test is passed *********")
        #
        # else:
        #     # Log and take a screenshot
        #     self.logger.error("************** Acronym creation test is failed **********")
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
        #     assert False
        # time.sleep(3)
        # self.cp.setsearch(self.enterquestion)
        # self.cp.clickonquestionedit()
        # self.cp.clickonbuttonedit()
        # self.cp.clickonquestionpublish()
        # time.sleep(3)
        # if "Question update and published successfully" in self.driver.page_source:
        #     self.logger.info("********** Acronym creation test is passed *********")
        #
        # else:
        #     # Log and take a screenshot
        #     self.logger.error("************** Acronym creation test is failed **********")
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
        #     assert False
        # time.sleep(3)
        self.cp.clickontemplates()
        self.cp.clickonmarkingsystemnew()
        self.cp.clickontemplateedit()
        time.sleep(3)









