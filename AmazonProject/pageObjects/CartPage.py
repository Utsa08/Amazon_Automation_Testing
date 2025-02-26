import time

from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self,driver):
        self.driver = driver

    checkBox = (By.XPATH,"//span[contains(text(),'This order contains a gift')]")
    pay = (By.XPATH,"//input[@name='proceedToRetailCheckout']")

    def getCheckBox(self):
        self.driver.find_element(*CartPage.checkBox).click()

    def getPay(self):
        self.driver.find_element(*CartPage.pay).click()