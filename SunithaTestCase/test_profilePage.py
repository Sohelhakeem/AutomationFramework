import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from sunithaPageObjects.MyProfile import MyprofilePage
from sunithaPageObjects.CompanyProfile import LoginPage
from pageObjects.randomGen import randomGen
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = "https://testapp.inlink.pro/"
    username = "content@yopmail.com"
    password = "Inlink@123"
    overviewTextarea = "InLinks is the first"
    firstName = randomGen.random_first_name()
    lastName = randomGen.random_last_name()
    emailAddress = randomGen.random_email()
    phoneNumber = randomGen.random_phone_number()
    degree = randomGen.random_degree()  # "B.Sc"
    specialization = randomGen.random_specialization()
    university = randomGen.random_university()
    savEbutton = "//button[normalize-space()='Save']"
    addressInput = randomGen.random_addressInput()
    pinCode = randomGen.random_pinCode()
    urlInput = "www.instagram.com"
    # relative_ones = "imageFiles/image02.jpg"
    # image_path = os.path.abspath(relative_ones)
    image_path = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/4.jpg"
    Update_profile = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/4.jpg"
    BannerPath = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/3.jpg"
    Update_banner = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/3.jpg"
    overviewText = randomGen.random_overviwDescription()
    empid = "8679"

    logger = LogGen.loggen()

    @pytest.mark.run(order=1)
    # @pytest.mark.skip(reason="skipping this test")
    def test_BannerImage(self):  # def test_loginTitle(self):self #def test_ProfileUploading
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()

        # Banner image uploading----------------------------------------------------------------------
        self.my.uploadBannerImage(self.BannerPath)
        self.my.SaveBannerImage()

        if "Banner image uploaded successfully." in self.driver.page_source:
            self.logger.info("********* test_BannerImage Test is Passed ***********")

        else:
            self.logger.info("********* test_BannerImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_BannerImage.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

        self.driver.find_element(By.XPATH,
                                 "//button[@class='Toastify__close-button Toastify__close-button--light']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]").click()
        self.my.BannerImageEdit()
        self.my.BannerImageRemove()

        if "Banner image removed successfully" in self.driver.page_source:
            self.logger.info("********* test_BannerImage Test is Passed ***********")
            assert True

        else:
            self.logger.error("********* test_BannerImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_BannerImage.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            self.driver.close()
            assert False

        # Profile image uploading-----------------------------------------------------------------------

    @pytest.mark.run(order=2)
    # @pytest.mark.skip(reason="skipping this test")
    def test_profileImages(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()

        self.my.setprofileImage(self.image_path)

        self.my.saveProfileImage()
        time.sleep(3)
        if "Profile image uploaded successfully." in self.driver.page_source:
            self.logger.info("********* test_ProfileUploading Test is Passed ***********")

        else:
            self.logger.error("********* test_ProfileUploading Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_webinar.png")
            self.driver.close()

        self.my.ProfileEditButton()

        self.my.ProfileRemove()
        time.sleep(3)
        if "Profile image removed successfully." in self.driver.page_source:
            self.logger.info("********* test_ProfileUploading Test is Passed ***********")

        else:
            self.logger.error("********* test_ProfileUploading Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_webinar.png")
            self.driver.close()

    # Required Details------------------------------------------------------------------------------
    @pytest.mark.run(order=3)
    # @pytest.mark.skip(reason="skipping this test")
    def test_RequiredDetails(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()
        self.my.clickfirstEdit()
        self.my.empID(self.empid)
        self.my.clickDepartment()
        self.my.clickDepartmentName()
        self.my.clickDivision()
        self.my.clickDivisionName()
        # self.my.clickToScroll()
        # time.sleep(3)
        self.my.clickDesignation()
        self.my.clickDesignationName()
        self.my.updateEdit()
        time.sleep(4)
        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_RequiredDetails Test is Passed ***********")

        else:
            self.logger.info("********* test_RequiredDetails Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_RequiredDetails.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

    # OverView___________________________________________________________________________________
    @pytest.mark.run(order=4)
    # @pytest.mark.skip(reason="skipping this test")
    def test_OverView(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()
        self.my.overViewEdit()
        self.my.setoverviewTextarea(self.overviewText)
        self.my.clickOverViewSave()
        time.sleep(2)

        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_OverView Test is Passed ***********")

        else:
            self.logger.error("********* test_OverView Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_OverView.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
        # Personal Details____________________________________________________________________________

    @pytest.mark.run(order=5)
    # @pytest.mark.skip(reason="skipping this test")
    def test_PersonalDetails(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()
        self.my.clickToScroll()
        self.my.clickpersonalDetails()
        self.my.setfirstName(self.firstName)
        self.my.setlastName(self.lastName)
        self.my.setEmailAddress(self.emailAddress)
        self.my.phoneNumber(self.phoneNumber)
        self.my.genderRadiobutton()
        # self.my.maritalStatus()
        # time.sleep(2)
        self.my.bloodGroupClick()
        self.my.selectBloodGroup()
        self.my.saveButton()
        time.sleep(3)

        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_PersonalDetails Test is Passed ***********")

        else:
            self.logger.info("********* test_PersonalDetails Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_PersonalDetails.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

    # Educational Details_________________________________________________________________________________
    @pytest.mark.run(order=6)
    # @pytest.mark.skip(reason="skipping this test")
    def test_EducationalDetails(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()

        self.my.clickToScrolll()
        self.my.educatinalDetails()

        self.my.degreeField(self.degree)
        self.my.specializationField(self.specialization)
        self.my.UniversityField(self.university)
        self.my.savEbutton()
        time.sleep(3)

        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_EducationalDetails Test is Passed ***********")

        else:
            self.logger.info("********* test_EducationalDetails Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_EducationalDetails.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

        # Address__________________________________________________________________________

    @pytest.mark.run(order=7)
    # @pytest.mark.skip(reason="skipping this test")
    def test_Address(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsFeedModule()

        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()
        # time.sleep(3)

        self.my.clickToScrolll()
        # self.my.educatinalDetails()

        self.my.AddressEdit()
        # time.sleep(2)
        self.my.addressField(self.addressInput)
        # time.sleep(2)
        self.my.countryField()
        # time.sleep(2)
        self.my.countryListindia()
        # time.sleep(2)
        # self.my.countryselect()

        self.my.statelistbox()
        self.my.stateSelection()
        self.my.cityListbox()
        self.my.citySelection()
        self.my.pincodeInput(self.pinCode)
        # self.my.checkbox()
        # time.sleep(2)
        self.my.SaveButton()
        time.sleep(2)
        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_Address Test is Passed ***********")

        else:
            self.logger.info("********* test_Address Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_Address.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

        # Social Media Links________________________________________

    @pytest.mark.run(order=8)
    # @pytest.mark.skip(reason="skipping this test")
    def test_SocialMediaLinks(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # time.sleep(2)
        # self.lp.clickNewsFeedModule()

        self.my = MyprofilePage(self.driver)
        self.my.clickMyProfileModule()

        self.my.clickToScrolll()
        self.my.socialMediaLinks()
        self.my.socialMediaDropdown()
        self.my.nameSelection()
        self.my.urlField(self.urlInput)
        self.my.finalSave()
        time.sleep(2)
        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_SocialMediaLinks Test is Passed ***********")
            self.driver.close()

        else:
            self.logger.error("********* test_SocialMediaLinks Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_SocialMediaLinks.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
