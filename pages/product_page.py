from playwright.sync_api import expect
import random

from pages.base_page import BasePage
from pages.cart_page import CartPage

from utils.config import BASE_URL, LINKS

class ProductPage(BasePage):

	def __init__(self, page):
		super().__init__(page)
		self.add_product_button = page.get_by_role("button", name="Add to cart")
		self.name_product = page.locator(".product-information h2")
		self.price_product = page.locator(".product-information span span")

	def go_to_product_page(self):
		super().open(random.choice(LINKS['product_pages']))

	def add_product_to_cart(self):
		self.add_product_button.click()
		return CartPage(self.page)
		
	def get_name_product(self):
		return self.name_product.inner_text()

	def get_price_product(self):
		return self.price_product.inner_text().strip()










