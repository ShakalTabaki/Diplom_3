import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL


class BasePage:
    URL = BASE_URL

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.driver.current_url

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        for i in range(3):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                return

            except (ElementClickInterceptedException, StaleElementReferenceException):

                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located(
                        ("xpath", "//div[contains(@class,'Modal_modal_overlay')]")
                    )
                )

        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Отправить текст в поле")
    def send_keys(self, locator, text, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание изменения текста элемента")
    def wait_for_text_not_to_be(self, locator, texts, timeout=15):
        return WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(*locator).text not in texts)


    @allure.step("Ожидание появления текста в списке элементов")
    def wait_for_text_in_elements(self, locator, text, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: any(
                text in el.text for el in d.find_elements(*locator)
            )
        )
