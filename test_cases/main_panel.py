from main_page import Page
from locators import (MainPanelLocators, SystemObjectsLocators, AreaSettingsLocators,
                      InputLinkSettingsLocators, OutputLinkSettingsLocators, 
                      RS_485_SettingsLocators, AddressableLoopSettingsLocators, EventLogLocators)
from selenium.common.exceptions import StaleElementReferenceException
from loguru import logger
import keyboard
import os
from datetime import datetime
from time import time
from time import sleep


class MainPanel(Page):  # Класс для тестирования по тест-кейсу "Главная панель" (DRBN-T52)

# Общие функции
    def check_presence_and_spelling(self, locator, button_name):
        assert self.is_element_present(*locator), \
            f'Button "{button_name}" is not presented'
        button_text = self.browser.find_element(*locator).text
        assert button_text == button_name, \
            f'Button "{button_name}" has a spelling error6, button text: {button_text}'

    def presence_and_spelling(self, locator, button_name):  # Проверка на наличие элемента и ошибки
        logger.info(f'Checking the button "{button_name}"...')
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
        self.button_should_be_clickable(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')
        self.browser.find_element(*MainPanelLocators.SAVE_BUTTON).click()
    
    def button_should_be_clickable(self, locator, button):
        assert self.is_element_clickable(*locator), f'Button "{button}" is not clickable'


# Проверка title
    def check_tab_name_on_title(self):
        logger.info('Checking the title...')
        title = self.browser.title.split()[0]
        assert title == 'Веб-конфигуратор', 'The tab name in the title does not match, ' \
            f'expected "Веб-конфигуратор", received "{title}"'

    def check_version_on_title(self, version):  # Номер версии конфигуратора в title
        ver = self.browser.title.split()[1]
        assert ver == version, 'The configurator version in the title does not match, ' \
            f'expected "{version}", received "{ver}"'


# Проверка логотипа "Рубикон"
    def should_be_logo(self):
        logger.info('Checking the logo...')
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
        logger.info('Checking the button "В Файл для Интеллекта"...')
        assert self.is_element_present(*MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON), \
            'Button "В Файл для Интеллекта" is not presented'

    def should_be_from_file_button(self):
        self.presence_and_spelling(MainPanelLocators.FROM_FILE_BUTTON, 'ИЗ ФАЙЛА')
    
    def should_be_event_log_button(self):
        self.presence_and_spelling(MainPanelLocators.EVENT_LOG_BUTTON, 'ЖУРНАЛ')
        
    def should_be_terminal_button(self):
        self.presence_and_spelling(MainPanelLocators.TERMINAL_BUTTON, 'ТЕРМИНАЛ')

    def should_be_light_mode_icon(self):
        logger.info('Checking the light mode icon...')
        assert self.is_element_present(*MainPanelLocators.LIGHT_MODE_ICON), \
            'Icon "Light Mode" is not presented'


# Проверка статуса подключения
    def should_be_online_mark(self):
        logger.info('Checking online status...')
        assert self.is_element_present(*MainPanelLocators.ONLINE_MARK), \
            'Online mark is not presented'
    
    def status_should_be_online(self):
        status = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).text
        assert status == 'online', f'Connection status not "online", status: {status}'

    def online_mark_color_should_be_green(self):
        color = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).value_of_css_property('color')
        assert '0, 230, 118' in color, \
            f'Connection status color is not green: "rgba(0, 230, 118, 1)", received color: {color}'
    
    def should_be_offline_mark(self):
        logger.info('Checking offline status...')
        sleep(1)  # f
        assert self.is_element_present(*MainPanelLocators.OFFLINE_MARK), \
            'Offline mark is not presented'
    
    def status_should_be_offline(self):
        status = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).text
        assert status == 'offline', f'Connection status not "offline", status: {status}'

    def online_mark_color_should_be_yellow(self):
        color = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).value_of_css_property('color')
        assert '255, 215, 64' in color, \
            f'Connection status color is not yellow: "rgba(255, 215, 64, 1)", received color: {color}'


