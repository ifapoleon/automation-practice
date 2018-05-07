from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
import sys
sys.path.append("tests")


class Order(object):

    def __init__(self, driver):
        self.driver = driver
        self.locator = NewOrderLocators
        self.timer = 60

    def shopTShorts(self):
        self.driver.find_element(*self.locator.SECTION).click()

    def chooseParticular(self):
        t_shirt = self.driver.find_element(*self.locator.TSHIRT)
        ActionChains(self.driver).move_to_element(t_shirt).perform()

    def addToCart(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDTOCART)).click()

    def proceedToCheckout(self):
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.CHECKOUT1)).click()
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.CHECKOUT2)).click()

    def enterAccount(self, email, password):
        self.driver.find_element(*self.locator.ACCOUNT_EMAIL).send_keys(email)
        self.driver.find_element(*self.locator.ACCOUNT_PASS).send_keys(password)

    def loginInto(self):
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()

    def chooseAddress(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS)).click()

    def shippingMethod(self):
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.ACCEPT_RULES)).click()
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.SHIPTO)).click()

    def paymentMethod(self):
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.CASH_METHOD)).click()

    def sendOrder(self):
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.SEND_ORDER)).click()

    def checkOrderStatus(self, status):
        WebDriverWait(self.driver, self.timer).until(EC.text_to_be_present_in_element(self.locator.ORDER_STATUS, status))
