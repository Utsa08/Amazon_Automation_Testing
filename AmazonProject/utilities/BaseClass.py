import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_driver(self):
        return self.driver

    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "ap_email_login")))
        wait.until(expected_conditions.text_to_be_present_in_element_value((By.ID, "nav-link-accountList")))
        wait.until(expected_conditions.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        wait.until(expected_conditions.presence_of_element_located((By.ID, "nav-search-submit-button")))
        wait.until(expected_conditions.presence_of_element_located((By.ID,"nav-cart-count")))
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[contains(text(),'This order contains a gift')]")))

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # filehandler object
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger