from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
import sys
sys.path.append("tests")

class SignInAndCreate(object):

    def __init__(self, driver):
        self.driver = driver
        self.locator = CreateAccountLocators
        self.timer = 10

    def signIn(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SIGN_IN_BUTTON)).click()

    def enterEmail(self, email):
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(self.locator.ENTER_EMAIL)).send_keys(email)

    def submitEmail(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SUBMIT_EMAIL_BUTTON)).click()

    def addFirstName(self, first_name):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.FIRST_NAME)).send_keys(first_name)

    def addLastName(self, last_name):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.LAST_NAME)).send_keys(last_name)

    def addPassword(self, password):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.PASSWORD)).send_keys(password)

    def addAddressFirstName(self, first_name):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_FIRST_NAME)).clear()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_FIRST_NAME)).send_keys(first_name)

    def addAddressLastName(self, last_name):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_LAST_NAME)).clear()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_LAST_NAME)).send_keys(last_name)

    def addAddress(self, address):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS)).send_keys(address)

    def addAddressCity(self, city):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_CITY)).send_keys(city)

    def selectState(self, state):
        try:
            element = WebDriverWait(self.driver, self.timer).until(
                EC.presence_of_element_located(self.locator.ADDRESS_STATE))

        finally:
            select_state = Select(element)
            select_state.select_by_visible_text(state)

    def addAddressZipCode(self, zip_code):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_ZIP_CODE)).send_keys(zip_code)

    def selectCountry(self, country):
        try:
            element = WebDriverWait(self.driver, self.timer).until(
                EC.presence_of_element_located(self.locator.ADDRESS_COUNTRY))

        finally:
            select_country = Select(element)
            select_country.select_by_visible_text(country)

    def addAddressPhone(self, phone_number):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_PHONE_NUMBER)).send_keys(phone_number)

    def addAddressAlias(self, alias):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_ALIAS)).clear()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_ALIAS)).send_keys(alias)

    def register(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.REGISTER_BUTTON)).click()
