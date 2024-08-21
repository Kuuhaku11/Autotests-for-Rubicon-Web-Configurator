from main_page import Page # type: ignore
from locators import (MainPanelLocators, SystemObjectsLocators, AreaSettingsLocators,  # type: ignore
                      InputLinkSettingsLocators, OutputLinkSettingsLocators, 
                      RS_485_SettingsLocators, AddressableLoopSettingsLocators)
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MainPanel(Page):  # Класс для тестирования по тест-кейсу "Главная панель" (DRBN-T52)

# Общие функции
    def check_presence_and_spelling(self, locator, button_name):
        assert self.is_element_present(*locator), \
            f'Button "{button_name}" is not presented'
        button_text = self.browser.find_element(*locator).text
        assert button_text == button_name, \
            f'Button "{button_name}" has a spelling error, button text: {button_text}'

    def presence_and_spelling(self, locator, button_name):  # Проверка на наличие элемента и ошибки
        print(f'Checking the button "{button_name}"...')
        try:
            self.check_presence_and_spelling(locator, button_name)
        except StaleElementReferenceException:  # Firefox выдает ошибку из-за обновления элементов
            self.check_presence_and_spelling(locator, button_name)

    def refresh_page(self):
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого

    def open_terminal(self):
        sleep(0.3)  # f
        self.browser.find_element(*MainPanelLocators.TERMINAL_BUTTON).click()
        assert self.is_element_present(*MainPanelLocators.TERMINAL_FORM), \
            'Terminal does not open'
    
    def close_terminal(self):
        sleep(1)
        self.browser.find_element(*MainPanelLocators.CLOSE_TERMINAL_ARROW).click()
        assert self.is_element_present(*MainPanelLocators.CLOSE_TERMINAL_ARROW), \
            'Terminal does not close'

    def open_ppk_objects(self):
        self.browser.find_element(*SystemObjectsLocators.PPK_R_ARROW).click()

    def open_module_objects(self, module_num):
        self.browser.find_element(*SystemObjectsLocators.MODULE_ARROW(module_num)).click()

    def close_expanded_tabs(self):  # Закрыть все вкладки
        self.browser.find_element(*MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON).click()

    def save_settings(self):
        self.browser.find_element(*MainPanelLocators.SAVE_BUTTON).click()
    
    def button_should_be_clickable(self, locator, button):
        assert self.is_element_clickable(*locator), f'Button "{button}" is not clickable'


# Проверка title
    def check_tab_name_on_title(self):  # Название вкладки
        print('Checking the title...')
        title = self.browser.title
        assert title.split()[0] == 'Веб-конфигуратор', \
            f'The tab name in the title does not match, expected "Веб-конфигуратор"'

    def check_version_on_title(self, version):  # Номер версии конфигуратора в title
        title = self.browser.title
        assert title.split()[1] == version, \
            f'The configurator version in the title does not match, expected "{version}"'


# Проверка логотипа "Рубикон"
    def should_be_logo(self):
        print('Checking the logo...')
        assert self.is_element_present(*MainPanelLocators.LOGO), 'Logo is not presented'
        assert self.is_element_visible(*MainPanelLocators.LOGO), 'Logo is not displayed'
    
    def page_should_refresh_when_click_logo(self):  # Обновляется ли страница при клике на лого?
        self.close_expanded_tabs()  # Закрыть все вкладки
        self.browser.find_element(*SystemObjectsLocators.SYSTEM_ARROW).click()  # Скрываем объекты
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого
        assert self.browser.find_element(*SystemObjectsLocators.PPK_R_FORM_NUMB_1).is_displayed(), \
            'Page has not been refresh, system elements are visible'


