import time

import pytest
# import self
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from sunithaPageObjects.CompanyProfile import LoginPage
from utilities.customLogger import LogGen
from pageObjects.randomGen import randomGen


class Test_001_Login:
    baseURL = "https://testapp.inlink.pro/"
    username = "content@yopmail.com"
    password = "Inlink@123"

    BannerPath = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/3.jpg"
    Upload_AgainBanner = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/5.jpg"
    ProfilePath = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/4.jpg"
    UpdateProfile_Again = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/7.jpg"

    Companyname = randomGen.random_addressInput() #"Econtent"
    orgname = randomGen.random_first_name()    #"Software and IT"
    industry = "educational services"
    website = "https://www.google.com/"
    companysummary = randomGen.random_overviwDescription()
    address = randomGen.random_addressInput()
    pincode = randomGen.random_pinCode()
    domainname = "yopmail.com"
    contactperson = randomGen.random_first_name()
    url = "https://www.instagram.com/"

    awards_path = "C:/Users/HP/PycharmProjects/AutomationFramework/imageFiles/11.jpg"
    awardTitle = randomGen.random_addressInput()

    logger = LogGen.loggen()


    @pytest.mark.sunitha
    @pytest.mark.run(order=1)
    #@pytest.mark.skip(reason="skipping this test")
    def test_BannerImage(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCompanyProfile()
        self.lp.BannerImageClick(self.BannerPath)
        self.lp.SaveBannerImage()
        time.sleep(3)
        if "Banner image uploaded successfully." in self.driver.page_source:
            self.logger.info("********* test_BannerImage Test is Passed ***********")

        else:
            self.logger.info("********* test_BannerImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_BannerImage.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
        time.sleep(3)
        self.lp.EditBanner()
        self.lp.UploadBannerImageAgain(self.Upload_AgainBanner)
        self.lp.SaveBannerImage()
        time.sleep(3)
        if "Banner image uploaded successfully." in self.driver.page_source:
            self.logger.info("********* test_BannerImage Test is Passed ***********")
            assert True

        else:
            self.logger.error("********* test_BannerImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_BannerImage.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            self.driver.close()
            assert False

        time.sleep(3)
        self.lp.EditBanner()
        self.lp.BannerImageRemove()
        time.sleep(3)
        if "Banner image removed successfully" in self.driver.page_source:
            self.logger.info("********* test_BannerImage Test is Passed ***********")
            assert True
            

        else:
            self.logger.error("********* test_BannerImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_BannerImage.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            self.driver.close()
            assert False

    @pytest.mark.run(order=2)
    #@pytest.mark.skip(reason="skipping this test")
    def test_ProfileImage(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCompanyProfile()

        self.lp.ProfileImageClick(self.ProfilePath)
        self.lp.SaveProfileImage()
        time.sleep(4)
        if "Profile image uploaded successfully." in self.driver.page_source:
            self.logger.info("********* test_ProfileImage Test is Passed ***********")

        else:
            self.logger.error("********* test_ProfileImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_ProfileImage.png")
            self.driver.close()

        self.lp.EditProfile()
        self.lp.UploadProfileImage(self.UpdateProfile_Again)
        self.lp.SaveProfileImage()
        time.sleep(4)
        if "Profile image uploaded successfully." in self.driver.page_source:
            self.logger.info("********* test_ProfileImage Test is Passed ***********")

        else:
            self.logger.error("********* test_ProfileImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_ProfileImage.png")
            self.driver.close()

        self.lp.EditProfile()
        self.lp.ProfileImageRemove()
        time.sleep(4)
        if "Profile image removed successfully." in self.driver.page_source:
            self.logger.info("********* test_ProfileImage Test is Passed ***********")

        else:
            self.logger.error("********* test_ProfileImage Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_ProfileImage.png")
            self.driver.close()


    @pytest.mark.run(order=3)
    #@pytest.mark.skip(reason="skipping this test")
    def test_OfficialDetails(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCompanyProfile()

        self.lp.ofc_details()
        self.lp.setCompany(self.Companyname)
        self.lp.setOrganisation(self.orgname)
        #  self.lp.RemoveIndustry()
        # self.lp.setIndustry(self.industry)
        # self.lp.clickIndustryName()
        self.lp.clickCalendar()
        self.lp.clickDate()
        self.lp.setwebsite(self.website)
        self.lp.clicksave()
        time.sleep(2)
        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_OfficialDetails Test is Passed ***********")

        else:
            self.logger.info("********* test_OfficialDetails Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_OfficialDetails.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False


    @pytest.mark.run(order=4)
    #@pytest.mark.skip(reason="skipping this test")
    def test_OverView(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        # self.lp.clickNewsfeedModule()
        self.lp.clickCompanyProfile()
        # self.lp.scrollIntoOverView()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.lp.clickEdit()
        self.lp.setCompanySummary(self.companysummary)
        self.lp.setAddress(self.address)
        # self.lp.setindia()
        self.lp.clickState()
        self.lp.clickstatelistbox()
        self.lp.selectState()
        self.lp.clickcity()
        self.lp.selectCity()
        self.lp.setpincode(self.pincode)
        self.lp.setdomainName(self.domainname)
        self.lp.setcontactPerson(self.contactperson)
        self.lp.clicksave()
        time.sleep(2)  # Company profile updated
        if "Company profile updated" in self.driver.page_source:
            self.logger.info("********* test_OverView Test is Passed ***********")

        else:
            self.logger.info("********* test_OverView Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_OverView.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

    @pytest.mark.run(order=5)
    #@pytest.mark.skip(reason="skipping this test")
    def test_Awards(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCompanyProfile()

        # actions = ActionChains(self.driver)
        # actions.send_keys(Keys.PAGE_DOWN).perform()
        self.lp.AwardsEdit()
        self.lp.ClickPreview(self.awards_path)
        self.lp.TitleInput(self.awardTitle)
        self.lp.SaveAward()
        time.sleep(2)
        if "Award added successfully" in self.driver.page_source:
            self.logger.info("********* test_Awards Test is Passed ***********")

        else:
            self.logger.info("********* test_Awards Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_Awards.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

    @pytest.mark.run(order=6)
    #@pytest.mark.skip(reason="skipping this test")
    def test_socialMediaLinks(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCompanyProfile()
        self.lp.clicksocialMediaLinks()
        self.lp.clicksocilmedialist()
        self.lp.clickSocialMediaName()
        self.lp.setUrl(self.url)
        self.lp.clickUrlsave()
        time.sleep(2)
        if "Profile updated  successfully" in self.driver.page_source:
            self.logger.info("********* test_socialMediaLinks Test is Passed ***********")

        else:
            self.logger.info("********* test_socialMediaLinks Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_socialMediaLinks.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

    @pytest.mark.run(order=7)
    #@pytest.mark.skip(reason="skipping this test")
    def test_ClickingElements(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        # time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        # time.sleep(2)
        self.lp.clickLogin()
        # time.sleep(2)
        #self.lp.clickNewsfeedModule()
        # time.sleep(2)
        self.lp.clickCompanyProfile()

        # time.sleep(3)
        self.lp.NetworksClick()
        time.sleep(2)
        if "Networks" in self.driver.page_source:
            self.logger.info("********* test_ClickingElements Test is Passed ***********")

        else:
            self.logger.info("********* test_ClickingElements Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_ClickingElements.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False

        # time.sleep(2)
        self.driver.back()
        # time.sleep(3)
        self.lp.CertificationsClick()
        time.sleep(3)
        if "Certification" in self.driver.page_source:
            self.logger.info("********* test_ClickingElements Test is Passed ***********")

        else:
            self.logger.info("********* test_ClickingElements Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_ClickingElements.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
        self.driver.back()
        time.sleep(3)

        self.lp.ResourceClick()
        time.sleep(2)
        if "My Resources" in self.driver.page_source:
            self.logger.info("********* test_ClickingElements Test is Passed ***********")

        else:
            self.logger.info("********* test_ClickingElements Test is failed ***********")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_ClickingElements.png")
            self.logger.error("Page source:\n%s" % self.driver.page_source)
            assert False
        time.sleep(3)
        self.driver.back()
        self.driver.back()
        # time.sleep(3)
        self.lp.Settings()
        # time.sleep(2)
        self.lp.NewsFeed()
        time.sleep(2)
