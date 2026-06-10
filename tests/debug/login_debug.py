import pytest
import re
from playwright.sync_api import Page, expect, Browser, Locator

url = 'https://automationexercise.com/'
user_name = 'wesss'

def test_login(page: Page):
	page.goto(url)

	page.get_by_role('link', name='Signup / Login').click()

	page.locator('[data-qa="login-email"]').fill('dj2risk2@mediaeast.uk')

	page.locator('[data-qa="login-password"]').fill('wesss')

	page.get_by_role('button', name='Login').click()

	expect(page).to_have_url('https://automationexercise.com/')

	expect(page.get_by_role('link', name='Logout')).to_be_visible()
	
	expect(page.get_by_text(f'Logged in as {user_name}')).to_be_visible()
