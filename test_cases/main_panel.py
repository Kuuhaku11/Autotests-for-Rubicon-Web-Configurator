from main_page import Page # type: ignore
from locators import MainPanelLocators, SystemObjectsLocators # type: ignore
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Класс для тестирования по тест-кейсу "Главная панель"
class MainPanel(Page):
# Общие функции
    def check_presence_and_spelling(self, locator, button_name):
        assert self.is_element_present(*locator), \
            f'Button "{button_name}" is not presented'
        button_text = self.browser.find_element(*locator).text
        assert button_text == button_name, \
            f'Button "{button_name}" has a spelling error, button text: {button_text}'

    def refresh_page(self):
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого

    def open_terminal(self):
        self.browser.find_element(*MainPanelLocators.TERMINAL_BUTTON).click()
        assert self.is_element_present(*MainPanelLocators.TERMINAL_FORM), \
            'Terminal does not open'

    def open_ppk_objects(self):
        self.browser.find_element(*SystemObjectsLocators.PPK_R_ARROW).click()

    def open_module_objects(self, module_num):
        self.browser.find_element(*SystemObjectsLocators.MODULE_ARROW[module_num + 1]).click()

    def close_expanded_tabs(self):  # Закрыть все вкладки
        self.browser.find_element(*MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON).click()

# Проверка title
    def check_tab_name_on_title(self):  # Название вкладки
        title = self.browser.title
        assert title.split()[0] == 'Веб-конфигуратор', \
            f'The tab name in the title does not match, should be "Веб-конфигуратор"'

    def check_version_on_title(self, version):  # Номер версии конфигуратора в title
        title = self.browser.title
        assert title.split()[1] == version, \
            f'The configurator version in the title does not match, should be "{version}"'

# Проверка логотипа "Рубикон"
    def should_be_logo(self):
        assert self.is_element_present(*MainPanelLocators.LOGO), 'Logo is not presented'
        assert self.browser.find_element(*MainPanelLocators.LOGO).is_displayed(), \
            'Logo is not displayed'
    
    def does_page_refresh_when_click_logo(self):  # Обновляется ли страница при клике на лого?
        self.close_expanded_tabs()  # Закрыть все влкадки
        self.browser.find_element(*SystemObjectsLocators.SYSTEM_ARROW).click()  # Скрываем объекты системы
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого
        assert self.browser.find_element(*SystemObjectsLocators.PPK_R_FORM_1).is_displayed(), \
            'The page has not been refresh, system elements are visible'

# Проверка панели настроек
    def should_be_to_ppk_button(self):
        self.check_presence_and_spelling(MainPanelLocators.TO_PPK_BUTTON, 'В ППК')

    def should_be_from_ppk_button(self):
        self.check_presence_and_spelling(MainPanelLocators.FROM_PPK_BUTTON, 'ИЗ ППК')
    
    def should_be_save_button(self):
        self.check_presence_and_spelling(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')

    def should_be_restore_button(self):
        self.check_presence_and_spelling(MainPanelLocators.RESTORE_BUTTON, 'ВОССТАНОВИТЬ')

    def should_be_to_file_button(self):
        self.check_presence_and_spelling(MainPanelLocators.TO_FILE_BUTTON, 'В ФАЙЛ')

    def should_be_to_file_for_intellect_button(self):
        assert self.is_element_present(*MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON), \
            'Button "В Файл для Интеллекта" is not presented'

    def should_be_from_file_button(self):
        self.check_presence_and_spelling(MainPanelLocators.FROM_FILE_BUTTON, 'ИЗ ФАЙЛА')
    
    def should_be_log_button(self):
        self.check_presence_and_spelling(MainPanelLocators.LOG_BUTTON, 'ЖУРНАЛ')
        
    def should_be_terminal_button(self):
        self.check_presence_and_spelling(MainPanelLocators.TERMINAL_BUTTON, 'ТЕРМИНАЛ')

    def should_be_light_mode_icon(self):
        assert self.is_element_present(*MainPanelLocators.LIGHT_MODE_ICON), \
            'Icon "Light Mode" is not presented'

# Проверка статуса подключения
    def should_be_online_mark(self):
        assert self.is_element_present(*MainPanelLocators.ONLINE_MARK), \
            'Online mark is not presented'
    
    def status_should_be_online(self):
        status = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).text
        assert status == 'online', f'Connection status not "online", status: {status}'

    def online_mark_color_should_be_green(self):
        color = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).value_of_css_property('color')
        assert color == 'rgba(0, 230, 118, 1)', \
            f'Connection status color is not green: "rgba(0, 230, 118, 1)", color: {color}'
    
    def should_be_offline_mark(self):
        sleep(2)  # Ожидание пока может подгрузиться online статус
        assert self.is_element_present(*MainPanelLocators.OFFLINE_MARK), \
            'Offline mark is not presented'
    
    def status_should_be_offline(self):
        status = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).text
        assert status == 'offline', f'Connection status not "offline", status: {status}'

    def online_mark_color_should_be_yellow(self):
        color = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).value_of_css_property('color')
        assert color == 'rgba(255, 215, 64, 1)', \
            f'Connection status color is not yellow: "rgba(255, 215, 64, 1)", color: {color}'

# Проверка кнопки В ППК с открытым Терминалом
    def recording_setting_for_ppk(self):
        self.browser.find_element(*SystemObjectsLocators.PPK_R_FORM_1).click()  # ППК стал активным
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК

    def recording_setting_for_module(self, module_num):
        # Модуль Области стал активным
        self.browser.find_element(*SystemObjectsLocators.MODULE_FORM[module_num - 1]).click()
        assert self.is_element_clickable(*MainPanelLocators.TO_PPK_BUTTON), \
            'The button "В ППК" is not clickable'
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК

    def check_record(self, module_num=0):
        assert self.is_element_present(*SystemObjectsLocators.RECORD_START[module_num]), \
            f'Recording for {'ppk' if module_num == 0 else f'module{module_num}'} has not started'
        assert self.is_element_present(*SystemObjectsLocators.RECORD_END), \
            f'Recording for {'ppk' if module_num == 0 else f'module{module_num}'} has not ended'

# Проверка кнопки ИЗ ППК с открытым Терминалом


# Проверка полной записи в ППК
