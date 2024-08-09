from main_page import Page # type: ignore
from locators import MainPanelLocators, SystemObjectsLocators # type: ignore
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException


def presence_and_spelling(self, locator, button_name):
    assert self.is_element_present(*locator), \
        f'Button "{button_name}" is not presented'
    button_text = self.browser.find_element(*locator).text
    assert button_text == button_name, \
        f'Button "{button_name}" has a spelling error, button text: {button_text}'

class MainPanel(Page):  # Класс для тестирования по тест-кейсу "Главная панель" (DRBN-T52)
# Общие функции
    # Проверка на наличие элемента и орфографические ошибки
    def check_presence_and_spelling(self, locator, button_name):
        print(f'Checking the button "{button_name}"...')
        try:
            presence_and_spelling(self, locator, button_name)
        except StaleElementReferenceException:  # Firefox выдает ошибку из-за обновления элементов
            presence_and_spelling(self, locator, button_name)

    def refresh_page(self):
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого

    def open_terminal(self):
        sleep(0.3)  # f
        self.browser.find_element(*MainPanelLocators.TERMINAL_BUTTON).click()
        assert self.is_element_present(*MainPanelLocators.TERMINAL_FORM), \
            'Terminal does not open'

    def open_ppk_objects(self):
        self.browser.find_element(*SystemObjectsLocators.PPK_R_ARROW).click()

    def open_module_objects(self, module_num):
        self.browser.find_element(SystemObjectsLocators.MODULE_ARROW[0],
        f'{SystemObjectsLocators.MODULE_ARROW[1]}{module_num}_').click()

    def close_expanded_tabs(self):  # Закрыть все вкладки
        self.browser.find_element(*MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON).click()

# Проверка title
    def check_tab_name_on_title(self):  # Название вкладки
        print('Checking the title...')
        title = self.browser.title
        assert title.split()[0] == 'Веб-конфигуратор', \
            f'The tab name in the title does not match, should be "Веб-конфигуратор"'

    def check_version_on_title(self, version):  # Номер версии конфигуратора в title
        title = self.browser.title
        assert title.split()[1] == version, \
            f'The configurator version in the title does not match, should be "{version}"'

# Проверка логотипа "Рубикон"
    def should_be_logo(self):
        print('Checking the logo...')
        assert self.is_element_present(*MainPanelLocators.LOGO), 'Logo is not presented'
        assert self.is_element_visible(*MainPanelLocators.LOGO), \
            'Logo is not displayed'
    
    def does_page_refresh_when_click_logo(self):  # Обновляется ли страница при клике на лого?
        self.close_expanded_tabs()  # Закрыть все влкадки
        self.browser.find_element(*SystemObjectsLocators.SYSTEM_ARROW).click()  # Скрываем объекты системы
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого
        assert self.browser.find_element(*SystemObjectsLocators.PPK_R_FORM_NUMB_1).is_displayed(), \
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
        print('Checking the button "В Файл для Интеллекта"...')
        assert self.is_element_present(*MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON), \
            'Button "В Файл для Интеллекта" is not presented'

    def should_be_from_file_button(self):
        self.check_presence_and_spelling(MainPanelLocators.FROM_FILE_BUTTON, 'ИЗ ФАЙЛА')
    
    def should_be_log_button(self):
        self.check_presence_and_spelling(MainPanelLocators.LOG_BUTTON, 'ЖУРНАЛ')
        
    def should_be_terminal_button(self):
        self.check_presence_and_spelling(MainPanelLocators.TERMINAL_BUTTON, 'ТЕРМИНАЛ')

    def should_be_light_mode_icon(self):
        print('Checking the light mode icon...')
        assert self.is_element_present(*MainPanelLocators.LIGHT_MODE_ICON), \
            'Icon "Light Mode" is not presented'