# Проверка кнопки В ППК с открытым Терминалом
    def recording_setting_for_module(self, module_num):  # Модуль Области стал активным
        logger.info(f'Checking recording setting for module {module_num}...')
        self.browser.find_element(*SystemObjectsLocators.MODULE_FORM(module_num)).click()
        assert self.is_element_clickable(*MainPanelLocators.TO_PPK_BUTTON), \
            'Button "В ППК" is not clickable'
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК
        assert self.is_element_present(*MainPanelLocators.TO_PPK_BUTTON_IS_BLINKING), \
            'Button "В ППК" does not blink'

    def check_record(self, module='', timeout=30):
        logger.info(f'Checking start and finish of recording for {'ppk' if module == '' else module[1:]}...')
        start_time = time()
        assert self.is_element_present(*SystemObjectsLocators.RECORD_START(module)), \
            f'Recording for {'ppk' if module == '' else module[1:]} has not started'
        assert self.is_element_visible(*SystemObjectsLocators.RECORD_FINISH, max(timeout, 10)), \
            f'Recording for {'ppk' if module == '' else module[1:]} has not finished, ' \
            f'time spent: {time() - start_time:.2f}'
        logger.success(f'Record to {'ppk' if module == '' else module[1:]} was successful, ' \
                       f'time spent: {time() - start_time:.2f}')


# Проверка кнопки ИЗ ППК
    def unload_settings(self):
        logger.info(f'Checking unloading settings from ppk...')
        sleep(1)
        button = self.browser.find_element(*MainPanelLocators.FROM_PPK_BUTTON)
        button.click()
        if '250, 250, 250' in button.value_of_css_property('color'):  # Темная тема
            assert self.is_element_present(*MainPanelLocators.FROM_PPK_BUTTON_IS_BLINKING_DARK), \
            'Button "ИЗ ППК" does not blink'
        else:
            assert self.is_element_present(*MainPanelLocators.FROM_PPK_BUTTON_IS_BLINKING_LIGHT), \
            'Button "ИЗ ППК" does not blink'

    def check_unload(self, m1_wait, m2_wait, m3_wait):
        logger.info(f'Checking start and finish of unloading for ppk and moduls...')
        start_time = time()
        assert self.is_element_present(*SystemObjectsLocators.UNLOAD_START), \
            f'Unload for all ppkr has not started, time spent: {time() - start_time:.2f}'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_1, 5), \
            f'Unload for module 1 has not started, time spent: {time() - start_time:.2f}'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_2, max(m1_wait, 40)), \
            f'Unload for module 2 has not started, time spent: {time() - start_time:.2f}'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_3, max(m2_wait, 40)), \
            f'Unload for module 3 has not started, time spent: {time() - start_time:.2f}'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH, max(m3_wait, 40)), \
            f'Unload for all ppkr has not finished, time spent: {time() - start_time:.2f}'
        logger.success(f'Unload from ppk was successful, time spent: {time() - start_time:.2f}')


