from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import psutil
from loguru import logger


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