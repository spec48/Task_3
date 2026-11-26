import allure

from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.modal_overlay_locators import ModalOverlayLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликнуть на кнопку "Войти в аккаунт"')
    def click_to_account_login_button(self):
        self.click_element(MainPageLocators.ACCOUNT_LOGIN_BUTTON)

    @allure.step('Кликнуть на "Личный кабинет"')
    def click_to_account_button(self):
        self.click_element(HeaderLocators.PROFILE_BUTTON)

    @allure.step('Кликнуть на "Лента заказов"')
    def click_to_order_feed_button(self):
        self.click_element(HeaderLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть на кнопку "Оформить заказ"')
    def click_to_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        self.wait_for_element_to_be_visible(MainPageLocators.KRATOR_BUN)
        return self.get_url()

    @allure.step('Кликнуть на ингредиент')
    def click_to_ingredient(self, ingredient):
        self.find_element(ingredient)
        self.click_element(ingredient)

    @allure.step('Получить название ингредиента')
    def get_name_of_ingredient(self, locator):
        return self.get_text_from_element(locator)

    @allure.step('Получить счётчик ингредиента')
    def get_counter_of_ingredient(self, locator):
        return self.get_text_from_element(locator)

    @allure.step('Переместить ингредиент в корзину')
    def drag_and_drop_element(self, source, target):

        from selenium.webdriver.remote.webelement import WebElement

        if not isinstance(source, WebElement):
            source = self.find_element(source)
        if not isinstance(target, WebElement):
            target = self.find_element(target)

        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();

                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dragEnterEvent = new DragEvent('dragenter', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dragEnterEvent);

                var dragOverEvent = new DragEvent('dragover', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dragOverEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);

                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source, target)

    @allure.step('Создать бургер')
    def create_a_burger(self):
        self.drag_and_drop_element(MainPageLocators.KRATOR_BUN, MainPageLocators.ORDER)
        self.drag_and_drop_element(MainPageLocators.GALACTIC_SAUCE, MainPageLocators.ORDER)
        self.drag_and_drop_element(MainPageLocators.CHOP, MainPageLocators.ORDER)
        self.click_to_order_button()

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_until_not_visible(MainPageLocators.NUMBER_9999)
        self.find_element(MainPageLocators.ORDER_NUMBER)
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Ожидать номер заказа')
    def wait_order_number(self):
        self.wait_until_not_visible(MainPageLocators.NUMBER_9999)
        self.find_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Закрыть окно заказа')
    def close_popup_window(self):
        self.click_element(MainPageLocators.CLOSE_POPUP)
        self.wait_until_not_visible(ModalOverlayLocators.MODAL_OVERLAY)

    @allure.step('Создать заказ')
    def create_an_order(self):
        self.create_a_burger()
        self.wait_order_number()
        self.close_popup_window()