# Полная запись в ППК
    def add_areas(self, areas):
        logger.info(f'Creating {areas} areas...')
        for _ in range(areas):  # Создать Зоны пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ADD_ICON).click()

    def add_inputlink(self, inlinks):
        logger.info(f'Creating {inlinks} inputlinks...')
        if inlinks > 0:
            for i in range(inlinks):  # Создать ТС входы
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ADD_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Список входов
            for i in range(inlinks):  # Сделать ТС входы каждого типа
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(i + 1)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 6 + 1)).click()  # Изменить тип входа
                self.is_not_element_present(*SystemObjectsLocators.UNIT_MENU_CONFIG)
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()

    def add_ouputlink(self, outlinks):
        logger.info(f'Creating {outlinks} outputlinks...')
        if outlinks > 0:
            for i in range(outlinks):  # Создать ТС выходы
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ADD_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Список выходов
            for i in range(outlinks):  # Сделать ТС выходы каждого типа
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(i + 1)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 3 + 1)).click()  # Изменить тип выхода
                self.is_not_element_present(*SystemObjectsLocators.UNIT_MENU_CONFIG)
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
    
    def add_BIS_M(self, BIS_Ms):
        logger.info(f'Creating {BIS_Ms} BIS M...')
        if BIS_Ms > 0:
            for i in range(BIS_Ms):  # Создать БИС-Мы
                self.browser.find_element(*SystemObjectsLocators.RS_485_ADD_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Список БИС-М
            for i in range(BIS_Ms):  # Сделать БИС-Мы каждого типа
                self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(i + 1)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 4 + 1)).click()  # Изменить тип выхода
                self.is_not_element_present(*SystemObjectsLocators.UNIT_MENU_CONFIG)  # Поле мешающее нажатию
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
    
    def open_ADDRESSABLE_LOOP(self, AL):
        assert self.is_element_clickable(*SystemObjectsLocators.ADDRESSABLE_LOOP(AL)), \
            'Addressable loop arrow is not clickable'
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_LOOP(AL)).click()

    def add_addressable_devices(self, AL, addr_devs):
        logger.info(f'Creating {addr_devs} addressable devices on addressable loop {AL}...')
        if addr_devs > 0:
            for i in range(addr_devs):  # Создать АУ
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL)).click()
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
            for i in range(addr_devs):  # Сделать АУ каждого типа
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, i + 1)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 13 + 1)).click()  # Изменить тип выхода
                self.is_not_element_present(*SystemObjectsLocators.UNIT_MENU_CONFIG)
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()


# Проверка полной выгрузки из ППК
    def check_number_of_areas(self, areas):
        logger.info(f'Checking number of areas...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_AREAS).text
        assert str(areas) == count, f'Number of areas is not equal {areas}, number = {count}'

    def check_number_of_inputlink(self, inlinks):
        logger.info(f'Checking number of inlinks...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_INPUTLINK).text
        assert str(inlinks) == count, f'Number of inputlinks is not equal {inlinks}, number = {count}'

    def check_number_of_outputlink(self, outlinks):
        logger.info(f'Checking number of outlinks...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_OUTPUTLINK).text
        assert str(outlinks) == count, f'Number of outputlinks is not equal {outlinks}, number = {count}'

    def check_number_of_BIS_M(self, BIS_Ms):
        logger.info(f'Checking number of BIS_Ms...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_RS_485).text
        assert str(BIS_Ms) == count, f'Number of RS-485 devices is not equal {BIS_Ms}, number = {count}'

    def check_number_of_addressable_devices(self, AL, addr_devs):
        logger.info(f'Checking number of addr_devs...')
        count = self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL)).text
        assert str(addr_devs) == count, \
            f'Number of addressable_devices on loop {AL} is not equal {addr_devs}, number = {count}'

    
# Проверка кнопки "Сохранить"
    def check_save_setting_disable(self, locator, object_name):  # Проверка, что чекбокс включен
        assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
            AreaSettingsLocators.CHECKBOX_CHECKED[1] + locator[1]), \
            f'Checkbox "отключен" in {object_name} was not saved'
    
    def check_save_settings(self, areas, inlinks, outlinks, BIS_Ms, addr_devs):
        logger.info('Checking save settings...')
        self.button_should_be_clickable(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')
        self.save_settings()
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Раскрыть Зоны
            assert self.is_element_present(*SystemObjectsLocators.AREA_SAVE_ICON), \
                'Settings not saved, there is no green dot near the area #1'  # Проверка появления зеленой точки   
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(1)).click()
            self.browser.find_element(*AreaSettingsLocators.DISABLE(1)).click()
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Закрыть Зоны
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Раскрыть ТС входы
            assert self.is_element_present(*SystemObjectsLocators.INPUTLINK_SAVE_ICON), \
                'Settings not saved, there is no green dot near the inputlink #1'
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(1)).click()
            self.browser.find_element(*InputLinkSettingsLocators.DISABLE(1)).click()
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Раскрыть ТС выходы
            assert self.is_element_present(*SystemObjectsLocators.OUTPUTLINK_SAVE_ICON), \
                'Settings not saved, there is no green dot near the outputlink #1'
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(1)).click()
            self.browser.find_element(*OutputLinkSettingsLocators.DISABLE(1)).click()
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Раскрыть RS-485
            assert self.is_element_present(*SystemObjectsLocators.BIS_M_SAVE_ICON), \
                'Settings not saved, there is no green dot near the BIS_M #1'
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(1)).click()
            self.browser.find_element(*RS_485_SettingsLocators.DISABLE(1)).click()
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
        if addr_devs > 0:
            for AL in 1, 2:
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
                assert self.is_element_present(*SystemObjectsLocators.ADDRESSABLE_DEVICE_SAVE_ICON(AL)), \
                    f'Settings not saved, there is no green dot near the addressable device #1 on loop {AL}'
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, 1)).click()
                self.browser.find_element(*AddressableLoopSettingsLocators.DISABLE(AL, 1)).click()
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
        self.save_settings()
        self.restore_settings()
        self.refresh_page()
        sleep(0.5)
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(1)).click()
            self.check_save_setting_disable(AreaSettingsLocators.DISABLE(1), f'area #{1}')
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(1)).click()
            self.check_save_setting_disable(InputLinkSettingsLocators.DISABLE(1), f'inputlink #{1}')
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(1)).click()
            self.check_save_setting_disable(OutputLinkSettingsLocators.DISABLE(1), f'outputlink #{1}')
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(1)).click()
            self.check_save_setting_disable(RS_485_SettingsLocators.DISABLE(1), f'RS-485 #{1}')
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
        if addr_devs > 0:
            for AL in 1, 2:
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, 1)).click()
                self.check_save_setting_disable(AddressableLoopSettingsLocators.DISABLE(AL, 1),
                                                f'addressable device #{1} on loop {AL}')
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
        

