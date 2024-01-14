import os
import requests
import re
from .sbis_base_page import SbisBasePage
from pages.locators import SbisDownloadPageLocators


def convert_bytes_to_mb(bytes_size):
    mb_size = bytes_size / (1024.0 * 1024)
    return round(mb_size, 2)


class SbisDownloadPage(SbisBasePage):
    def should_be_download_page(self):
        self.should_be_download_url()
        self.should_be_download_form()

    def should_be_download_url(self):
        assert "download" in self.browser.current_url, 'In URL ABSENT download word'

    def should_be_download_form(self):
        assert self.is_element_present(*SbisDownloadPageLocators.DOWNLOAD_FORM), "download form is not presented"

    def click_tab_plugin_for_download_app_for_windows(self):
        """Выбираем в меню СБИС плагин"""
        tab_buttons = self.get_elements(*SbisDownloadPageLocators.TAB_BUTTONS)
        tab_plugin = tab_buttons[1]
        tab_plugin.click()

    def open_windows_window(self):
        """В меню СБИС плагин выбираем окно для Windows"""
        windows_window = self.get_element(*SbisDownloadPageLocators.WINDOWS_WINDOW)
        windows_window.click()

    def download_web_installer_for_windows(self):
        """Нажимаем скачать ВЕБ установщик для Windows
            и сравниваем размер файла указанный на сайте и размер скачанного файла"""
        download_file = self.get_element(*SbisDownloadPageLocators.WINDOWS_FILE_DOWNLOAD)
        # download_file.click()
        text_weight_file_url = download_file.text  # Получаем текст с размером файла написанный на сайте
        file_url = download_file.get_attribute("href")  # Получаем URL файла
        current_dir = os.path.abspath(os.path.dirname("__file__"))
        file_name = os.path.basename(file_url)  # Определяем имя файла по URL
        save_path = f'{current_dir}/{file_name}'  # Определяем путь для сохранения файла (в текущей директории)
        response = requests.get(file_url)  # Скачиваем файл
        assert response.status_code == 200, 'Не удалось скачать файл'

        # Сохраняем файл
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"Файл успешно сохранен в {save_path}")

        reg = r'\d+.\d+'
        match_text_fsize_url = (re.search(reg, text_weight_file_url)).group(0)  # Получаем Вес при помощи регулярки
        file_size_bytes = os.path.getsize(save_path)  # Получаем размер скаченного файла в байтах

        file_size_mb = convert_bytes_to_mb(file_size_bytes)
        assert float(match_text_fsize_url) == float(
            file_size_mb), "Размер файла указанный на Сайте и размер скаченного файла отличаются"
