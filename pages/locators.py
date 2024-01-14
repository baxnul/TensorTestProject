from selenium.webdriver.common.by import By

""" ALL LOCATOR have selector and locator
    Example: (Tuple have: By selector, locator)
    and some LOCATOR have timeout wait
    Example: (Tuple have: By selector, locator, timeout wait) """


class SbisBasePageLocators:
    CONTACT_LINK = (By.XPATH, "//a[@href='/contacts']")
    FOOTER_TRANSIT_DOWNLOAD_SBIS = (By.CSS_SELECTOR, "[href='/download?tab=ereport&innerTab=ereport25']")


class SbisMainPageLocators:
    pass


class SbisContactPageLocators:
    CONTACT_FORM = (By.ID, "contacts_list")
    TENSOR_IMG = (By.CSS_SELECTOR, "[alt='Разработчик системы СБИС — компания «Тензор»']")
    FORM_LIST_PARTNER = (By.NAME, "viewContainer")
    BEFORE_EDIT_REGION = (By.ID, "city-id-2")
    CURRENT_SELECTED_REGION = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")
    TOTAL_EDIT_REGION = (By.CSS_SELECTOR, "[title='Камчатский край']")
    CURRENT_REGION_PARTNER = (By.ID, 'city-id-2')


class SbisDownloadPageLocators:
    DOWNLOAD_FORM = (By.CLASS_NAME, "sbis_ru-VerticalTabs__right")
    TAB_BUTTONS = (By.CLASS_NAME, "controls-tabButton__overlay")
    WINDOWS_WINDOW = (By.XPATH, "//span[contains(text(), 'Windows')]")
    WINDOWS_FILE_DOWNLOAD = (By.CSS_SELECTOR, "[href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")


class TensorBasePageLocators:
    TENSOR_IMG = (By.CSS_SELECTOR,
                  ".tensor_ru-Header__logo-img.tensor_ru-Header--anim.tensor_ru-Header__logo-img--show-hide-md.tensor_ru-Header__logo-img--hide-scrolled")


class TensorMainPageLocators:
    POWER_IN_PEOPLE = (By.XPATH, "//*[contains(text(), 'Сила в людях')]")
    LINK_ABOUT = (By.XPATH, '//a[@href="/about"]')


class TensorAboutPageLocators:
    ABOUT_COMPANY_BANNER = (By.CLASS_NAME, "tensor_ru-About__Banner-title")
    WORK_BLOCK_IMG = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper>img")
