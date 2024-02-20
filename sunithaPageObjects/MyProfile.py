
import time

from selenium.webdriver.support import expected_conditions as EC

# import self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MyprofilePage:
    textbox_username_name = "email"
    textbox_password_name = "password"
    button_login_xpath = "//button[normalize-space()='Login']"
    # fileimge_button_xpath="//div[@id='scrollID']//div[3]//*[name()='svg']"
    newsFeed_click_xpath = "//div[@class='resNavLink activeLink']"
    MyProfile_click_xpath = "//span[normalize-space()='My Profile']"

    # ---------------------------------Banner image uploading
    Banner_image_click_id = "previewBanner"
    Banner_image_save_button = "//button[normalize-space()='Save']"
    # need to validate the banner image
    Banner_image_edit_xpath = "//span[@class='flexInline primaryTxt pointer editIcon pointer']"

    # Remove Banner image
    Banner_image_Remove_xpath = "//span[normalize-space()='Remove']"
    #update banner image
    Banner_image_update_xpath = "//div[@id='basic-menu']//li[1]"

    # --------------------------------Profile image uploading
    profile_image_id = "previewProfile"
    Profile_image_save_button = "//button[normalize-space()='Save']" ##validate the saved toaster
    #after upload the profile
    Profile_image_edit_xpath = "//span[@class='flexInline primaryTxt pointer editIconAvatar']"
    Profile_image_Remove = "//span[normalize-space()='Remove']" ##validate the removed toaster
    #profile image update
    profile_image_update_id = "updatePreview" ##validate the updated toaster
    #Remove profile image
    profile_image_Remove_xpath = "//span[normalize-space()='Remove']"

    # ----------------------------------Required Details
    edit_click_xpath = "//div[@class='cmProfileEdit']//button[@aria-label='Edit']"
    employeeID_input_xpath  = "(//input[@type='text'])[3]"
    department_click_xpath = "//div[contains(@class,'MuiFormControl-root MuiFormControl-fullWidth empApp css-tzsjye')]//div[@id='demo-simple-select']"
    department_selection_click_xpath = "//li[@role='option']//span[@class='flexRow alignCntr capitalTxt'][normalize-space()='IT team']"#//span[normalize-space()='IT team']"
    division_click_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/div[@class='flexCol pdngTMD brdrTSM']/div[3]/div[1]/div[1]"
    division_selection_click_xpath = "//li[@role='option']//span[@class='flexRow alignCntr capitalTxt wordBreakAll ellipseLen2'][normalize-space()='Mobile']"
    designation_clik_xpath = "//div[4]//div[1]//div[1]//div[1]//div[1]"
    designation_selection_click_xpath = "//li[@role='option']//span[@class='flexRow alignCntr capitalTxt wordBreakAll ellipseLen2'][normalize-space()='IT engineer']"
    updateEdit_click_xpath = "//button[normalize-space()='Update']"

    # -----------------------------------OverView
    overview_edit_click_xpath = "(//button[@aria-label='Edit'])[2]"
    overview_textarea_click_id = "desc"
    overview_save_click_xpath = "//button[normalize-space()='Save']"

    # ------------------------------------Personal Details
    personalDetails_click_xpath = "//div[@class='flexCol mrgnVXS']//div[3]//div[1]//div[1]//div[2]"
    personal_details_scroll="//h4[text()='Work details']"
    firstName_input_id = "firstName"
    lastName_input_id = "lastName"
    emailAddress_input_id = "address"
    phoneNumber_input_id  = "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedStart css-162edyi']"
    gender_Radiobutton_xpath ="//span[normalize-space()='Male']"
    marital_status_click_xpath="//div[@class='flexRow pdngBMD']//label[1]//span[1]//span[1]//*[name()='svg']"
    Blood_group_listbox_click_id = "bloodGroup"
    select_blood_group_xpath = "//li[normalize-space()='A +ve']"
    save_button_click_xpath = "(//button[normalize-space()='Save'])[1]"

    # ------------------------------------Educational Details
    unmarried_label_xpath = "//span[normalize-space()='unmarried']"
    educational_details_button_xpath = "(//button[@aria-label='Edit'])[4]"
    degree_input_id = "degree"
    specialization_input_id = "specialization"
    university_input_id = "university"
    savE_button_click_xpath = "//button[normalize-space()='Save']"

    # --------------------------------------Address
    Address_edit_button_xpath = "(//button[@class='btnBox pointer'])[5]"
    address_input_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/div[@class='flexCol']/div[@class='MuiFormControl-root MuiFormControl-marginDense MuiFormControl-fullWidth css-47xwek']/div[@class='MuiFormControl-root MuiTextField-root css-i44wyl']/div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall css-1v3mfg2']/input[1]"
    country_input_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/div[@class='flexCol']/div[@class='MuiFormControl-root MuiFormControl-marginDense MuiFormControl-fullWidth mrgnRMD css-47xwek']/div[@class='ReactFlagsSelect-module_flagsSelect__2pfa2']/button[1]"
    country_listbox_click_xpath = "//li[@id='rfs-IN']//span[@class='ReactFlagsSelect-module_selectOptionValue__vS99-']"
    state_listbox_click_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/div[@class='flexCol']/div[@class='resColRow']/div[@class='MuiFormControl-root MuiFormControl-marginDense MuiFormControl-fullWidth mrgnRMD css-47xwek']/div[@class='MuiFormControl-root MuiTextField-root css-i44wyl']/div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall css-1v3mfg2']/div[1]"
    state_selection_click_xpath = "//li[normalize-space()='Andhra Pradesh']"
    city_listbox_click_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/div[@class='flexCol']/div[@class='resColRow']/div[@class='MuiFormControl-root MuiFormControl-marginDense MuiFormControl-fullWidth css-47xwek']/div[@class='MuiFormControl-root MuiTextField-root css-i44wyl']/div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall css-1v3mfg2']/div[1]"
    city_selection_click_xpath = "//li[normalize-space()='Adoni']"
    pincode_input_id = "pincode"
    checkbox_click_xpath = "//input[@value='false']"
    saVe_button_click_xpath = "//button[normalize-space()='Save']"

    # -------------------------------------------Social Media Links
    socialMediaLinks_button_xpath = "(//button[@class='btnBox pointer'])[6]"
    socialMedia_name_dropdown_id = "name"
    socialMedia_selection_xpath = "//li[normalize-space()='Instagram']"
    url_input_id = "url"
    save_Button_click_xpath = "//button[normalize-space()='Save']"



    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        #time.sleep(2)
        # self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        # self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.NAME, self.textbox_username_name)))
        element.send_keys(username)

    def setPassword(self, password):
        # time.sleep(2)
        # self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        # self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.NAME, self.textbox_password_name)))
        element.send_keys(password)

    def clickLogin(self):
        time.sleep(2)
        # self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        element.click()

    def clickNewsFeedModule(self):
        # time.sleep(2)
        self.driver.find_element(By.XPATH, self.newsFeed_click_xpath).click()

    def clickMyProfileModule(self):
        # time.sleep(2)
        # Scroll to bring the element into view
        # element = self.driver.find_element(By.XPATH, self.MyProfile_click_xpath)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.MyProfile_click_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Wait for a short while to ensure the element is clickable
        time.sleep(0.5)
        # Click the Company Sign Up button
        element.click()
        # time.sleep(2)

    # -------------------------------------Banner image uploading
    def uploadBannerImage(self,BannerPath ):
        time.sleep(2)
        # self.driver.find_element(By.ID,self.Banner_image_click_id).send_keys(BannerPath)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.Banner_image_click_id)))
        element.send_keys(BannerPath)

    def SaveBannerImage(self):
        # time.sleep(5)
        # self.driver.find_element(By.XPATH,self.Banner_image_save_button).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Banner_image_save_button)))
        element.click()
        time.sleep(2)

    def BannerImageEdit(self):
        time.sleep(1)
        # self.driver.find_element(By.XPATH,self.Banner_image_edit_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Banner_image_edit_xpath)))
        element.click()


    def BannerImageUpdate(self,Update_banner):
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, self.Banner_image_update_xpath).send_keys(self.Update_banner)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Banner_image_update_xpath)))
        element.send_keys(Update_banner)

    def BannerImageRemove(self):
        # time.sleep(3)
        # self.driver.find_element(By.XPATH,self.Banner_image_Remove_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Banner_image_Remove_xpath)))
        element.click()
        time.sleep(2)

    # ---------------------------------Profile image uploading
    def setprofileImage(self,image_path):
        # driver= webdriver.chrome
        # time.sleep(2)
        # self.driver.find_element(By.ID, self.profile_image_id).send_keys(image_path)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.profile_image_id)))
        element.send_keys(image_path)

    def saveProfileImage(self):
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, self.Profile_image_save_button).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Profile_image_save_button)))
        element.click()
        time.sleep(2)

    def ProfileEditButton(self):
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, self.Profile_image_edit_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Profile_image_edit_xpath)))
        element.click()

    def ProfileRemove(self):
        # time.sleep(5)
        # self.driver.find_element(By.XPATH,self.Profile_image_Remove).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Profile_image_Remove)))
        element.click()


    def ProfileUpdate(self,Update_profile):
        # time.sleep(5)
        # self.driver.find_element(By.ID,self.profile_image_update_id).send.keys(Update_profile)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.profile_image_update_id)))
        element.send_keys(Update_profile)


    # ---------------------------------------Required Details
    def clickfirstEdit(self):
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, self.edit_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.edit_click_xpath)))
        element.click()


    def empID(self,empid):
        # wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH,self.employeeID_input_xpath).send_keys(Keys.CONTROL, 'a',
                                                                        Keys.DELETE)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH,self.employeeID_input_xpath)))
        element.send_keys(empid)
        # time.sleep(2)
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.employeeID_input_xpath)))
        # element.click()
        # element.clear()


    def clickDepartment(self):
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, self.department_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.department_click_xpath)))
        element.click()

    def clickDepartmentName(self):
        # time.sleep(4)
        # self.driver.find_element(By.XPATH,self.department_selection_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.department_selection_click_xpath)))
        element.click()

    def clickDivision(self):
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, self.division_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.division_click_xpath)))
        element.click()

    def clickDivisionName(self):
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, self.division_selection_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.division_selection_click_xpath)))
        element.click()

    def clickToScroll(self):
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.personal_details_scroll)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

    def clickDesignation (self):
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, self.designation_clik_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.designation_clik_xpath)))
        element.click()

    def clickDesignationName (self):
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, self.designation_selection_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.designation_selection_click_xpath)))
        element.click()

    def updateEdit (self):
        # time.sleep(4)
        # self.driver.find_element(By.XPATH, self.updateEdit_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.updateEdit_click_xpath)))
        element.click()

    # -------------------------------------OverView
    def overViewEdit(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.overview_edit_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.overview_edit_click_xpath)))
        element.click()

    def setoverviewTextarea(self, overviewText):
        time.sleep(2)
        self.driver.find_element(By.ID, self.overview_textarea_click_id).send_keys(Keys.CONTROL, 'a',
                                                                        Keys.DELETE)
        self.driver.find_element(By.ID, self.overview_textarea_click_id).send_keys(overviewText)


    def clickOverViewSave(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.overview_save_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.overview_save_click_xpath)))
        element.click()


        # -----------------------------------Personal Details
    def clickpersonalDetails(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.personalDetails_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.personalDetails_click_xpath)))
        element.click()

    def setfirstName(self,firstName):
        # time.sleep(2)
        self.driver.find_element(By.ID, self.firstName_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID, self.firstName_input_id).send_keys(firstName)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.firstName_input_id)))
        element.send_keys(firstName)

    def setlastName(self,lastName):
        # time.sleep(2)
        self.driver.find_element(By.ID, self.lastName_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID, self.lastName_input_id).send_keys(lastName)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.lastName_input_id)))
        element.send_keys(lastName)

    def setEmailAddress(self,emailAddress):
        # time.sleep(2)
        self.driver.find_element(By.ID,self.emailAddress_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID,self.emailAddress_input_id).send_keys(emailAddress)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.emailAddress_input_id)))
        element.send_keys(emailAddress)

    def phoneNumber(self, phoneNumber):
        # time.sleep(2)
        self.driver.find_element(By.XPATH, self.phoneNumber_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.XPATH, self.phoneNumber_input_id).send_keys(phoneNumber)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.phoneNumber_input_id)))
        element.send_keys(phoneNumber)

    def genderRadiobutton(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.gender_Radiobutton_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.gender_Radiobutton_xpath)))
        element.click()

    def maritalStatus(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.marital_status_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.marital_status_click_xpath)))
        element.click()

    def bloodGroupClick (self):
        # time.sleep(2)
        # self.driver.find_element(By.ID,self.Blood_group_listbox_click_id).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.Blood_group_listbox_click_id)))
        element.click()

    def selectBloodGroup(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.select_blood_group_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_blood_group_xpath)))
        element.click()

    def saveButton(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.save_button_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.save_button_click_xpath)))
        element.click()


        # ------------------------------Educational Details
    def clickToScrolll(self):
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.unmarried_label_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

    def educatinalDetails(self):
        # time.sleep(1)
        self.driver.find_element(By.XPATH,self.educational_details_button_xpath).click()
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.educational_details_button_xpath)))
        # element.click()

    def degreeField(self,degree):
        # time.sleep(2)
        self.driver.find_element(By.ID,self.degree_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID,self.degree_input_id).send_keys(degree)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.degree_input_id)))
        element.send_keys(degree)

    def specializationField(self,specialization):
        # time.sleep(2)
        self.driver.find_element(By.ID,self.specialization_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID,self.specialization_input_id).send_keys(specialization)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.specialization_input_id)))
        element.send_keys(specialization)

    def UniversityField(self,university):
        # time.sleep(2)
        self.driver.find_element(By.ID,self.university_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID,self.university_input_id).send_keys(university)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.university_input_id)))
        element.send_keys(university)

    def savEbutton(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.savE_button_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.savE_button_click_xpath)))
        element.click()


    # --------------------------------------Address
    def AddressEdit(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.Address_edit_button_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Address_edit_button_xpath)))
        element.click()

    def addressField(self,addressInput):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.address_input_xpath).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.XPATH,self.address_input_xpath).send_keys(addressInput)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.address_input_xpath)))
        element.clear()
        element.send_keys(addressInput)

    def countryField(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.country_input_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.country_input_xpath)))
        element.click()

    def countryListindia(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.country_listbox_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.country_listbox_click_xpath)))
        element.click()

    #def countryselect (self):
        #time.sleep(3)
        #self.driver.find_element(By.XPATH,self.country_listbox_click_xpath).click()

    def statelistbox (self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.state_listbox_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.state_listbox_click_xpath)))
        element.click()

    def stateSelection(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.state_selection_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.state_selection_click_xpath)))
        element.click()

    def cityListbox (self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.city_listbox_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.city_listbox_click_xpath)))
        element.click()

    def citySelection (self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.city_selection_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.city_selection_click_xpath)))
        element.click()

    def pincodeInput (self,pinCode):
        # time.sleep(2)
        self.driver.find_element(By.ID, self.pincode_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID,self.pincode_input_id).send_keys(pinCode)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.pincode_input_id)))
        element.send_keys(pinCode)

    def checkbox(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.checkbox_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.checkbox_click_xpath)))
        element.click()

    def SaveButton(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.saVe_button_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.saVe_button_click_xpath)))
        element.click()


    # ----------------------------------Social Media Links
    def socialMediaLinks(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.socialMediaLinks_button_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.socialMediaLinks_button_xpath)))
        element.click()

    def socialMediaDropdown(self):
        # time.sleep(2)
        # self.driver.find_element(By.ID,self.socialMedia_name_dropdown_id).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.socialMedia_name_dropdown_id)))
        element.click()

    def nameSelection(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,self.socialMedia_selection_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.socialMedia_selection_xpath)))
        element.click()

    def urlField(self,urlInput):
        # time.sleep(2)
        self.driver.find_element(By.ID, self.url_input_id).send_keys(Keys.CONTROL + 'a')
        # self.driver.find_element(By.ID,self.url_input_id).send_keys(urlInput)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.url_input_id)))
        element.send_keys(urlInput)

    def finalSave(self):
        time.sleep(2)
        # self.driver.find_element(By.XPATH,self.save_Button_click_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.save_Button_click_xpath)))
        element.click()















































