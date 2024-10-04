from main_page import Page
from locators import (MainPanelLocators, SystemObjectsLocators)
from selenium.common.exceptions import StaleElementReferenceException
from loguru import logger
import keyboard
import os
from time import sleep


class Sidebar(Page):  # Класс для тестирования по тест-кейсу "Главная панель" (DRBN-T52)

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

    def open_ADDRESSABLE_LOOP(self, AL, ppk):
        assert self.is_element_clickable(SystemObjectsLocators.ADDRESSABLE_LOOP(ppk, AL)), \
            f'Addressable loop arrow on PPK#{ppk} is not clickable'
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_LOOP(ppk, AL)).click()
    
    def check_input_characters(self, locator):
        expected_value = 'azAOЁZайёяАЯ0123456789`@#№$%^:;&?!*()[]|/<>.,-_=+}~{ьъзшщюц'
        self.browser.find_element(*locator).send_keys(expected_value)
        value = self.browser.find_element(*locator).get_attribute('value')
        assert expected_value == value, f'Value in search field does not match, ' \
                                        f'expected "{expected_value}", received "{value}"'


# Проверка поля поиска
    def should_be_search_field(self):
        logger.info('Checking search field...')
        assert self.is_element_visible(SystemObjectsLocators.SEARCH_ITEM), 'Search field is not displayed'

    def check_input_characters_in_search_field(self):
        self.check_input_characters(SystemObjectsLocators.SEARCH_FIELD)

    def clear_search_field(self):
        self.browser.find_element(*SystemObjectsLocators.SEARCH_CLEAR_ICON).click()
        value = self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).get_attribute('value')
        assert value == '', f'Search field was not cleared, resulting value: {value}'


