from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_KINK = (By.XPATH, '//a[text()="Посмотреть корзину"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    PRICE = (By.CSS_SELECTOR, '#content_inner .price_color')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')

class BasketPageLocators():
    PRODUCT_IS = (By.CSS_SELECTOR, '#content_inner :nth-child(2)')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner div")