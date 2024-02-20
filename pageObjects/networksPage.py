import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class networksPage:
    module_Networks_xpath = "(//div[contains(@class,'resNavLink')])[3]"
    searchField_xpath = "//input[@type='search']"
    tab_Pending_xpath = "//button[normalize-space()='Pending']"
    tab_FOLLOW_xpath = "//button[normalize-space()='FOLLOW']"
    tab_Blocklist_xpath = "//button[normalize-space()='Blocklist']"
    Button_Invite_xpath = "(//button[normalize-space()='Invite'])[1]"
    # Click_CompanyName_xpath = "//span[contains(text(),'TestXeeRW Innovations Private Limited')]"
    Button_Connect_xpath = "//button[contains(text(),'Connect')]"
    Button_Follow_xpath = "//button[contains(text(),'Follow')]"
    DD_selectDropDown_xpath = "//div[@aria-haspopup='listbox']"
    DD_Manufacturer_xpath = "//span[contains(text(),'Manufacturer')]"
    DD_share_holder_xpath = "//span[normalize-space()='share holder']"
    DD_vendor_xpath = "//span[normalize-space()='vendor']"
    DD_partner_xpath = "//span[normalize-space()='partner']"
    DD_distributor_xpath = "//span[normalize-space()='distributor']"
    Text_RM_searchField_xpath = "//input[@type='text']"
    icon_SelectRM_xpath = "//div[@class='flexCol brdrRadiusSM rmBlock scrollY']//div[3]//*[name()='svg']"
    checkbox_xpath = "//input[@type='checkbox']"
    ButtonConnect2_xpath = "//button[normalize-space()='Connect']"
    ButtonCancel_xpath = "//button[normalize-space()='Cancel']"
    Button_OK_xpath = "//button[normalize-space()='OK']"
    Button_Approve_xpath = "//button[text()='Approve']"
    Button_Accept_xpath = "//button[text()='Accept']"
    Button_Cancel_xpath = "//button[text()='Cancel']"
    Button_Reject_xpath = "//button[text()='Reject']"
    textarea_xpath = "//textarea[@placeholder='Please write a short note, why you want to reject this connection.']"
    Button_Reject2_xpath = "//button[normalize-space()='Reject']"
    RejectEmployeeText_xpath = "//div[contains(text(),'Connection rejected successfully')]"

    def __init__(self, driver):
        self.driver = driver

    def clickNetworks(self):
        self.driver.find_element(By.XPATH, self.module_Networks_xpath).click()

    def setsearchField(self, username):
        time.sleep(2)
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.searchField_xpath))
        )
        search_field.clear()
        search_field.send_keys(username)
        time.sleep(1)

    def clickPendingTab(self):
        self.driver.find_element(By.XPATH, self.tab_Pending_xpath).click()

    def clickFOLLOWTab(self):
        self.driver.find_element(By.XPATH, self.tab_FOLLOW_xpath).click()

    def clickBlocklistTab(self):
        self.driver.find_element(By.XPATH, self.tab_Blocklist_xpath).click()
    def clickSelectRM(self):
        self.driver.find_element(By.XPATH, self.icon_SelectRM_xpath).click()

    def clickInviteTab(self):
        self.driver.find_element(By.XPATH, self.Button_Invite_xpath).click()

    # def clickCompanyName(self):
    #     self.driver.find_element(By.ID, self.Click_CompanyName_xpath).click()
    def clickConnectButton(self):
        self.driver.find_element(By.XPATH, self.Button_Connect_xpath).click()
    def clickFollowButton(self):
        self.driver.find_element(By.XPATH, self.Button_Follow_xpath).click()
    def clickDropDownList(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.DD_selectDropDown_xpath))
        )
        element.click()
    def clickManufacturer(self):
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.DD_Manufacturer_xpath).click()
    def clickshareHolder(self):
        self.driver.find_element(By.XPATH, self.DD_share_holder_xpath).click()
    def clickvendor(self):
        self.driver.find_element(By.XPATH, self.DD_vendor_xpath).click()

    def clickpartner(self):
        self.driver.find_element(By.XPATH, self.DD_partner_xpath).click()
    def clickdistributor(self):
        self.driver.find_element(By.XPATH, self.DD_distributor_xpath).click()
    def setRM_searchField(self , name):
        self.driver.find_element(By.XPATH, self.Text_RM_searchField_xpath).send_keys(name)

    def clickcheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath).click()
    def clickButtonConnect2(self):
        self.driver.find_element(By.XPATH, self.ButtonConnect2_xpath).click()

    def clickCancelButton(self):
        self.driver.find_element(By.XPATH, self.ButtonCancel_xpath).click()

    def clickApproveButton(self):
        self.driver.find_element(By.XPATH, self.Button_Approve_xpath).click()
    def clickRejectButton(self):
        self.driver.find_element(By.XPATH, self.Button_Reject_xpath).click()
        time.sleep(2)

    def clickAcceptButton(self):
        self.driver.find_element(By.XPATH, self.Button_Accept_xpath).click()
    def clickOKButton(self):
        self.driver.find_element(By.XPATH, self.Button_OK_xpath).click()

    def setTextarea (self, text):
        self.driver.find_element(By.XPATH, self.textarea_xpath).send_keys(text)
    def clickReject2Button (self):
        self.driver.find_element(By.XPATH, self.Button_Reject2_xpath).click()

    def Text_Connection_rejected_successfully(self):
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.RejectEmployeeText_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
