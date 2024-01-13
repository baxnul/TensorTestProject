from selenium.webdriver.common.by import By

""" ALL LOCATOR have selector and locator
    Example: (Tuple have: By selector, locator)
    and some LOCATOR have timeout wait
    Example: (Tuple have: By selector, locator, timeout wait) """


class SbisBasePageLocators:
    CONTACT_LINK = (By.XPATH, "//a[@href='/contacts']")


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


class TensorBasePageLocators:
    TENSOR_IMG = (By.CSS_SELECTOR,
                  ".tensor_ru-Header__logo-img.tensor_ru-Header--anim.tensor_ru-Header__logo-img--show-hide-md.tensor_ru-Header__logo-img--hide-scrolled")


class TensorMainPageLocators:
    POWER_IN_PEOPLE = (By.XPATH, "//*[contains(text(), 'Сила в людях')]")
    LINK_ABOUT = (By.XPATH, '//a[@href="/about"]')


class TensorAboutPageLocators:
    ABOUT_COMPANY_BANNER = (By.CLASS_NAME, "tensor_ru-About__Banner-title")
    WORK_BLOCK_IMG = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper>img")
