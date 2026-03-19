import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from data import LOGIN_URL


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    browser = request.param

    if browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()
    yield driver
    driver.quit()
    

@pytest.fixture
def auth_user(driver):

    email = "gimpel_36@gmail.com"
    password = "123456"

    login_page = LoginPage(driver)

    driver.get(LOGIN_URL)
    login_page.login(email, password)

    return email