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
        assert self.is_element_present(locator), \
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
        assert self.is_element_clickable(MainPanelLocators.LOGO), 'Logo is not clickable'
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого

    def open_terminal(self, ppk=1):
        sleep(0.3)  # f
        if ppk > 1 and not self.is_element_visible(SystemObjectsLocators.PPK_R_FORM(2)):
            self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()
        self.browser.find_element(*MainPanelLocators.TERMINAL_BUTTON).click()
        assert self.is_element_present(MainPanelLocators.TERMINAL_FORM), \
            'Terminal does not open'

    def close_terminal(self):
        sleep(1)
        self.browser.find_element(*MainPanelLocators.CLOSE_TERMINAL_ARROW).click()
        assert self.is_element_present(MainPanelLocators.CLOSE_TERMINAL_ARROW), \
            'Terminal does not close'

    def open_ppk_objects(self, ppk):
        self.browser.find_element(*SystemObjectsLocators.PPK_R_ARROW(ppk)).click()

    def close_ppk_objects(self, ppk_num):
        self.browser.find_element(*SystemObjectsLocators.PPK_R_ARROW(ppk_num)).click()

    def open_module_objects(self, module_num, ppk):
        self.browser.find_element(*SystemObjectsLocators.MODULE_ARROW(module_num, ppk)).click()

    def close_expanded_tabs(self):  # Закрыть все вкладки
        self.browser.find_element(*MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON).click()

    def save_settings(self):
        self.button_should_be_clickable(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')
        self.browser.find_element(*MainPanelLocators.SAVE_BUTTON).click()
    
    def button_should_be_clickable(self, locator, button):
        assert self.is_element_clickable(locator), f'Button "{button}" is not clickable'

    def expand_all_objects(self, ppk):
        self.open_module_objects(1, ppk)
        self.open_module_objects(2, ppk)
        self.open_module_objects(3, ppk)
        self.open_ADDRESSABLE_LOOP(1, ppk)
        self.open_ADDRESSABLE_LOOP(2, ppk)


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
        assert self.is_element_present(MainPanelLocators.LOGO), 'Logo is not presented'
        assert self.is_element_visible(MainPanelLocators.LOGO), 'Logo is not displayed'
    
    def page_should_refresh_when_click_logo(self):  # Обновляется ли страница при клике на лого?
        self.close_expanded_tabs()  # Закрыть все вкладки
        self.browser.find_element(*SystemObjectsLocators.SYSTEM_ARROW).click()  # Скрываем объекты
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого
        assert self.is_element_visible(SystemObjectsLocators.PPK_R_FORM(1)), \
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
        assert self.is_element_present(MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON), \
            'Button "В Файл для Интеллекта" is not presented'

    def should_be_from_file_button(self):
        self.presence_and_spelling(MainPanelLocators.FROM_FILE_BUTTON, 'ИЗ ФАЙЛА')
    
    def should_be_event_log_button(self):
        self.presence_and_spelling(MainPanelLocators.EVENT_LOG_BUTTON, 'ЖУРНАЛ')
        
    def should_be_terminal_button(self):
        self.presence_and_spelling(MainPanelLocators.TERMINAL_BUTTON, 'ТЕРМИНАЛ')

    def should_be_light_mode_icon(self):
        logger.info('Checking the light mode icon...')
        assert self.is_element_present(MainPanelLocators.LIGHT_MODE_ICON), \
            'Icon "Light Mode" is not presented'


# Проверка статуса подключения
    def should_be_online_mark(self):
        logger.info('Checking online status...')
        assert self.is_element_visible(MainPanelLocators.ONLINE_MARK), \
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
        assert self.is_element_present(MainPanelLocators.OFFLINE_MARK), \
            'Offline mark is not presented'
    
    def status_should_be_offline(self):
        status = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).text
        assert status == 'offline', f'Connection status not "offline", status: {status}'

    def online_mark_color_should_be_yellow(self):
        color = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).value_of_css_property('color')
        assert '255, 215, 64' in color, \
            f'Connection status color is not yellow: "rgba(255, 215, 64, 1)", received color: {color}'


# Проверка кнопки В ППК с открытым Терминалом
    def recording_setting_for_module(self, module_num, ppk):  # Модуль Области стал активным
        self.browser.find_element(*SystemObjectsLocators.MODULE_FORM(module_num, ppk)).click()
        assert self.is_element_clickable(MainPanelLocators.TO_PPK_BUTTON), \
            'Button "В ППК" is not clickable'
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК
        assert self.is_element_present(MainPanelLocators.TO_PPK_BUTTON_IS_BLINKING), \
            'Button "В ППК" does not blink'

    def check_record(self, ppk, module='', timeout=30):
        start_time = time()
        assert self.is_element_present(SystemObjectsLocators.RECORD_START(ppk, module)), \
            f'Recording for {f'PPK#{ppk}' if module == '' else f'PPK#{ppk} {module}'} has not started'
        assert self.is_element_visible(SystemObjectsLocators.RECORD_FINISH, max(timeout, 10)), \
            f'Recording for {'PPK#{ppk}' if module == '' else f'PPK#{ppk} {module}'} has not finished, ' \
            f'time spent: {time() - start_time:.2f}'
        logger.success(f'Record to {'PPK#{ppk}' if module == '' else f'PPK#{ppk} {module}'} was successful, ' \
                    f'time spent: {time() - start_time:.2f}')


# Проверка кнопки ИЗ ППК
    def unload_settings(self):
        logger.info(f'Checking unloading settings from all ppk...')
        sleep(1)
        button = self.browser.find_element(*MainPanelLocators.FROM_PPK_BUTTON)
        button.click()
        if '250, 250, 250' in button.value_of_css_property('color'):  # Темная тема
            sleep(1)
            assert self.is_element_present(MainPanelLocators.FROM_PPK_BUTTON_IS_BLINKING_DARK), \
            'Button "ИЗ ППК" does not blink'
        else:
            assert self.is_element_present(MainPanelLocators.FROM_PPK_BUTTON_IS_BLINKING_LIGHT), \
            'Button "ИЗ ППК" does not blink'

    def check_unload(self, m1_wait, m2_wait, m3_wait, ppk_num):
        start_time = time()
        assert self.is_element_present(SystemObjectsLocators.UNLOAD_START), \
            f'Unload for all ppkr has not started, time spent: {time() - start_time:.2f}'
        for ppk in range(1, ppk_num + 1):
            assert self.is_element_visible(SystemObjectsLocators.UNLOAD_START_MODULE(
                ppk, '1(Области)'), max(m3_wait, 30) * (1 + (ppk > 1))), \
                f'Unload for PPK#{ppk} module#1 has not started, time spent: {time() - start_time:.2f}'
            assert self.is_element_visible(SystemObjectsLocators.UNLOAD_START_MODULE(
                ppk, '2(Выходы)'), max(m1_wait, 30) * (1 + (ppk > 1))), \
                f'Unload for PPK#{ppk} module#2 has not started, time spent: {time() - start_time:.2f}'
            assert self.is_element_visible(SystemObjectsLocators.UNLOAD_START_MODULE(
                ppk, '3(Адресные шлейфы)'), max(m2_wait, 30) * (1 + (ppk > 1))), \
                f'Unload for PPK#{ppk} module#3 has not started, time spent: {time() - start_time:.2f}'
        assert self.is_element_visible(SystemObjectsLocators.UNLOAD_FINISH, 
            max(m3_wait, 30) * (1 + (ppk_num > 1))), \
            f'Unload for all ppkr has not finished, time spent: {time() - start_time:.2f}'
        logger.success(f'Unload from all ppk was successful, time spent: {time() - start_time:.2f}')