# Проверка кнопки "восстановить"
    def restore_settings(self):
        self.browser.find_element(*MainPanelLocators.RESTORE_BUTTON).click()
        assert self.is_not_element_present(*MainPanelLocators.RESTORE_MESSAGE, 10), \
            'restore message did not disappear in 10 seconds'

    def should_not_be_areas_settings(self, areas):
        logger.info(f'Checking default settings in {areas} areas...')
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Раскрыть Зоны
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
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Закрыть Зоны

    def should_not_be_inputlinks_settings(self, inlinks):
        logger.info(f'Checking default settings in {inlinks} inputlinks...')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Раскрыть ТС входы
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
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
    
    def should_not_be_outputlinks_settings(self, outlinks):
        logger.info(f'Checking default settings in {outlinks} outputlinks...')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Раскрыть ТС выходы
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
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
        
    def should_not_be_BIS_Ms_settings(self, BIS_Ms):
        logger.info(f'Checking default settings in {BIS_Ms} BIS_Ms...')
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Раскрыть RS-485
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
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
    
    def should_not_be_addressable_devices_settings(self, AL, addr_devs):
        logger.info(f'Checking default settings in {addr_devs} addressable devices in addressable loop {AL}...')
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
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
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()


# Полная перезапись настроек ранее добавленных объектов
    def select_in_list(self, locator, item):  # Выбрать пункт в настройке с выпадающим списком
        self.browser.find_element(*locator).click()
        self.browser.find_element(*SystemObjectsLocators.DROP_DOWN_LIST(item)).click()
    
    def move_element(self, device, link):  # Перемещает device в поле link
        self.browser.execute_script('arguments[0].scrollIntoView(true);', device)  # Прокрутить до элемента
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

    def rewrite_areas_settings(self, areas):
        logger.info(f'Rewrite settings in {areas} areas...')
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Раскрыть Зоны
        for area_num in range(1, areas):  # У каждой Зоны Пожаротушения изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(area_num)).click()
            self.browser.execute_script("scrollBy(0, -1000);")  # Прокрутка страницы вверх
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
            self.browser.find_element(*AreaSettingsLocators.RETRY_DELAY(area_num)).send_keys(123456)
            self.select_in_list(AreaSettingsLocators.LAUNCH_ALGORITHM_ARROW(area_num), 4)
            self.browser.find_element(*AreaSettingsLocators.RESET_DELAY(area_num)).send_keys(123456)
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()  # Закрыть Зоны
    
    def rewrite_inputlinks_settings(self, inlinks, areas, addr_devs):
        logger.info(f'Rewrite settings in {inlinks} inputlinks...')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Раскрыть ТС входы
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()
        for num in range(1, inlinks + 1):  # У каждого ТС входа изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num)).click()
            if num <= addr_devs:
                link = self.browser.find_element(*InputLinkSettingsLocators.UNIT_ID(num))
                assert self.is_element_present(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num)), \
                    f'Addressable device #{num} for inputlink #{num} not found'
                device = self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num))
                self.move_element(device, link)
            elif num == addr_devs + 1:
                logger.warning(f'Not enough addressable devices for inputlinks, total devices: {addr_devs}')
            if areas > 0:
                self.select_in_list(InputLinkSettingsLocators.PARENT_AREA(num), areas)
            elif num == 1:
                logger.warning('There is no one area for inputlinks')
            self.browser.find_element(*InputLinkSettingsLocators.DISABLE(num)).click()
            if num % 6 == 5:  # Тип ТС входа - вход команд
                self.select_in_list(InputLinkSettingsLocators.COMMAND_ARROW(num), 17)
            if num % 6 == 0:  # Тип ТС входа - вход технический
                self.browser.find_element(*InputLinkSettingsLocators.CHANNEL(num)).send_keys(1234)
                self.browser.find_element(*InputLinkSettingsLocators.FIX(num)).click()
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()
      
    def rewrite_outputlinks_settings(self, outlinks, areas, BIS_Ms):
        logger.info(f'Rewrite settings in {outlinks} outputlinks...')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Раскрыть ТС выходы
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Раскрыть RS-485
        BIS_num = 1
        for num in range(1, outlinks + 1):
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num)).click()
            if BIS_num <= BIS_Ms:
                link = self.browser.find_element(*OutputLinkSettingsLocators.UNIT_ID(num))
                if BIS_num % 4 == 0: BIS_num += 1  # Если тип БИС-Ма - ТИ, то пропускаем его
                assert self.is_element_present(*SystemObjectsLocators.RS_485_ITEMS(BIS_num)), \
                    f'BIS-M #{BIS_num} for outputlink #{num} not found'
                BIS_m = self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(BIS_num))
                self.move_element(BIS_m, link)
                BIS_num += 1
            elif BIS_num == BIS_Ms + 1:
                logger.warning(f'Not enough BIS_Ms for outputlinks, total BIS_Ms: {BIS_Ms}')
                BIS_num += 1
            if areas > 0:
                self.select_in_list(OutputLinkSettingsLocators.PARENT_AREA(num), areas)
            elif num == 1:
                logger.warning('There is no one area for inputlinks')
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
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Скрыть RS-485
    
    def rewrite_BIS_Ms_settings(self, BIS_Ms):
        logger.info(f'Rewrite settings in {BIS_Ms} BIS_Ms...')
        if BIS_Ms > 0:
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
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
    
    def rewrite_addressable_devices_settings(self, AL, addr_devs):
        logger.info(f'Rewrite settings in {addr_devs} addressable devices in addressable loop {AL}...')
        if addr_devs > 0:
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
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()

