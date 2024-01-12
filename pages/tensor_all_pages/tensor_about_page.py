from pages.tensor_all_pages.tensor_base_page import BasePage
from pages.locators import TensorAboutPageLocators, TensorBasePageLocators


class TensorAboutPage(BasePage):
    def should_be_about_page(self):
        self.should_be_about_url()
        self.should_be_main_tensor_link()

    def should_be_about_url(self):
        assert "tensor" in self.browser.current_url, 'In URL ABSENT tensor word'

    def should_be_main_tensor_link(self):
        assert self.is_element_present(*TensorAboutPageLocators.ABOUT_COMPANY_BANNER, timeout=10)
