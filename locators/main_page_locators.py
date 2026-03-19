from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]")
    FIRST_BUN = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]")
    INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "(//p[contains(@class,'counter_counter')])[1]")
    BURGER_CONSTRUCTOR = (By.XPATH, "//span[contains(@class,'constructor-element__row')]")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")