# Проверка поиска всех объектов
    def search_func(self, key, object, quantity=2, method='by address'):
        self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys(key)
        actually_quantity = len(self.browser.find_elements(*SystemObjectsLocators.SEARCH_ELEMENT(object)))
        assert actually_quantity == quantity, f'"{object}" not found {quantity} times {method}, '\
            f'total found {actually_quantity}'
        self.clear_search_field()
    
    def search_sub(self, object, parent, obj_num=1):
        for num in range(1, obj_num + 1):
            actually_quantity = len(self.browser.find_elements(
                *SystemObjectsLocators.SEARCH_ELEMENT(f'#{num} {object} ')))
            assert actually_quantity == 8, f'Subunit {parent} "#{num} {object} " not found ' \
                f'{8} times, total found {actually_quantity}'

    def load_configuration_from_file(self):
        logger.info(f'Loading configuration for search objects from file...')
        self.browser.find_element(*MainPanelLocators.FROM_FILE_BUTTON).click()
        try:
            file_path = rf'{os.getcwd()}\configurations\auto_test_config_for_search_2_ppk.json'
            assert os.path.exists(file_path), f'Configuration file not found: "{file_path}"'
            sleep(0.5)
            keyboard.write(file_path)
            keyboard.send('enter')
            sleep(0.5)
        except:  # При ошибке, закрыть диалоговое окно windows
            keyboard.press_and_release('esc')

    def search_by_address(self):
        logger.info('Checking search objects by address...')
        for num in range(1, 11):  # Поиск всех Зон Пожаротушения
            if num == 1:
                self.search_func('#1', '#1 Зона Пожаротушения ', 4)
            else:
                self.search_func(f'#{num}', f'#{num} Зона Пожаротушения ')
 
        dict = {1: 'Вход неисправность ', 2: 'Ссылка на область ', 3: 'ИПР ',
                4: 'ИП ', 5: 'Вход команд ', 0: 'Вход технический '}
        for num in range(1, 13):  # Поиск всех ТС входов
            if num == 1:
                self.search_func('#1', '#1 Вход неисправность ', 4)
            else:
                self.search_func(f'#{num}', f'#{num} {dict[num % 6]}')

        dict = {1: 'Индикатор ', 2: 'Направление на БИСМ2 ', 0: 'Выход на реле '}
        for num in range(1, 10):  # Поиск всех ТС выходов
            if num == 1:
                self.search_func('#1', '#1 Индикатор ', 4)
            else:
                self.search_func(f'#{num}', f'#{num} {dict[num % 3]}')

        dict = {1: 'БИС-М', 2: 'БИС-М2', 3: 'БИС-М3', 0: 'ТИ'}
        for num in range(1, 13):  # Поиск всех устройств на RS-485
            if num == 2:
                self.search_func('#2', '#2 БИС-М2 2002', 4)
            else:
                if num % 4 == 0:
                    self.search_func(f'#{num}', f'#{num} ТИ ')  # Баг, не отображается серийник TODO
                else:
                    self.search_func(f'#{num}', f'#{num} {dict[num % 4]} {2000 + num}')
        self.search_func('#1', '#1 БИС-М1 ', 24)

        dict = {1: 'АМК', 2: 'АР1', 3: 'АР-5', 4: 'АРмини', 5: 'АТИ', 6: 'АхДПИ', 7: 'ИР',
                8: 'ИСМ1', 9: 'ИСМ2', 10: 'ИСМ4', 11: 'ИСМ5', 12: 'МКЗ', 0: 'ОСЗ'}
        for num in range(1, 26):  # Поиск всех АУ
            if num == 1:
                self.search_func('#1', '#1 АМК 1001', 4)
                self.search_func(f'#1', f'#1 {dict[num % 13]} {2000 + num}')
            elif num == 2:
                self.search_func('#2', f'#2 {dict[num % 13]} {1000 + num}')
                self.search_func(f'#2', '#2 АР1 2002', 4)
            else:
                self.search_func(f'#{num}', f'#{num} {dict[num % 13]} {1000 + num}')
                self.search_func(f'#{num}', f'#{num} {dict[num % 13]} {2000 + num}')

    def search_by_SN(self):
        logger.info('Checking search objects by serial number...')
        dict = {1: 'БИС-М', 2: 'БИС-М2', 3: 'БИС-М3', 0: 'ТИ'}
        for num in range(1, 13):  # Поиск всех устройств на RS-485
            if num % 4 != 0:  # Баг, не отображается серийник ТИ TODO
                self.search_func(2000 + num, f'#{num} {dict[num % 4]} {2000 + num}', 2, 'by S/N')

        dict = {1: 'АМК', 2: 'АР1', 3: 'АР-5', 4: 'АРмини', 5: 'АТИ', 6: 'АхДПИ', 7: 'ИР',
                8: 'ИСМ1', 9: 'ИСМ2', 10: 'ИСМ4', 11: 'ИСМ5', 12: 'МКЗ', 0: 'ОСЗ'}
        for num in range(1, 26):  # Поиск всех АУ
                self.search_func(1000 + num, f'#{num} {dict[num % 13]} {1000 + num}', 2, 'by S/N')
                self.search_func(2000 + num, f'#{num} {dict[num % 13]} {2000 + num}', 2, 'by S/N')
    
    def search_by_device_name(self):
        logger.info('Checking search objects by device name...')
        for num in range(1, 11):  # Поиск всех Зон Пожаротушения
            self.search_func(f'Зона Пожаротушения', f'#{num} Зона Пожаротушения ', 2, 'by device name')
 
        dict = {1: 'Вход неисправность ', 2: 'Ссылка на область ', 3: 'ИПР ',
                4: 'ИП ', 5: 'Вход команд ', 0: 'Вход технический '}
        for num in range(1, 13):  # Поиск всех ТС входов
            self.search_func(dict[num % 6], f'#{num} {dict[num % 6]}', 2, 'by device name')

        dict = {1: 'Индикатор ', 2: 'Направление на БИСМ2 ', 0: 'Выход на реле '}
        for num in range(1, 10):  # Поиск всех ТС выходов
            self.search_func(dict[num % 3], f'#{num} {dict[num % 3]}', 2, 'by device name')

        dict = {1: 'БИС-М', 2: 'БИС-М2', 3: 'БИС-М3', 0: 'ТИ'}
        for num in range(1, 13):  # Поиск всех устройств на RS-485
            if num % 4 == 0:
                self.search_func('ТИ', f'#{num} ТИ ', 2, 'by device name')  # Баг, не отображается серийник TODO
            else:
                self.search_func(dict[num % 4], f'#{num} {dict[num % 4]} {2000 + num}', 2, 'by device name')
        self.search_func('БИС-М1', '#1 БИС-М1 ', 18)

        dict = {1: 'АМК', 2: 'АР1', 3: 'АР-5', 4: 'АРмини', 5: 'АТИ', 6: 'АхДПИ', 7: 'ИР',
                8: 'ИСМ1', 9: 'ИСМ2', 10: 'ИСМ4', 11: 'ИСМ5', 12: 'МКЗ', 0: 'ОСЗ'}
        for num in range(1, 26):  # Поиск всех АУ
            self.search_func(dict[num % 13], f'#{num} {dict[num % 13]} {1000 + num}', 2, 'by device name')
            self.search_func(dict[num % 13], f'#{num} {dict[num % 13]} {2000 + num}', 2, 'by device name')
    
    def search_by_name(self):  # Поиск всех элементов по имени
        for char in 'azAOЁZайёяАЯ0123456789`@#№$%^:;&?!*()[]|/<>.,-_=+}~{ьъзшщюц':
            self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys(char)
            assert self.is_element_present(SystemObjectsLocators.SEARCH_BY_NAME(char)), \
                f'"{char}" not found by name'
            self.clear_search_field()
    
    def search_subunits(self):  # Поиск всех субюнитов у АУ
        self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys('АР-5')
        self.search_sub('Вход', 'АР-5', 5)
        self.search_sub('Изолятор', 'АР-5')
        self.search_sub('Тампер', 'АР-5')
        self.clear_search_field()

        self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys('АРмини')
        self.search_sub('Вход', 'АРмини', 2)
        self.clear_search_field()

        self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys('ИР')
        self.search_sub('Изолятор', 'ИР')
        self.clear_search_field()

        for num in 1, 2:
            self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys(f'ИСМ{num}')
            self.search_sub('Вход', f'ИСМ{num}', 2)
            self.search_sub('Реле', f'ИСМ{num}', 2)
            self.search_sub('Изолятор', f'ИСМ{num}')
            self.search_sub('Тампер', f'ИСМ{num}')
            self.clear_search_field()

        self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys('ИСМ4')
        self.search_sub('Вход', 'ИСМ4', 2)
        self.search_sub('Реле ИСМ 4', 'ИСМ4', 2)
        self.search_sub('Изолятор', 'ИСМ4')
        self.search_sub('Тампер', 'ИСМ4')
        self.clear_search_field()

        self.browser.find_element(*SystemObjectsLocators.SEARCH_FIELD).send_keys('ИСМ5')
        self.search_sub('Вход', 'ИСМ5', 2)
        self.search_sub('Выход ИСМ 5', 'ИСМ5', 2)
        self.search_sub('Тампер', 'ИСМ5')
        self.clear_search_field()