from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class Page():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):  # Есть ли элемент на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, wait=3.0):  # Ожидание пока элемент не исчезнет
        try:
            self.browser.implicitly_wait(0)  # Временное отключение неявного ожидание
            WebDriverWait(self.browser, wait).until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            self.browser.implicitly_wait(self.timeout)  # Восстановление неявного ожидания
            return False
        return True

    def is_element_clickable(self, how, what, wait=3):
        try:
            self.browser.implicitly_wait(0)
            WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        self.browser.implicitly_wait(self.timeout)
        return True

    def is_element_visible(self, how, what, wait=3):
        try:
            self.browser.implicitly_wait(0)
            WebDriverWait(self.browser, wait).until(EC.visibility_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        self.browser.implicitly_wait(self.timeout)
        return True

    def open(self):  # Открытие браузера
        self.browser.get(self.url)
        self.browser.maximize_window()  # Разворот окна на весь экран