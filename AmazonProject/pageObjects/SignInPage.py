import time

from selenium.webdriver.common.by import By


class SignInPage:

    def __init__(self,driver):
        self.driver = driver

    phoneNo= (By.ID,"ap_email_login")
    cButton = (By.ID,"continue")

    def getPhoneNo(self):
        self.driver.find_element(*SignInPage.phoneNo).send_keys("8420159388")
        time.sleep(2)

    def getCButton(self):
        self.driver.find_element(*SignInPage.cButton).click()
        self.driver.back()
        self.driver.back()