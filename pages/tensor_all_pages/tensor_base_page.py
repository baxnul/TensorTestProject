from pages.base_page import BasePage
from pages.locators import TensorBasePageLocators


class TensorBasePage(BasePage):
    def go_to_main_page(self):
        contact_link = self.browser.find_element(*TensorBasePageLocators.TENSOR_IMG)
        contact_link.click()

    def should_be_main_tensor_link(self):
        assert self.is_element_present(*TensorBasePageLocators.TENSOR_IMG), "tensor img link is not presented"
