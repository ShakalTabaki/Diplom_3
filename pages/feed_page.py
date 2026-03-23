import allure
from pages.base_page import BasePage
from data import FEED_URL
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    
    def __init__(self, driver):
        self.driver = driver


    @allure.step("Открыть ленту заказов")
    def open_feed_page(self):
        self.driver.get(FEED_URL)


    @allure.step("Получить количество заказов за всё время")
    def get_total_orders(self):
        element = self.wait_for_element(FeedPageLocators.TOTAL_ORDERS)
        return int(element.text)


    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        element = self.wait_for_element(FeedPageLocators.TODAY_ORDERS)
        return int(element.text)


    @allure.step("Проверить наличие заказа в разделе 'В работе'")
    def is_order_in_work(self, order_number):
        order_number = order_number.strip()
        self.wait_for_text_in_elements(
            FeedPageLocators.ORDER_NUMBERS,
            order_number
        )

        return True