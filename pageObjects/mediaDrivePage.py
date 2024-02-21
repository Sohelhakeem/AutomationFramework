import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mediaDrivePage:
    ModuleMediaDrive_xpath = "//span[text()='Media Drive']"
    NoText_xpath = "//span[text()='There are no items']"
    ButtonNew_xpath = "//button[normalize-space()='New']"
    CreateFolder_xpath = "//span[text()='Create Folder']"
    inputFolderName = "//input[@placeholder='Enter a folder name']"
    buttonCreate = "//button[@id='Create']"
    UploadFolder_xpath = "//span[text()='Upload Folder']"
    UploadFiles_xpath = "(//input[@id='filesType'])[1]"
    threeDotsMenu_xapth = "//span[@class=' lightTxt pdngRSM pointer']//*[name()='svg']"
    threeDotsShare_xapth = "//li[@value='share']"
    ShareInputSearch_xapth = "//input[@placeholder='Search by Name & Company']"
    threeDotsZip_xpath = "//li[@value='zip']"
    # //div[contains(text(),'File/Folder converted to zip')]
    threeDotsMoveTo_xpath = "//li[@value='MoveTo']"
    MoveToSearchInput_xpath = "//input[@id='search']"
    # clickSearchedFolder = "(//span[text()='folder'])[2]"
    # add this above in scripts tpo search
    ClickButtonMove_xpath = "//button[normalize-space()='Move']"
    # //div[contains(text(),'Folder moved successfully')]
    ClickMoveToTrash_xpath = "//li[@value='delete']"
    conTrash_xpath = "(//button[text()='Trash'])[2]"
    # //div[contains(text(),'Item Moved to Trash.')]
    rename_xpath = "//li[@value='rename']"
    renameInput_xpath = "//input[@id='renameInput']"
    # //div[contains(text(),'Folder name updated successfully')]



    def __init__(self, driver):
        self.driver = driver


    def clickMediaDrive(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ModuleMediaDrive_xpath))
        )
        element.click()
    def clickButtonNew(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ButtonNew_xpath))
        )
        element.click()
    def setinputFolderName(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.inputFolderName))
        )
        element.send_keys(name)
    def setUploadFolder(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.UploadFolder_xpath))
        )
        element.send_keys(name)
    def setUploadFiles(self, file_path):
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.UploadFiles_xpath))
        )
        file_input.send_keys(file_path)


    def clickUploadFiles(self):
        element = self.driver.find_element(By.XPATH, self.UploadFiles_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
    def clickbuttonCreate(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.buttonCreate))
        )
        element.click()
    def NoTextDisplayed(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.NoText_xpath))
        )
        element.is_displayed()
    def clickthreeDotsMenu(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsMenu_xapth))
        )
        element.click()
    def clickthreeDotsShare(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsShare_xapth))
        )
        element.click()
    def setShareInputSearch(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ShareInputSearch_xapth))
        )
        element.send_keys(name)
    def clickZipthreeDots(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsZip_xpath))
        )
        element.click()
    def clickMoveTothreeDots(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.threeDotsMoveTo_xpath))
        )
        element.click()
    def setMoveToSearchInput(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MoveToSearchInput_xpath))
        )
        element.send_keys(name)
    def setrenameInput(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.renameInput_xpath))
        )
        element.send_keys(name)
    def ClickButtonMove(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ClickButtonMove_xpath))
        )
        element.click()
    def ClickMoveToTrash(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ClickMoveToTrash_xpath))
        )
        element.click()
    def ClickconTrash(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.conTrash_xpath))
        )
        element.click()
    def ClickRename(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.rename_xpath))
        )
        element.click()


    def clickCreateFolder(self):
        self.driver.find_element(By.XPATH, self.CreateFolder_xpath).click()