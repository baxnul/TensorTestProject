from pages.tensor_all_pages.tensor_about_page import TensorAboutPage
from pages.tensor_all_pages.tensor_main_page import TensorMainPage
from pages.links import TensorUrls
from logger.setting_logger import logging


class TestContactFromMainPage:
    def test_guest_should_see_main_page_link(self, browser):
        """Проверка наличия баннера Тензор"""
        logging.info("Starting test_guest_should_see_main_page_link")
        page = TensorMainPage(browser, TensorUrls.TENSOR_MAIN_PAGE_LINK)
        page.open()
        page.should_be_main_tensor_link()
        logging.info("Test test_guest_should_see_main_page_link passed successfully")

    def test_guest_can_go_to_contact_page(self, browser):
        logging.info("Starting test_guest_can_go_to_contact_page")
        page = TensorMainPage(browser, TensorUrls.TENSOR_MAIN_PAGE_LINK)
        page.open()
        page.should_be_tensor_page()
        page.go_to_about_page()
        about_page = TensorAboutPage(browser, browser.current_url)
        about_page.should_be_about_page()
        logging.info("Test test_guest_can_go_to_contact_page passed successfully")

