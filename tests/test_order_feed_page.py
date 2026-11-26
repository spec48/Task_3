import allure
import pytest

from data import PREFIX_OF_NUMBER_2
from locators.order_feed_page_locators import OrderFeedPageLocators
from urls import LOGIN_URL, ORDER_FEED_URL


class TestOrderFeedPage:

    @allure.title('При клике на заказ, открывается всплывающее окно с деталями')
    def test_popup_window_with_order_details_is_displayed(self, user, main_page, login_page, order_page):
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.create_an_order()
        main_page.click_to_order_feed_button()
        last_feed_number = order_page.create_numbers_list()[0]
        order_page.click_order_number()
        details_popup_number = order_page.get_number_from_details_popup()
        assert details_popup_number == last_feed_number, 'Всплывающее окно с деталями не открылось'

    @allure.title('Заказ пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_order_from_history_page_is_displayed_in_order_feed_page(self, user, main_page, login_page, order_page,
                                                                     profile_page, history_page):
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.create_an_order()
        main_page.click_to_account_button()
        profile_page.click_to_order_history_link()
        order_in_history = history_page.get_last_number()
        main_page.click_to_order_feed_button()
        orders_in_feed = order_page.create_numbers_list()
        assert order_in_history in orders_in_feed, ('Заказ пользователя из раздела "История заказов" не отображается '
                                                    'на странице "Лента заказов"')

    @allure.title('При создании нового заказа счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @pytest.mark.parametrize("counter", [
        OrderFeedPageLocators.FOR_ALL_TIME_COUNTER,
        OrderFeedPageLocators.TODAY_COUNTER
    ]
                             )
    def test_creating_an_order_completed_counters_increase(self, user, main_page, login_page, order_page, counter):
        order_page.go_url(ORDER_FEED_URL)
        counter_before_order = order_page.get_counter(counter)
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.create_an_order()
        main_page.click_to_order_feed_button()
        counter_after_order = order_page.get_counter(counter)
        assert counter_after_order > counter_before_order, 'Счётчик "Выполнено" не увеличился'

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_after_creating_an_order_order_number_appears_in_progress_section(self, user, main_page, login_page, order_page):
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.create_a_burger()
        order_number = PREFIX_OF_NUMBER_2 + main_page.get_order_number()
        main_page.close_popup_window()
        main_page.click_to_order_feed_button()
        number_in_progress = order_page.get_number_list_in_progress(order_number)
        assert order_number in number_in_progress, 'Номер заказа не появился в разделе "В работе"'
