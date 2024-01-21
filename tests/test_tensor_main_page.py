from loguru import logger

from pages.tensor_all_pages.tensor_about_page import TensorAboutPage
from pages.tensor_all_pages.tensor_main_page import TensorMainPage
from pages.links import TensorUrls


class TestContactFromMainPage:
    @logger.catch()
    def test_guest_should_see_main_page_link(self, browser):
        """Проверка наличия баннера Тензор"""
        page = TensorMainPage(browser, TensorUrls.TENSOR_MAIN_PAGE_LINK)
        page.open()
        page.should_be_main_tensor_link()

    @logger.catch()
    def test_guest_can_go_to_contact_page(self, browser):
        page = TensorMainPage(browser, TensorUrls.TENSOR_MAIN_PAGE_LINK)
        page.open()
        page.should_be_tensor_page()
        page.go_to_about_page()
        about_page = TensorAboutPage(browser, browser.current_url)
        about_page.should_be_about_page()