# Полная запись в ППК
    def add_areas(self, areas, ppk):
        logger.info(f'Creating {areas} areas on PPK#{ppk}...')
        for _ in range(areas):  # Создать Зоны пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ADD_ICON(ppk)).click()

    def add_inputlink(self, inlinks, ppk):
        logger.info(f'Creating {inlinks} inputlinks on PPK#{ppk}...')
        if inlinks > 0:
            for i in range(inlinks):  # Создать ТС входы
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ADD_ICON(ppk)).click()
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()  # Список входов
            for i in range(inlinks):  # Сделать ТС входы каждого типа
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(i + 1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                sleep(0.1)
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 6 + 1)).click()  # Изменить тип входа
                self.is_not_element_present(SystemObjectsLocators.UNIT_MENU_CONFIG)  # f
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()

    def add_ouputlink(self, outlinks, ppk):
        logger.info(f'Creating {outlinks} outputlinks on PPK#{ppk}...')
        if outlinks > 0:
            for i in range(outlinks):  # Создать ТС выходы
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ADD_ICON(ppk)).click()
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()  # Список выходов
            for i in range(outlinks):  # Сделать ТС выходы каждого типа
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(i + 1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                sleep(0.1)
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 3 + 1)).click()  # Изменить тип выхода
                self.is_not_element_present(SystemObjectsLocators.UNIT_MENU_CONFIG)  # f
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
    
    def add_BIS_M(self, BIS_Ms, ppk):
        logger.info(f'Creating {BIS_Ms} BIS M on PPK#{ppk}...')
        if BIS_Ms > 0:
            for i in range(BIS_Ms):  # Создать БИС-Мы
                self.browser.find_element(*SystemObjectsLocators.RS_485_ADD_ICON(ppk)).click()
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()  # Список БИС-М
            for i in range(BIS_Ms):  # Сделать БИС-Мы каждого типа
                self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(i + 1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                sleep(0.1)
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 4 + 1)).click()  # Изменить тип выхода
                self.is_not_element_present(SystemObjectsLocators.UNIT_MENU_CONFIG)  # f
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
    
    def open_ADDRESSABLE_LOOP(self, AL, ppk):
        assert self.is_element_clickable(SystemObjectsLocators.ADDRESSABLE_LOOP(ppk, AL)), \
            f'Addressable loop arrow on PPK#{ppk} is not clickable'
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_LOOP(ppk, AL)).click()

    def add_addressable_devices(self, AL, addr_devs, ppk):
        logger.info(f'Creating {addr_devs} addressable devices on addressable loop {AL} on PPK#{ppk}...')
        if addr_devs > 0:
            for i in range(addr_devs):  # Создать АУ
                self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL, ppk)).click()
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
            for i in range(addr_devs):  # Сделать АУ каждого типа
                self.browser.find_element(
                    *SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, i + 1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
                sleep(0.2)
                self.browser.find_element(*SystemObjectsLocators.TYPES(i % 13 + 1)).click()  # Изменить тип выхода
                self.is_not_element_present(SystemObjectsLocators.UNIT_MENU_CONFIG)  # f
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()


# Проверка полной выгрузки из ППК
    def check_number_of_areas(self, areas, ppk):
        logger.info(f'Checking number of areas on PPK#{ppk} ...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_AREAS(ppk)).text
        assert str(areas) == count, f'Number of areas on PPK#{ppk} is not equal {areas}, number = {count}'

    def check_number_of_inputlink(self, inlinks, ppk):
        logger.info(f'Checking number of inlinks on PPK#{ppk}...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_INPUTLINK(ppk)).text
        assert str(inlinks) == count, f'Number of inputlinks on PPK#{ppk} is not equal {inlinks}, number = {count}'

    def check_number_of_outputlink(self, outlinks, ppk):
        logger.info(f'Checking number of outlinks on PPK#{ppk}...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_OUTPUTLINK(ppk)).text
        assert str(outlinks) == count, f'Number of outputlinks on PPK#{ppk} is not equal {outlinks}, number = {count}'

    def check_number_of_BIS_M(self, BIS_Ms, ppk):
        logger.info(f'Checking number of BIS_Ms on PPK#{ppk}...')
        count = self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_RS_485(ppk)).text
        assert str(BIS_Ms) == count, f'Number of RS-485 devices on PPK#{ppk} is not equal {BIS_Ms}, number = {count}'

    def check_number_of_addressable_devices(self, AL, addr_devs, ppk):
        logger.info(f'Checking number of addr_devs on loop {AL} on PPK#{ppk}...')
        count = self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL, ppk)).text
        assert str(addr_devs) == count, \
            f'Number of addressable_devices on loop {AL} on PPK#{ppk} is not equal {addr_devs}, number = {count}'

    
# Проверка кнопки "Сохранить"
    def check_save_setting_disable(self, locator, object_name, ppk):  # Проверка, что чекбокс включен
        assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED(locator[1])), \
            f'Checkbox "отключен" in PPK#{ppk} {object_name} was not saved'
    
    def check_save_settings(self, areas, inlinks, outlinks, BIS_Ms, addr_devs, ppk_num):
        logger.info('Checking save settings...')
        self.button_should_be_clickable(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')
        self.save_settings()
        for ppk in range(1, ppk_num + 1):
            self.open_ppk_objects(ppk)
            self.expand_all_objects(ppk)
            if areas > 0:
                self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()  # Раскрыть Зоны
                assert self.is_element_present(SystemObjectsLocators.AREA_SAVE_ICON(ppk)), \
                    f'Settings not saved, there is no green dot near the PPK#{ppk} area#1'  # Проверка появления зеленой точки   
                self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(1, ppk)).click()
                self.browser.find_element(*AreaSettingsLocators.DISABLE(1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()  # Закрыть Зоны
            if inlinks > 0:
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()  # Раскрыть ТС входы
                assert self.is_element_present(SystemObjectsLocators.INPUTLINK_SAVE_ICON(ppk)), \
                    f'Settings not saved, there is no green dot near the PPK#{ppk} inputlink#1'
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(1, ppk)).click()
                self.browser.find_element(*InputLinkSettingsLocators.DISABLE(1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()
            if outlinks > 0:
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()  # Раскрыть ТС выходы
                assert self.is_element_present(SystemObjectsLocators.OUTPUTLINK_SAVE_ICON(ppk)), \
                    f'Settings not saved, there is no green dot near the PPK#{ppk} outputlink#1'
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(1, ppk)).click()
                self.browser.find_element(*OutputLinkSettingsLocators.DISABLE(1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
            if BIS_Ms > 0:
                self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()  # Раскрыть RS-485
                assert self.is_element_present(SystemObjectsLocators.BIS_M_SAVE_ICON(ppk)), \
                    f'Settings not saved, there is no green dot near the PPK#{ppk} BIS_M#1'
                self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(1, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.DISABLE(1, ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
            if addr_devs > 0:
                for AL in 1, 2:
                    self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
                    assert self.is_element_present(SystemObjectsLocators.ADDRESSABLE_DEVICE_SAVE_ICON(AL, ppk)), \
                        'Settings not saved, there is no green dot ' \
                        f'near the addressable device #1 on loop {AL} on PPK#{ppk}'
                    self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, 1, ppk)).click()
                    self.browser.find_element(*AddressableLoopSettingsLocators.DISABLE(AL, 1, ppk)).click()
                    self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
            self.close_ppk_objects(ppk)
        self.save_settings()
        self.restore_settings()
        self.refresh_page()
        sleep(0.5)
        for ppk in range(1, ppk_num + 1):
            self.open_ppk_objects(ppk)
            self.expand_all_objects(ppk)
            if areas > 0:
                self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(1, ppk)).click()
                self.check_save_setting_disable(AreaSettingsLocators.DISABLE(1, ppk), 'area#1', ppk)
                self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()
            if inlinks > 0:
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(1, ppk)).click()
                self.check_save_setting_disable(InputLinkSettingsLocators.DISABLE(1, ppk), 'inputlink#1', ppk)
                self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()
            if outlinks > 0:
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(1, ppk)).click()
                self.check_save_setting_disable(OutputLinkSettingsLocators.DISABLE(1, ppk), 'outputlink#1', ppk)
                self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
            if BIS_Ms > 0:
                self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
                self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(1, ppk)).click()
                self.check_save_setting_disable(RS_485_SettingsLocators.DISABLE(1, ppk), 'RS-485#1', ppk)
                self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
            if addr_devs > 0:
                for AL in 1, 2:
                    self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
                    self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, 1, ppk)).click()
                    self.check_save_setting_disable(AddressableLoopSettingsLocators.DISABLE(AL, 1, ppk),
                                                    f'addressable device#1 on loop {AL}', ppk)
                    self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
            self.close_ppk_objects(ppk)
        

