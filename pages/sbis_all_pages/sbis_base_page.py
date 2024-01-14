from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import SbisBasePageLocators


class SbisBasePage(BasePage):
    def go_to_contact_page(self):
        contact_link = self.element_to_be_clickable(*SbisBasePageLocators.CONTACT_LINK)
        contact_link.click()

    def should_be_contact_link(self):
        assert self.is_element_present(*SbisBasePageLocators.CONTACT_LINK), "contact link is not presented"

    def go_to_download_page(self):
        self.execute_script_click(*SbisBasePageLocators.FOOTER_TRANSIT_DOWNLOAD_SBIS)


