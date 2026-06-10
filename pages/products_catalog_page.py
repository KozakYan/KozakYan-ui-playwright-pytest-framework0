from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.product_page import ProductPage

from utils.config import BASE_URL, LINKS

class CatalogPage(BasePage):

	def __init__(self, page):
		super().__init__(page)
		self.add_product_button = page.get_by_role("button", name="Add to cart")
		self.view_products = page.get_by_role("link", name="View Product")
		self.button_close_pop_ap_added = page.get_by_role("button", name="Continue Shopping")
		self.button_view_cart_on_pop_ap_added = page.get_by_role("link", name="View Cart")

	def open_catalog_page(self):
		super().open(LINKS["catalog"])

	def add_to_cart(self):
		self.add_product_button.click()

	def open_first_product(self):
		self.view_products.first.click()
		return ProductPage(self.page)

	def clouse_pop_ap_added(self):
		self.button_close_pop_ap_added.click()

	def go_to_cart_page_in_pop_ap_added(self):
		self.button_view_cart_on_pop_ap_added.click()

	
