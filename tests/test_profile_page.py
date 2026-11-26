import allure

from urls import PROFILE_URL, ORDER_HISTORY_URL, LOGIN_URL


class TestProfilePage:

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_check_transition_to_profile_page(self, user, main_page, login_page, profile_page):
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.click_to_account_button()
        assert PROFILE_URL == profile_page.get_current_url(), 'Переход на страницу "Личный кабинет" не выполнен'

    @allure.title('Переход в раздел "История заказов"')
    def test_check_transition_to_order_history_page(self, user, main_page, login_page, profile_page):
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.click_to_account_button()
        profile_page.click_to_order_history_link()
        assert ORDER_HISTORY_URL == profile_page.get_current_url(), 'Переход на страницу "История заказов" не выполнен'

    @allure.title('Выход из аккаунта')
    def test_check_transition_to_login_page(self, user, main_page, login_page, profile_page):
        login_page.go_url(LOGIN_URL)
        login_page.fill_out_the_login_form(user)
        main_page.click_to_account_button()
        profile_page.click_to_logout_button()
        assert LOGIN_URL == login_page.get_current_url(), 'Выход из аккаунта не выполнен'
