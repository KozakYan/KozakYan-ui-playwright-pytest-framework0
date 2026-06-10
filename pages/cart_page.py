from playwright.sync_api import expect
import allure

from pages.base_page import BasePage

from utils.config import BASE_URL, LINKS

class CartPage(BasePage):

	def __init__(self, page):
		super().__init__(page)
		self.name_product_in_cart = page.locator(".cart_description h4")
		self.price_product_in_cart = page.locator(".cart_price")
		self.remove_product_button = page.locator(".cart_quantity_delete")
		self.text_empty_cart = page.get_by_text('Cart is empty!')

	def open_cart_page(self):
		with allure.step("open cart page"):
			super().open(LINKS["cart"])

	def assert_name_product_in_cart(self, name_product):
		with allure.step("comparison of product name in catalog and cart"):
			name_product_in_cart = self.name_product_in_cart.inner_text()
			assert name_product == name_product_in_cart

	def assert_price_product_in_cart(self, price_product):
		with allure.step("comparison of product price in catalog and cart"):
			price_product_in_cart = self.price_product_in_cart.inner_text().strip()
			assert price_product == price_product_in_cart

	def remove_product(self):
		with allure.step("remove product in cart"):
			while self.remove_product_button.count() > 0:
				btn = self.remove_product_button.first
				btn.click()
				btn.wait_for(state="detached")

	def assert_empty_cart(self):
		with allure.step("assert visible text 'Cart is empty!' after remove product"):
			self.text_empty_cart.wait_for(state="visible")
			expect(self.text_empty_cart).to_be_visible()













