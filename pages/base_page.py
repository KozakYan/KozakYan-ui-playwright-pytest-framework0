from playwright.sync_api import Page

from utils.config import BASE_URL

class BasePage():

	def __init__(self, page: Page):
		self.page = page

	def open(self, path=""):
		self.page.goto(f"{BASE_URL}{path}")



	# def click(self):

	# def fill()

	# def viseble_text(self):


