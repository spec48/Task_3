import allure

from locators.login_page_locators import LoginPageLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Кликнуть на линк "Восстановить пароль"')
    def click_to_password_recovery_link(self):
        self.wait_for_element_to_be_visible(LoginPageLocators.RECOVERY_PASSWORD_LINK)
        self.click_element(LoginPageLocators.RECOVERY_PASSWORD_LINK)

    @allure.step('Заполнить форму логина')
    def fill_out_the_login_form(self, data):
        self.wait_for_element_to_be_visible(LoginPageLocators.EMAIL_FIELD)
        self.click_element(LoginPageLocators.EMAIL_FIELD)
        self.fill_out_the_field(LoginPageLocators.EMAIL_FIELD, data['email'])
        self.click_element(LoginPageLocators.PASSWORD_FIELD)
        self.fill_out_the_field(LoginPageLocators.PASSWORD_FIELD, data['password'])
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_until_not_visible(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        return self.get_url()
