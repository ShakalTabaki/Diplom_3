import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from data import BASE_URL, FEED_URL

class TestMainPage: 

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_from_feed(self, driver):

        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        feed_page.open_feed_page()
        main_page.click_constructor()

        assert driver.current_url == BASE_URL

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_feed_button(self, driver):

        page = MainPage(driver)
        page.open_main_page()
        page.click_feed()

        assert driver.current_url == FEED_URL


    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):

        page = MainPage(driver)
        page.open_main_page()
        page.click_ingredient()

        assert page.is_modal_visible()


    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):

        page = MainPage(driver)
        page.open_main_page()
        page.drag_ingredient_to_constructor()
        page.wait_for_counter_increase()
        counter = page.get_ingredient_counter()

        assert int(counter) > 0
