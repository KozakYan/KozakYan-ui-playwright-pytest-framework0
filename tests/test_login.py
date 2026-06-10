import pytest
import allure
import re
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

from utils.config import BASE_URL
from data.auth.users import VALID_USER
from data.auth.invalid_data import INVALID_LOGIN_DATA

pytestmark = allure.feature("sing in")

@allure.title("login user")
def test_login(login_page, logout):
	login_page.open_login_page()
	login_page.login(
        VALID_USER["email"],
        VALID_USER["password"]
    )
	login_page.assert_visible_button_logout()
	login_page.assert_visible_text_after_login(VALID_USER["user_name"])

@allure.title("login user which invalid data")
@pytest.mark.parametrize("email, password", INVALID_LOGIN_DATA)
def test_invalid_login(go_to_page_login, email, password):
    go_to_page_login.login(email, password)
    go_to_page_login.assert_invalid_login_message_visible()

@allure.title("login user which empty email")
def test_login_empty_email(go_to_page_login):
    go_to_page_login.login("", VALID_USER["password"])
    go_to_page_login.is_email_valid()
    
@allure.title("login user which empty password")
def test_login_empty_password(go_to_page_login):
    go_to_page_login.login(VALID_USER["email"], "")
    go_to_page_login.is_password_valid()
