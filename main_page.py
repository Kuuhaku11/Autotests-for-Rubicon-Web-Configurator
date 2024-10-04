from locators import (MainPanelLocators, SystemObjectsLocators)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import psutil
from loguru import logger
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
        self.presence_and_spelling(locator, name, 'tab')

        self.browser.find_element(*arrow_locator).click()
        assert self.is_not_element_present(sub_locator), \
            'System tab did not collapse after clicking arrow'
        sleep(0.5)
        self.browser.find_element(*arrow_locator).click()
        assert self.is_element_present(sub_locator), \
            'System tab did not open after clicking arrow'

        for _ in range(2):
            sleep(0.2)
            element = self.browser.find_element(*locator)
            self.browser.execute_script(
                'arguments[0].dispatchEvent(new MouseEvent("dblclick", { bubbles: true }));', element)
        assert self.is_not_element_present(sub_locator), \
            'System tab did not collapse after double click'
        sleep(0.5)
        for _ in range(2):
            element = self.browser.find_element(*locator)
            self.browser.execute_script(
                'arguments[0].dispatchEvent(new MouseEvent("dblclick", { bubbles: true }));', element)
        self.browser.find_element(*arrow_locator).click()
        assert self.is_element_present(sub_locator), \
            'System tab did not open after double click'