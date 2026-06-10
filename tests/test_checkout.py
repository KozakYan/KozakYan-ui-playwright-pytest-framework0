import pytest
import allure
import re
from playwright.sync_api import Page, expect

from pages.products_catalog_page import CatalogPage

from utils.config import BASE_URL

pytestmark = allure.feature("checout")

@allure.title("e2e test add product to cart")
def test_add_product_to_cart(login, product_catalog_page, clean_cart):
	product_catalog_page.open_catalog_page()
	product_page = product_catalog_page.open_first_product()
	name_product = product_page.get_name_product()
	price_product = product_page.get_price_product()
	cart_page = product_page.add_product_to_cart()
	product_catalog_page.go_to_cart_page_in_pop_ap_added()
	cart_page.assert_name_product_in_cart(name_product)
	cart_page.assert_price_product_in_cart(price_product)

@allure.title("remove product in cart")
def test_remove_product_in_cart(login, add_product_to_cart, cart_page):
	cart_page.open_cart_page()
	cart_page.remove_product()
	cart_page.assert_empty_cart()



