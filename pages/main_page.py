import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from data import BASE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на 'Лента заказов'")
    def click_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_on_element(MainPageLocators.FIRST_BUN)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить отображение модального окна")
    def is_modal_visible(self):
        return self.wait_for_element(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
       
        self.wait_for_element(MainPageLocators.FIRST_BUN)
        self.wait_for_element(MainPageLocators.BURGER_CONSTRUCTOR)

        element_from = self.driver.find_element(*MainPageLocators.FIRST_BUN)
        element_to = self.driver.find_element(*MainPageLocators.BURGER_CONSTRUCTOR)

        self.driver.execute_script("""
            function simulateHTML5DragAndDrop(source, target) {
                var dataTransfer = new DataTransfer();

                // dragstart
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                source.dispatchEvent(dragStartEvent);

                // dragenter
                var dragEnterEvent = new DragEvent('dragenter', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                target.dispatchEvent(dragEnterEvent);

                // dragover + preventDefault (очень важно!)
                var dragOverEvent = new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                target.dispatchEvent(dragOverEvent);
                if (dragOverEvent.defaultPrevented) {
                    console.log('dragover prevented');
                }

                // drop
                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                target.dispatchEvent(dropEvent);

                // dragend
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                source.dispatchEvent(dragEndEvent);
            }

            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """, element_from, element_to)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):

        counter = self.wait_for_element(MainPageLocators.INGREDIENT_COUNTER)
        return counter.text
    
    @allure.step("Дождаться увеличения счётчика ингредиента")
    def wait_for_counter_increase(self, timeout=15):
        from selenium.webdriver.support.ui import WebDriverWait
        from locators.main_page_locators import MainPageLocators

        WebDriverWait(self.driver, timeout).until(lambda d: int(d.find_element(*MainPageLocators.INGREDIENT_COUNTER).text or "0") > 0)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        self.wait_for_text_not_to_be(MainPageLocators.ORDER_NUMBER, ["", "9999"])
        number = self.wait_for_element(MainPageLocators.ORDER_NUMBER)
        return number.text

    @allure.step("Создание заказа")
    def create_order(self):
        self.drag_ingredient_to_constructor()
        self.wait_for_counter_increase()
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)
        order_number = self.get_order_number()
        return order_number