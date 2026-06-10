import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.header_component import HeaderComponent
from pages.products_catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


from utils.config import BASE_URL, LINKS

from data.auth.users import VALID_USER
from data.auth.invalid_data import INVALID_LOGIN_DATA

@pytest.fixture()
def login_page(page: Page):
	loginpage_obj = LoginPage(page)
	return loginpage_obj

@pytest.fixture
def login(login_page):
	login_page.open(LINKS["login"])
	login_page.login(
	VALID_USER["email"],
	VALID_USER["password"]
	)
	return login_page

@pytest.fixture
def go_to_page_login(login_page):
	login_page.open(LINKS["login"])
	return login_page

@pytest.fixture
def header_component(page: Page):
	header_component_obj = HeaderComponent(page)
	return header_component_obj

@pytest.fixture
def logout(header_component):
	yield
	header_component.logout()

@pytest.fixture
def product_catalog_page(page: Page):
	product_catalog_page_obj = CatalogPage(page)
	return product_catalog_page_obj

@pytest.fixture
def product_page(page: Page):
	return ProductPage(page)

@pytest.fixture #спростити всі фікстури пейджів до такого варіанту
def cart_page(page: Page):
	return CartPage(page)

@pytest.fixture
def add_product_to_cart(product_page):
	product_page.go_to_product_page()
	product_page.add_product_to_cart()

@pytest.fixture
def clean_cart(cart_page):
	yield
	cart_page.remove_product()
	