# Проверка кнопки "восстановить"
    def restore_settings(self):
        self.browser.find_element(*MainPanelLocators.RESTORE_BUTTON).click()
        sleep(0.1)
        assert self.is_not_element_present(MainPanelLocators.RESTORE_MESSAGE, 10), \
            'restore message did not disappear in 10 seconds'

    def should_not_be_areas_settings(self, areas, ppk):
        logger.info(f'Checking default settings in {areas} areas...')
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()  # Раскрыть Зоны
        for num in range(1, areas):  # Проверка соответствия настроек в каждой Зоне Пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(num, ppk)).click()
            self.value_check(AreaSettingsLocators.ENTERS_THE_AREA(num, ppk),
                             '', 'входит в область', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.DISABLE(num, ppk), 'отключен', f'area #{num}')
            self.value_check(AreaSettingsLocators.DELAY_IN_EVACUATION(num, ppk),
                             '0', 'задержка эвакуации', f'area #{num}')
            self.value_check(AreaSettingsLocators.EXTINGUISHING_START_TIME(num, ppk),
                             '0', 'время пуска тушения', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.EXTINGUISHING(num, ppk),
                                    'есть пожаротушение', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.GAS_OUTPUT_SIGNAL(num, ppk),
                                    'требуется сигнал выхода газа', f'area #{num}')
            self.value_check(AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR(num, ppk),
                             'нет', 'взаимно исключает ДУ', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.EXTINGUISHING_BY_MFA(num, ppk),
                                    'тушение по ИПР', f'area #{num}')
            self.checkbox_unchecked(AreaSettingsLocators.FORWARD_IN_RING(num, ppk), 
                                    'пересылать по кольцу', f'area #{num}')
            self.value_check(AreaSettingsLocators.RETRY_DELAY(num, ppk),
                             '60', 'задержка перезапроса', f'area #{num}')
            self.value_check(AreaSettingsLocators.LAUNCH_ALGORITHM(num, ppk),
                             'B (перезапрос)', 'алгоритм ЗКПС', f'area #{num}')                
            self.value_check(AreaSettingsLocators.RESET_DELAY(num, ppk),
                             '25', 'задержка сброса', f'area #{num}')
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()  # Закрыть Зоны

    def should_not_be_inputlinks_settings(self, inlinks, ppk):
        logger.info(f'Checking default settings in {inlinks} inputlinks...')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()  # Раскрыть ТС входы
        for num in range(1, inlinks + 1):  # Проверка соответствия настроек в каждом ТС входе
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num, ppk)).click()
            self.value_check(InputLinkSettingsLocators.UNIT_ID(num, ppk),
                             '', 'ссылка(ИД)', f'inputlink #{num}')
            self.value_check(InputLinkSettingsLocators.PARENT_AREA(num, ppk),
                             '', 'входит в область', f'inputlink #{num}')
            self.checkbox_unchecked(InputLinkSettingsLocators.DISABLE(num, ppk), 
                                    'отключен', f'inputlink #{num}')
            if num % 6 == 5:  # Тип ТС входа - вход команд
                self.value_check(InputLinkSettingsLocators.COMMAND(num, ppk),
                                 'сброс', 'команда', f'inputlink #{num}')
            if num % 6 == 0:  # Тип ТС входа - вход технический
                self.value_check(InputLinkSettingsLocators.CHANNEL(num, ppk),
                                 '0', 'канал', f'inputlink #{num}')
                self.checkbox_unchecked(InputLinkSettingsLocators.FIX(num, ppk),
                                        'фиксировать', f'inputlink #{num}')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()
    
    def should_not_be_outputlinks_settings(self, outlinks, ppk):
        logger.info(f'Checking default settings in {outlinks} outputlinks...')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()  # Раскрыть ТС выходы
        for num in range(1, outlinks + 1):  # Проверка соответствия настроек в каждом ТС выходе
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num, ppk)).click()
            self.value_check(OutputLinkSettingsLocators.UNIT_ID(num, ppk),
                             '', 'ссылка(ИД)', f'outputlink #{num}')
            self.value_check(OutputLinkSettingsLocators.PARENT_AREA(num, ppk), 
                             '', 'входит в область', f'outputlink #{num}')
            self.checkbox_unchecked(OutputLinkSettingsLocators.DISABLE(num, ppk),
                                    'отключен', f'outputlink #{num}')
            if num % 3 == 0:  # Тип ТС выхода - выход на реле
                self.value_check(OutputLinkSettingsLocators.TURN_ON_DELAY(num, ppk),
                                 '0', 'задержка включения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.TURN_OFF_DELAY(num, ppk),
                                 '0', 'задержка выключения', f'outputlink #{num}')              
                self.checkbox_unchecked(OutputLinkSettingsLocators.NO_STOP(num, ppk),
                                        'продолжать если НЕ условие', f'outputlink #{num}')
                self.checkbox_unchecked(OutputLinkSettingsLocators.NO_RESTART_DELAY_ON(num, ppk),
                                        'продолжать задержку включения при повторном', f'outputlink #{num}')
                self.checkbox_unchecked(OutputLinkSettingsLocators.NO_RESTART_DELAY_OFF(num, ppk),
                                        'продолжать задержку вЫключения при повторном', f'outputlink #{num}')
                self.checkbox_unchecked(OutputLinkSettingsLocators.SINGLE_PULSE(num, ppk),
                                        'однократный импульс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num, ppk), 
                                 'отключено', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE2(num, ppk), 
                                 'отключено', 'на ПОЖАР (пожар-2)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num, ppk), 
                                 'отключено', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FAULT(num, ppk), 
                                 'отключено', 'на неисправность', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_REPAIR(num, ppk), 
                                 'отключено', "на 'в ремонте'", f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION(num, ppk), 
                                 'отключено', 'на газ-уходи', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING(num, ppk), 
                                 'отключено', 'на пуск тушения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AFTER_EXTINGUICHING(num, ppk), 
                                 'отключено', 'на тушение закончено', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING_FAILED(num, ppk), 
                                 'отключено', 'на тушение закончено неудачно', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AUTO_OFF(num, ppk), 
                                 'отключено', 'на авт. откл', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_RESET(num, ppk), 
                                 'отключено', 'на сброс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR(num, ppk), 
                                 'отключено', 'на дверь открыта', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_BLOCKED(num, ppk), 
                                 'отключено', 'на блокировка', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION_PAUSE(num, ppk), 
                                 'отключено', 'на останов', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR_PAUSE(num, ppk), 
                                 'отключено', 'на останов по двери', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_CANCELLED(num, ppk), 
                                 'отключено', 'на отмену пуска тушения', f'outputlink #{num}')
                for tech_num in range(15):
                    self.value_check(OutputLinkSettingsLocators.ON_TECH(num, tech_num, ppk), 
                                     'отключено', f'на технический сигнал {tech_num}', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.AND_OR(num, ppk),
                                 'по ИЛИ', 'И/или', f'outputlink #{num}')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
        
    def should_not_be_BIS_Ms_settings(self, BIS_Ms, ppk):
        logger.info(f'Checking default settings in {BIS_Ms} BIS_Ms...')
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()  # Раскрыть RS-485
        for num in range(1, BIS_Ms + 1):  # Проверка соответствия настроек в каждом БИС-Ме
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(num, ppk)).click()
            self.checkbox_unchecked(RS_485_SettingsLocators.DISABLE(num, ppk), 'отключен', f'RS-485 #{num}')
            if num % 4 == 0:  # Тип RS-485 - ТИ
                self.checkbox_checked(RS_485_SettingsLocators.FIRE(num, ppk), 
                                      'ПОЖАР', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.ATTENTION(num, ppk), 
                                        'ВНИМАНИЕ', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.FAULT(num, ppk), 
                                        'НЕИСПРАВНОСТЬ', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.AUTO_OFF(num, ppk), 
                                        'автоматика ОТКЛ', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LEVEL_CONFIRM(num, ppk),
                                 '80', 'уровень ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LENGTH_CONFIRM(num, ppk),
                                 '10', 'длительность ответа', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.PULSE_DIAL(num, ppk), 
                                        'импульсный набор', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.NO_CONFIRM(num, ppk), 
                                        'не ждать ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.PHONE_NUMBER(num, ppk),
                                 '', 'номер телефона', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.ACCOUNT(num, ppk),
                                 '1000', 'аккаунт', f'RS-485 #{num}')
            else:
                if num % 4 == 3:  # Тип RS-485 - БИС-М3
                    self.checkbox_unchecked(RS_485_SettingsLocators.DEFAULT_GREEN(num, ppk), 
                                            'по умолчанию зеленые', f'RS-485 #{num}')
                    self.value_check(RS_485_SettingsLocators.BACKLIGHT(num, ppk),
                                     '0', 'подсветка', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.BRIGHTNESS(num, ppk),
                                 '7', 'яркость', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.TIMEOUT(num, ppk),
                                 '20', 'таймаут нажатий', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.NO_SOUND(num, ppk), 
                                        'без звука', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.NO_ALARM_SOUND(num, ppk), 
                                        'без звука тревог', f'RS-485 #{num}')
                self.checkbox_unchecked(RS_485_SettingsLocators.KEY_SENSITIVE(num, ppk), 
                                        'чувствительность клавиш', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.DEFAULT_ID(num, ppk),
                                 '0', 'ИД по умолчанию', f'RS-485 #{num}')
            self.value_check(RS_485_SettingsLocators.SN(num, ppk),
                             str(2000 + num), 'серийный номер', f'RS-485 #{num}')
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
    
    def should_not_be_addressable_devices_settings(self, AL, addr_devs, ppk):
        logger.info(f'Checking default settings in {addr_devs} addressable devices in addressable loop {AL}...')
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
        for num in range(1, addr_devs + 1):  # У каждого АУ на указаном шлейфу изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, num, ppk)).click()
            self.checkbox_unchecked(AddressableLoopSettingsLocators.DISABLE(AL, num, ppk), 
                                    'отключен', f'addressable device #{num} on loop {AL}')
            if num % 13 == 2:  # Тип АУ - АР1
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num, ppk),
                                 'контроль линии, нет пожар2', 'режим', f'addressable device #{num} on loop {AL}')
            if num % 13 == 4:  # Тип АУ - АРмини
                self.checkbox_checked(AddressableLoopSettingsLocators.TWO_INPUTS(AL, num, ppk), 
                                      'два входа', f'addressable device #{num} on loop {AL}')
            if num % 13 == 5:  # Тип АУ - АТИ
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num, ppk),
                                 'A1', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_unchecked(AddressableLoopSettingsLocators.DIFFERENTIAL(AL, num, ppk),
                                        'дифференциальный', f'addressable device #{num} on loop {AL}')
            if num % 13 == 6:  # Тип АУ - АхДПИ
                self.value_check(AddressableLoopSettingsLocators.THRESHOLD(AL, num, ppk),
                                 '17', 'порог чувствительности', f'addressable device #{num} on loop {AL}')
                self.value_check(AddressableLoopSettingsLocators.GROUP(AL, num, ppk),
                                 '0', 'ЗКПС', f'addressable device #{num} on loop {AL}')
            if num % 13 == 10:  # Тип АУ - ИСМ4
                self.value_check(AddressableLoopSettingsLocators.MODE220(AL, num, ppk),
                                 '220v', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_unchecked(AddressableLoopSettingsLocators.MOTOR(AL, num, ppk), 
                                        'мотор с переполюсовкой', f'addressable device #{num} on loop {AL}')
            if num % 13 == 11:  # Тип АУ - ИСМ5
                self.value_check(AddressableLoopSettingsLocators.MODE24(AL, num, ppk),
                                 'любое', 'напряжение питания', f'addressable device #{num} on loop {AL}')
            self.value_check(AddressableLoopSettingsLocators.SN(AL, num, ppk),
                             str(AL * 1000 + num), 'серийный номер', f'addressable device #{num} on loop {AL}')
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()


# Полная перезапись настроек ранее добавленных объектов
    def select_in_list(self, locator, item):  # Выбрать пункт в настройке с выпадающим списком
        assert self.is_element_clickable(locator), f'Drop down list did not open: {locator[1]}'
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

    def rewrite_areas_settings(self, areas, ppk):
        logger.info(f'Rewrite settings in {areas} areas on PPK#{ppk}...')
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()  # Раскрыть Зоны
        for area_num in range(1, areas):  # У каждой Зоны Пожаротушения изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(area_num, ppk)).click()
            self.browser.execute_script("scrollBy(0, -1000);")  # Прокрутка страницы вверх
            self.select_in_list(AreaSettingsLocators.ENTERS_THE_AREA(area_num, ppk), areas - 1)
            self.browser.find_element(*AreaSettingsLocators.DISABLE(area_num, ppk)).click()
            self.browser.find_element(*AreaSettingsLocators.DELAY_IN_EVACUATION(area_num, ppk)
                                      ).send_keys(123456)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING_START_TIME(area_num, ppk)
                                      ).send_keys(123456)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING(area_num, ppk)).click()
            self.browser.find_element(*AreaSettingsLocators.GAS_OUTPUT_SIGNAL(area_num, ppk)).click()
            self.select_in_list(AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR_ARROW(area_num, ppk), 5)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING_BY_MFA(area_num, ppk)).click()
            self.browser.find_element(*AreaSettingsLocators.FORWARD_IN_RING(area_num, ppk)).click()
            self.browser.find_element(*AreaSettingsLocators.RETRY_DELAY(area_num, ppk)).send_keys(123456)
            self.select_in_list(AreaSettingsLocators.LAUNCH_ALGORITHM_ARROW(area_num, ppk), 4)
            self.browser.find_element(*AreaSettingsLocators.RESET_DELAY(area_num, ppk)).send_keys(123456)
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()  # Закрыть Зоны
    
    def rewrite_inputlinks_settings(self, inlinks, areas, addr_devs, ppk):
        logger.info(f'Rewrite settings in {inlinks} inputlinks on PPK#{ppk}...')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()  # Раскрыть ТС входы
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1, ppk)).click()
        for num in range(1, inlinks + 1):  # У каждого ТС входа изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num, ppk)).click()
            if num <= addr_devs:
                link = self.browser.find_element(*InputLinkSettingsLocators.UNIT_ID(num, ppk))
                assert self.is_element_present(SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num, ppk)), \
                    f'Addressable device #{num} for inputlink #{num} not found'
                device = self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num, ppk))
                self.move_element(device, link)
            elif num == addr_devs + 1:
                logger.warning(f'Not enough addressable devices for inputlinks, total devices: {addr_devs}')
            if areas > 0:
                self.select_in_list(InputLinkSettingsLocators.PARENT_AREA(num, ppk), areas)
            elif num == 1:
                logger.warning('There is no one area for inputlinks')
            self.browser.find_element(*InputLinkSettingsLocators.DISABLE(num, ppk)).click()
            if num % 6 == 5:  # Тип ТС входа - вход команд
                self.select_in_list(InputLinkSettingsLocators.COMMAND_ARROW(num, ppk), 17)
            if num % 6 == 0:  # Тип ТС входа - вход технический
                self.browser.find_element(*InputLinkSettingsLocators.CHANNEL(num, ppk)).send_keys(1234)
                self.browser.find_element(*InputLinkSettingsLocators.FIX(num, ppk)).click()
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1, ppk)).click()
      
    def rewrite_outputlinks_settings(self, outlinks, areas, BIS_Ms, ppk):
        logger.info(f'Rewrite settings in {outlinks} outputlinks on PPK#{ppk}...')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()  # Раскрыть ТС выходы
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()  # Раскрыть RS-485
        BIS_num = 1
        for num in range(1, outlinks + 1):
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num, ppk)).click()
            if BIS_num <= BIS_Ms:
                link = self.browser.find_element(*OutputLinkSettingsLocators.UNIT_ID(num, ppk))
                if BIS_num % 4 == 0: BIS_num += 1  # Если тип БИС-Ма - ТИ, то пропускаем его
                assert self.is_element_present(SystemObjectsLocators.RS_485_ITEMS(BIS_num, ppk)), \
                    f'BIS-M #{BIS_num} for outputlink #{num} not found'
                BIS_m = self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(BIS_num, ppk))
                self.move_element(BIS_m, link)
                BIS_num += 1
            elif BIS_num == BIS_Ms + 1:
                logger.warning(f'Not enough BIS_Ms for outputlinks, total BIS_Ms: {BIS_Ms}')
                BIS_num += 1
            if areas > 0:
                self.select_in_list(OutputLinkSettingsLocators.PARENT_AREA(num, ppk), areas)
            elif num == 1:
                logger.warning('There is no one area for inputlinks')
            self.browser.find_element(*OutputLinkSettingsLocators.DISABLE(num, ppk)).click()
            if num % 3 == 0:  # Тип ТС выхода - выход на реле
                self.browser.find_element(*OutputLinkSettingsLocators.TURN_ON_DELAY(num, ppk)).send_keys(123456)
                self.browser.find_element(*OutputLinkSettingsLocators.TURN_OFF_DELAY(num, ppk)).send_keys(123456)
                self.browser.find_element(*OutputLinkSettingsLocators.NO_STOP(num, ppk)).click()
                self.browser.find_element(*OutputLinkSettingsLocators.NO_RESTART_DELAY_ON(num, ppk)).click()
                self.browser.find_element(*OutputLinkSettingsLocators.NO_RESTART_DELAY_OFF(num, ppk)).click()
                self.browser.find_element(*OutputLinkSettingsLocators.SINGLE_PULSE(num, ppk)).click()
                self.select_in_list(OutputLinkSettingsLocators.ON_FIRE1_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_FIRE2_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_FAULT_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_REPAIR_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EVACUATION_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EXTINGUICHING_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_AFTER_EXTINGUICHING_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EXTINGUICHING_FAILED_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_AUTO_OFF_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_RESET_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_DOOR_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_BLOCKED_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_EVACUATION_PAUSE_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_DOOR_PAUSE_ARROW(num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.ON_CANCELLED_ARROW(num, ppk), 3)
                for tech_num in range(15):
                    self.select_in_list(OutputLinkSettingsLocators.ON_TECH_ARROW(num, tech_num, ppk), 3)
                self.select_in_list(OutputLinkSettingsLocators.AND_OR_ARROW(num, ppk), 2)
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()  # Скрыть RS-485
    
    def rewrite_BIS_Ms_settings(self, BIS_Ms, ppk):
        logger.info(f'Rewrite settings in {BIS_Ms} BIS_Ms on PPK#{ppk}...')
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()  # Раскрыть RS-485
        for num in range(1, BIS_Ms + 1):  # У каждого БИС-Ма изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(num, ppk)).click()
            self.browser.execute_script("scrollBy(0, -1000);")  # Прокрутка страницы вверх
            self.browser.find_element(*RS_485_SettingsLocators.DISABLE(num, ppk)).click()
            if num % 4 == 0:  # Тип RS-485 - ТИ
                self.browser.find_element(*RS_485_SettingsLocators.FIRE(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.ATTENTION(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.FAULT(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.AUTO_OFF(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.LEVEL_CONFIRM(num, ppk)).send_keys(12345)
                self.browser.find_element(*RS_485_SettingsLocators.LENGTH_CONFIRM(num, ppk)).send_keys(123)
                self.browser.find_element(*RS_485_SettingsLocators.PULSE_DIAL(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.NO_CONFIRM(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.PHONE_NUMBER(num, ppk)
                                          ).send_keys(1234567890123456)
                self.browser.find_element(*RS_485_SettingsLocators.ACCOUNT(num, ppk)).send_keys(12345)
            else:
                if num % 4 == 3:  # Тип RS-485 - БИС-М3
                    self.browser.find_element(*RS_485_SettingsLocators.DEFAULT_GREEN(num, ppk)).click()
                    self.browser.find_element(*RS_485_SettingsLocators.BACKLIGHT(num, ppk)).send_keys(1234)
                self.browser.find_element(*RS_485_SettingsLocators.BRIGHTNESS(num, ppk)).send_keys(123)
                self.browser.find_element(*RS_485_SettingsLocators.TIMEOUT(num, ppk)).send_keys(1234)
                self.browser.find_element(*RS_485_SettingsLocators.NO_SOUND(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.NO_ALARM_SOUND(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.KEY_SENSITIVE(num, ppk)).click()
                self.browser.find_element(*RS_485_SettingsLocators.DEFAULT_ID(num, ppk)).send_keys(12345678901)
            self.browser.find_element(*RS_485_SettingsLocators.SN(num, ppk)).send_keys('\b\b\b\b', 65536 - num)
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
    
    def rewrite_addressable_devices_settings(self, AL, addr_devs, ppk):
        logger.info(f'Rewrite settings in {addr_devs} addressable devices on loop {AL} on PPK#{ppk}...')
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
        for num in range(1, addr_devs + 1):  # У каждого АУ на указаном шлейфу изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, num, ppk)).click()
            self.browser.find_element(*AddressableLoopSettingsLocators.DISABLE(AL, num, ppk)).click()
            if num % 13 == 2:  # Тип АУ - АР1
                self.select_in_list(AddressableLoopSettingsLocators.MODE_ARROW(AL, num, ppk), 3)
            if num % 13 == 4:  # Тип АУ - АРмини
                self.browser.find_element(*AddressableLoopSettingsLocators.TWO_INPUTS(AL, num, ppk)).click()
            if num % 13 == 5:  # Тип АУ - АТИ
                self.select_in_list(AddressableLoopSettingsLocators.MODE_ARROW(AL, num, ppk), 6)
                self.browser.find_element(*AddressableLoopSettingsLocators.DIFFERENTIAL(AL, num, ppk)).click()
            if num % 13 == 6:  # Тип АУ - АхДПИ
                self.browser.find_element(*AddressableLoopSettingsLocators.THRESHOLD(AL, num, ppk)).send_keys(99)
                self.browser.find_element(*AddressableLoopSettingsLocators.GROUP(AL, num, ppk)).send_keys(1234)
            if num % 13 == 10:  # Тип АУ - ИСМ4
                self.select_in_list(AddressableLoopSettingsLocators.MODE220_ARROW(AL, num, ppk), 5)
                self.browser.find_element(*AddressableLoopSettingsLocators.MOTOR(AL, num, ppk)).click()
            if num % 13 == 11:  # Тип АУ - ИСМ5
                self.select_in_list(AddressableLoopSettingsLocators.MODE24_ARROW(AL, num, ppk), 2)
            self.browser.find_element(*AddressableLoopSettingsLocators.SN(AL, num, ppk)).send_keys(
                '\b\b\b\b', 16777216 - num - (AL - 1) * addr_devs)  # Стирает 4 символа и вставляет сн
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()

# Проверка полной перезаписи настроек
    def value_check(self, locator, expected_value, set_name, object_name):  # Проверка значения настройки
        value = self.browser.find_element(*locator).get_attribute('value')
        assert expected_value == value, f'Value in "{set_name}" in {object_name} does not match, ' \
                                        f'expected "{expected_value}", received "{value}"'

    def checkbox_checked(self, locator, checkbox_name, object_name):  # Проверка, что чекбокс включен
        assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED(locator[1])), \
            f'Checkbox "{checkbox_name}" in {object_name} is unchecked, expected to be checked'
    
    def checkbox_unchecked(self, locator, checkbox_name, object_name):  # Проверка, что чекбокс включен
        assert self.is_not_element_present(AreaSettingsLocators.CHECKBOX_CHECKED(locator[1]), 0.1), \
            f'Checkbox "{checkbox_name}" in {object_name} is checked, expected to be unchecked'

    def should_be_areas_settings(self, areas, ppk):
        logger.info(f'Checking settings in {areas} areas on PPK#{ppk}...')
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()
        for num in range(1, areas):  # Проверка соответствия настроек в каждой Зоне Пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(num, ppk)).click()
            self.value_check(AreaSettingsLocators.ENTERS_THE_AREA(num, ppk),
                             f'#{areas} Зона Пожаротушения ', 'входит в область', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.DISABLE(num, ppk), 'отключен', f'area #{num}')
            self.value_check(AreaSettingsLocators.DELAY_IN_EVACUATION(num, ppk),
                             '1800', 'задержка эвакуации', f'area #{num}')
            self.value_check(AreaSettingsLocators.EXTINGUISHING_START_TIME(num, ppk),
                             '255', 'время пуска тушения', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.EXTINGUISHING(num, ppk),
                                  'есть пожаротушение', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.GAS_OUTPUT_SIGNAL(num, ppk),
                                  'требуется сигнал выхода газа', f'area #{num}')
            self.value_check(AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR(num, ppk),
                             'не (пожар ИЛИ 1) блокирует 6', 'взаимно исключает ДУ', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.EXTINGUISHING_BY_MFA(num, ppk),
                                  'тушение по ИПР', f'area #{num}')
            self.checkbox_checked(AreaSettingsLocators.FORWARD_IN_RING(num, ppk), 
                                  'пересылать по кольцу', f'area #{num}')
            self.value_check(AreaSettingsLocators.RETRY_DELAY(num, ppk),
                             '16383', 'задержка перезапроса', f'area #{num}')
            self.value_check(AreaSettingsLocators.LAUNCH_ALGORITHM(num, ppk),
                             'C2 (два пожара или пожар+неисправность)', 'алгоритм ЗКПС', f'area #{num}')                
            self.value_check(AreaSettingsLocators.RESET_DELAY(num, ppk),
                             '16383', 'задержка сброса', f'area #{num}')
        if areas > 0:
            self.browser.find_element(*SystemObjectsLocators.AREA_ARROW(ppk)).click()

    def should_be_inputlinks_settings(self, inlinks, areas, addr_devs, ppk):
        logger.info(f'Checking settings in {inlinks} inputlinks on PPK#{ppk}...')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1, ppk)).click()
        for num in range(1, inlinks + 1):  # Проверка соответствия настроек в каждом ТС входе
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(num, ppk)).click()
            if num <= addr_devs:
                device_name = self.browser.find_element(
                    *SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(1, num, ppk)).text
                self.value_check(InputLinkSettingsLocators.UNIT_ID(num, ppk),
                                device_name, 'ссылка(ИД)', f'inputlink #{num}')
            if areas > 0:
                self.value_check(InputLinkSettingsLocators.PARENT_AREA(num, ppk),
                                f'#{areas} Зона Пожаротушения ', 'входит в область', f'inputlink #{num}')
            self.checkbox_checked(InputLinkSettingsLocators.DISABLE(num, ppk), 'отключен', f'inputlink #{num}')
            if num % 6 == 5:  # Тип ТС входа - вход команд
                self.value_check(InputLinkSettingsLocators.COMMAND(num, ppk),
                                 f'СДУ - газ пошел', 'команда', f'inputlink #{num}')
            if num % 6 == 0:  # Тип ТС входа - вход технический
                self.value_check(InputLinkSettingsLocators.CHANNEL(num, ppk),
                                 f'14', 'канал', f'inputlink #{num}')
                self.checkbox_checked(InputLinkSettingsLocators.FIX(num, ppk), 'фиксировать', f'inputlink #{num}')
        if inlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW(ppk)).click()
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(1, ppk)).click()

    def should_be_outputlinks_settings(self, outlinks, areas, BIS_Ms, ppk):
        logger.info(f'Checking settings in {outlinks} outputlinks on PPK#{ppk}...')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
        BIS_num = 1
        for num in range(1, outlinks + 1):  # Проверка соответствия настроек в каждом ТС выходе
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(num, ppk)).click()
            if BIS_num <= BIS_Ms:
                if BIS_num % 4 == 0: BIS_num += 1  # Если тип БИС-Ма - ТИ, то пропускаем его
                BIS_name = self.browser.find_element(
                    *SystemObjectsLocators.RS_485_ITEMS(BIS_num, ppk)).text
                BIS_num += 1
                self.value_check(OutputLinkSettingsLocators.UNIT_ID(num, ppk),
                                BIS_name, 'ссылка(ИД)', f'outputlink #{num}')
            if areas > 0:
                self.value_check(OutputLinkSettingsLocators.PARENT_AREA(num, ppk), 
                                f'#{areas} Зона Пожаротушения ', 'входит в область', f'outputlink #{num}')
            self.checkbox_checked(OutputLinkSettingsLocators.DISABLE(num, ppk), 'отключен', f'outputlink #{num}')
            if num % 3 == 0:  # Тип ТС выхода - выход на реле
                self.value_check(OutputLinkSettingsLocators.TURN_ON_DELAY(num, ppk),
                                 '16383', 'задержка включения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.TURN_OFF_DELAY(num, ppk),
                                 '16383', 'задержка выключения', f'outputlink #{num}')              
                self.checkbox_checked(OutputLinkSettingsLocators.NO_STOP(num, ppk),
                                      'продолжать если НЕ условие', f'outputlink #{num}')
                self.checkbox_checked(OutputLinkSettingsLocators.NO_RESTART_DELAY_ON(num, ppk),
                                      'продолжать задержку включения при повторном', f'outputlink #{num}')
                self.checkbox_checked(OutputLinkSettingsLocators.NO_RESTART_DELAY_OFF(num, ppk),
                                      'продолжать задержку вЫключения при повторном', f'outputlink #{num}')
                self.checkbox_checked(OutputLinkSettingsLocators.SINGLE_PULSE(num, ppk),
                                      'однократный импульс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num, ppk), 
                                 'если есть', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE2(num, ppk), 
                                 'если есть', 'на ПОЖАР (пожар-2)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FIRE1(num, ppk), 
                                 'если есть', 'на ВНИМАНИЕ (пожар-1)', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_FAULT(num, ppk), 
                                 'если есть', 'на неисправность', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_REPAIR(num, ppk), 
                                 'если есть', "на 'в ремонте'", f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION(num, ppk), 
                                 'если есть', 'на газ-уходи', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING(num, ppk), 
                                 'если есть', 'на пуск тушения', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AFTER_EXTINGUICHING(num, ppk), 
                                 'если есть', 'на тушение закончено', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EXTINGUICHING_FAILED(num, ppk), 
                                 'если есть', 'на тушение закончено неудачно', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_AUTO_OFF(num, ppk), 
                                 'если есть', 'на авт. откл', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_RESET(num, ppk), 
                                 'если есть', 'на сброс', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR(num, ppk), 
                                 'если есть', 'на дверь открыта', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_BLOCKED(num, ppk), 
                                 'если есть', 'на блокировка', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_EVACUATION_PAUSE(num, ppk), 
                                 'если есть', 'на останов', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_DOOR_PAUSE(num, ppk), 
                                 'если есть', 'на останов по двери', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.ON_CANCELLED(num, ppk), 
                                 'если есть', 'на отмену пуска тушения', f'outputlink #{num}')
                for tech_num in range(15):
                    self.value_check(OutputLinkSettingsLocators.ON_TECH(num, tech_num, ppk), 
                                     'если есть', f'на технический сигнал {tech_num}', f'outputlink #{num}')
                self.value_check(OutputLinkSettingsLocators.AND_OR(num, ppk),
                                 'по И', 'И/или', f'outputlink #{num}')
        if outlinks > 0:
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW(ppk)).click()
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
    
    def should_be_BIS_Ms_settings(self, BIS_Ms, ppk):
        logger.info(f'Checking settings in {BIS_Ms} BIS_Ms on PPK#{ppk}...')
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()
        for num in range(1, BIS_Ms + 1):  # Проверка соответствия настроек в каждом БИС-Ме
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(num, ppk)).click()
            self.checkbox_checked(RS_485_SettingsLocators.DISABLE(num, ppk), 'отключен', f'RS-485 #{num}')
            if num % 4 == 0:  # Тип RS-485 - ТИ
                self.checkbox_unchecked(RS_485_SettingsLocators.FIRE(num, ppk), 
                                        'ПОЖАР', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.ATTENTION(num, ppk), 
                                      'ВНИМАНИЕ', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.FAULT(num, ppk), 
                                      'НЕИСПРАВНОСТЬ', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.AUTO_OFF(num, ppk), 
                                      'автоматика ОТКЛ', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LEVEL_CONFIRM(num, ppk),
                                 '2000', 'уровень ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.LENGTH_CONFIRM(num, ppk),
                                 '15', 'длительность ответа', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.PULSE_DIAL(num, ppk), 
                                      'импульсный набор', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.NO_CONFIRM(num, ppk), 
                                      'не ждать ответа', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.PHONE_NUMBER(num, ppk),
                                 '1234567890123456', 'номер телефона', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.ACCOUNT(num, ppk),
                                 '9999', 'аккаунт', f'RS-485 #{num}')
            else:
                if num % 4 == 3:  # Тип RS-485 - БИС-М3
                    self.checkbox_checked(RS_485_SettingsLocators.DEFAULT_GREEN(num, ppk), 
                                          'по умолчанию зеленые', f'RS-485 #{num}')
                    self.value_check(RS_485_SettingsLocators.BACKLIGHT(num, ppk),
                                     '255', 'подсветка', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.BRIGHTNESS(num, ppk),
                                 '15', 'яркость', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.TIMEOUT(num, ppk),
                                 '255', 'таймаут нажатий', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.NO_SOUND(num, ppk), 
                                      'без звука', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.NO_ALARM_SOUND(num, ppk), 
                                      'без звука тревог', f'RS-485 #{num}')
                self.checkbox_checked(RS_485_SettingsLocators.KEY_SENSITIVE(num, ppk), 
                                      'чувствительность клавиш', f'RS-485 #{num}')
                self.value_check(RS_485_SettingsLocators.DEFAULT_ID(num, ppk),
                                 '2147483647', 'ИД по умолчанию', f'RS-485 #{num}')
            self.value_check(RS_485_SettingsLocators.SN(num, ppk),
                             str(65536 - num), 'серийный номер', f'RS-485 #{num}')
        if BIS_Ms > 0:
            self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW(ppk)).click()

    def should_be_addressable_devices_settings(self, AL, addr_devs, ppk):
        logger.info(f'Checking settings in {addr_devs} addressable devices in loop {AL} on PPK#{ppk}...')
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()
        self.browser.execute_script("scrollBy(0, 200);")
        for num in range(1, addr_devs + 1):  # У каждого АУ на указаном шлейфу изменить все настройки
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, num, ppk)).click()
            if num % 13 != 10:  # Если не ИСМ4 (у него отключен)
                self.checkbox_checked(AddressableLoopSettingsLocators.DISABLE(AL, num, ppk), 
                                      'отключен', f'addressable device #{num} on loop {AL}')
            if num % 13 == 2:  # Тип АУ - АР1
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num, ppk),
                                 'нет контроля, нет пожар2', 'режим', f'addressable device #{num} on loop {AL}')
            if num % 13 == 4:  # Тип АУ - АРмини
                self.checkbox_unchecked(AddressableLoopSettingsLocators.TWO_INPUTS(AL, num, ppk), 
                                        'два входа', f'addressable device #{num} on loop {AL}')
            if num % 13 == 5:  # Тип АУ - АТИ
                self.value_check(AddressableLoopSettingsLocators.MODE(AL, num, ppk),
                                 'off', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_checked(AddressableLoopSettingsLocators.DIFFERENTIAL(AL, num, ppk),
                                      'дифференциальный', f'addressable device #{num} on loop {AL}')
            if num % 13 == 6:  # Тип АУ - АхДПИ
                self.value_check(AddressableLoopSettingsLocators.THRESHOLD(AL, num, ppk),
                                 '50', 'порог чувствительности', f'addressable device #{num} on loop {AL}')
                self.value_check(AddressableLoopSettingsLocators.GROUP(AL, num, ppk),
                                 '255', 'ЗКПС', f'addressable device #{num} on loop {AL}')
            if num % 13 == 10:  # Тип АУ - ИСМ4
                self.checkbox_unchecked(AddressableLoopSettingsLocators.DISABLE(AL, num, ppk), 
                                        'отключен', f'addressable device #{num} on loop {AL}')
                self.value_check(AddressableLoopSettingsLocators.MODE220(AL, num, ppk),
                                 'игнорировать', 'режим', f'addressable device #{num} on loop {AL}')
                self.checkbox_checked(AddressableLoopSettingsLocators.MOTOR(AL, num, ppk), 
                                      'мотор с переполюсовкой', f'addressable device #{num} on loop {AL}')
            if num % 13 == 11:  # Тип АУ - ИСМ5
                self.value_check(AddressableLoopSettingsLocators.MODE24(AL, num, ppk),
                                 '24v', 'напряжение питания', f'addressable device #{num} on loop {AL}')
            self.value_check(AddressableLoopSettingsLocators.SN(AL, num, ppk),
                             str(16777216 - num - (AL - 1) * addr_devs), 'серийный номер', 
                             f'addressable device #{num} on loop {AL}')
        if addr_devs > 0:
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL, ppk)).click()


