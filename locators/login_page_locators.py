
from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    EMAIL_INPUT = (By.XPATH, "//*[text()='Email']//following-sibling::*")
    PASSWORD_INPUT = (By.XPATH, "//*[text()='Пароль']//following-sibling::*")