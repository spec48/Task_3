import allure

from locators.order_history_page_locators import OrderHistoryPageLocators
from page_objects.base_page import BasePage


class OrderHistoryPage(BasePage):

    @allure.step('Получить последний номер заказа')
    def get_last_number(self):
        self.find_elements(OrderHistoryPageLocators.ORDER_IN_HISTORY)
        items = self.find_elements(OrderHistoryPageLocators.ORDER_IN_HISTORY)
        number = items[-1].text
        return number
