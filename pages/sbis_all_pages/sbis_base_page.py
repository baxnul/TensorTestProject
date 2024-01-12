from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import SbisBasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        """Открыть ссылку"""
        self.browser.get(self.url)

    def go_to_contact_page(self):
        contact_link = self.browser.find_element(*SbisBasePageLocators.CONTACT_LINK)
        contact_link.click()

    def should_be_contact_link(self):
        assert self.is_element_present(*SbisBasePageLocators.CONTACT_LINK), "contact link is not presented"

    def is_element_present(self, by, locator, timeout=4) -> bool:
        """Проверка на присутсвие элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False
        return True

    def get_element(self, by, locator, timeout=10) -> object:
        """Найти и получить элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {locator} not found: {e}")
            return None

    def is_not_element_present(self, by, locator, timeout=4) -> bool:
        """Элемент не появляется на странице в течение заданного времени.
        Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by, locator, timeout=4) -> bool:
        """Проверить, что какой-то элемент исчезает.
         Будет ждать до тех пор, пока элемент не исчезнет."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False
        return True

    def switch_to_last_window(self):
        return self.browser.switch_to.window(self.browser.window_handles[-1])  # Переключиться на последнюю вкладку
