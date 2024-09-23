import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", choices=("chrome", "edge", "firefox")
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")

    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge()
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()

    driver.get("https://pf.com.pk/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()
