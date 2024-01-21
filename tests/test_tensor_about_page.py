from loguru import logger

from pages.tensor_all_pages.tensor_about_page import TensorAboutPage
from pages.links import TensorUrls


class TestImgFromAboutPage:
    @logger.catch()
    def test_guest_should_see_about_page_link(self, browser):
        """Проверка наличия баннера Тензор"""
        page = TensorAboutPage(browser, TensorUrls.TENSOR_ABOUT_PAGE_LINK)
        page.open()
        page.should_be_about_page()

    @logger.catch()
    def test_guest_can_go_to_contact_page(self, browser):
        page = TensorAboutPage(browser, TensorUrls.TENSOR_ABOUT_PAGE_LINK)
        page.open()
        page.should_be_all_img_same_size()
