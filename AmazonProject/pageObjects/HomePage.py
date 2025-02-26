import time

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    signIn = (By.ID,"nav-link-accountList")
    search = (By.ID,"twotabsearchtextbox")
    submit = (By.ID, "nav-search-submit-button")

    def getSignIn(self):
        self.driver.find_element(*HomePage.signIn).click()
        time.sleep(3)

    def getSearch(self):
        self.driver.find_element(*HomePage.search).send_keys("One Plus Nord")

    def getSubmit(self):
        self.driver.find_element(*HomePage.submit).click()