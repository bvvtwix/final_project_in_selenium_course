from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/" , "Current URL is not equal login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        registration_email.send_keys(email)
        registration_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        registration_password1.send_keys(password)
        registration_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        registration_password2.send_keys(password)
        reg_button_click = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button_click.click()
