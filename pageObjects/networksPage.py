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
    Button_following_xpath = "//button[contains(text(),'Following')]"
    Button_Unfollow_xpath = "//button[normalize-space()='Unfollow']"
    Button_Block_xpath = "//span[contains(text(),'BLOCK')]"
    Button_Unblock_xpath = "//button[contains(text(),'UnBlock')]"
    Button_Confirm_Unblock_xpath = "//button[normalize-space()='UnBlock']"
    Button_Confirm_Block_xpath = "//button[normalize-space()='BLOCK']"
    DD_selectDropDown_xpath = "//div[@aria-haspopup='listbox']"
    DD_Manufacturer_xpath = "//div[@id='menu-']//li[1]//span[1]"
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
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.module_Networks_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.module_Networks_xpath).click()

    def setsearchField(self, companyName):
        time.sleep(2)
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.searchField_xpath))
        )
        search_field.clear()
        search_field.send_keys(companyName)
        time.sleep(2)

    def clickPendingTab(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_Pending_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.tab_Pending_xpath).click()

    def clickFOLLOWTab(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_FOLLOW_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.tab_FOLLOW_xpath).click()

    def clickBlocklistTab(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_Blocklist_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.tab_Blocklist_xpath).click()
    def clickSelectRM(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.icon_SelectRM_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.icon_SelectRM_xpath).click()

    def clickInviteTab(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Invite_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Button_Invite_xpath).click()

    # def clickCompanyName(self):
    #     self.driver.find_element(By.ID, self.Click_CompanyName_xpath).click()
    def clickConnectButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Connect_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Button_Connect_xpath).click()
    def clickFollowButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Follow_xpath)))
        element.click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.Button_Follow_xpath).click()

    def clickFollowingButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_following_xpath)))
        element.click()

    def clickUnfollowButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Unfollow_xpath)))
        element.click()

    def ClickBlockCompany(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Block_xpath)))
        element.click()

    def ClickConfirmBlock(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Confirm_Block_xpath)))
        element.click()

    def ClickUnblockCompany(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Unblock_xpath)))
        element.click()

    def ClickConfirmUnblock(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Confirm_Unblock_xpath)))
        element.click()

    def clickDropDownList(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.DD_selectDropDown_xpath))
        )
        element.click()
    def clickManufacturer(self):
        time.sleep(0.5)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_Manufacturer_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.DD_Manufacturer_xpath).click()
    def clickshareHolder(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_share_holder_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.DD_share_holder_xpath).click()
    def clickvendor(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_vendor_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.DD_vendor_xpath).click()

    def clickpartner(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_partner_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.DD_partner_xpath).click()
    def clickdistributor(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_distributor_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.DD_distributor_xpath).click()
    def setRM_searchField(self , name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Text_RM_searchField_xpath)))
        element.send_keys(name)
        # self.driver.find_element(By.XPATH, self.Text_RM_searchField_xpath).send_keys(name)

    def clickcheckbox(self):
        element = self.driver.find_element(By.XPATH, self.checkbox_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        element.click()
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.checkbox_xpath)))
        # element.click()
        # self.driver.find_element(By.XPATH, self.checkbox_xpath).click()
    def clickButtonConnect2(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.ButtonConnect2_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.ButtonConnect2_xpath).click()

    def clickCancelButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.ButtonCancel_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.ButtonCancel_xpath).click()

    def clickApproveButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Approve_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Button_Approve_xpath).click()
    def clickRejectButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Reject_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Button_Reject_xpath).click()
        time.sleep(2)

    def clickAcceptButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Accept_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Button_Accept_xpath).click()
    def clickOKButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_OK_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Button_OK_xpath).click()

    def setTextarea (self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textarea_xpath)))
        element.send_keys(text)
        # self.driver.find_element(By.XPATH, self.textarea_xpath).send_keys(text)
    def clickReject2Button (self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_Reject2_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.Button_Reject2_xpath).click()

    def Text_Connection_rejected_successfully(self):
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.RejectEmployeeText_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
