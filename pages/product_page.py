from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def check_product_name(self):
        product_main = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_main_text = product_main.text

        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        product_in_basket_text = product_in_basket.text

        assert product_in_basket_text == product_main_text, f'Добавлен не верный продукт {product_in_basket_text}'

    def check_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE)
        product_price_text = product_price.text

        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket_text = price_in_basket.text

        assert price_in_basket_text == product_price_text, 'Не совпадает цена товара'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET) == False, "Success message is presented, but should not be"

    def should_not_be_success_message_by_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET), "Success message is presented, but should not be"