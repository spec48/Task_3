import allure
import pytest

from locators.ingredient_page_locators import IngredientPageLocators
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL


class TestIngredientPage:

    @allure.title('При клике на ингредиент, появляется всплывающее окно с деталями.')
    @pytest.mark.parametrize("main_page_ingredient, popup_ingredient", [
        [MainPageLocators.KRATOR_BUN, IngredientPageLocators.KRATOR_BUN_IN_POPUP]
    ]
                             )
    def test_popup_window_with_ingredient_details_is_displayed(self, main_page, ingredient_page,
                                                               main_page_ingredient, popup_ingredient):
        main_page.go_url(BASE_URL)
        ingredient_name_from_main_page = main_page.get_name_of_ingredient(main_page_ingredient)
        main_page.click_to_ingredient(main_page_ingredient)
        ingredient_name_from_details_window = ingredient_page.get_name_of_ingredient_from_popup_window(popup_ingredient)
        assert ingredient_name_from_main_page == ingredient_name_from_details_window, \
            'Всплывающее окно с деталями ингредиента не появилось'

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @pytest.mark.parametrize("main_page_ingredient, popup_ingredient", [
        [MainPageLocators.KRATOR_BUN, IngredientPageLocators.KRATOR_BUN_IN_POPUP]
    ]
                             )
    def test_details_window_closed_by_clicking_to_close_button(self, main_page, ingredient_page,
                                                               main_page_ingredient, popup_ingredient):
        main_page.go_url(BASE_URL)
        main_page.click_to_ingredient(main_page_ingredient)
        ingredient_page.click_to_close_button()
        assert ingredient_page.detail_window_closes(popup_ingredient), \
            'Всплывающее окно не закрывается кликом по крестику'