# Проверка статуса подключения
    def should_be_online_mark(self):
        print('Checking online status...')
        assert self.is_element_present(*MainPanelLocators.ONLINE_MARK), \
            'Online mark is not presented'
    
    def status_should_be_online(self):
        status = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).text
        assert status == 'online', f'Connection status not "online", status: {status}'

    def online_mark_color_should_be_green(self):
        color = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).value_of_css_property('color')
        assert '0, 230, 118' in color, \
            f'Connection status color is not green: "rgb(0, 230, 118)", color: {color}'
    
    def should_be_offline_mark(self):
        print('Checking offline status...')
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
        print('Checking recording setting for ppk...')
        self.browser.find_element(*SystemObjectsLocators.PPK_R_FORM_NUMB_1).click()  # ППК стал активным
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК

    def recording_setting_for_module(self, module_num):  # Модуль Области стал активным
        print(f'Checking recording setting for module {module_num}...')
        self.browser.find_element(SystemObjectsLocators.MODULE_FORM[0],
            f'{SystemObjectsLocators.MODULE_FORM[1]}{module_num}_').click()
        assert self.is_element_clickable(*MainPanelLocators.TO_PPK_BUTTON), \
            'The button "В ППК" is not clickable'
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК
        assert self.is_element_present(*MainPanelLocators.TO_PPK_BUTTON_IS_BLINKING), \
            'The button "В ППК" does not blink'

    def check_record(self, module=''):
        print(f'Checking start and finish of recording for {'ppk' if module == '' else module[1:]}...')
        assert self.is_element_present(SystemObjectsLocators.RECORD_START[0], 
            f'{SystemObjectsLocators.RECORD_START[1]}{module}")]'), \
                f'Recording for {'ppk' if module == '' else module[1:]} has not started'
        flag = self.is_element_visible(*SystemObjectsLocators.RECORD_FINISH, 180)  # Ожидание 3 мин
        assert flag, f'Recording for {'ppk' if module == '' else module[1:]} has not finished'

# Проверка кнопки ИЗ ППК
    def unload_settings(self):
        print(f'Checking unloading settings from ppk...')
        sleep(1)
        self.browser.find_element(*MainPanelLocators.FROM_PPK_BUTTON).click()
        assert self.is_element_present(*MainPanelLocators.FROM_PPK_BUTTON_IS_BLINKING), \
            'The button "ИЗ ППК" does not blink'

    def check_unload(self):
        print(f'Checking start and finish of unloading for ppk and moduls...')
        assert self.is_element_present(*SystemObjectsLocators.UNLOAD_START), \
            f'Unload for all ppkr has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_1, 30), \
            f'Unload for module 1 has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH_MODULE_1, 30), \
            f'Unload for module 1 has not finished or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_2, 30), \
            f'Unload for module 2 has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH_MODULE_2, 30), \
            f'Unload for module 2 has not finished or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_3, 30), \
            f'Unload for module 3 has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH_MODULE_3, 30), \
            f'Unload for module 3 has not finished or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH, 30), \
            f'Unload for all ppkr has not finished or there is a spelling error'

