import allure

from urls import RECOVERY_URL, RESET_URL, LOGIN_URL


class TestRecoveryPasswordPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_check_transition_to_password_recovery_page(self, login_page, recovery_page):
        login_page.go_url(LOGIN_URL)
        login_page.click_to_password_recovery_link()
        assert RECOVERY_URL == recovery_page.get_current_url(), 'Переход на страницу восстановления пароля не выполнен'

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_check_transition_to_password_reset_page(self, login_page, recovery_page, reset_page):
        login_page.go_url(LOGIN_URL)
        login_page.click_to_password_recovery_link()
        recovery_page.fill_out_the_email_field()
        assert RESET_URL == reset_page.get_current_url(), 'Переход на страницу сброса пароля не выполнен'

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_check_activity_password_field(self, login_page, recovery_page, reset_page):
        login_page.go_url(LOGIN_URL)
        login_page.click_to_password_recovery_link()
        recovery_page.fill_out_the_email_field()
        assert reset_page.active_password_fild_is_displayed(), 'Поле password не активно'
