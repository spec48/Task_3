from selenium.webdriver.common.by import By


class PasswordResetPageLocators:

    SAVE_BUTTON = By.XPATH, "//button[text()='Сохранить']"
    SHOW_PASSWORD_BUTTON = By.XPATH, "//div[@class='input__icon input__icon-action']"
    ACTIVE_PASSWORD_FIELD = By.XPATH, ("//div[@class='input pr-6 pl-6 input_type_text "
                                    "input_size_default input_status_active']")
