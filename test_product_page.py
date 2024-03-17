import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time

@pytest.mark.add_to_cart_guest
class TestGuestAddToCartFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_cart()
        page.should_be_correct_product_name()
        page.should_be_correct_cart_price()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_disappear_success_message()

@pytest.mark.add_to_cart_user
class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = f"pupkin{time.time()}@randmail.com"
        password = f"qwerty123456{time.time()}"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_cart()
        page.should_be_correct_product_name()
        page.should_be_correct_cart_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_empty_cart()

@pytest.mark.login_guest
class TestGuestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
