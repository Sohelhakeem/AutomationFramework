import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class forgotPasswordPage:

    linkForgotPassword_xpath = "//button[text()='Forgot password?']"
    enterEmail_xpath = "//input[@type='text']"
    SendButton_xpath = "//button[@type='submit']"
    textBox_enterOtp_xpath = "//input[@type='tel']"
    textNewPass_name = "newPassword"
    textConPass_name = "confirmPassword"
    buttonResetPass_name = "//button[normalize-space()='Reset password']"
    def __init__(self, driver):
        self.driver = driver

    def clickforgotPassword(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.linkForgotPassword_xpath)))
        element.click()


    def setEmail(self, email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.enterEmail_xpath)))
        element.send_keys(email)
    def setNewPass(self, email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.NAME, self.textNewPass_name)))
        element.send_keys(email)
    def setConPass(self, email):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.NAME, self.textConPass_name)))
        element.send_keys(email)


    def clickSendButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.SendButton_xpath)))
        element.click()

    def clickResetPass(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.buttonResetPass_name)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        element.click()
        time.sleep(1)

    def setOtp(self, otp):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textBox_enterOtp_xpath)))
        element.send_keys(otp)

    def clickOtp(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.NAME, self.textBox_enterOtp_xpath)))
        element.click()

