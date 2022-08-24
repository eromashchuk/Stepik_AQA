from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):
    def add_to_cart(self):
        self.should_be_submit_button()
        self.add_item_to_cart()
        self.bookname_same_in_basket()
        self.correct_price_in_basket()
            
    def should_be_submit_button(self):
        assert self.is_element_present(*ProductPageLocators.SBM_BUTTON), "Submit button is not presented" 
        #символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать

    def add_item_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.SBM_BUTTON)
        button.click()
        self.browser.implicitly_wait(15)
        self.solve_quiz_and_get_code()

    def bookname_same_in_basket(self):
        item = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        item_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET_NAME)
        assert item.text == item_in_basket.text, "Item name different in the basket"
        print(f"{item_in_basket.text} in the basket")

    def correct_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET)
        assert price.text == price_in_basket.text, "Price incorrect in the basket"
        print(f"Price {price_in_basket.text} is correct")

    #метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    #метод, который проверяет, что сообщение исчезает
    def success_message_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"

