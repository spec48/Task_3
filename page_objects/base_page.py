from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 4
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_elements(*locator)

    def wait_until_not_visible(self, locator):
        self.wait.until_not(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_visibility_of_all_elements(self, locator):
        self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))

    def click_element(self, locator):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    def fill_out_the_field(self, field, value):
        self.find_element(field).send_keys(value)

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text