# Проверка полной записи в ППК
    def add_10_areas(self):
        print('Creating 10 areas...')
        for _ in range(10):  # Создать 10 Зон пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ADD_ICON).click()

    def add_12_inputlink(self):
        print('Creating 12 inputlinks...')
        for i in range(12):  # Создать 12 ТС входов
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Список входов
        for i in range(12):  # Сделать по 2 ТС входа каждого типа
            self.browser.find_element(SystemObjectsLocators.INPUTLINK_ITEMS[0], 
                f'{SystemObjectsLocators.INPUTLINK_ITEMS[1]}{i + 1}_').click()  # Список входов
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(SystemObjectsLocators.TYPES[0], 
                f'{SystemObjectsLocators.TYPES[1]}{i % 6 + 1})').click()  # Изменить тип входа
            sleep(0.1)  # f

    def add_9_ouputlink(self):
        print('Creating 9 outputlinks...')
        for i in range(9):  # Создать 9 ТС выходов
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Список выходов
        for i in range(9):  # Сделать по 3 ТС выхода каждого типа
            self.browser.find_element(SystemObjectsLocators.OUTPUTLINK_ITEMS[0], 
                f'{SystemObjectsLocators.OUTPUTLINK_ITEMS[1]}{i + 1}_').click()  # Открыть настройки
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(SystemObjectsLocators.TYPES[0], 
                f'{SystemObjectsLocators.TYPES[1]}{i % 3 + 1})').click()  # Изменить тип выхода
            sleep(0.1)  # f
    
    def add_8_BIS_M(self):
        print('Creating 8 BIS M...')
        for i in range(8):  # Создать 8 БИС-М
            self.browser.find_element(*SystemObjectsLocators.RS_485_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Список БИС-М
        for i in range(8):  # Сделать по 2 БИС-М каждого типа
            self.browser.find_element(SystemObjectsLocators.RS_485_ITEMS[0], 
                f'{SystemObjectsLocators.RS_485_ITEMS[1]}{i + 1}_').click()  # Открыть настройки
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(SystemObjectsLocators.TYPES[0], 
                f'{SystemObjectsLocators.TYPES[1]}{i % 4 + 1})').click()  # Изменить тип БИС-М
            sleep(0.1)  # f
    
    def open_ADDRESSABLE_LOOP(self, AL):
        assert self.is_element_clickable(SystemObjectsLocators.ADDRESSABLE_LOOP[0], 
            f'{SystemObjectsLocators.ADDRESSABLE_LOOP[1]}{AL}_'), \
            'Addressable loop arrow is not clickable'
        self.browser.find_element(SystemObjectsLocators.ADDRESSABLE_LOOP[0], 
            f'{SystemObjectsLocators.ADDRESSABLE_LOOP[1]}{AL}_').click()  # Открыть шлейф

    def add_26_addressable_devices(self, AL):
        print(f'Creating 26 addressable devices on addressable loop {AL}...')
        for i in range(26):  # Создать 26 АУ
            self.browser.find_element(SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON[0], 
                f'{SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON[1]}{AL}_AU').click()
        self.browser.find_element(SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW[0], 
            f'{SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW[1]}{AL}_AU').click()  # Список АУ
        for i in range(26):  # Сделать по 2 АУ каждого типа
            self.browser.find_element(SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS[0], 
                f'{SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS[1]}{AL}_AU_{i + 1}_').click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(SystemObjectsLocators.TYPES[0], 
                f'{SystemObjectsLocators.TYPES[1]}{i % 13 + 1})').click()
            sleep(0.15)  # f
    
    def check_number_of_objects(self):
        print(f'Creating number of created objects...')
        assert '10' == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_AREAS).text, \
            'The number of areas is not equal 10'
        assert '12' == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_INPUTLINK).text, \
            'The number of inputlinks is not equal 12'
        assert '9' == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_OUTPUTLINK).text, \
            'The number of outputlinks is not equal 9'
        assert '8' == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_RS_485).text, \
            'The number of BIS-M is not equal 8'
        assert '26' == self.browser.find_element(SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON[0],
            f'{SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON[1]}1_AU > span').text, \
            'The number of addressable_devices on the first loop is not equal 26'
        assert '26' == self.browser.find_element(SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON[0],
            f'{SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON[1]}2_AU > span').text, \
            'The number of addressable_devices on the second loop  is not equal 26'
    
    def clear_module_1(self):  # Полное независимое удаление всех объектов модуля Области
        print(f'Clearing module 1...')
        if self.is_element_present(*SystemObjectsLocators.DELETE_AREAS):
            self.browser.find_element(*SystemObjectsLocators.DELETE_AREAS).click()
        if self.is_element_present(*SystemObjectsLocators.DELETE_INPUTLINKS):
            self.browser.find_element(*SystemObjectsLocators.DELETE_INPUTLINKS).click()
        if self.is_element_present(*SystemObjectsLocators.DELETE_OUTPUTLINKS):
            self.browser.find_element(*SystemObjectsLocators.DELETE_OUTPUTLINKS).click()
    
    def clear_module_2(self):  # Полное независимое удаление всех объектов модуля Выходы
        print(f'Clearing module 2...')
        if self.is_element_present(*SystemObjectsLocators.DELETE_RS_485):
            self.browser.find_element(*SystemObjectsLocators.DELETE_RS_485).click()
    
    def clear_module_3(self):  # Полное независимое удаление всех объектов модуля Адресные шлейфы
        print(f'Clearing module 3...')
        if self.is_element_present(SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[0], 
                                   f'{SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[1]}{1}_AU'):
            self.browser.find_element(SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[0], 
                f'{SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[1]}{1}_AU').click()
        if self.is_element_present(SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[0], 
                                   f'{SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[1]}{2}_AU'):
            self.browser.find_element(SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[0], 
                f'{SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES[1]}{2}_AU').click()
