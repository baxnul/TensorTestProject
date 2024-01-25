from pages.sbis_all_pages.sbis_contact_page import SbisContactPage
from pages.sbis_all_pages.sbis_download_page import SbisDownloadPage
from pages.sbis_all_pages.sbis_main_page import SbisMainPage
from pages.links import SbisUrls


class TestContactFromMainPage:
    def test_guest_should_see_contact_link(self, browser):
        """Проверка наличия кнопки контакты"""
        page = SbisMainPage(browser, SbisUrls.SBIS_MAIN_PAGE_LINK)
        page.open()
        page.should_be_contact_link()

    def test_guest_can_go_to_contact_page(self, browser):
        page = SbisMainPage(browser, SbisUrls.SBIS_MAIN_PAGE_LINK)
        page.open()
        page.go_to_contact_page()
        contact_page = SbisContactPage(browser, browser.current_url)
        contact_page.should_be_contact_page()

    def test_guest_can_go_to_download_page(self, browser):
        page = SbisMainPage(browser, SbisUrls.SBIS_MAIN_PAGE_LINK)
        page.open()
        page.go_to_download_page()
        download_page = SbisDownloadPage(browser, browser.current_url)
        download_page.should_be_download_page()
