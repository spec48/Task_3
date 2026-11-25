from selenium.webdriver.common.by import By


class MainPageLocators:

    ACCOUNT_LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    KRATOR_BUN = By.XPATH, "//p[contains(@class,'BurgerIngredient_ingredient') and text()='Краторная булка N-200i']"
    KRATOR_BUN_COUNTER = By.XPATH, "//section[1]//ul[1]/a[1]//p"
    GALACTIC_SAUCE = By.XPATH, "//p[text()='Соус традиционный галактический']"
    GALACTIC_SAUCE_COUNTER = By.XPATH, "//section[1]//ul[2]/a[4]//p"
    CHOP = By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']"
    CHOP_COUNTER = By.XPATH, "//section[1]//ul[3]/a[8]//p"
    ORDER = By.XPATH, "//section[2]"
    ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    NUMBER_9999 = By.XPATH, "//h2[text()='9999']"
    ORDER_NUMBER = By.XPATH, ("//h2[contains(@class,'Modal_modal__title_shadow__3ikwq') "
                              "and not(contains(text(), '9999'))]")
    CLOSE_POPUP = By.XPATH, "//section/div[1]/button"
