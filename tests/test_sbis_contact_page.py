from pages.sbis_all_pages.sbis_contact_page import SbisContactPage
from pages.tensor_all_pages.tensor_main_page import TensorMainPage
from pages.links import SbisUrls


class TestContactFromMainPage:
    def test_guest_should_see_contact_page(self, browser):
        page = SbisContactPage(browser, SbisUrls.SBIS_CONTACT_PAGE_LINK)
        page.open()
        page.should_be_contact_page()
        page.should_be_defined_user_location()
        page.should_be_list_partner()

    def test_guest_should_see_link_tensor_page(self, browser):
        page = SbisContactPage(browser, SbisUrls.SBIS_CONTACT_PAGE_LINK)
        page.open()
        page.click_tensor_img()
        tensor_page = TensorMainPage(browser, browser.current_url)
        tensor_page.switch_to_last_window()  # Переключиться на последнюю вкладку браузера
        tensor_page.should_be_tensor_page()

    def test_guest_can_edit_current_region(self, browser):
        page = SbisContactPage(browser, SbisUrls.SBIS_CONTACT_PAGE_LINK)
        page.open()
        page.edit_current_selected_region()
        page.select_new_region()
        page.should_be_selected_new_region()
        page.list_of_partners_should_be_equal_kamchatskij()
        page.current_url_have_text_kamchatskij()
        page.title_have_text_kamchatskij()
