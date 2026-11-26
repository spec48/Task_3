import allure

from data import user_data
from locators.modal_overlay_locators import ModalOverlayLocators
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from page_objects.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        self.wait_until_not_visible(ModalOverlayLocators.MODAL_OVERLAY)
        self.wait_for_element_to_be_visible(PasswordRecoveryPageLocators.RECOVERY_BUTTON)
        return self.get_url()

    @allure.step('Заполнить поле email')
    def fill_out_the_email_field(self):
        self.wait_for_element_to_be_visible(PasswordRecoveryPageLocators.EMAIL_FIELD)
        self.click_element(PasswordRecoveryPageLocators.EMAIL_FIELD)
        self.fill_out_the_field(PasswordRecoveryPageLocators.EMAIL_FIELD, user_data['email'])
        self.click_element(PasswordRecoveryPageLocators.RECOVERY_BUTTON)
