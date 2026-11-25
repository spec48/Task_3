import allure
import pytest

from data import PREFIX_OF_NUMBER_1
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL, ORDER_FEED_URL, LOGIN_URL


class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    def test_check_transition_to_main_page(self, main_page, order_page):
        order_page.go_url(ORDER_FEED_URL)
        order_page.click_to_constructor_button()
        assert BASE_URL == main_page.get_current_url(), 'Переход на страницу "Конструктор" не выполнен'

    @allure.title('Переход по клику на "Лента заказов"')
    def test_check_transition_to_order_feed_page(self, main_page, order_page):
        main_page.go_url(BASE_URL)
        main_page.click_to_order_feed_button()
        assert ORDER_FEED_URL == order_page.get_current_url(), 'Переход на страницу "Лента заказов" не выполнен'

    @allure.title('При добавлении ингредиента в заказ, увеличивается счетчик данного ингредиента')
    @pytest.mark.parametrize("from_ingredients, to_order, counter_locator, counter", [
        [MainPageLocators.KRATOR_BUN, MainPageLocators.ORDER, MainPageLocators.KRATOR_BUN_COUNTER, 2],
        [MainPageLocators.GALACTIC_SAUCE, MainPageLocators.ORDER, MainPageLocators.GALACTIC_SAUCE_COUNTER, 1],
        [MainPageLocators.CHOP, MainPageLocators.ORDER, MainPageLocators.CHOP_COUNTER, 1]
    ]
                             )
    def test_adding_an_ingredient_the_counter_increases(self, main_page, from_ingredients, to_order,
                                                             counter_locator, counter):
        main_page.go_url(BASE_URL)
        start_counter = main_page.get_counter_of_ingredient(counter_locator)
        main_page.drag_and_drop_element(from_ingredients, to_order)
        end_counter = main_page.get_counter_of_ingredient(counter_locator)
        assert int(start_counter) + int(end_counter) == counter, 'Счетчик ингредиента не увеличился'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_creating_an_order_by_a_logged_in_user_success(self, user, main_page, login_page, order_page):
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.create_a_burger()
        order_number = PREFIX_OF_NUMBER_1 + main_page.get_order_number()
        main_page.close_popup_window()
        main_page.click_to_order_feed_button()
        numbers_list = order_page.create_numbers_list()
        assert order_number in numbers_list, 'Заказ не оформлен'