# Проверка кнопки "в файл" и кнопки "из файла"
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

    def click_from_file_button(self):
        logger.info(f'Click from file button')
        self.browser.find_element(*MainPanelLocators.FROM_FILE_BUTTON).click()
        sleep(1)

    def load_configuration_from_file(self):
        logger.info(f'Loading configuration from file...')
        try:
            file_path = r'%USERPROFILE%\Downloads\config.json'
            assert os.path.exists(file_path), f'Configuration file not found: "{file_path}"'
            keyboard.write(file_path)
            keyboard.send('enter')
            sleep(0.5)
        except:  # При ошибке, закрыть диалоговое окно windows
            keyboard.press_and_release('esc')

    def delete_config_file(self):
        logger.info(f'Deleting a configuration file...')
        os.remove(r'%USERPROFILE%\Downloads\config.json')


# Проверка кнопки "в файл для Интеллекта"
    def click_to_file_for_intellect_button(self):
        logger.info(f'Click to file for Intellect button')
        self.browser.find_element(*MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON).click()

    def delete_config_for_Intellect_file(self):
        logger.info(f'Deleting a configuration file...')
        file_path = r'%USERPROFILE%\Downloads\configintellect.json'
        assert os.path.exists(file_path), f'Configuration file for Intellect not found: "{file_path}"'
        os.remove(file_path)


