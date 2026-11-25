from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    ORDER_NUMBERS = By.XPATH, "//p[@class='text text_type_digits-default']"
    POPUP_NUMBER = By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']"
    FOR_ALL_TIME_COUNTER = By.XPATH, "//div[2]/p[contains(@class,'OrderFeed_number__2MbrQ')]"
    TODAY_COUNTER = By.XPATH, "//div[3]/p[contains(@class,'OrderFeed_number__2MbrQ')]"
    NUMBER_IN_PROGRESS = By.XPATH, "//div[1]/ul[2]/li[contains(@class,'text_type_digits-default')]"
    COMPLETE_IN_PROGRESS = By.XPATH, "//li[text()='Все текущие заказы готовы!']"
    COMPLETE_IN_PROGRESS2 = By.XPATH, "//li[@class='text text_type_main-small']"
