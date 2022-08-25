import pytest
from pages.main_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url) # переходим на страницу логина
        login_page.should_be_login_page()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link) 
    page.open()                      # Гость открывает главную страницу 
    page.go_direct_to_basket_page()  # Переходит в корзину по кнопке в шапке сайта
    in_basket = BasketPage(browser, browser.current_url)
    in_basket.this_basket_is_empty() # Ожидаем, что в корзине нет товаров и есть сообщение, что корзина пуста