# Проверка терминала 
    def should_be_object_creation_messages(self, areas, inlinks, outlinks, BIS_Ms, addr_devs, ppk_num):
        logger.info(f'Checking object creation messages in terminal when unloading')
        for ppk in range(1, ppk_num + 1):
            assert self.is_element_visible(SystemObjectsLocators.PPK_R_FORM(ppk), 10), f'PPK#{ppk} not found'
            for num in range(1, areas + 1):  # Проверка сообщений создания Зон Пожаротушения
                assert self.is_element_present(MainPanelLocators.CREATE_MESSAGE(
                    f'Модуль#1(Области).Область#{num}(Зона Пожаротушения)', ppk)), \
                    f'There is no message about creation PPK#{ppk} area #{num} or there is a spelling error'
            for num in range(1, inlinks + 1):  # Проверка сообщений создания ТС входов
                type = ('вход неисправность', 'Ссылка на область', 'ИПР', 'ИП', 'вход команд', 'вход технический')
                assert self.is_element_present(MainPanelLocators.CREATE_MESSAGE(
                    f'Модуль#1(Области).ТС вход#{num}({type[num % 6 - 1]})', ppk)), 'There is no message ' \
                    f'about creation  PPK#{ppk} input link #{num} "{type[num % 6 - 1]}" or there is a spelling error'
            for num in range(1, outlinks + 1):  # Проверка сообщений создания ТС выходов
                type = ('индикатор', 'направление на БИСМ2', 'выход на реле')
                assert self.is_element_present(MainPanelLocators.CREATE_MESSAGE(
                    f'Модуль#1(Области).ТС выход#{num}({type[num % 3 - 1]})', ppk)), 'There is no message ' \
                    f'about creation  PPK#{ppk} output link #{num} "{type[num % 3 - 1]}" or there is a spelling error'
            for num in range(1, BIS_Ms + 1):  # Проверка сообщений создания БИСМов
                type = ('БИС-М', 'БИС-М2', 'БИС-М3', 'ТИ')
                assert self.is_element_present(MainPanelLocators.CREATE_MESSAGE(
                    f'Модуль#2(Выходы).RS-485#{num}({type[num % 4 - 1]})', ppk)), 'There is no message ' \
                    f'about creation  PPK#{ppk} BIS-M #{num} "{type[num % 4 - 1]}" or there is a spelling error'
            for AL in 1, 2:  # Проверка сообщений создания АУ
                for num in range(1, addr_devs + 1):
                    type = ('АМК', 'АР1', 'АР-5', 'АРмини', 'АТИ', 'АхДПИ', 'ИР', 
                            'ИСМ1', 'ИСМ2', 'ИСМ4', 'ИСМ5', 'МКЗ', 'ОСЗ')
                    assert self.is_element_present(MainPanelLocators.CREATE_MESSAGE(
                        f'Модуль#3(Адресные шлейфы).АШ#{AL}.Адресные устройства#{num}({type[num % 13 - 1]})', ppk)), \
                        f'There is no message about creation  PPK#{ppk} addressable device #{num} ' \
                        f'"{type[num % 13 - 1]}" on loop {AL} or there is a spelling error'
                
    def should_be_alternating_colors_in_terminal(self):
        logger.info(f'Checking alternation of colors in dark mode terminal')
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

    def clearing_ppk(self, ppk_num):
        self.open_terminal()
        for ppk in range(1, ppk_num + 1):
            self.open_ppk_objects(ppk)
            for module in ('Модуль#3 Адресные шлейфы', 3), ('Модуль#2 Выходы', 2), ('Модуль#1 Области', 1):
                logger.info(f'Clearing PPK#{ppk} module {module[1]}...')
                self.browser.find_element(*SystemObjectsLocators.MODULE_FORM(module[1], ppk)).click()
                button = self.browser.find_element(*SystemObjectsLocators.CLEAR_MODULE_BUTTON)
                self.browser.execute_script('arguments[0].click();', button)
                assert self.is_element_visible(MainPanelLocators.MODULE_CLEANING_MESSAGE(
                    module[0], ppk), 10), f'There is no message about cleaning PPK#{ppk} module {module[0]}'
            self.close_ppk_objects(ppk)
            

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
        assert self.is_element_visible(EventLogLocators.DATE_TIME, 10), \
            'First message did not appear in 10 seconds'
        
    def check_value_of_columns(self, ppk_num):
        logger.info('Checking value of columns and date and time format...')
        assert self.is_element_visible(SystemObjectsLocators.PPK_R_FORM(ppk_num), 10), f'PPK#{ppk_num} not found'
        try:
            first_date_time = datetime.strptime(
                self.browser.find_element(*EventLogLocators.DATE_TIME).text, '%Y.%m.%d %H:%M:%S')
        except ValueError:
            assert False, 'String does not match the date and time format'
        date = first_date_time.strftime('%Y.%m.%d')
        actually_date = datetime.now().strftime('%Y.%m.%d')
        assert date == actually_date, \
            f'Date of the first event does not match "{actually_date}", received date: {date}'
        # event_value = self.browser.find_element(*EventLogLocators.EVENT).text
        # assert event_value == '-', f'Event value does not match, expected: "-", received: {event_value}'
        # address_value = self.browser.find_element(*EventLogLocators.ADDRESS).text
        # assert address_value == f'#{ppk_num}.1', \
        #     f'Address value does not match, expected: "#{ppk_num}.1", received: {address_value}'
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