# Проверка полной перезаписи настроек
    def value_check(self, locator, expected_value, set_name, object_name):  # Проверка значения настройки
        value = self.browser.find_element(*locator).get_attribute('value')
        assert expected_value == value, f'Value in "{set_name}" in {object_name} does not match, ' \
                                        f'expected "{expected_value}", received "{value}"'

    def checkbox_checked(self, locator, checkbox_name, object_name):  # Проверка, что чекбокс включен
        assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
            AreaSettingsLocators.CHECKBOX_CHECKED[1] + locator[1]), \
            f'Checkbox "{checkbox_name}" in {object_name} is unchecked, expected to be checked'
    
    def checkbox_unchecked(self, locator, checkbox_name, object_name):  # Проверка, что чекбокс включен
        assert self.is_not_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
            AreaSettingsLocators.CHECKBOX_CHECKED[1] + locator[1], 0.1), \
            f'Checkbox "{checkbox_name}" in {object_name} is checked, expected to be unchecked'

    def should_be_areas_settings(self, areas):
        logger.info(f'Checking settings in {areas} areas...')
        if areas > 0:
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
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()

    def should_be_inputlinks_settings(self, inlinks, areas, addr_devs):
        logger.info(f'Checking settings in {inlinks} inputlinks...')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()
        for num in range(1, inlinks + 1):  # Проверка соответствия настроек в каждом ТС входе
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num)).click()
            if num <= addr_devs:
                device_name = self.browser.find_element(
                    *SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num)).text
                self.value_check(InputLinkSettingsLocators.UNIT_ID(num),
                                device_name, 'ссылка(ИД)', f'inputlink #{num}')
            if areas > 0:
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
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1)).click()

    def should_be_outputlinks_settings(self, outlinks, areas, BIS_Ms):
        logger.info(f'Checking settings in {outlinks} outputlinks...')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
        BIS_num = 1
        for num in range(1, outlinks + 1):  # Проверка соответствия настроек в каждом ТС выходе
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num)).click()
            if BIS_num <= BIS_Ms:
                if BIS_num % 4 == 0: BIS_num += 1  # Если тип БИС-Ма - ТИ, то пропускаем его
                BIS_name = self.browser.find_element(
                    *SystemObjectsLocators.RS_485_ITEMS(BIS_num)).text
                BIS_num += 1
                self.value_check(OutputLinkSettingsLocators.UNIT_ID(num),
                                BIS_name, 'ссылка(ИД)', f'outputlink #{num}')
            if areas > 0:
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
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()
    
    def should_be_BIS_Ms_settings(self, BIS_Ms):
        logger.info(f'Checking settings in {BIS_Ms} BIS_Ms...')
        if BIS_Ms > 0:
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
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()

    def should_be_addressable_devices_settings(self, AL, addr_devs):
        logger.info(f'Checking settings in {addr_devs} addressable devices in addressable loop {AL}...')
        if addr_devs > 0:
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
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()


