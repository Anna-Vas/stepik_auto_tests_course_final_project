from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BUTTON_GO_TO_CART = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CLASS_NAME, "icon-user")

class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_CART_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class CartPageLocators:
    MESSAGE_CART_EMPTY = (By.CSS_SELECTOR, "#content_inner p")