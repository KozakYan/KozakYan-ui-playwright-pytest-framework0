import pytest
import allure
import re
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.header_component import HeaderComponent

from data.auth.users import VALID_USER
from data.auth.invalid_data import INVALID_LOGIN_DATA

pytestmark = allure.feature("follow in main manu")

@allure.title("logout user")
def test_logout(login, header_component, login_page):
	header_component.logout()
	login_page.assert_url_login_page()
	login_page.assert_button_login()