# Проверка кнопки "в файл"
    def click_to_file_button(self):
        logger.info(f'Click to file button')
        self.browser.find_element(*MainPanelLocators.TO_FILE_BUTTON).click()
    
    def dismiss(self):
        logger.info(f'Click on the cancel button')
        prompt = self.browser.switch_to.alert
        prompt.dismiss()

    def accept(self):
        logger.info(f'Click on the confirm button')
        prompt = self.browser.switch_to.alert
        prompt.accept()
        sleep(0.1)  # Без задержки не успевает создать файл


# Проверка кнопки "в файл для Интеллекта"
    def click_to_file_for_intellect_button(self):
        logger.info(f'Click to file for Intellect button')
        self.browser.find_element(*MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON).click()

    def delete_config_for_Intellect_file(self):
        logger.info(f'Deleting a configuration file...')
        file_path = r'C:\Users\ITV\Downloads\configintellect.json'
        assert os.path.exists(file_path), f'Configuration file for Intellect not found: "{file_path}"'
        os.remove(file_path)


# Проверка кнопки "из файла"
    def click_from_file_button(self):
        logger.info(f'Click from file button')
        self.browser.find_element(*MainPanelLocators.FROM_FILE_BUTTON).click()
        sleep(1)

    def load_configuration_from_file(self):
        logger.info(f'Loading configuration from file...')
        try:
            file_path = r'C:\Users\ITV\Downloads\config.json'
            assert os.path.exists(file_path), f'Configuration file not found: "{file_path}"'
            keyboard.write(file_path)
            keyboard.send('enter')
            sleep(0.5)
        except:  # При ошибке, закрыть диалоговое окно windows
            keyboard.press_and_release('esc')

    def delete_config_file(self):
        logger.info(f'Deleting a configuration file...')
        os.remove(r'C:\Users\ITV\Downloads\config.json')


