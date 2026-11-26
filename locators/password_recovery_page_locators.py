from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    EMAIL_FIELD = By.XPATH, "//input[@type='text']"
    RECOVERY_BUTTON = By.XPATH, "//button[text()='Восстановить']"
