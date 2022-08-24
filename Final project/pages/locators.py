from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  
    
class LoginPageLocators():
    LOGIN_URL = "'login' in self.browser.current_url"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    SBM_BUTTON = (By.CSS_SELECTOR, ".btn-lg.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR,'.product_main .price_color')
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR,'#messages :nth-child(3) p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