# Проверка терминала
    def should_be_alternating_colors_in_terminal(self):
        logger.info(f'Checking alternation of colors in dark mode terminal')
        self.open_terminal()
        color1 = self.browser.find_element(*MainPanelLocators.TERMINAL_ITEMS(1)).value_of_css_property('color')
        assert '158, 158, 158' in color1, 'Color of the first message in dark mode terminal ' \
            f'is not grey: "rgba(158, 158, 158, 1)", received color: {color1}'
        color2 = self.browser.find_element(*MainPanelLocators.TERMINAL_ITEMS(2)).value_of_css_property('color')
        assert '250, 250, 250' in color2, 'Color of the second message in dark mode terminal ' \
            f'is not white: "rgba(250, 250, 250, 1)", received color: {color2}'
        self.close_terminal()
        self.browser.find_element(*MainPanelLocators.LIGHT_MODE_ICON).click()
        logger.info(f'Checking alternation of colors in light mode terminal')
        self.open_terminal()
        color1 = self.browser.find_element(*MainPanelLocators.TERMINAL_ITEMS(1)).value_of_css_property('color')
        assert '158, 158, 158' in color1, 'Color of the first message in light mode terminal ' \
            f'is not grey: "rgba(158, 158, 158, 1)", received color: {color1}'
        color2 = self.browser.find_element(*MainPanelLocators.TERMINAL_ITEMS(2)).value_of_css_property('color')
        assert '33, 33, 33' in color2, 'Color of the second message in light mode terminal ' \
            f'is not black: "rgba(33, 33, 33, 1)", received color: {color2}'
        self.close_terminal()
        self.browser.find_element(*MainPanelLocators.DARK_MODE_ICON).click()
        
    def should_be_object_creation_messages(self, areas, inlinks, outlinks, BIS_Ms, addr_devs):
        logger.info(f'Checking object creation messages in terminal when unloading')
        for num in range(1, areas + 1):  # Проверка сообщений создания Зон Пожаротушения
            assert self.is_element_present(*MainPanelLocators.CREATE_MESSAGE(
                f'Модуль#1(Области).Область#{num}(Зона Пожаротушения)')), \
                f'There is no message about creation area #{num} or there is a spelling error'
        for num in range(1, inlinks + 1):  # Проверка сообщений создания ТС входов
            type = ('вход неисправность', 'Ссылка на область', 'ИПР', 'ИП', 'вход команд', 'вход технический')
            assert self.is_element_present(*MainPanelLocators.CREATE_MESSAGE(
                f'Модуль#1(Области).ТС вход#{num}({type[num % 6 - 1]})')), 'There is no message ' \
                f'about creation input link #{num} "{type[num % 6 - 1]}" or there is a spelling error'
        for num in range(1, outlinks + 1):  # Проверка сообщений создания ТС выходов
            type = ('индикатор', 'направление на БИСМ2', 'выход на реле')
            assert self.is_element_present(*MainPanelLocators.CREATE_MESSAGE(
                f'Модуль#1(Области).ТС выход#{num}({type[num % 3 - 1]})')), 'There is no message ' \
                f'about creation output link #{num} "{type[num % 3 - 1]}" or there is a spelling error'
        for num in range(1, BIS_Ms + 1):  # Проверка сообщений создания БИСМов
            type = ('БИС-М', 'БИС-М2', 'БИС-М3', 'ТИ')
            assert self.is_element_present(*MainPanelLocators.CREATE_MESSAGE(
                f'Модуль#2(Выходы).RS-485#{num}({type[num % 4 - 1]})')), 'There is no message ' \
                f'about creation BIS-M #{num} "{type[num % 4 - 1]}" or there is a spelling error'
        for AL in 1, 2:  # Проверка сообщений создания АУ
            for num in range(1, addr_devs + 1):
                type = ('АМК', 'АР1', 'АР-5', 'АРмини', 'АТИ', 'АхДПИ', 'ИР', 
                        'ИСМ1', 'ИСМ2', 'ИСМ4', 'ИСМ5', 'МКЗ', 'ОСЗ')
                assert self.is_element_present(*MainPanelLocators.CREATE_MESSAGE(
                    f'Модуль#3(Адресные шлейфы).АШ#{AL}.Адресные устройства#{num}({type[num % 13 - 1]})')), \
                    f'There is no message about creation addressable device #{num} ' \
                    f'"{type[num % 13 - 1]}" on loop {AL} or there is a spelling error'

    def clearing_ppk(self):
        self.open_terminal()
        self.open_ppk_objects()
        for module in ('Модуль#3 Адресные шлейфы', 3), ('Модуль#2 Выходы', 2), ('Модуль#1 Области', 1):
            logger.info(f'Clearing module {module[1]}...')
            self.browser.find_element(*SystemObjectsLocators.MODULE_FORM(module[1])).click()
            self.browser.find_element(*SystemObjectsLocators.CLEAR_MODULE_BUTTON).click()
            assert self.is_element_visible(*MainPanelLocators.MODULE_CLEANING_MESSAGE(
                module[0]), 10), 'There is no message about cleaning module 3'
            

