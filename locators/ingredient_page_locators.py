from selenium.webdriver.common.by import By


class IngredientPageLocators:

    POPUP_WINDOW = By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']"
    KRATOR_BUN_IN_POPUP = By.XPATH, ("//p[contains(@class,'text text_type_main-medium mb-8')"
                                     " and text()='Краторная булка N-200i']")
    CLOSE_BUTTON = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
