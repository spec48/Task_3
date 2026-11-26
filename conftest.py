import pytest
from selenium import webdriver

from helpers import generate_user_data
from page_objects.ingredient_page import IngredientPage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage
from page_objects.order_history_page import OrderHistoryPage
from page_objects.password_recovery_page import PasswordRecoveryPage
from page_objects.password_reset_page import PasswordResetPage
from page_objects.profile_page import ProfilePage
from user_methods import UserMethods


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    yield browser
    browser.quit()

@pytest.fixture()
def user():
    user_methods = UserMethods()
    user_data = generate_user_data()
    user_methods.create_user(user_data)
    yield user_data
    user_methods.delete_user()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture
def recovery_page(driver):
    page = PasswordRecoveryPage(driver)
    return page

@pytest.fixture
def reset_page(driver):
    page = PasswordResetPage(driver)
    return page

@pytest.fixture
def profile_page(driver):
    page = ProfilePage(driver)
    return page

@pytest.fixture
def order_page(driver):
    page = OrderFeedPage(driver)
    return page

@pytest.fixture
def ingredient_page(driver):
    page = IngredientPage(driver)
    return page

@pytest.fixture
def history_page(driver):
    page = OrderHistoryPage(driver)
    return page
