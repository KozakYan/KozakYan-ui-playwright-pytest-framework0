import allure

from playwright.sync_api import expect

from pages.base_page import BasePage

from utils.config import BASE_URL, LINKS


class LoginPage(BasePage):

	def __init__(self, page):
		super().__init__(page)
		self.signup_login_link = page.get_by_role('link', name='Signup / Login')
		self.email_login_input = page.locator('[data-qa="login-email"]')
		self.password_login_input = page.locator('[data-qa="login-password"]')
		self.button_login = page.get_by_role('button', name='Login')
		self.button_logout = page.get_by_role('link', name='Logout')
		self.message_invalid_login_data = page.get_by_text('Your email or password is incorrect!')

	def open_login_page(self):
		with allure.step("open login page"):
			self.open()
			self.signup_login_link.click()

	def login(self, email, password):
		with allure.step("login user"):
			self.email_login_input.fill(email)
			self.password_login_input.fill(password)
			self.button_login.click()

	def assert_visible_button_logout(self):
		with allure.step("assert visible button logout after login"):
			expect(self.button_logout).to_be_visible()

	def assert_visible_text_after_login(self, username):
		with allure.step("assert visible text 'Logged in as...'"):
			expect(self.page.get_by_text(f"Logged in as {username}")).to_be_visible()

	def assert_invalid_login_message_visible(self):
		with allure.step("assert visible text 'Your email or password is incorrect!'"):
			expect(self.message_invalid_login_data).to_be_visible()

	def assert_url_login_page(self):
		with allure.step("assert url login page"):
			expect(self.page).to_have_url(f'{BASE_URL}{LINKS["login"]}')

	def assert_button_login(self):
		with allure.step("assert visible button login in page login"):
			expect(self.button_login).to_be_visible()

	def is_email_valid(self):
		with allure.step("assert hover on input email after invalid login"):
			assert not self.email_login_input.evaluate(
				"el => el.checkValidity()"
			)

	def is_password_valid(self):
		with allure.step("assert hover on input password after invalid login"):
			assert not self.password_login_input.evaluate(
				"el => el.checkValidity()"
			)


