import allure

from locators.password_reset_page_locators import PasswordResetPageLocators
from page_objects.base_page import BasePage


class PasswordResetPage(BasePage):

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        self.find_element(PasswordResetPageLocators.SAVE_BUTTON)
        return self.get_url()

    @allure.step('Поле "Пароль" активно')
    def active_password_fild_is_displayed(self):
        self.wait_for_element_to_be_visible(PasswordResetPageLocators.SHOW_PASSWORD_BUTTON)
        self.click_element(PasswordResetPageLocators.SHOW_PASSWORD_BUTTON)
        return self.find_element(PasswordResetPageLocators.ACTIVE_PASSWORD_FIELD).is_displayed()
