from .sbis_base_page import BasePage
from pages.locators import SbisContactPageLocators


class SbisContactPage(BasePage):
    def should_be_contact_page(self):
        self.should_be_contact_url()
        self.should_be_contact_form()

    def should_be_contact_url(self):
        assert "contacts" in self.browser.current_url, 'In URL ABSENT contacts word'

    def should_be_contact_form(self):
        assert self.is_element_present(*SbisContactPageLocators.CONTACT_FORM), "contact form is not presented"

    def click_tensor_img(self):
        tensor_img = self.get_element(*SbisContactPageLocators.TENSOR_IMG)
        tensor_img.click()
