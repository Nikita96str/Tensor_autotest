import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service 
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def browser():
    print('fixture is working')
    driver_service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=driver_service)
    yield driver
    driver.quit()
    