from locators import (MainPanelLocators, SystemObjectsLocators, ConfigurationLocators)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import psutil
from loguru import logger
from time import time
from time import sleep


def get_memory_info_static(browser_name):  # Выводит затраты оперативной памяти тестируемой страницой
        proc = [i for i in psutil.process_iter(['pid', 'name', 'create_time'])
                if i.info['name'] == f'{browser_name}.exe']  # Список всех процессов браузера
        proc.sort(key=lambda i: i.info['create_time'])  # Сортировка по времени создания
        pid = proc[-2 if browser_name == 'chrome' else -4].info['pid']  # PID процесса тестируемой страницы
        mem_info = psutil.Process(pid).memory_info()
        logger.warning(f'Memory usage by page: VMS: {mem_info.vms / (1024 ** 2):.2f} MB; ' \
                                             f'RSS: {mem_info.rss / (1024 ** 2):.2f} MB (PID: {pid})')
        

class Page():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)

    def get_memory_info(self):
        get_memory_info_static(str(type(self.browser)).split('.')[2])  # chrome or firefox

    def is_element_present(self, locator):  # Есть ли элемент на странице
        try:
            self.browser.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, locator, wait=3.0):  # Ожидание пока элемент не исчезнет
        try:
            self.browser.implicitly_wait(0)  # Временное отключение неявного ожидание
            WebDriverWait(self.browser, wait).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            self.browser.implicitly_wait(self.timeout)  # Восстановление неявного ожидания
            return False

    def is_element_clickable(self, locator, wait=3):
        try:
            self.browser.implicitly_wait(0)
            WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable(locator))
            self.browser.implicitly_wait(self.timeout)
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator, wait=3):
        try:
            self.browser.implicitly_wait(0)
            WebDriverWait(self.browser, wait).until(EC.visibility_of_element_located(locator))
            self.browser.implicitly_wait(self.timeout)
            return True
        except TimeoutException:
            return False

    def open(self):  # Открытие браузера
        self.browser.get(self.url)
        self.browser.maximize_window()  # Разворот окна на весь экран
    
    def check_record(self, ppk, module='', timeout=30):
        start_time = time()
        assert self.is_element_present(SystemObjectsLocators.RECORD_START(ppk, module)), \
            f'Recording for {f'PPK#{ppk}' if module == '' else f'PPK#{ppk} {module}'} has not started'
        assert self.is_element_visible(SystemObjectsLocators.RECORD_FINISH, max(timeout, 10)), \
            f'Recording for {'PPK#{ppk}' if module == '' else f'PPK#{ppk} {module}'} has not finished, ' \
            f'time spent: {time() - start_time:.2f}'
        logger.success(f'Record to {'PPK#{ppk}' if module == '' else f'PPK#{ppk} {module}'} was successful, ' \
                    f'time spent: {time() - start_time:.2f}')
    
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

    def check_unload(self, ppk_num, m1_wait=30, m2_wait=30, m3_wait=30):
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
        assert self.is_element_present(MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON), \
            'Close all tabs button is not presented'
        self.browser.find_element(*MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON).click()
       
    def open_ADDRESSABLE_LOOP(self, AL, ppk):
        assert self.is_element_clickable(SystemObjectsLocators.ADDRESSABLE_LOOP(ppk, AL)), \
            f'Addressable loop arrow on PPK#{ppk} is not clickable'
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_LOOP(ppk, AL)).click()

    def open_all_objects(self, ppk):
        self.open_module_objects(1, ppk)
        self.open_module_objects(2, ppk)
        self.open_module_objects(3, ppk)
        self.open_ADDRESSABLE_LOOP(1, ppk)
        self.open_ADDRESSABLE_LOOP(2, ppk)

    def save_settings(self):
        self.button_should_be_clickable(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')
        self.browser.find_element(*MainPanelLocators.SAVE_BUTTON).click()
    
    def button_should_be_clickable(self, locator, button):
        assert self.is_element_clickable(locator), f'Button "{button}" is not clickable'
    
    def check_presence_and_spelling(self, locator, name, obj):
        assert self.is_element_present(locator), \
            f'{obj} "{name}" is not presented'
        button_text = self.browser.find_element(*locator).text
        assert button_text == name, \
            f'{obj} "{name}" has a spelling error, button text: {button_text}'

    def presence_and_spelling(self, locator, name, obj='Button'):  # Проверка на наличие элемента и ошибки
        logger.info(f'Checking the {obj} "{name}"...')
        try:
            self.check_presence_and_spelling(locator, name, obj)
        except StaleElementReferenceException:  # Firefox выдает ошибку из-за обновления элементов
            self.check_presence_and_spelling(locator, name, obj)
    
    def check_tab_with_arrow(self, locator, arrow_locator, sub_locator, name):
        '''Проверяет вкладку на наличие и орфографические ошибки,
        сворачивание и разворачивание вкладки при нажатии на стрелку и при двойном нажатии вкладки 
        (при разворачивании проверяется наличие объекта sub_locator)
        '''
        self.browser.find_element(*arrow_locator).click()
        sleep(0.2)
        assert self.is_element_visible(sub_locator), \
            f'{name} tab did not open after clicking arrow'
        self.browser.find_element(*arrow_locator).click()
        sleep(0.2)
        assert self.is_not_element_present(sub_locator), \
            f'{name} tab did not collapse after clicking arrow'

        element = self.browser.find_element(*locator)
        self.browser.execute_script(
            'arguments[0].dispatchEvent(new MouseEvent("dblclick", { bubbles: true }));', element)
        sleep(0.2)
        assert self.is_element_visible(sub_locator), \
            f'{name} tab did not open after double click'
        self.browser.execute_script(
            'arguments[0].dispatchEvent(new MouseEvent("dblclick", { bubbles: true }));', element)
        sleep(0.2)
        assert self.is_not_element_present(sub_locator), \
            f'{name} tab did not collapse after double click'
        
    def check_positioning(self, locator, path, modules='1111'):
        '''Проверяет вкладку на выделение красным при позиционированиии черным без него, 
        наличие указанных панелей настроек справа.
        '''
        self.browser.find_element(*locator).click()
        sleep(0.2)
        color = self.browser.find_element(*locator).value_of_css_property('background-color')
        assert '255, 49, 80' in color, f'Tab background color is not red: ' \
            f'"rgba(255, 49, 80, 0.24)", received color: {color}'

        assert len(self.browser.find_elements(*ConfigurationLocators.PATH)) == 2, \
            'Path to the tab is not present'
        if path != '#1 ППК-Р':  # Для ППК другая схема
            text = self.browser.find_elements(*ConfigurationLocators.PATH)[1].text
            assert text == path, f'Path to the tab is not match, expected: {path}, received: {text}' 

        if modules[0] == '1':
            assert self.is_element_present(ConfigurationLocators.CONFIGURATION_PANEL), \
                'Configuration panel is not present, but should be'
        else:
            assert self.is_not_element_present(ConfigurationLocators.CONFIGURATION_PANEL), \
                'Configuration panel present, but should not be'
        if modules[1] == '1':
            assert self.is_element_present(ConfigurationLocators.STATUS_PANEL), \
                'Status panel is not present, but should be'
        else:
            assert self.is_not_element_present(ConfigurationLocators.STATUS_PANEL), \
                'Status panel present, but should not be'
        if modules[2] == '1':
            assert self.is_element_present(ConfigurationLocators.COMMAND_PANEL), \
                'Command panel is not present, but should be'
        else:
            assert self.is_not_element_present(ConfigurationLocators.COMMAND_PANEL), \
                'Command panel present, but should not be'
        if modules[3] == '1':
            assert self.is_element_present(ConfigurationLocators.INFORMATION_PANEL), \
                'Information panel is not present, but should be'
        else:
            assert self.is_not_element_present(ConfigurationLocators.INFORMATION_PANEL), \
                'Information panel present, but should not be'

    def check_delete_button(self):  # Перед выполнением не должно быть меток на удаение
        assert self.is_element_present(ConfigurationLocators.DELETE_BUTTON), 'Delete button is not present'
        self.browser.find_element(*ConfigurationLocators.DELETE_BUTTON).click()
        assert self.is_element_present(ConfigurationLocators.DELETE_MARK), 'Tab was not marked for deletion'
        assert self.is_element_present(ConfigurationLocators.RESTORE_BUTTON), 'Restore button is not present'
        self.browser.find_element(*ConfigurationLocators.RESTORE_BUTTON).click()
        assert self.is_not_element_present(ConfigurationLocators.DELETE_MARK), 'Tab was not unmarked for deletion'
        assert self.is_element_present(ConfigurationLocators.DELETE_BUTTON), 'Delete button is not present'

    def check_change_address_field(self, max_num):  # Проверка границ и стрелок в поле ввода
        assert self.is_element_present(ConfigurationLocators.CHANGE_ADDRESS_BUTTON), \
            'Change address button is not present'
        self.browser.find_element(*ConfigurationLocators.CHANGE_ADDRESS_BUTTON).click()
        assert self.is_element_present(ConfigurationLocators.CHANGE_ADDRESS_INPUT), \
            'Change address input field is not present'
        actions = ActionChains(self.browser)
        input_field = self.browser.find_element(*ConfigurationLocators.CHANGE_ADDRESS_INPUT)
        sleep(0.3)
        actions.move_to_element_with_offset(input_field, 100, -1).click().perform()  # +1
        actions.move_to_element_with_offset(input_field, 100, 1).click().perform()  # -1
        actions.move_to_element_with_offset(input_field, 100, 1).click().perform()  # -1
        value = input_field.get_attribute('value')
        assert value == '1', \
            f'Value in change address input field does not match, expected "1", received: {value}'
        input_field.send_keys(Keys.BACKSPACE, max_num + 1, max_num)
        actions.move_to_element_with_offset(input_field, 100, 1).click().perform()  # -1
        actions.move_to_element_with_offset(input_field, 100, -1).click().perform()  # +1
        actions.move_to_element_with_offset(input_field, 100, -1).click().perform()  # +1
        value = input_field.get_attribute('value')
        assert value == str(max_num), \
            f'Value in change address input field does not match, expected {max_num}, received: {value}'
        self.browser.find_element(*ConfigurationLocators.CHANGE_ADDRESS_OK).click()
    
    def change_address(self, num):
        self.browser.find_element(*ConfigurationLocators.CHANGE_ADDRESS_BUTTON).click()
        input_field = self.browser.find_element(*ConfigurationLocators.CHANGE_ADDRESS_INPUT)
        input_field.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, num)
        self.browser.find_element(*ConfigurationLocators.CHANGE_ADDRESS_OK).click()
