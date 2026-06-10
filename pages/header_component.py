from playwright.sync_api import expect
import allure

from pages.base_page import BasePage
from utils.config import BASE_URL, LINKS

class HeaderComponent(BasePage):

	def __init__(self, page):
		super().__init__(page)
		self.button_logout = page.get_by_role('link', name='Logout')

	def logout(self):
		with allure.step("logout button click"):
			self.button_logout.click()

	def assert_invisible_logout_button(self):
		with allure.step("assert invisible logout button after logout"):
			expect(self.button_logout).not_to_be_visible()

