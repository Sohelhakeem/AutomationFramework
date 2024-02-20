import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Certification:
    certificationprogramme_xpath = "//span[normalize-space()='Certification Programme']"
    markingsystem_xpath = "//span[normalize-space()='Marking System']"
    markingsystem_new_xpath = "//button[normalize-space()='New']"
    acronym1_xpath = "//input[@placeholder='Enter acronym 1']"
    addanotherfield_xpath = "//button[normalize-space()='Another field']"
    acronym2_xpath = "//input[@placeholder='Enter acronym 2']"
    save_xpath  = "//button[normalize-space()='Save']"
    search_xpath = "//input[@placeholder='Search...']"
    acronymedit_xpath = "//div[@class='flexAutoRow pdngHXXS alignCntr']//span[@class='flexInline primaryTxt pointer']"
    acronympublish_xpath = "//button[normalize-space()='Publish']"
    questionbank_xpath = "//span[normalize-space()='Question bank']"
    enterquestion_xpath = "//input[@placeholder='Enter the question here']"
    firstanswer_xpath = "//div[@class='flexMinWidthRow']//input[@id='title']"
    add_xpath = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-disableElevation css-191um2i']"
    secondanswer_xpath = "//input[@placeholder='Type the answer 2']"
    categoryselect_xpath = "//body/div[@id='root']/div[@class='baseBlockCntnr']/div[@class='flexCol fullHeight']/div[@class=' innerMainCntnr sideNav']/div[@class='flexCol']/div[@class='flexCol respdngSM']/div[@class='pdngSM']/div[@class='flexCol whiteBg pdngSM']/div[@class='resColRow']/div[@class='QuestionBankRight pdngHXS']/div[@class='flexCol pdngXS ']/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]"
    selectanswer_xpath = "(//div[@class='flexAutoRow alignCntr'])[2]"
    selectmarkingsystem_xpath = "//div[contains(@class,'MuiFormControl-root MuiFormControl-fullWidth css-tzsjye')]//div[@id='demo-simple-select']"
    selectmarkingsystemoption_xpath = "//li[normalize-space()='TE']"
    selectacronym_xpath = "//div[@class='flexWrap']//div[1]//span[1]"
    unpublished_xpath = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/button[1]"
    publish_xpath = "//span[text()='Publish']"
    questionsearch_xpath = "//input[@placeholder=':Search...:']"
    questionedit_xpath = "svg.MuiSvgIcon-root.MuiSvgIcon-colorPrimary.MuiSvgIcon-fontSizeMedium.pointer.css-19h30gq"
    buttonedit_xpath = "(//span[@class='flexInline'])[3]"
    questionpublish_xpath = "//button[normalize-space()='Publish']"
    templates_xpath = "//span[normalize-space()='Templates']"
    templateedit_xpath = "//div[@class='templatemediaOverlay certHover']"




    def __init__(self, driver):
        self.driver = driver


    def clickoncertificationprogramme(self):
        self.driver.find_element(By.XPATH,self.certificationprogramme_xpath).click()

    def clickonmarkingsystem(self):
        self.driver.find_element(By.XPATH,self.markingsystem_xpath).click()

    def clickonmarkingsystemnew(self):
        self.driver.find_element(By.XPATH,self.markingsystem_new_xpath).click()

    def setacronym1(self,acronym1):
        self.driver.find_element(By.XPATH,self.acronym1_xpath).send_keys(acronym1)

    def clickonaddanotherfield(self):
        self.driver.find_element(By.XPATH,self.addanotherfield_xpath).click()

    def setacronym2(self,acronym2):
        self.driver.find_element(By.XPATH,self.acronym2_xpath).send_keys(acronym2)

    def clickonsave(self):
        self.driver.find_element(By.XPATH,self.save_xpath).click()


    def setsearch(self,search):
        self.driver.find_element(By.XPATH,self.search_xpath).send_keys(search)

    def clickonacronymedit(self):
        self.driver.find_element(By.XPATH,self.acronymedit_xpath).click()

    def clickonacronympublish(self):
        self.driver.find_element(By.XPATH,self.acronympublish_xpath).click()

    def clickonquestionbank(self):
        self.driver.find_element(By.XPATH,self.questionbank_xpath).click()

    def setenterquestion(self,enterquestion):
        self.driver.find_element(By.XPATH,self.enterquestion_xpath).send_keys(enterquestion)

    def setfirstanswer(self,firstanswer):
        self.driver.find_element(By.XPATH,self.firstanswer_xpath).send_keys(firstanswer)

    def clickonadd(self):
        self.driver.find_element(By.XPATH,self.add_xpath).click()

    def setsecondanswer(self,secondanswer):
        self.driver.find_element(By.XPATH,self.secondanswer_xpath).send_keys(secondanswer)

    def clickoncategoryselect(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.categoryselect_xpath).click()
        categoryselect_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.categoryselect_xpath))
        )

        categoryselect_button.click()

    def clickonselectanswer(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.selectanswer_xpath).click()
        selectanswer_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.categoryselect_xpath))
        )

        selectanswer_button.click()

    def clickonselectmarkingsystem(self):
        select_markingsystem = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectmarkingsystem_xpath))
        )

        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(select_markingsystem).perform()

        select_markingsystem = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectmarkingsystem_xpath))
        )

        # Click on the radio button
        select_markingsystem.click()

    def clickonselectmarkingsystemoption(self):
        self.driver.find_element(By.XPATH,self.selectmarkingsystemoption_xpath).click()

    def clickonselectacronym(self):
        # self.driver.find_element(By.XPATH,self.selectacronym_xpath).click()
        select_acronym = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectacronym_xpath))
        )

        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(select_acronym).perform()

        select_acronym = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectacronym_xpath))
        )

        # Click on the radio button
        select_acronym.click()

    def clickonquestionsave(self):
        # self.driver.find_element(By.XPATH,self.save_xpath).click()
        question_save = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.save_xpath))
        )

        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(question_save).perform()

        question_save = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.save_xpath))
        )

        # Click on the radio button
        question_save.click()

    def clickonunpublished(self):
        # self.driver.find_element(By.XPATH,self.unpublished_xpath).click()
        unpublished = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.unpublished_xpath))
        )

        # Click on the radio button
        unpublished.click()

    def clickonpublished(self):
        published = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.publish_xpath))
        )

        # Click on the radio button
        published.click()

    def setsearch(self,search):
        self.driver.find_element(By.XPATH,self.search_xpath).send_keys(search)

    def clickonquestionedit(self):
        # Wait for the SVG element to be clickable
        svg_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,self.questionedit_xpath))
        )
        # Click on the SVG element
        svg_element.click()

    def clickonbuttonedit(self):
        edit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.buttonedit_xpath))
        )

        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)

        # Click on the element using JavaScript
        self.driver.execute_script("arguments[0].click();", edit_button)

    def clickonquestionpublish(self):
        publish_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.questionpublish_xpath))
        )

        # Scroll the publish button into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", publish_button)

        time.sleep(1)

        publish_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.questionpublish_xpath))
        )

        # Click on the publish button
        publish_button.click()

    def clickontemplates(self):
        element = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.templates_xpath))
        )

        element.click()

    def clickontemplateedit(self):
        # element = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, self.templateedit_xpath))
        # )

        # Perform mouseover action
        hover_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.templateedit_xpath))
        )

        # Move the mouse pointer to the hover element
        ActionChains(self.driver).move_to_element(hover_element).perform()

        # Wait for a brief moment
        time.sleep(1)

        # Click on the target element
        hover_element.click()








