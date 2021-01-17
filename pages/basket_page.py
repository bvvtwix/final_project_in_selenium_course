from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present \
                   (*BasketPageLocators.PRODUCT_IS) == False, "Product in basket is presented, but should not be"
        assert self.is_not_element_present \
            (*BasketPageLocators.BASKET_IS_EMPTY), "Empty basket message is presented, but should not be"