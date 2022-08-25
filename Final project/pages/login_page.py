from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL, "Login url is not presented" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" 
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" 
        #символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать

    def register_new_user(self, email, password):
        email_f = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_f.send_keys(email)
        password1_f = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_f.send_keys(password)
        password2_f = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2_f.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        time.sleep(1)
        reg_button.click()
        time.sleep(1)
        self.browser.implicitly_wait(15)
        success = self.browser.find_element(*LoginPageLocators.REGISTER_SUCCESS)
        assert success, "User was not registered"
        
