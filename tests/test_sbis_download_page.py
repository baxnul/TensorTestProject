from loguru import logger

from pages.sbis_all_pages.sbis_download_page import SbisDownloadPage
from pages.links import SbisUrls


class TestContactFromDownloadPage:
    @logger.catch()
    def test_guest_should_see_contact_page(self, browser):
        page = SbisDownloadPage(browser, SbisUrls.SBIS_DOWNLOAD_PAGE_LINK)
        page.open()
        page.should_be_download_page()
        page.click_tab_plugin_for_download_app_for_windows()
        page.open_windows_window()
        page.download_web_installer_for_windows()
