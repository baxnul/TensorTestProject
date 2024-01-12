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
    TENSOR_IMG = (By.XPATH, '//*[@alt="Разработчик системы СБИС — компания «Тензор»"]')


class TensorBasePageLocators:
    TENSOR_IMG = (By.CSS_SELECTOR,
                  ".tensor_ru-Header__logo-img.tensor_ru-Header--anim.tensor_ru-Header__logo-img--show-hide-md.tensor_ru-Header__logo-img--hide-scrolled")


class TensorMainPageLocators:
    POWER_IN_PEOPLE = (By.XPATH, "//*[contains(text(), 'Сила в людях')]")
    LINK_ABOUT = (By.XPATH, '//a[@href="/about"]')


class TensorAboutPageLocators:
    ABOUT_COMPANY_BANNER = (By.CLASS_NAME, "tensor_ru-About__Banner-title")
