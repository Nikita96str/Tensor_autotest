from site_page import PageClass

def test_yandex_search(browser):
    yandex_page = PageClass(browser)
    yandex_page.go_to_site()
    yandex_page.enter_word('Тензор')
    yandex_page.check_suggestions()
    yandex_page.press_enter()
    yandex_page.check_first_link()
