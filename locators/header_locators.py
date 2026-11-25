from selenium.webdriver.common.by import By


class HeaderLocators:

    PROFILE_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
