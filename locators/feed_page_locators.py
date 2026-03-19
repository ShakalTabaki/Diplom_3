from selenium.webdriver.common.by import By


class FeedPageLocators:

    TOTAL_ORDERS = (By.XPATH, "//*[text()='Выполнено за все время:']/following-sibling::p[1]")
    TODAY_ORDERS = (By.XPATH, "//*[text()='Выполнено за сегодня:']/following-sibling::p[1]")
    ORDER_NUMBERS = (By.XPATH, "(//p[contains(@class,'digits-default')])[1]")