from .base_page import BasePage
from .locators import CartPageLocators

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}

class CartPage(BasePage):
    def should_be_empty_cart(self):
        message_empty_cart = self.browser.find_element(*CartPageLocators.MESSAGE_CART_EMPTY)
        message_empty_cart_text = message_empty_cart.text
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        message_empty_cart_correct = languages[language]
        assert message_empty_cart_correct in message_empty_cart_text, "No message about empty cart"
