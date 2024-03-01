import time

import pytest
from openpyxl.reader.excel import load_workbook

from sunithaPageObjects.CompanyProfile import LoginPage
from selenium import webdriver
from pageObjects.randomGen import randomGen
from sunithaPageObjects.WebinarPage import WebinarPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Webinar:
    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active
    baseURL = ReadConfig.getApplicationURL()
    username = worksheet["A2"].value
    password = "Inlink@123"
    description = "About Media Drive Module of Inlink"
    LimitSeats = "10"
    coHost = "gra"
    panelist = "oli"
    Email = "ksunik7k3@gmail.com"
    PastTabSearch = "QA Meeting"
    EditTitle = "Automation team meeting"
    web = "Webinar "
    PTS = "Training Meeting"
    Training = "Training Meeting"
    logger = LogGen.loggen()

    title = "Webinar Meeting"
    description = "Webinar Meeting for Dev Meeting"
    email = "sunitha@instavc.com"

    # title = randomGen.random_first_name()
    # description = randomGen.random_Description()
    # email = randomGen.random_email()


    Trainingtitle = "Training meeting"
    TriningDiscription = "All modules of inlynk, code review with automation team  "

    EmpMail = "nxyonio@mailcatch.com"
    EmpPassword = "Inlink@123"

    username1 = worksheet["A25"].value

    PartnerMail = worksheet["I3"].value

    PartnerPassword = "Inlink@123"

    ShareHolderMail = worksheet["I2"].value
    shareholderPassword = "Inlink@123"
    workbook.close()

    @pytest.mark.run(order=1)
    # @pytest.mark.skip(reason="skipping this test")
    def test_webinar(self):
        self.driver = webdriver.Chrome()
        # self.driver = setup()
        self.driver.maximize_window()
        self.logger.info("****** Login verification *****")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()

        # Webinar Creation----------------------------------Webinar Creation
        self.logger.info("****** TC_01 '+' New button webinar meeting creation*****")
        self.wp.NewButton()
        self.logger.info("****** TC_02	Verify 'Webinar meeting' radio button *****")
        self.wp.WebinarRadioButton()
        self.logger.info("****** TC_03	Verify the Enter Title input field *****")
        self.wp.setTitle(self.title)
        self.logger.info("****** TC_04	Verify the Enter Description input field *****")
        self.wp.setDescription(self.description)
        self.logger.info("****** TC_05	Verify Date and Time Selection *****")
        self.wp.DateTime()
        # Need to Update the Date#
        self.wp.CalendarforwardArrow()
        self.wp.selectDate()
        self.wp.calendarHours()
        self.wp.Hrs()
        self.wp.SelectHours()
        self.wp.minutes()
        self.wp.SelectMinutes()
        self.logger.info("****** TC_06	Verify the RSVP toggle button *****")
        self.wp.ToggleButton()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.logger.info("****** TC_07 limit seats input *****")
        self.wp.LimitSeats(self.LimitSeats)
        self.logger.info("****** TC_08	Verify Add 'co- host' search bar *****")
        self.wp.coHostSearch(self.coHost)
        self.logger.info("****** TC_09	Verify the Add Participants Check box *****")
        self.wp.AddPanelist(self.panelist)
        self.wp.SelectPanelist()
        self.wp.selectCoHost()
        self.logger.info(
            "****** TC_11	Verify Network relation searching by name, of already selected relation(check box) *****")
        self.wp.manufacturer()
        self.wp.shareHolder()
        self.wp.vendor()
        self.wp.partner()
        self.wp.distributor()
        self.wp.memberEMail(self.email)
        self.logger.info("****** TC_10	Verify 'Invite Members' Search bar *****")
        self.wp.setAddEmail()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.logger.info("****** TC_02	Verify 'Training' radio button *****")
        self.wp.PublicEnable()
        self.logger.info("****** TC_12	Verify 'Schedule webinar button and button *****")
        self.wp.Schedule()
        time.sleep(3)

        if "Created webinar successfully" in self.driver.page_source:
            self.logger.info("********* test_webinar Test is Passed ***********")
            # self.driver.close()
        else:
            self.logger.info("********* test_webinar Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_webinar.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
        time.sleep(2)
        self.driver.close()

    @pytest.mark.run(order=2)
    # @pytest.mark.suni
    @pytest.mark.skip(reason="skipping this test")
    def test_EmployeeBookSeat(self):
        self.driver = webdriver.Chrome()
        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.EmpMail)
        self.lp.setpassword(self.EmpPassword)
        self.lp.clickLogin()
        # # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        self.wp.CalendarFeb()
        # # self.wp.MarchMonth()
        # # self.wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        self.wp.BookSeat()
        time.sleep(2)
        if "Your seat has been successfully booked." in self.driver.page_source:
            self.logger.info("********* test_EmployeeBookSeat is Passed ***********")

        else:
            self.logger.info("********* test_PastSearchBar is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_EmployeeBookSeat.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            # assert False
        time.sleep(2)
        self.wp.CloseToaster()
        self.wp.Logout()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.PartnerMail)  # as Partner booking the seat
        self.lp.setpassword(self.PartnerPassword)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        self.wp.CalendarFeb()
        # self.wp.MarchMonth()
        # self.wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        self.wp.BookSeat()
        time.sleep(2)
        if "Your seat has been successfully booked." in self.driver.page_source:
            self.logger.info("********* test_EmployeeBookSeat is Passed ***********")

        else:
            self.logger.info("********* test_PastSearchBar is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_EmployeeBookSeat.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            # assert False

        time.sleep(2)
        self.wp.CloseToaster()
        self.wp.Logout()
        # self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.ShareHolderMail)  # as a share holder booking the seat
        self.lp.setpassword(self.shareholderPassword)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        self.wp.CalendarFeb()
        # self.wp.MarchMonth()
        # self.wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        self.wp.BookSeat()
        time.sleep(2)
        if "Your seat has been successfully booked." in self.driver.page_source:
            self.logger.info("********* test_EmployeeBookSeat is Passed ***********")

        else:
            self.logger.info("********* test_PastSearchBar is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_EmployeeBookSeat.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            # assert False
        time.sleep(1)
        self.driver.close()

    # Webinar Past tab -------------------------------------------Webinar Past tab
    @pytest.mark.run(order=3)
    # @pytest.mark.skip(reason="skipping this test")
    def test_PastTabsSessionVerification(self):
        # login code
        self.driver = webdriver.Chrome()

        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username1)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_14	Verify when User selects the Past tab *****")
        self.wp.PastTab()
        self.logger.info("****** TC_15	Verify the Custom calendar filter *****")
        # self.wp.FebMonth()
        self.wp.FebDate()
        self.wp.PastViewButton()
        self.logger.info("****** TC_32	Verify the User Accessibility of Chat History *****")
        self.wp.ChatHistory()
        time.sleep(2)
        self.wp.CloseChatHistrory()
        self.logger.info("****** TC_33	Verify the User Accessibility of Poll History *****")
        self.wp.ViewPollHistory()

        if "Results" in self.driver.page_source:
            self.logger.info("********* test_PastTabsSessionVerification is Passed ***********")
            # self.driver.close()

        else:
            self.logger.info("********* test_PastTabsSessionVerification is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_PastTabsSessionVerification.png")
            # self.driver.close()
            assert False

        self.wp.ClosePollHistory()
        self.wp.PastSessionBreadcrumb()
        self.driver.close()

    # webinar past session search bar----------------------------webinar past session search bar
    @pytest.mark.run(order=4)
    @pytest.mark.sunitha
    # @pytest.mark.skip(reason="skipping this test")
    def test_PastSessionCardSearch(self):
        self.driver = webdriver.Chrome()
        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username1)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.wp.PastTab()
        # self.wp.FebMonth()
        self.wp.FebDate()
        self.logger.info("****** TC_32	Verify the User Accessibility of Chat History *****")
        self.wp.PastSearch(self.PastTabSearch)
        time.sleep(2)
        if "Webinar meeting" in self.driver.page_source:
            self.logger.info("********* test_PastSessionCardSearch Test is Passed ***********")

        else:
            self.logger.error("********* test_PastSessionCardSearch Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_PastSessionCardSearch.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

        self.wp.SessionCard()
        self.wp.SessionCardClose()
        self.driver.close()

        # Webinar past tab filter-------------------------------Webinar past tab filter

    @pytest.mark.run(order=5)
    # @pytest.mark.skip(reason="skipping this test")
    def test_PastTabFilter(self):
        self.driver = webdriver.Chrome()
        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username1)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()

        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.wp.PastTab()
        time.sleep(2)
        self.logger.info("****** TC_30	Verify Custom Calendar Filter *****")
        # self.wp.FebMonth()
        self.wp.FebDate()
        self.logger.info("****** TC_23	Verify the Filter in the Past Tab page *****")
        self.wp.PastTabFilter()
        self.wp.TrainingCheckBox()
        self.wp.ApplyButton()
        self.logger.info("****** TC_29	Verify the filter functionalityF *****")
        self.wp.PastTabFilter()
        self.wp.TrainingCheckBox()
        self.wp.WebinarCheckbox()
        self.wp.ApplyButton()
        self.driver.close()

        # webinar upcoming tab------------------------------------------webinar upcoming tab

    @pytest.mark.run(order=6)
    # @pytest.mark.skip(reason="skipping this test")
    def test_WebinarUpcomingTab(self):
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
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()

        self.logger.info("****** TC_14	Verify when User selects the Upcoming tab *****")
        self.wp.UpcomingTab()
        self.logger.info("******  TC_15	Verify the Custom calendar filter *****")
        # self.wp.CalendarFeb()
        self.wp.MarchMonth()
        self.logger.info(
            "****** TC_16	Verify the visibility of all the Trainings and Webinars for the selected date from calendar*****")
        self.wp.UpcomingMar25()
        self.wp.SessionEdit()
        # self.wp.editListbox()
        # self.wp.EditTitle(self.EditTitle)
        # self.wp.UpdateMeeting()
        # self.wp.UpdateConfirm()
        ## again click on edit
        # self.wp.SessionEdit()
        self.logger.info("****** TC_18	Verify Copy link option *****")
        self.wp.copyLink()
        self.wp.SessionEdit()
        self.logger.info("****** TC_19	Verify Copy invitation option *****")
        self.wp.copyInvitation()
        self.wp.CopyButton()
        self.wp.CancelCard()
        # self.wp.SessionEdit()
        # time.sleep(2)
        self.logger.info("****** TC_20	Verify View Registrants option for Training/Webinar *****")
        self.wp.ViewRegistrants()
        self.wp.BreadCrumb()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter *****")
        self.wp.MarchMonth()
        self.wp.UpcomingMar25()
        # self.wp.CalendarFeb()
        self.logger.info("****** TC_17	Verify the 3 dot more button (for host) *****")
        self.wp.SessionEdit()
        # self.wp.searchWebinarMeeting(self.web)
        # self.wp.SessionEdit()
        self.logger.info("****** TC_22	Verify Delete Training/Webinar option in 3dot button *****")
        self.wp.DeleteSession()
        self.wp.DeleteWebinar()
        self.driver.close()

        # Training Session________________________________Training Session

    @pytest.mark.run(order=7)
    # @pytest.mark.skip(reason="skipping this test")
    def test_TrainingCreation(self):
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
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_01 '+' New button webinar meeting creation*****")
        self.wp.NewButton()
        self.logger.info("****** TC_03	Verify the Enter Title input field *****")
        self.wp.EditTitle(self.Trainingtitle)
        self.logger.info("****** TC_03	Verify the Enter description input field *****")
        self.wp.setDescription(self.TriningDiscription)
        self.logger.info("****** TC_05	Verify Date and Time Selection *****")
        self.wp.DateTime()
        # Need to Update the Date#
        self.wp.CalendarforwardArrow()
        self.wp.selectDate()
        self.wp.calendarHours()
        # self.tw.NormalPath()#
        self.wp.Hrs()
        self.wp.SelectHours()
        self.wp.minutes()
        self.wp.SelectMinutes()
        self.logger.info("****** TC_06	Verify the RSVP toggle button *****")
        self.wp.ToggleButton()
        self.logger.info(
            "****** TC_07	Verify Limit seats toggle button and'Select number of seats' input field *****")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wp.LimitSeats(self.LimitSeats)
        self.logger.info("****** TC_08	Verify Add 'co- host' search bar *****")
        self.wp.coHostSearch(self.coHost)
        # self.wp.selectCoHost()
        self.logger.info(
            "****** TC_11	Verify Network relation searching by name, of already selected relation(check box) *****")
        self.wp.manufacturer()
        self.wp.shareHolder()
        self.wp.vendor()
        self.wp.partner()
        self.wp.distributor()
        self.logger.info("****** TC_10	Verify 'Invite Members' Search bar*****")
        self.wp.memberEMail(self.Email)
        self.logger.info("****** TC_12	Verify 'Schedule training button and 'Cancel' button *****")
        self.wp.Schedule()
        time.sleep(2)

        if "Created training successfully" in self.driver.page_source:
            self.logger.info("********* test_TrainingCreation is Passed ***********")
            self.driver.close()


        else:
            self.logger.info("********* test_TrainingSession is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_TrainingCreation.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            # assert False
        time.sleep(2)

    @pytest.mark.run(order=8)
    # @pytest.mark.skip(reason="skipping this test")
    def test_EmployeeBookSeat(self):
        self.driver = webdriver.Chrome()
        # self.driver = setup()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.EmpMail)
        self.lp.setpassword(self.EmpPassword)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        # self.wp.CalendarFeb()
        self.wp.MarchMonth()
        self.wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        self.wp.BookSeat()
        time.sleep(2)
        if "Your seat has been successfully booked." in self.driver.page_source:
            self.logger.info("********* test_EmployeeBookSeat is Passed ***********")

        else:
            self.logger.info("********* test_PastSearchBar is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_EmployeeBookSeat.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            # assert False
        time.sleep(2)
        self.wp.CloseToaster()
        self.wp.Logout()
        # self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.PartnerMail)  # as Partner booking the seat
        self.lp.setpassword(self.PartnerPassword)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        # self.wp.CalendarFeb()
        self.wp.MarchMonth()
        self.wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        self.wp.BookSeat()
        time.sleep(2)
        if "Your seat has been successfully booked." in self.driver.page_source:
            self.logger.info("********* test_EmployeeBookSeat is Passed ***********")

        else:
            self.logger.info("********* test_PastSearchBar is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_EmployeeBookSeat.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            # assert False

        time.sleep(2)
        self.wp.CloseToaster()
        self.wp.Logout()
        # self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.ShareHolderMail)  # as a share holder booking the seat
        self.lp.setpassword(self.shareholderPassword)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.wp = WebinarPage(self.driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        # self.wp.CalendarFeb()
        self.wp.MarchMonth()
        self.wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        self.wp.BookSeat()
        time.sleep(2)
        if "Your seat has been successfully booked." in self.driver.page_source:
            self.logger.info("********* test_EmployeeBookSeat is Passed ***********")

        else:
            self.logger.info("********* test_PastSearchBar is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_EmployeeBookSeat.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            # assert False
        time.sleep(1)
        self.driver.close()

        # Training upcoming tab-------------------------------------Training upcoming tab

    @pytest.mark.run(order=9)
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="skipping this test")
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
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_23	Verify the Filter in the Upcoming Tab page*****")
        # self.wp.UpcomingTab()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        # self.wp.CalendarFeb()
        self.wp.MarchMonth()
        self.wp.UpcomingMar25()
        self.logger.info("****** TC_22	Verify Delete Training/Webinar option in 3dot button*****")
        self.wp.SessionEdit()
        self.wp.editListbox()
        self.logger.info("****** TC_03	Verify the Enter Title input field*****")
        self.wp.EditTitle(self.EditTitle)
        self.wp.UpdateMeeting()
        self.wp.UpdateConfirm()
        self.wp.SessionEdit()
        self.logger.info("****** TC_20	Verify View Registrants option for Training/Webinar*****")
        self.wp.ViewRegistrants()
        self.wp.BreadCrumb()
        self.wp.UpcomingTab()
        self.wp.MarchMonth()
        self.wp.UpcomingMar25()
        self.wp.SessionEdit()
        self.logger.info("****** TC_22	Verify Delete Training/Webinar option in 3dot button*****")
        self.wp.DeleteSession()
        self.wp.DeleteWebinar()
        self.driver.close()

    # Training Past tab_______________________________________Training Past tab
    @pytest.mark.run(order=10)
    @pytest.mark.skip(reason="skipping this test")
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
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        self.wp.clickTAndWModule()
        self.logger.info("****** TC_31	Verify the Training and Webinar Details in the past tab*****")
        self.wp.PastTab()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        # self.wp.FebMonth()
        self.logger.info("****** TC_27	Verify User Accessibility of Past sessions for (HOST)*****")
        self.wp.FebDate()
        time.sleep(2)

        if "training meeting" in self.driver.page_source:
            self.logger.info("********* test_TrainingPastTab is passed ***********")
        else:
            self.logger.info("********* test_TrainingPastTab is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_TrainingPastTab.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
        time.sleep(2)
        self.logger.info("****** TC_31(After click on the Training or Webinar past session card)*****")
        self.wp.PastViewButton()
        self.wp.ChatHistory()
        self.wp.CloseChatHistrory()
        self.wp.PastSessionBreadcrumb()
        time.sleep(2)
        self.driver.close()












