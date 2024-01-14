from .sbis_base_page import SbisBasePage
from pages.locators import SbisContactPageLocators


class SbisContactPage(SbisBasePage):
    def should_be_contact_page(self):
        self.should_be_contact_url()
        self.should_be_contact_form()

    def should_be_contact_url(self):
        assert "contacts" in self.browser.current_url, 'In URL ABSENT contacts word'

    def should_be_contact_form(self):
        assert self.is_element_present(*SbisContactPageLocators.CONTACT_FORM), "contact form is not presented"

    def click_tensor_img(self):
        tensor_img = self.get_element(*SbisContactPageLocators.TENSOR_IMG)
        tensor_img.click()

    def should_be_defined_user_location(self):
        assert self.is_element_present(*SbisContactPageLocators.BEFORE_EDIT_REGION), "User location undefined"

    def should_be_list_partner(self):
        assert self.is_element_present(*SbisContactPageLocators.FORM_LIST_PARTNER), "partner list undefined"

    def edit_current_selected_region(self):
        """Нажать на текст с надписью региона который определился"""
        click_region = self.element_to_be_clickable(*SbisContactPageLocators.CURRENT_SELECTED_REGION)
        click_region.click()

    def select_new_region(self):
        """Редактировать регион"""
        find_new_region = self.element_to_be_clickable(*SbisContactPageLocators.TOTAL_EDIT_REGION,
                                                       timeout=15)
        find_new_region.click()

    def should_be_selected_new_region(self):
        assert self.wait_for_text_in_element(*SbisContactPageLocators.CURRENT_SELECTED_REGION,
                                             text_='Камчатский край'), "Kamchatsky region is not selected"

    def url_edited_for_new_region(self):
        """В URL должно поменяться регион на выбранный"""
        contact_url_after = self.browser.current_url  # URL после смены региона

    def current_url_have_text_kamchatskij(self):
        """Сравниваем есть ли в текущем url текст 41-kamchatskij-kraj,
            который мы выбрали для проверки возможности смены локации"""
        current_url = self.browser.current_url
        assert "41-kamchatskij-kraj" in current_url, "text '41-kamchatskij-kraj' not in current url"

    def title_have_text_kamchatskij(self):
        assert "Камчатский край" in self.browser.title, "Title on page not change on 'Камчатский край'"

    def list_of_partners_shoul_be_equal_kamchatskij(self):
        assert self.wait_for_text_in_element(*SbisContactPageLocators.CURRENT_REGION_PARTNER,
                                             text_='Петропавловск-Камчатский'), "Kamchatsky region is not view in list partners"
