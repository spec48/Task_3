import allure
from selenium.common import TimeoutException

from locators.ingredient_page_locators import IngredientPageLocators
from page_objects.base_page import BasePage


class IngredientPage(BasePage):

    @allure.step('Получить названия ингредиента')
    def get_name_of_ingredient_from_popup_window(self, locator):
        self.find_element(IngredientPageLocators.CLOSE_BUTTON)
        return self.get_text_from_element(locator)

    @allure.step('Кликнуть на крестик')
    def click_to_close_button(self):
        self.find_element(IngredientPageLocators.CLOSE_BUTTON)
        self.click_element(IngredientPageLocators.CLOSE_BUTTON)

    @allure.step('Ожидать закрытия окна с деталями')
    def detail_window_closes(self,locator):
        try:
            self.wait_until_not_visible(locator)
            return True
        except TimeoutException:
            return False
