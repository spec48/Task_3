import allure

from locators.header_locators import HeaderLocators
from locators.modal_overlay_locators import ModalOverlayLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from page_objects.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        self.wait_until_not_visible(ModalOverlayLocators.MODAL_OVERLAY)
        self.wait_for_element_to_be_visible(OrderFeedPageLocators.ORDER_NUMBERS)
        return self.get_url()

    @allure.step('Кликнуть на "Конструктор"')
    def click_to_constructor_button(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Создать список номеров из "Лента заказов"')
    def create_numbers_list(self):
        self.wait_until_not_visible(ModalOverlayLocators.MODAL_OVERLAY)
        items = self.find_elements(OrderFeedPageLocators.ORDER_NUMBERS)
        numbers_list = []
        for item in items:
            number = item.text
            numbers_list.append(number)
        return numbers_list

    @allure.step('Кликнуть на номер заказа')
    def click_order_number(self):
        self.click_element(OrderFeedPageLocators.ORDER_NUMBERS)

    @allure.step('Получить номер из окна с деталями')
    def get_number_from_details_popup(self):
        self.wait_until_not_visible(ModalOverlayLocators.MODAL_OVERLAY)
        self.wait_for_element_to_be_visible(OrderFeedPageLocators.POPUP_NUMBER)
        return self.get_text_from_element(OrderFeedPageLocators.POPUP_NUMBER)

    @allure.step('Получить счётчик "Выполнено"')
    def get_counter(self, locator):
        self.wait_until_not_visible(ModalOverlayLocators.MODAL_OVERLAY)
        self.wait_for_element_to_be_visible(OrderFeedPageLocators.ORDER_NUMBERS)
        return self.get_text_from_element(locator)

    @allure.step('Ожидать появление номера заказа в "В работе"')
    def wait_numbers_in_progress(self):
        self.wait.until(lambda d: len(d.find_elements(*OrderFeedPageLocators.NUMBER_IN_PROGRESS)) > 0)
        return [element.text for element in self.find_elements(OrderFeedPageLocators.NUMBER_IN_PROGRESS)]

    @allure.step('Получить список номеров заказов в "В работе"')
    def get_number_list_in_progress(self, expected_number):
        self.wait.until(lambda d: expected_number in self.wait_numbers_in_progress())
        return [element.text for element in self.find_elements(OrderFeedPageLocators.NUMBER_IN_PROGRESS)]
