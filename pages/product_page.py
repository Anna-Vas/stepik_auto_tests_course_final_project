from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Add to cart button is not present"
    def press_button_add_to_cart(self):
        self.should_be_button_add_to_cart()
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
    def should_be_message_added_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDED_TO_CART), "Message about product added to cart is not present"
    def should_be_correct_product_name(self):
        self.should_be_product_name()
        self.should_be_message_added_to_cart()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_TO_CART).text
        assert product_name == message_product_name,\
            f"No product name in the message: product name should be {product_name}, not {message_product_name}"
    def should_be_message_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART_TOTAL), "Message with the cart price is not presented"
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
    def should_be_correct_cart_price(self):
        self.should_be_message_cart_price()
        self.should_be_product_price()
        message_cart_total = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_cart_total,\
            f"Incorrect product price in the message: price should be {product_price}, not {message_cart_total}"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDED_TO_CART), "Success message is presented, but should not be"
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDED_TO_CART), "Success message does not disappear"