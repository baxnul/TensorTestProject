from pages.tensor_all_pages.tensor_about_page import TensorAboutPage
from pages.links import TensorUrls

from logger.setting_logger import logging


class TestImgFromAboutPage:
    def test_guest_should_see_about_page_link(self, browser):
        """Проверка наличия баннера Тензор"""
        logging.info("Starting test_guest_should_see_about_page_link")
        page = TensorAboutPage(browser, TensorUrls.TENSOR_ABOUT_PAGE_LINK)
        page.open()
        page.should_be_about_page()
        logging.info("Test test_guest_should_see_about_page_link passed successfully")

    def test_guest_can_go_to_contact_page(self, browser):
        logging.info("Starting test_guest_can_go_to_contact_page")
        page = TensorAboutPage(browser, TensorUrls.TENSOR_ABOUT_PAGE_LINK)
        page.open()
        page.should_be_all_img_same_size()
        logging.info("Test test_guest_can_go_to_contact_page passed successfully")