# Проверка журнала
    def check_column_name(self, num, expected_name):
        column_text = self.browser.find_element(*EventLogLocators.NAME_COLUMN(num)).text
        assert column_text == expected_name, \
            f'{num} column is not called "{expected_name}", received text: {column_text}'

    def check_column_names(self):
        logger.info('Checking column names in event log...')
        self.browser.find_element(*MainPanelLocators.EVENT_LOG_BUTTON).click()
        self.check_column_name(1, 'Дата и время')
        self.check_column_name(2, 'Событие')
        self.check_column_name(3, 'Адрес')
        self.check_column_name(4, '№ Область')
    
    def check_button_to_display_number_of_events(self):
        logger.info('Checking the button to display number of events...')
        events_on_page = self.browser.find_element(*EventLogLocators.EVENTS_NUMBER)  
        events_on_page.click()
        self.browser.find_element(*EventLogLocators.EVENTS_100).click()
        assert events_on_page.text == '100', \
            f'Number of events displayed is not 100, received: {events_on_page.text}'
        assert self.is_element_visible(*EventLogLocators.DATE_TIME, 10), \
            'First message did not appear in 10 seconds'
        
    def check_value_of_columns(self, ppk_num):
        logger.info('Checking value of columns and date and time format...')
        try:
            first_date_time = datetime.strptime(
                self.browser.find_element(*EventLogLocators.DATE_TIME).text, '%Y.%m.%d %H:%M:%S')
        except ValueError:
            assert False, 'String does not match the date and time format'
        date = first_date_time.strftime('%Y.%m.%d')
        actually_date = datetime.now().strftime('%Y.%m.%d')
        assert date == actually_date, \
            f'Date of the first event does not match "{actually_date}", received date: {date}'
        event_value = self.browser.find_element(*EventLogLocators.EVENT).text
        assert event_value == '-', f'Event value does not match, expected: "-", received: {event_value}'
        address_value = self.browser.find_element(*EventLogLocators.ADDRESS).text
        assert address_value == f'#{ppk_num}.1', \
            f'Address value does not match, expected: "#{ppk_num}.1", received: {address_value}'
        area_value = self.browser.find_element(*EventLogLocators.AREA).text
        assert area_value == '-', f'Area value does not match, expected: "-", received: {area_value}'
    
    def check_colors_of_the_button(self):
        logger.info('Checking colors of the event log button ...')
        event_log_button = self.browser.find_element(*MainPanelLocators.EVENT_LOG_BUTTON)
        color = event_log_button.value_of_css_property('background-color')  # Проверка цветов кнопки
        assert '147, 147, 147' or '158, 158, 158' in color, \
            f'Event log button background color is not grey, received color: {color}'
        event_log_button.click()
        self.browser.find_element(*MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON).click()  # Для отжатия
        sleep(0.5)
        color = event_log_button.value_of_css_property('background-color')
        assert '0, 0, 0' in color, 'Event log button background color is not black: ' \
            f'"rgba(0, 0, 0, 0)", received color: {color}'