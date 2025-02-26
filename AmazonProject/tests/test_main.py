import time

from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ItemsPage import ItemsPage
from pageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass


class TestMain(BaseClass):

    def test_main(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.getSignIn()

        signinPage = SignInPage(self.driver)
        time.sleep(5)
        signinPage.getPhoneNo()
        log.info("SignIn With Phone No.")
        time.sleep(5)
        signinPage.getCButton()

        homePage.getSearch()
        homePage.getSubmit()

        itemsPage = ItemsPage(self.driver)
        itemsPage.getItemtoCart()
        log.info("Added to cart")
        itemsPage.getOpenCart()

        cartPage = CartPage(self.driver)
        cartPage.getCheckBox()
        cartPage.getPay()
        log.info("Proceed to Pay")

    time.sleep(12)