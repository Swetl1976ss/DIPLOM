from .base_page import BasePage
from selenium.webdriver.common.by import By


class AuthPage(BasePage):
    URL = "https://www.chitai-gorod.ru/login"
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    USER_ICON = (By.CSS_SELECTOR, ".user-icon")

    def login(self, credentials):
        self.is_visible(self.EMAIL_INPUT).send_keys(credentials["email"])
        self.is_visible(self.PASSWORD_INPUT).send_keys(credentials["password"])
        self.is_visible(self.SUBMIT_BUTTON).click()

    def is_authorized(self):
        return len(self.browser.find_elements(*self.USER_ICON)) > 0