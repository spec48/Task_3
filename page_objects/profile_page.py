import allure

from locators.profile_page_locators import ProfilePageLocators
from page_objects.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        self.wait_for_element_to_be_visible(ProfilePageLocators.ORDER_HISTORY_LINK)
        return self.get_url()

    @allure.step('Клик на "Выход"')
    def click_to_logout_button(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Клик на "История заказов"')
    def click_to_order_history_link(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)
