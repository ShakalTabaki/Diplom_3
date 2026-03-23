import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

        self.wait_for_element(MainPageLocators.CREATE_ORDER_BUTTON)
