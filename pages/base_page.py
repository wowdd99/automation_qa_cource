from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        with allure.step(f'Open page: {self.url}'):
            self.driver.get(self.url)

    @allure.step('Check element is visible')
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Check elements are visible')
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    #позволяет искать по дом-дереву
    @allure.step('Check element is present')
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Check elements are present')
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Check elements is not visible')
    def elements_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Check elements is clickable')
    def elements_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Scroll to element')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # def remove_footer(self):
    #     self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
    #     self.driver.execute_script("document.getElementsById('close-fixedban').remove();")

    @allure.step('Remove fixedban')
    def remove_fixedban(self):
        self.driver.execute_script("document.getElementById('fixedban').style.display = 'none'")
        print('Remove Fixedban')


