import time

from selenium.webdriver.common.by import By

class ItemsPage:

    def __init__(self,driver):
        self.driver = driver

    addToCart= (By.CSS_SELECTOR,".a-button.a-button-primary.a-button-icon")
    openCart = (By.ID,"nav-cart-count")

    def getItemtoCart(self):
        card = self.driver.find_elements(By.XPATH,"//div[@class='puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right']")
        for c in card:
            itemName = c.find_elements(By.XPATH,"div/div/div/a/h2")
            for i in itemName:
                if i.text == "OnePlus Nord CE4 Lite 5G (Ultra Orange, 8GB RAM, 128GB Storage)":
                    c.find_element(*ItemsPage.addToCart).click()

    def getOpenCart(self):
            self.driver.find_element(*ItemsPage.openCart).click()