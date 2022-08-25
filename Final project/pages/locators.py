from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BUSKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    ALL_ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")

class LoginPageLocators():
    LOGIN_URL = "'login' in self.browser.current_url"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTER_SUCCESS = (By.CSS_SELECTOR, "#messages .alertinner.wicon")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  

class ProductPageLocators():
    SBM_BUTTON = (By.CSS_SELECTOR, ".btn-lg.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR,'.product_main .price_color')
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR,'#messages :nth-child(3) p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

