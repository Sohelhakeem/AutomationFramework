import time

import pytest

from sunithaPageObjects.CompanyProfile import LoginPage
from selenium import webdriver
from pageObjects.randomGen import randomGen
from sunithaPageObjects.WebinarPage import WebinarPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Webinar:
    baseURL = "https://testapp.inlink.pro/"
    username = "content@yopmail.com"
    password = "Inlink@123"
    description = "About Media Drive Module of Inlink"
    LimitSeats = "10"
    coHost = "Vr"
    panelist = "mai"
    Email = "ksunik7k3@gmail.com"
    PastTabSearch = "Invc"
    EditTitle = "QA meeting"
    web = "Webinar "
    PTS = "Training Meeting"
    Training = "Training Meeting"
    logger = LogGen.loggen()

    title = randomGen.random_first_name()
    description = randomGen.random_Description()
    email = randomGen.random_email()

    @pytest.mark.run(order=1)
    def test_webinar(self):
        self.driver = webdriver.Chrome()
        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()
        # Webinar Creation----------------------------------

        self.wp.NewButton()
        self.wp.WebinarRadioButton()
        self.wp.setTitle(self.title)
        self.wp.setDescription(self.description)
        self.wp.DateTime()
        # Need to Update the Date#
        self.wp.selectDate()
        self.wp.calendarHours()
        self.wp.Hrs()
        self.wp.SelectHours()
        self.wp.minutes()
        self.wp.SelectMinutes()
        self.wp.ToggleButton()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wp.LimitSeats(self.LimitSeats)
        self.wp.coHostSearch(self.coHost)
        self.wp.AddPanelist(self.panelist)
        self.wp.SelectPanelist()
        self.wp.selectCoHost()
        self.wp.manufacturer()
        self.wp.shareHolder()
        self.wp.vendor()
        self.wp.partner()
        self.wp.distributor()
        self.wp.memberEMail(self.email)
        self.wp.setAddEmail()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wp.PublicEnable()
        self.wp.Schedule()
        time.sleep(3)

        if "Created webinar successfully" in self.driver.page_source:
            self.logger.info("********* test_webinar Test is Passed ***********")

        else:
            self.logger.info("********* test_webinar Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_webinar.png")
            self.driver.close()
            assert False

    # Webinar Past tab -------------------------------------------
    @pytest.mark.run(order=2)
    def test_PastTab(self):

        # login code
        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()
        self.wp.PastTab()
        self.wp.JanMonth()
        self.wp.JanDate()
        self.wp.PastViewButton()
        self.wp.ChatHistory()
        self.wp.CloseChatHistrory()
        self.wp.ViewPollHistory()

        if "Results" in self.driver.page_source:
            self.logger.info("********* test_PastTab is Passed ***********")

        else:
            self.logger.info("********* test_PastTab is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_PastTab.png")
            self.driver.close()
            assert False

            self.wp.ClosePollHistory()
            self.wp.PastSessionBreadcrumb()

    # webinar past session search bar----------------------------
    @pytest.mark.run(order=3)
    def test_PastSession(self):

        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()
        self.wp.PastTab()
        self.wp.JanMonth()
        self.wp.JanDate()
        self.wp.PastSearch(self.PastTabSearch)
        time.sleep(2)
        if "InVC Webinar Meeting" in self.driver.page_source:
            self.logger.info("********* test_PastSession Test is Passed ***********")

        else:
            self.logger.error("********* test_PastSession Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_PastSession.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
            # self.driver.close()
        self.wp.SessionCard()
        self.wp.SessionCardClose()
        # click on jan 17
        # self.wp.calendarjan17()

        # Webinar past tab filter-------------------------------

    @pytest.mark.run(order=4)
    def test_PastTabFilter(self):

        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()
        self.wp.PastTab()
        time.sleep(2)
        self.wp.JanMonth()
        self.wp.JanDate()

        self.wp.PastTabFilter()
        self.wp.TrainingCheckBox()
        self.wp.ApplyButton()

        self.wp.PastTabFilter()
        self.wp.WebinarCheckbox()
        self.wp.ApplyButton()

        # webinar upcoming tab------------------------------------------

    @pytest.mark.run(order=5)
    def test_UpcomingTab(self):
        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()

        self.wp.UpcomingTab()
        self.wp.CalendarFeb()
        # self.wp.UpcomingFeb25()
        # self.wp.searchWebinarMeeting(self.web)

        # if "webinar meeting" in self.driver.page_source:
        #     self.logger.info("********* test_UpcomingTab is Passed ***********")
        #
        # else:
        #     self.logger.info("********* test_UpcomingTab is failed ***********")
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_UpcomingTab.png")
        #     self.driver.close()
        #     assert False

        self.wp.SessionEdit()
        # self.wp.editListbox()
        # self.wp.EditTitle(self.EditTitle)
        # self.wp.UpdateMeeting()
        # self.wp.UpdateConfirm()
        ## again click on edit
        # self.wp.SessionEdit()
        self.wp.copyLink()
        self.wp.SessionEdit()
        self.wp.copyInvitation()
        self.wp.CopyButton()
        self.wp.CancelCard()
        # self.wp.SessionEdit()
        # time.sleep(2)
        self.wp.ViewRegistrants()
        self.wp.BreadCrumb()
        self.wp.CalendarFeb()
        self.wp.SessionEdit()
        # self.wp.searchWebinarMeeting(self.web)
        # self.wp.SessionEdit()
        self.wp.DeleteSession()
        self.wp.DeleteWebinar()

        # Training Session..........................

    @pytest.mark.run(order=6)
    def test_TrainingSession(self):
        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()

        self.wp.NewButton()
        self.wp.EditTitle(self.title)
        self.wp.setDescription(self.description)
        self.wp.DateTime()
        # Need to Update the Date#
        self.wp.selectDate()
        self.wp.calendarHours()
        # self.tw.NormalPath()#
        self.wp.Hrs()
        self.wp.SelectHours()
        self.wp.minutes()
        self.wp.SelectMinutes()
        self.wp.ToggleButton()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wp.LimitSeats(self.LimitSeats)
        self.wp.coHostSearch(self.coHost)
        # self.wp.selectCoHost()
        self.wp.manufacturer()
        self.wp.shareHolder()
        self.wp.vendor()
        self.wp.partner()
        self.wp.distributor()
        self.wp.memberEMail(self.Email)
        ##self.wp.AddEmail()
        # self.wp.PublicEnable()
        # time.sleep(2)
        self.wp.Schedule()
        #  FILTER
        # self.wp.PastTabFilter()
        # self.wp.WebinarCheckbox()
        # self.wp.ApplyButton()
        time.sleep(2)

        if "Created training successfully" in self.driver.page_source:
            self.logger.info("********* test_TrainingSession is Passed ***********")

        else:
            self.logger.info("********* test_TrainingSession is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_TrainingSession.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
        time.sleep(2)

        # Training upcoming tab-------------------------------------

    @pytest.mark.run(order=7)
    def test_TrainingUpcoming(self):

        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()
        self.wp.UpcomingTab()
        self.wp.CalendarFeb()
        # self.wp.TrainingSearch(self.Training)
        #
        # if "Created training successfully" in self.driver.page_source:
        #     self.logger.info("********* test_TrainingSession is Passed ***********")
        #
        # else:
        #     self.logger.info("********* test_TrainingSession is failed ***********")
        #     self.driver.save_screenshot(".\\ScreenShots\\" + "test_webinar.png")
        #     self.driver.close()
        #     assert False

        self.wp.SessionEdit()
        self.wp.editListbox()
        self.wp.EditTitle(self.EditTitle)
        self.wp.UpdateMeeting()
        self.wp.UpdateConfirm()

        #  filter again
        # self.wp.TriningJan26()
        # self.wp.TrainingSearch(self.Training)
        # self.wp.PastTabFilter()
        # self.wp.WebinarCheckbox()
        # self.wp.ApplyButton()
        # again click on edit
        self.wp.SessionEdit()
        self.wp.ViewRegistrants()
        self.wp.BreadCrumb()

        # self.wp.TriningJan26()
        # self.wp.TrainingSearch(self.Training)

        # again click on filter
        # self.wp.PastTabFilter()
        # self.wp.WebinarCheckbox()
        # self.wp.ApplyButton()
        self.wp.SessionEdit()
        self.wp.DeleteSession()
        self.wp.DeleteWebinar()

    # Training Past tab_______________________________________
    @pytest.mark.run(order=8)
    def test_TrainingPastTab(self):

        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()

        self.wp.PastTab()
        self.wp.JanDate()
        self.wp.PastViewButton()
        self.wp.ChatHistory()

        if "training meeting" in self.driver.page_source:
            self.logger.info("********* test_TrainingPastTab is passed ***********")

        else:
            self.logger.info("********* test_TrainingPastTab is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_TrainingPastTab.png")
            self.driver.close()
            assert False

            self.wp.CloseChatHistrory()
            self.wp.PastSessionBreadcrumb()

        # Training past session search bar----------------------------------
        # start the meeting__________

    @pytest.mark.run(order=9)
    def test_PastSearchBar(self):

        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.wp.clickTAndWModule()

        self.wp.NewButton()
        self.wp.EditTitle(self.EditTitle)
        self.wp.setDescription(self.description)
        self.wp.DateTime()
        # Need to Update the Date#
        self.wp.todayDate()
        self.wp.calendarHours()
        # self.tw.NormalPath()#
        self.wp.Hrs()
        self.wp.SelectHours()
        self.wp.minutes()
        self.wp.SelectMinutes()
        self.wp.ToggleButton()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wp.LimitSeats(self.LimitSeats)
        self.wp.coHostSearch(self.coHost)
        # self.wp.selectCoHost()
        self.wp.manufacturer()
        self.wp.shareHolder()
        self.wp.vendor()
        self.wp.partner()
        self.wp.distributor()
        self.wp.memberEMail(self.Email)
        self.wp.Schedule()
        time.sleep(2)

        if "Created training successfully" in self.driver.page_source:
            self.logger.info("********* test_PastSearchBar is Passed ***********")

        else:
            self.logger.info("********* test_PastSearchBar is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_PastSearchBar.png")
            self.driver.close()
            assert False
            self.wp.TodayMeetingStart()
            # self.wp.TrainingPTS(self.PTS)
            # self.wp.UpcomingTab()
            # time.sleep(2)
