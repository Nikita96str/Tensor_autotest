from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"
        self.original_window = self.driver.current_window_handle
    def find_element(self, locator,time=10):
        return Wait(self.driver,time).until(EC.presence_of_element_located(locator),
                                            message=f"Не могу найти элемент по локатору {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def redirect_driver(self):
        for window_handle in self.driver.window_handles:
            if window_handle != self.original_window:
                return self.driver.switch_to.window(window_handle)

    def find_curr_url(self, locator, time=10):
        Wait(self.driver, time).until(EC.element_to_be_clickable(locator))
        current_yandex_url = self.driver.current_url
        return current_yandex_url
