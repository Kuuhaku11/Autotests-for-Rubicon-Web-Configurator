from main_page import Page
from locators import MainPanelLocators
import time


# Класс для тестирования по тест-кейсу "Главная панель"
class MainPanel(Page):
    def check_tab_name_on_title(self):  # Название вкладки
        title = self.browser.title
        assert title.split()[0] == 'Веб-конфигуратор', \
            f'The tab name in the title does not match, should be "Веб-конфигуратор"'

    def check_version_on_title(self, version):  # Номер версии конфигуратора в title
        title = self.browser.title
        assert title.split()[1] == version, \
            f'The configurator version in the title does not match, should be "{version}"'

    def should_be_logo(self):  # Проверка логотипа "Рубикон"
        assert self.is_element_present(*MainPanelLocators.LOGO), 'logo is not presented'
    
    def does_page_refresh_when_click_logo(self):  # Обновляется ли страница при клике на лого?
        self.browser.find_element(*MainPanelLocators.SYSTEM_ARROW).click()  # Скрываем объекты системы
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого
        assert self.browser.find_element(*MainPanelLocators.PPK_R_FORM).is_displayed(), \
            'the page has not been refresh, system elements are visible'