# Проверка панели настроек
    def should_be_to_ppk_button(self):
        self.presence_and_spelling(MainPanelLocators.TO_PPK_BUTTON, 'В ППК')

    def should_be_from_ppk_button(self):
        self.presence_and_spelling(MainPanelLocators.FROM_PPK_BUTTON, 'ИЗ ППК')
    
    def should_be_save_button(self):
        self.presence_and_spelling(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')

    def should_be_restore_button(self):
        self.presence_and_spelling(MainPanelLocators.RESTORE_BUTTON, 'ВОССТАНОВИТЬ')

    def should_be_to_file_button(self):
        self.presence_and_spelling(MainPanelLocators.TO_FILE_BUTTON, 'В ФАЙЛ')

    def should_be_to_file_for_intellect_button(self):
        print('Checking the button "В Файл для Интеллекта"...')
        assert self.is_element_present(*MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON), \
            'Button "В Файл для Интеллекта" is not presented'

    def should_be_from_file_button(self):
        self.presence_and_spelling(MainPanelLocators.FROM_FILE_BUTTON, 'ИЗ ФАЙЛА')
    
    def should_be_log_button(self):
        self.presence_and_spelling(MainPanelLocators.LOG_BUTTON, 'ЖУРНАЛ')
        
    def should_be_terminal_button(self):
        self.presence_and_spelling(MainPanelLocators.TERMINAL_BUTTON, 'ТЕРМИНАЛ')

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
        self.browser.find_element(*SystemObjectsLocators.MODULE_FORM(module_num)).click()
        assert self.is_element_clickable(*MainPanelLocators.TO_PPK_BUTTON), \
            'Button "В ППК" is not clickable'
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК
        assert self.is_element_present(*MainPanelLocators.TO_PPK_BUTTON_IS_BLINKING), \
            'Button "В ППК" does not blink'

    def check_record(self, module=''):
        print(f'Checking start and finish of recording for {'ppk' if module == '' else module[1:]}...')
        assert self.is_element_present(*SystemObjectsLocators.RECORD_START(module)), \
            f'Recording for {'ppk' if module == '' else module[1:]} has not started'
        flag = self.is_element_visible(*SystemObjectsLocators.RECORD_FINISH, 300)  # Ожидание 5 мин
        assert flag, f'Recording for {'ppk' if module == '' else module[1:]} has not finished'


# Проверка кнопки ИЗ ППК
    def unload_settings(self):
        print(f'Checking unloading settings from ppk...')
        sleep(1)
        self.browser.find_element(*MainPanelLocators.FROM_PPK_BUTTON).click()
        assert self.is_element_present(*MainPanelLocators.FROM_PPK_BUTTON_IS_BLINKING), \
            'Button "ИЗ ППК" does not blink'

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


# Полная запись в ППК
    def add_areas(self, areas):
        print(f'Creating {areas} areas...')
        for _ in range(areas):  # Создать Зоны пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ADD_ICON).click()

    def add_inputlink(self, inlinks):
        print(f'Creating {inlinks} inputlinks...')
        for i in range(inlinks):  # Создать ТС входы
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Список входов
        for i in range(inlinks):  # Сделать ТС входы каждого типа
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 6 + 1)).click()  # Изменить тип входа
            sleep(0.1)  # f

    def add_ouputlink(self, outlinks):
        print(f'Creating {outlinks} outputlinks...')
        for i in range(outlinks):  # Создать ТС выходы
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Список выходов
        for i in range(outlinks):  # Сделать ТС выходы каждого типа
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 3 + 1)).click()  # Изменить тип выхода
            sleep(0.1)  # f
        
    
    def add_BIS_M(self, BIS_Ms):
        print(f'Creating {BIS_Ms} BIS M...')
        for i in range(BIS_Ms):  # Создать БИС-Мы
            self.browser.find_element(*SystemObjectsLocators.RS_485_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Список БИС-М
        for i in range(BIS_Ms):  # Сделать БИС-Мы каждого типа
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 4 + 1)).click()  # Изменить тип выхода
            sleep(0.1)  # f
    
    def open_ADDRESSABLE_LOOP(self, AL):
        assert self.is_element_clickable(*SystemObjectsLocators.ADDRESSABLE_LOOP(AL)), \
            'Addressable loop arrow is not clickable'
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_LOOP(AL)).click()

    def add_addressable_devices(self, AL, addr_devs):
        print(f'Creating {addr_devs} addressable devices on addressable loop {AL}...')
        for i in range(addr_devs):  # Создать АУ
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL)).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
        for i in range(addr_devs):  # Сделать АУ каждого типа
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 13 + 1)).click()  # Изменить тип выхода
            sleep(0.15)  # f


# Проверка полной выгрузки из ППК
    def check_number_of_areas(self, areas):
        print(f'Checking number of areas...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_AREAS).text
        assert str(areas) == count, f'Number of areas is not equal {areas}, number = {count}'

    def check_number_of_inputlink(self, inlinks):
        print(f'Checking number of inlinks...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_INPUTLINK).text
        assert str(inlinks) == count, f'Number of inputlinks is not equal {inlinks}, number = {count}'

    def check_number_of_outputlink(self, outlinks):
        print(f'Checking number of outlinks...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_OUTPUTLINK).text
        assert str(outlinks) == count, f'Number of outputlinks is not equal {outlinks}, number = {count}'

    def check_number_of_BIS_M(self, BIS_Ms):
        print(f'Checking number of BIS_Ms...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_RS_485).text
        assert str(BIS_Ms) == count, f'Number of RS-485 devices is not equal {BIS_Ms}, number = {count}'

    def check_number_of_addressable_devices(self, AL, addr_devs):
        print(f'Checking number of addr_devs...')
        count = self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL)).text
        assert str(addr_devs) == count, \
            f'Number of addressable_devices on {AL} loop is not equal {addr_devs}, number = {count}'

    
# Проверка кнопки "Сохранить"
    def check_save_setting_disable(self, locator, object_name):  # Проверка, что чекбокс включен
        assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
            AreaSettingsLocators.CHECKBOX_CHECKED[1] + locator[1]), \
            f'Checkbox "отключен" in {object_name} was not saved'
    
    def check_save_settings(self):  # Проверить, что после обновления настройки сохраняются
        print('Checking save settings...')
        self.button_should_be_clickable(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')
        self.save_settings()
        self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Раскрыть Зоны
        assert self.is_element_present(*SystemObjectsLocators.SAVE_ICON), \
            'Settings not saved, there is no green dot near the area #1'  # Проверка появления зеленой точки   
        self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(1)).click()
        self.browser.find_element(*AreaSettingsLocators.DISABLE(1)).click()
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Раскрыть ТС входы
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(1)).click()
        self.browser.find_element(*InputLinkSettingsLocators.DISABLE(1)).click()
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Раскрыть ТС выходы
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(1)).click()
        self.browser.find_element(*OutputLinkSettingsLocators.DISABLE(1)).click()
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Раскрыть RS-485
        self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(1)).click()
        self.browser.find_element(*RS_485_SettingsLocators.DISABLE(1)).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, 1)).click()
        self.browser.find_element(*AddressableLoopSettingsLocators.DISABLE(1, 1)).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(2)).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(2, 1)).click()
        self.browser.find_element(*AddressableLoopSettingsLocators.DISABLE(2, 1)).click()
        self.save_settings()
        self.restore_settings()
        self.refresh_page()
        self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(1)).click()
        self.check_save_setting_disable(AreaSettingsLocators.DISABLE(1), f'area #{1}')
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(1)).click()
        self.check_save_setting_disable(InputLinkSettingsLocators.DISABLE(1), f'inputlink #{1}')
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(1)).click()
        self.check_save_setting_disable(OutputLinkSettingsLocators.DISABLE(1), f'outputlink #{1}')
        self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(1)).click()
        self.check_save_setting_disable(RS_485_SettingsLocators.DISABLE(1), f'RS-485 #{1}')
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, 1)).click()
        self.check_save_setting_disable(AddressableLoopSettingsLocators.DISABLE(1, 1),
                                        f'addressable device #{1} on loop {1}')
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(2, 1)).click()
        self.check_save_setting_disable(AddressableLoopSettingsLocators.DISABLE(2, 1),
                                        f'addressable device #{1} on loop {2}')
        

