from pages.sbis_all_pages.sbis_download_page import SbisDownloadPage
from pages.links import SbisUrls
from logger.logger import logging


class TestContactFromDownloadPage:
    def test_guest_should_see_contact_page(self, browser):
        logging.info("Starting test_guest_should_see_contact_page")
        page = SbisDownloadPage(browser, SbisUrls.SBIS_DOWNLOAD_PAGE_LINK)
        page.open()
        page.should_be_download_page()
        page.click_tab_plugin_for_download_app_for_windows()
        page.open_windows_window()
        page.download_web_installer_for_windows()
        logging.info("Test test_guest_should_see_contact_page passed successfully")
