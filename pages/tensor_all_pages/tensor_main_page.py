from pages.tensor_all_pages.tensor_base_page import BasePage
from pages.locators import TensorMainPageLocators, TensorBasePageLocators


class TensorMainPage(BasePage):
    def should_be_tensor_page(self):
        self.should_be_tensor_url()
        self.should_be_contact_form()
        self.should_be_module_power_in_people()

    def should_be_tensor_url(self):
        assert "tensor" in self.browser.current_url, 'In URL ABSENT tensor word'

    def should_be_contact_form(self):
        assert self.is_element_present(*TensorBasePageLocators.TENSOR_IMG), "Tensor IMG is not presented"

    def should_be_module_power_in_people(self):
        assert self.is_element_present(*TensorMainPageLocators.POWER_IN_PEOPLE), "Not module have descriptons Сила в Людях"

    def go_to_about_page(self):
        """Нажать кнопку подробнее во вкладке Сила в людях"""
        contact_link = self.get_element(*TensorMainPageLocators.LINK_ABOUT, timeout=15)
        contact_link.click()