# Проверка кнопки "восстановить"
    def restore_settings(self):
        self.browser.find_element(*MainPanelLocators.RESTORE_BUTTON).click()
        sleep(6)
        assert self.is_not_element_present(*MainPanelLocators.RESTORE_MESSAGE, 1), \
            'restore message did not disappear in 6 seconds'

    def should_not_be_areas_settings(self, areas):
        print(f'Checking default settings in {areas} areas...')
        for num in range(1, areas):  # Проверка соответствия настроек в каждой Зоне Пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(num)).click()
            self.value_check(AreaSettingsLocators.ENTERS_THE_AREA(num),
                             '', 'входит в область', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.DISABLE(num), 'отключен', f'area #{num}')
            self.value_check(AreaSettingsLocators.DELAY_IN_EVACUATION(num),
                             '0', 'задержка эвакуации', f'area #{num}')
            self.value_check(AreaSettingsLocators.EXTINGUISHING_START_TIME(num),
                             '0', 'время пуска тушения', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.EXTINGUISHING(num),
                                    'есть пожаротушение', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.GAS_OUTPUT_SIGNAL(num),
                                    'требуется сигнал выхода газа', f'area #{num}')
            self.value_check(AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR(num),
                             'нет', 'взаимно исключает ДУ', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.EXTINGUISHING_BY_MFA(num),
                                    'тушение по ИПР', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.FORWARD_IN_RING(num), 
                                    'пересылать по кольцу', f'area #{num}')
            self.value_check(AreaSettingsLocators.RETRY_DELAY(num),
                             '60', 'задержка перезапроса', f'area #{num}')
            self.value_check(AreaSettingsLocators.LAUNCH_ALGORITHM(num),
                             'B (перезапрос)', 'алгоритм ЗКПС', f'area #{num}')                
            self.value_check(AreaSettingsLocators.RESET_DELAY(num),
                             '25', 'задержка сброса', f'area #{num}')

    def should_not_be_inputlinks_settings(self, inlinks):
        print(f'Checking default settings in {inlinks} inputlinks...')
        for num in range(1, inlinks + 1):  # Проверка соответствия настроек в каждом ТС входе
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num)).click()
            self.value_check(InputLinkSettingsLocators.UNIT_ID(num),
                             '', 'ссылка(ИД)', f'inputlink #{num}')
            self.value_check(InputLinkSettingsLocators.PARENT_AREA(num),
                             '', 'входит в область', f'inputlink #{num}')
            self.checkbox_unchecked(InputLinkSettingsLocators.DISABLE(num), 
                                    'отключен', f'inputlink #{num}')
            if num % 6 == 5:  # Тип ТС входа - вход команд
                self.value_check(InputLinkSettingsLocators.COMMAND(num),
                                 'сброс', 'команда', f'inputlink #{num}')
            if num % 6 == 0:  # Тип ТС входа - вход технический
                self.value_check(InputLinkSettingsLocators.CHANNEL(num),
                                 '0', 'канал', f'inputlink #{num}')
                self.checkbox_unchecked(InputLinkSettingsLocators.FIX(num),
                                        'фиксировать', f'inputlink #{num}')
    
    def should_not_be_outputlinks_settings(self, outlinks):
        print(f'Checking default settings in {outlinks} outputlinks...')
        for num in range(1, outlinks + 1):  # Проверка соответствия настроек в каждом ТС выходе
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num)).click()
            self.value_check(OutputLinkSettingsLocators.UNIT_ID(num),
                             '', 'ссылка(ИД)', f'outputlink #{num}')
            self.value_check(OutputLinkSettingsLocators.PARENT_AREA(num), 
                             '', 'входит в область', f'outputlink #{num}')
            self.checkbox_unchecked(OutputLinkSettingsLocators.DISABLE(num),
                                    'отключен', f'outputlink #{num}')
            if num % 3 == 0:  # Тип ТС выхода - выход на реле
                self.value_check(OutputLinkSettingsLocators.TURN_ON_DELAY(num),
                                 '0', 'задержка включения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.TURN_OFF_DELAY(num),
                                 '0', 'задержка выключения', f'outputlink #{num}')              
                self.checkbox_unchecked(OutputLinkSettingsLocators.NO_STOP(num),
                                        'продолжать если НЕ условие', f'outputlink #{num}')
                self.checkbox_unchecked(OutputLinkSettingsLocators.NO_RESTART_DELAY_ON(num),
                                        'продолжать задержку включения при повторном', f'outputlink #{num}')
                self.checkbox_unchecked(OutputLinkSettingsLocators.NO_RESTART_DELAY_OFF(num),
                                        'продолжать задержку вЫключения при повторном', f'outputlink #{num}')
                self.checkbox_unchecked(OutputLinkSettingsLocators.SINGLE_PULSE(num),
                                        'однократный импульс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num), 
                                 'отключено', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE2(num), 
                                 'отключено', 'на ПОЖАР (пожар-2)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num), 
                                 'отключено', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FAULT(num), 
                                 'отключено', 'на неисправность', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_REPAIR(num), 
                                 'отключено', "на 'в ремонте'", f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION(num), 
                                 'отключено', 'на газ-уходи', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING(num), 
                                 'отключено', 'на пуск тушения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AFTER_EXTINGUICHING(num), 
                                 'отключено', 'на тушение закончено', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING_FAILED(num), 
                                 'отключено', 'на тушение закончено неудачно', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AUTO_OFF(num), 
                                 'отключено', 'на авт. откл', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_RESET(num), 
                                 'отключено', 'на сброс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR(num), 
                                 'отключено', 'на дверь открыта', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_BLOCKED(num), 
                                 'отключено', 'на блокировка', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION_PAUSE(num), 
                                 'отключено', 'на останов', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR_PAUSE(num), 
                                 'отключено', 'на останов по двери', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_CANCELLED(num), 
                                 'отключено', 'на отмену пуска тушения', f'outputlink #{num}')
                for tech_num in range(15):
                    self.value_check(OutputLinkSettingsLocators.ON_TECH(num, tech_num), 
                                     'отключено', f'на технический сигнал {tech_num}', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.AND_OR(num),
                                 'по ИЛИ', 'И/или', f'outputlink #{num}')
        
    def should_not_be_BIS_Ms_settings(self, BIS_Ms):
        print(f'Checking default settings in {BIS_Ms} BIS_Ms...')
        for num in range(1, BIS_Ms + 1):  # Проверка соответствия настроек в каждом БИС-Ме
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(num)).click()
            self.checkbox_unchecked(RS_485_SettingsLocators.DISABLE(num), 'отключен', f'RS-485 #{num}')
            if num % 4 == 0:  # Тип RS-485 - ТИ
                self.checkbox_checked(RS_485_SettingsLocators.FIRE(num), 
                                      'ПОЖАР', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.ATTENTION(num), 
                                        'ВНИМАНИЕ', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.FAULT(num), 
                                        'НЕИСПРАВНОСТЬ', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.AUTO_OFF(num), 
                                        'автоматика ОТКЛ', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LEVEL_CONFIRM(num),
                                 '80', 'уровень ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LENGTH_CONFIRM(num),
                                 '10', 'длительность ответа', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.PULSE_DIAL(num), 
                                        'импульсный набор', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.NO_CONFIRM(num), 
                                        'не ждать ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.PHONE_NUMBER(num),
                                 '', 'номер телефона', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.ACCOUNT(num),
                                 '1000', 'аккаунт', f'RS-485 #{num}')
            else:
                if num % 4 == 3:  # Тип RS-485 - БИС-М3
                    self.checkbox_unchecked(RS_485_SettingsLocators.DEFAULT_GREEN(num), 
                                            'по умолчанию зеленые', f'RS-485 #{num}')
                    self.value_check(RS_485_SettingsLocators.BACKLIGHT(num),
                                     '0', 'подсветка', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.BRIGHTNESS(num),
                                 '7', 'яркость', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.TIMEOUT(num),
                                 '20', 'таймаут нажатий', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.NO_SOUND(num), 
                                        'без звука', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.NO_ALARM_SOUND(num), 
                                        'без звука тревог', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.KEY_SENSITIVE(num), 
                                        'чувствительность клавиш', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.DEFAULT_ID(num),
                                 '0', 'ИД по умолчанию', f'RS-485 #{num}')
            self.value_check(RS_485_SettingsLocators.SN(num),
                             str(2000 + num), 'серийный номер', f'RS-485 #{num}')
    
    def should_not_be_addressable_devices_settings(self, AL, addr_devs):
        print(f'Checking default settings in {addr_devs} addressable devices in addressable loop {AL}...')
        for num in range(1, addr_devs + 1):  # У каждого АУ на указаном шлейфу изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, num)).click()
            self.checkbox_unchecked(AddressableLoopSettingsLocators.DISABLE(AL, num), 
                                    'отключен', f'addressable device #{num} on loop {AL}')
            if num % 13 == 2:  # Тип АУ - АР1
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num),
                                 'контроль линии, нет пожар2', 'режим', f'addressable device #{num} on loop {AL}')
            if num % 13 == 4:  # Тип АУ - АРмини
                self.checkbox_checked(AddressableLoopSettingsLocators.TWO_INPUTS(AL, num), 
                                      'два входа', f'addressable device #{num} on loop {AL}')
            if num % 13 == 5:  # Тип АУ - АТИ
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num),
                                 'A1', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_unchecked(AddressableLoopSettingsLocators.DIFFERENTIAL(AL, num),
                                        'дифференциальный', f'addressable device #{num} on loop {AL}')
            if num % 13 == 6:  # Тип АУ - АхДПИ
                self.value_check(AddressableLoopSettingsLocators.THRESHOLD(AL, num),
                                 '17', 'порог чувствительности', f'addressable device #{num} on loop {AL}')
                self.value_check(AddressableLoopSettingsLocators.GROUP(AL, num),
                                 '0', 'ЗКПС', f'addressable device #{num} on loop {AL}')
            if num % 13 == 10:  # Тип АУ - ИСМ4
                self.value_check(AddressableLoopSettingsLocators.MODE220(AL, num),
                                 '220v', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_unchecked(AddressableLoopSettingsLocators.MOTOR(AL, num), 
                                        'мотор с переполюсовкой', f'addressable device #{num} on loop {AL}')
            if num % 13 == 11:  # Тип АУ - ИСМ5
                self.value_check(AddressableLoopSettingsLocators.MODE24(AL, num),
                                 'любое', 'напряжение питания', f'addressable device #{num} on loop {AL}')
            self.value_check(AddressableLoopSettingsLocators.SN(AL, num),
                             str(AL * 1000 + num), 'серийный номер', f'addressable device #{num} on loop {AL}')


# Полная перезапись настроек ранее добавленных объектов
    def select_in_list(self, locator, item):  # Выбрать пункт в настройке с выпадающим списком
        self.browser.find_element(*locator).click()
        self.browser.find_element(*SystemObjectsLocators.DROP_DOWN_LIST(item)).click()

    def rewrite_areas_settings(self, areas):
        print(f'Rewrite settings in {areas} areas...')
        self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Раскрыть Зоны
        for area_num in range(1, areas):  # У каждой Зоны Пожаротушения изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(area_num)).click()
            self.browser.execute_script("scrollBy(0, -500);")  # Прокрутка страницы вверх
            self.select_in_list(AreaSettingsLocators.ENTERS_THE_AREA(area_num), areas - 1)
            self.browser.find_element(*AreaSettingsLocators.DISABLE(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.DELAY_IN_EVACUATION(area_num)
                                      ).send_keys(123456)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING_START_TIME(area_num)
                                      ).send_keys(123456)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.GAS_OUTPUT_SIGNAL(area_num)).click()
            self.select_in_list(AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR_ARROW(area_num), 5)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING_BY_MFA(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.FORWARD_IN_RING(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.RETRY_DELAY(area_num)
                                      ).send_keys(123456)
            self.select_in_list(AreaSettingsLocators.LAUNCH_ALGORITHM_ARROW(area_num), 4)
            self.browser.find_element(*AreaSettingsLocators.RESET_DELAY(area_num)
                                      ).send_keys(123456)
    
    def rewrite_inputlinks_settings(self, inlinks, areas):
        print(f'Rewrite settings in {inlinks} inputlinks...')
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Раскрыть ТС входы
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()
        for num in range(1, inlinks + 1):  # У каждого ТС входа изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num)).click()
            link = self.browser.find_element(*InputLinkSettingsLocators.UNIT_ID(num))
            assert self.is_element_present(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num)), \
                f'Addressable device #{num} for inputlink #{num} not found'
            device = self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num))
            self.browser.execute_script("arguments[0].scrollIntoView(true);", device)
            self.browser.execute_script("""
                var src = arguments[0];
                var tgt = arguments[1];
                var dataTransfer = new DataTransfer();     
                var dragStartEvent = new DragEvent('dragstart', {
                    dataTransfer: dataTransfer,
                    bubbles: true,
                    cancelable: true
                });
                src.dispatchEvent(dragStartEvent);
                var dropEvent = new DragEvent('drop', {
                    dataTransfer: dataTransfer,
                    bubbles: true,
                    cancelable: true
                });
                tgt.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                    dataTransfer: dataTransfer,
                    bubbles: true,
                    cancelable: true
                });
                src.dispatchEvent(dragEndEvent);
            """, device, link)
            self.select_in_list(InputLinkSettingsLocators.PARENT_AREA(num), areas)
            self.browser.find_element(*InputLinkSettingsLocators.DISABLE(num)).click()
            if num % 6 == 5:  # Тип ТС входа - вход команд
                self.select_in_list(InputLinkSettingsLocators.COMMAND_ARROW(num), 17)
            if num % 6 == 0:  # Тип ТС входа - вход технический
                self.browser.find_element(*InputLinkSettingsLocators.CHANNEL(num)).send_keys(1234)
                self.browser.find_element(*InputLinkSettingsLocators.FIX(num)).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()
      
    def rewrite_outputlinks_settings(self, outlinks, areas):
        print(f'Rewrite settings in {outlinks} outputlinks...')
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Раскрыть ТС выходы
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Раскрыть RS-485
        BIS_num = 1
        for num in range(1, outlinks + 1):
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num)).click()
            link = self.browser.find_element(*OutputLinkSettingsLocators.UNIT_ID(num))
            if BIS_num % 4 == 0: BIS_num += 1  # Если тип БИС-Ма - ТИ, то пропускаем его
            assert self.is_element_present(*SystemObjectsLocators.RS_485_ITEMS(BIS_num)), \
                f'BIS-M #{num} for outputlink #{num} not found'
            BIS_m = self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(BIS_num))
            self.browser.execute_script("arguments[0].scrollIntoView(true);", BIS_m)
            ActionChains(self.browser).drag_and_drop(BIS_m, link).perform()  # Перемещение БИС_М
            BIS_num += 1
            self.browser.find_element(*OutputLinkSettingsLocators.PARENT_AREA(num)).click()
            self.browser.find_element(*SystemObjectsLocators.DROP_DOWN_LIST(areas)).click()
            self.browser.find_element(*OutputLinkSettingsLocators.DISABLE(num)).click()
            if num % 3 == 0:  # Тип ТС выхода - выход на реле
                self.browser.find_element(*OutputLinkSettingsLocators.TURN_ON_DELAY(num)).send_keys(123456)
                self.browser.find_element(*OutputLinkSettingsLocators.TURN_OFF_DELAY(num)).send_keys(123456)
                self.browser.find_element(*OutputLinkSettingsLocators.NO_STOP(num)).click()
                self.browser.find_element(*OutputLinkSettingsLocators.NO_RESTART_DELAY_ON(num)).click()
                self.browser.find_element(*OutputLinkSettingsLocators.NO_RESTART_DELAY_OFF(num)).click()
                self.browser.find_element(*OutputLinkSettingsLocators.SINGLE_PULSE(num)).click()
                self.select_in_list(OutputLinkSettingsLocators.ON_FIRE1_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_FIRE2_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_FAULT_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_REPAIR_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EVACUATION_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EXTINGUICHING_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_AFTER_EXTINGUICHING_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EXTINGUICHING_FAILED_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_AUTO_OFF_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_RESET_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_DOOR_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_BLOCKED_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EVACUATION_PAUSE_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_DOOR_PAUSE_ARROW(num), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_CANCELLED_ARROW(num), 3)
                for tech_num in range(15):
                    self.select_in_list(OutputLinkSettingsLocators.ON_TECH_ARROW(num, tech_num), 3)
                self.select_in_list(OutputLinkSettingsLocators.AND_OR_ARROW(num), 2)
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Скрыть RS-485
    
    def rewrite_BIS_Ms_settings(self, BIS_Ms):
        print(f'Rewrite settings in {BIS_Ms} BIS_Ms...')
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Раскрыть RS-485
        for num in range(1, BIS_Ms + 1):  # У каждого БИС-Ма изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(num)).click()
            self.browser.execute_script("scrollBy(0, -1000);")  # Прокрутка страницы вверх
            self.browser.find_element(*RS_485_SettingsLocators.DISABLE(num)).click()
            if num % 4 == 0:  # Тип RS-485 - ТИ
                self.browser.find_element(*RS_485_SettingsLocators.FIRE(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.ATTENTION(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.FAULT(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.AUTO_OFF(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.LEVEL_CONFIRM(num)).send_keys(12345)
                self.browser.find_element(*RS_485_SettingsLocators.LENGTH_CONFIRM(num)).send_keys(123)
                self.browser.find_element(*RS_485_SettingsLocators.PULSE_DIAL(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.NO_CONFIRM(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.PHONE_NUMBER(num)
                                          ).send_keys(1234567890123456)
                self.browser.find_element(*RS_485_SettingsLocators.ACCOUNT(num)).send_keys(12345)
            else:
                if num % 4 == 3:  # Тип RS-485 - БИС-М3
                    self.browser.find_element(*RS_485_SettingsLocators.DEFAULT_GREEN(num)).click()
                    self.browser.find_element(*RS_485_SettingsLocators.BACKLIGHT(num)).send_keys(1234)
                self.browser.find_element(*RS_485_SettingsLocators.BRIGHTNESS(num)).send_keys(123)
                self.browser.find_element(*RS_485_SettingsLocators.TIMEOUT(num)).send_keys(1234)
                self.browser.find_element(*RS_485_SettingsLocators.NO_SOUND(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.NO_ALARM_SOUND(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.KEY_SENSITIVE(num)).click()
                self.browser.find_element(*RS_485_SettingsLocators.DEFAULT_ID(num)).send_keys(12345678901)
            self.browser.find_element(*RS_485_SettingsLocators.SN(num)).send_keys('\b\b\b\b', 65536 - num)
    
    def rewrite_addressable_devices_settings(self, AL, addr_devs):
        print(f'Rewrite settings in {addr_devs} addressable devices in addressable loop {AL}...')
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
        for num in range(1, addr_devs + 1):  # У каждого АУ на указаном шлейфу изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, num)).click()
            self.browser.find_element(*AddressableLoopSettingsLocators.DISABLE(AL, num)).click()
            if num % 13 == 2:  # Тип АУ - АР1
                self.select_in_list(AddressableLoopSettingsLocators.MODE_ARROW(AL, num), 3)
            if num % 13 == 4:  # Тип АУ - АРмини
                self.browser.find_element(*AddressableLoopSettingsLocators.TWO_INPUTS(AL, num)).click()
            if num % 13 == 5:  # Тип АУ - АТИ
                self.select_in_list(AddressableLoopSettingsLocators.MODE_ARROW(AL, num), 6)
                self.browser.find_element(*AddressableLoopSettingsLocators.DIFFERENTIAL(AL, num)).click()
            if num % 13 == 6:  # Тип АУ - АхДПИ
                self.browser.find_element(*AddressableLoopSettingsLocators.THRESHOLD(AL, num)).send_keys(99)
                self.browser.find_element(*AddressableLoopSettingsLocators.GROUP(AL, num)).send_keys(1234)
            if num % 13 == 10:  # Тип АУ - ИСМ4
                self.select_in_list(AddressableLoopSettingsLocators.MODE220_ARROW(AL, num), 5)
                self.browser.find_element(*AddressableLoopSettingsLocators.MOTOR(AL, num)).click()
            if num % 13 == 11:  # Тип АУ - ИСМ5
                self.select_in_list(AddressableLoopSettingsLocators.MODE24_ARROW(AL, num), 2)
            self.browser.find_element(*AddressableLoopSettingsLocators.SN(AL, num)).send_keys(
                '\b\b\b\b', 16777216 - num - (AL - 1) * addr_devs)  # Стирает 4 символа и вставляет сн

# Проверка полной перезаписи настроек
    def value_check(self, locator, expected_value, set_name, object_name):  # Проверка значения настройки
        value = self.browser.find_element(*locator).get_attribute('value')
        assert expected_value == value, f'Value in "{set_name}" in {object_name} does not match, ' \
                                        f'expected "{expected_value}", value received "{value}"'

    def checkbox_checked(self, locator, checkbox_name, object_name):  # Проверка, что чекбокс включен
        assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
            AreaSettingsLocators.CHECKBOX_CHECKED[1] + locator[1]), \
            f'Checkbox "{checkbox_name}" in {object_name} is unchecked, expected to be checked'
    
    def checkbox_unchecked(self, locator, checkbox_name, object_name):  # Проверка, что чекбокс включен
        assert self.is_not_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
            AreaSettingsLocators.CHECKBOX_CHECKED[1] + locator[1], 0.1), \
            f'Checkbox "{checkbox_name}" in {object_name} is checked, expected to be unchecked'

    def should_be_areas_settings(self, areas):
        print(f'Checking settings in {areas} areas...')
        self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()
        for num in range(1, areas):  # Проверка соответствия настроек в каждой Зоне Пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(num)).click()
            self.value_check(AreaSettingsLocators.ENTERS_THE_AREA(num),
                             f'#{areas} Зона Пожаротушения ', 'входит в область', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.DISABLE(num), 'отключен', f'area #{num}')
            self.value_check(AreaSettingsLocators.DELAY_IN_EVACUATION(num),
                             '1800', 'задержка эвакуации', f'area #{num}')
            self.value_check(AreaSettingsLocators.EXTINGUISHING_START_TIME(num),
                             '255', 'время пуска тушения', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.EXTINGUISHING(num),
                                  'есть пожаротушение', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.GAS_OUTPUT_SIGNAL(num),
                                  'требуется сигнал выхода газа', f'area #{num}')
            self.value_check(AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR(num),
                             'не (пожар ИЛИ 1) блокирует 6', 'взаимно исключает ДУ', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.EXTINGUISHING_BY_MFA(num),
                                  'тушение по ИПР', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.FORWARD_IN_RING(num), 
                                  'пересылать по кольцу', f'area #{num}')
            self.value_check(AreaSettingsLocators.RETRY_DELAY(num),
                             '16383', 'задержка перезапроса', f'area #{num}')
            self.value_check(AreaSettingsLocators.LAUNCH_ALGORITHM(num),
                             'C2 (два пожара или пожар+неисправность)', 'алгоритм ЗКПС', f'area #{num}')                
            self.value_check(AreaSettingsLocators.RESET_DELAY(num),
                             '16383', 'задержка сброса', f'area #{num}')

    def should_be_inputlinks_settings(self, inlinks, areas):
        print(f'Checking settings in {inlinks} inputlinks...')
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()
        for num in range(1, inlinks + 1):  # Проверка соответствия настроек в каждом ТС входе
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num)).click()
            device_name = self.browser.find_element(
                *SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num)).text
            self.value_check(InputLinkSettingsLocators.UNIT_ID(num),
                             device_name, 'ссылка(ИД)', f'inputlink #{num}')
            self.value_check(InputLinkSettingsLocators.PARENT_AREA(num),
                             f'#{areas} Зона Пожаротушения ', 'входит в область', f'inputlink #{num}')
            self.checkbox_checked(InputLinkSettingsLocators.DISABLE(num), 'отключен', f'inputlink #{num}')
            if num % 6 == 5:  # Тип ТС входа - вход команд
                self.value_check(InputLinkSettingsLocators.COMMAND(num),
                                 f'СДУ - газ пошел', 'команда', f'inputlink #{num}')
            if num % 6 == 0:  # Тип ТС входа - вход технический
                self.value_check(InputLinkSettingsLocators.CHANNEL(num),
                                 f'14', 'канал', f'inputlink #{num}')
                self.checkbox_checked(InputLinkSettingsLocators.FIX(num), 'фиксировать', f'inputlink #{num}')
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()

    def should_be_outputlinks_settings(self, outlinks, areas):
        print(f'Checking settings in {outlinks} outputlinks...')
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
        BIS_num = 1
        for num in range(1, outlinks + 1):  # Проверка соответствия настроек в каждом ТС выходе
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num)).click()
            if BIS_num % 4 == 0: BIS_num += 1  # Если тип БИС-Ма - ТИ, то пропускаем его
            BIS_name = self.browser.find_element(
                *SystemObjectsLocators.RS_485_ITEMS(BIS_num)).text
            BIS_num += 1
            self.value_check(OutputLinkSettingsLocators.UNIT_ID(num),
                             BIS_name, 'ссылка(ИД)', f'outputlink #{num}')
            self.value_check(OutputLinkSettingsLocators.PARENT_AREA(num), 
                             f'#{areas} Зона Пожаротушения ', 'входит в область', f'outputlink #{num}')
            self.checkbox_checked(OutputLinkSettingsLocators.DISABLE(num), 'отключен', f'outputlink #{num}')
            if num % 3 == 0:  # Тип ТС выхода - выход на реле
                self.value_check(OutputLinkSettingsLocators.TURN_ON_DELAY(num),
                                 '16383', 'задержка включения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.TURN_OFF_DELAY(num),
                                 '16383', 'задержка выключения', f'outputlink #{num}')              
                self.checkbox_checked(OutputLinkSettingsLocators.NO_STOP(num),
                                      'продолжать если НЕ условие', f'outputlink #{num}')
                self.checkbox_checked(OutputLinkSettingsLocators.NO_RESTART_DELAY_ON(num),
                                      'продолжать задержку включения при повторном', f'outputlink #{num}')
                self.checkbox_checked(OutputLinkSettingsLocators.NO_RESTART_DELAY_OFF(num),
                                      'продолжать задержку вЫключения при повторном', f'outputlink #{num}')
                self.checkbox_checked(OutputLinkSettingsLocators.SINGLE_PULSE(num),
                                      'однократный импульс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num), 
                                 'если есть', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE2(num), 
                                 'если есть', 'на ПОЖАР (пожар-2)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num), 
                                 'если есть', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FAULT(num), 
                                 'если есть', 'на неисправность', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_REPAIR(num), 
                                 'если есть', "на 'в ремонте'", f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION(num), 
                                 'если есть', 'на газ-уходи', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING(num), 
                                 'если есть', 'на пуск тушения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AFTER_EXTINGUICHING(num), 
                                 'если есть', 'на тушение закончено', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING_FAILED(num), 
                                 'если есть', 'на тушение закончено неудачно', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AUTO_OFF(num), 
                                 'если есть', 'на авт. откл', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_RESET(num), 
                                 'если есть', 'на сброс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR(num), 
                                 'если есть', 'на дверь открыта', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_BLOCKED(num), 
                                 'если есть', 'на блокировка', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION_PAUSE(num), 
                                 'если есть', 'на останов', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR_PAUSE(num), 
                                 'если есть', 'на останов по двери', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_CANCELLED(num), 
                                 'если есть', 'на отмену пуска тушения', f'outputlink #{num}')
                for tech_num in range(15):
                    self.value_check(OutputLinkSettingsLocators.ON_TECH(num, tech_num), 
                                     'если есть', f'на технический сигнал {tech_num}', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.AND_OR(num),
                                 'по И', 'И/или', f'outputlink #{num}')
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
    
    def should_be_BIS_Ms_settings(self, BIS_Ms):
        print(f'Checking settings in {BIS_Ms} BIS_Ms...')
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
        for num in range(1, BIS_Ms + 1):  # Проверка соответствия настроек в каждом БИС-Ме
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(num)).click()
            self.checkbox_checked(RS_485_SettingsLocators.DISABLE(num), 'отключен', f'RS-485 #{num}')
            if num % 4 == 0:  # Тип RS-485 - ТИ
                self.checkbox_unchecked(RS_485_SettingsLocators.FIRE(num), 
                                        'ПОЖАР', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.ATTENTION(num), 
                                      'ВНИМАНИЕ', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.FAULT(num), 
                                      'НЕИСПРАВНОСТЬ', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.AUTO_OFF(num), 
                                      'автоматика ОТКЛ', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LEVEL_CONFIRM(num),
                                 '2000', 'уровень ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LENGTH_CONFIRM(num),
                                 '15', 'длительность ответа', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.PULSE_DIAL(num), 
                                      'импульсный набор', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.NO_CONFIRM(num), 
                                      'не ждать ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.PHONE_NUMBER(num),
                                 '1234567890123456', 'номер телефона', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.ACCOUNT(num),
                                 '9999', 'аккаунт', f'RS-485 #{num}')
            else:
                if num % 4 == 3:  # Тип RS-485 - БИС-М3
                    self.checkbox_checked(RS_485_SettingsLocators.DEFAULT_GREEN(num), 
                                          'по умолчанию зеленые', f'RS-485 #{num}')
                    self.value_check(RS_485_SettingsLocators.BACKLIGHT(num),
                                     '255', 'подсветка', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.BRIGHTNESS(num),
                                 '15', 'яркость', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.TIMEOUT(num),
                                 '255', 'таймаут нажатий', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.NO_SOUND(num), 
                                      'без звука', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.NO_ALARM_SOUND(num), 
                                      'без звука тревог', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.KEY_SENSITIVE(num), 
                                      'чувствительность клавиш', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.DEFAULT_ID(num),
                                 '2147483647', 'ИД по умолчанию', f'RS-485 #{num}')
            self.value_check(RS_485_SettingsLocators.SN(num),
                             str(65536 - num), 'серийный номер', f'RS-485 #{num}')

    def should_be_addressable_devices_settings(self, AL, addr_devs):
        print(f'Checking settings in {addr_devs} addressable devices in addressable loop {AL}...')
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
        for num in range(1, addr_devs + 1):  # У каждого АУ на указаном шлейфу изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, num)).click()
            if num % 13 != 10:  # Если не ИСМ4 (у него отключен)
                self.checkbox_checked(AddressableLoopSettingsLocators.DISABLE(AL, num), 
                                      'отключен', f'addressable device #{num} on loop {AL}')
            if num % 13 == 2:  # Тип АУ - АР1
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num),
                                 'нет контроля, нет пожар2', 'режим', f'addressable device #{num} on loop {AL}')
            if num % 13 == 4:  # Тип АУ - АРмини
                self.checkbox_unchecked(AddressableLoopSettingsLocators.TWO_INPUTS(AL, num), 
                                        'два входа', f'addressable device #{num} on loop {AL}')
            if num % 13 == 5:  # Тип АУ - АТИ
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num),
                                 'off', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_checked(AddressableLoopSettingsLocators.DIFFERENTIAL(AL, num),
                                      'дифференциальный', f'addressable device #{num} on loop {AL}')
            if num % 13 == 6:  # Тип АУ - АхДПИ
                self.value_check(AddressableLoopSettingsLocators.THRESHOLD(AL, num),
                                 '50', 'порог чувствительности', f'addressable device #{num} on loop {AL}')
                self.value_check(AddressableLoopSettingsLocators.GROUP(AL, num),
                                 '255', 'ЗКПС', f'addressable device #{num} on loop {AL}')
            if num % 13 == 10:  # Тип АУ - ИСМ4
                self.checkbox_unchecked(AddressableLoopSettingsLocators.DISABLE(AL, num), 
                                        'отключен', f'addressable device #{num} on loop {AL}')
                self.value_check(AddressableLoopSettingsLocators.MODE220(AL, num),
                                 'игнорировать', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_checked(AddressableLoopSettingsLocators.MOTOR(AL, num), 
                                      'мотор с переполюсовкой', f'addressable device #{num} on loop {AL}')
            if num % 13 == 11:  # Тип АУ - ИСМ5
                self.value_check(AddressableLoopSettingsLocators.MODE24(AL, num),
                                 '24v', 'напряжение питания', f'addressable device #{num} on loop {AL}')
            self.value_check(AddressableLoopSettingsLocators.SN(AL, num),
                             str(16777216 - num - (AL - 1) * addr_devs), 'серийный номер', 
                             f'addressable device #{num} on loop {AL}')


# Очистка ППК от объектов
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
        if self.is_element_present(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(1)):
            self.browser.find_element(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(1)).click()
        if self.is_element_present(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(2)):
            self.browser.find_element(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(2)).click()