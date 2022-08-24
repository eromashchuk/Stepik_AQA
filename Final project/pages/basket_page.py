from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
import time

class BasketPage(BasePage):
    def this_basket_is_empty(self):
        self.should_be_empty_basket_message()
        self.basket_is_empty()

    #Ожидаем, что есть текст о том что корзина пуста 
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BUSKET_TEXT), "Busket button is not presented" 
 
    #Ожидаем, что в корзине нет товаров
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ALL_ITEMS_IN_BASKET), "Busket is not empty!"