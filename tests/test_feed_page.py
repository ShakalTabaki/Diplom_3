import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage

class TestFeedPage:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increases(self, driver, auth_user):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        feed_page.open_feed_page()
        total_before = feed_page.get_total_orders()

        main_page.open_main_page()
        main_page.create_order()

        feed_page.open_feed_page()
        total_after = feed_page.get_total_orders()

        assert total_after > total_before


    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_today_orders_counter_increases(self, driver, auth_user):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        feed_page.open_feed_page()
        today_before = feed_page.get_today_orders()

        main_page.open_main_page()
        main_page.create_order()

        feed_page.open_feed_page()
        today_after = feed_page.get_today_orders()

        assert today_after > today_before


    @allure.title("Проверить наличие заказа в разделе 'В работе'")
    def test_is_order_in_work(self, driver, auth_user):
        
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open_main_page()
        order_number = main_page.create_order()

        feed_page.open_feed_page()

        assert feed_page.is_order_in_work(order_number)