from pages.tensor_all_pages.tensor_base_page import TensorBasePage
from pages.locators import TensorAboutPageLocators, TensorBasePageLocators


class TensorAboutPage(TensorBasePage):
    def should_be_about_page(self):
        self.should_be_about_url()
        self.should_be_main_tensor_link()

    def should_be_about_url(self):
        assert "about" in self.browser.current_url, 'In URL ABSENT about word'

    def should_be_about_banner(self):
        assert self.is_element_present(*TensorAboutPageLocators.ABOUT_COMPANY_BANNER, timeout=10)

    def should_be_all_img_same_size(self):
        all_img = self.get_elements(*TensorAboutPageLocators.WORK_BLOCK_IMG, timeout=15)
        width = None
        height = None
        for element in all_img:
            width_value = element.get_attribute("width")
            height_value = element.get_attribute("height")
            if width is None and height is None:
                width = width_value
                height = height_value
            assert width == width_value and height == height_value, "В разделе \"Работаем\" картинки разных размеров"

