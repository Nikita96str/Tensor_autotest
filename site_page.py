from base_app import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Ya_Locators:
    # search task
    LOCATOR_SEARCH_FIELD = (By.NAME, 'text')
    LOCATOR_SUGGEST_FIELD = (By.CLASS_NAME, 'mini-suggest__popup-content')
    LOCATOR_FIRST_SITE = (By.XPATH, '/html/body/main/div[2]/div[2]/div/div[1]/ul/li[1]/div/div[2]/div/a/b')
    # image task
    LOCATOR_ICON_MENU = (By.CLASS_NAME, 'services-suggest__icons-more')
    LOCATOR_IMAGE_ICON = (By.XPATH, '/html/body/div[4]/div/div/div[1]/div/div[3]/div[1]/span[9]/a')
    LOCATOR_FIRST_IMAGE_CATEGORY = (By.CSS_SELECTOR, 'div.PopularRequestList-Item:nth-child(1)')
    LOCATOR_FIRST_PICTURE = (By.XPATH, "//div[starts-with(@class, 'serp-item serp-item_type_search serp-item_group_search serp-item_pos_0 justifier__item i-bem')]")
    LOCATOR_RIGHT_CIRCLE_BUTTON = (By.CSS_SELECTOR, 'div.CircleButton:nth-child(4) > i:nth-child(1)')
    LOCATOR_LEFT_CIRCLE_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev > i:nth-child(1)')
    LOCATOR_SELECTED_PICTURE = (By.CSS_SELECTOR, "div[class^='MMGallery-Item MMGallery-Item_selected']")
class PageClass(BaseClass):
    def enter_word(self, word):
        search_field = self.find_element(Ya_Locators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)

    def check_suggestions(self):
        suggest_field = self.find_element(Ya_Locators.LOCATOR_SUGGEST_FIELD)
        assert suggest_field, 'Таблица с подсказками не появилась'

    def press_enter(self):
        search_field = self.find_element(Ya_Locators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(Keys.ENTER)

    def check_first_link(self):
        first_link = self.find_element(Ya_Locators.LOCATOR_FIRST_SITE)
        first_link_text = self.find_element(Ya_Locators.LOCATOR_FIRST_SITE).text
        print('link: ',first_link_text)
        assert first_link_text == 'tensor.ru', 'Ссылка не соотвествует'

    def open_icon_menu(self):
        icon_menu = self.find_element(Ya_Locators.LOCATOR_ICON_MENU)
        icon_menu.click()
        image_icon = self.find_element(Ya_Locators.LOCATOR_IMAGE_ICON)
        image_icon.click()
        self.redirect_driver()

    def check_url(self, url):
        current_yandex_url = self.find_curr_url(Ya_Locators.LOCATOR_SEARCH_FIELD)
        print('current_yandex_url: ', current_yandex_url)
        assert url == current_yandex_url, 'Ссылки не совпадают'
        
    def open_image_category(self):
        first_image_catagory = self.find_element(Ya_Locators.LOCATOR_FIRST_IMAGE_CATEGORY)          
        first_image_catagory.click()
        self.redirect_driver()

    def check_search_text(self ): 
        search_field_text = self.find_element(Ya_Locators.LOCATOR_SEARCH_FIELD).get_attribute('value')
        print('search_field_text', search_field_text)
        assert len(search_field_text) != 0, 'Текст в поисковой строке не соответствует'

    def open_first_picture(self):
        first_picture = self.find_element(Ya_Locators.LOCATOR_FIRST_PICTURE)
        first_picture.click()
        self.redirect_driver()

    def press_right_circle_button(self):
        circle_button = self.find_element(Ya_Locators.LOCATOR_RIGHT_CIRCLE_BUTTON)
        circle_button.click()
        self.redirect_driver()
        
    def press_left_circle_button(self):
        circle_button = self.find_element(Ya_Locators.LOCATOR_LEFT_CIRCLE_BUTTON)
        circle_button.click()
        self.redirect_driver()

    def check_url_picture(self):
        selected_pic = self.find_element(Ya_Locators.LOCATOR_SELECTED_PICTURE)
        current_yandex_url = self.find_curr_url(Ya_Locators.LOCATOR_SELECTED_PICTURE)
        selected_pic.click()
        self.redirect_driver()
        after_click_yandex_url = self.find_curr_url(Ya_Locators.LOCATOR_SELECTED_PICTURE)
        assert current_yandex_url == after_click_yandex_url, 'Изображения не совпадают'
