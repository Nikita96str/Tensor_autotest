from site_page import PageClass

def test_yandex_image(browser):
    yandex_page = PageClass(browser)
    yandex_page.go_to_site()
    yandex_page.enter_word('')
    yandex_page.open_icon_menu()
    yandex_page.check_url('https://yandex.ru/images/')
    yandex_page.open_image_category()
    yandex_page.check_search_text()
    yandex_page.open_first_picture()
    yandex_page.check_url_picture()
    yandex_page.press_right_circle_button()
    yandex_page.check_url_picture()
    yandex_page.press_left_circle_button()
    yandex_page.check_url_picture()
