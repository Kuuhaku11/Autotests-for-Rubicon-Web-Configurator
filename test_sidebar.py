from test_cases.sidebar import Sidebar
import pytest
from loguru import logger
from time import sleep


#===================================================================================================
'''Боковая панель вкладок (DRBN-T73).
Предполагается проверка пустых ППК-Р с идущими подряд номерами от 1.
Некоторые тесты не будут работать, если конфигуратор уже отдельно открыт.
Установка необходимых пакетов: pip install -r requirements.txt
Команда для запуска через терминал: pytest -s -v --tb=short .\test_main_panel.py
Для запуска запуска тестов в firefox добавить параметр: --browser_name=firefox
Для повторной проверки упавших тестов рекомендуется добавить параметр: --reruns 1
Для пропуска отдельных тестов можно раскомментировать фикстуру: @pytest.mark.skip
'''

headless = False  # True / False | Запуск тестов без отображения в браузере
                 # (test_from_file_button не будет работать тк дилоговое окно windows не отобразится)

ppk_num = 2  # Количество подключенных ППК-Р (Если меньше, чем по факту, остальные не будет проверяться)
#===================================================================================================


link = 'http://localhost:8082/'
pytestmark = pytest.mark.parametrize('headless', [headless])

# @pytest.mark.skip
def test_search_field(browser):  # Проверка поля поиска
    page = Sidebar(browser, link)
    page.open()
    page.should_be_search_field()
    page.check_input_characters_in_search_field()
    page.clear_search_field()


# @pytest.mark.skip
def test_search_objects(browser):  # Проверка поиска всех объектов 
    page = Sidebar(browser, link)
    page.open()
    page.load_configuration_from_file()
    page.search_by_address()
    page.search_by_SN()
    page.search_by_device_name()
    page.search_by_name()
    page.search_subunits()


# @pytest.mark.skip
def test_system_tab(browser):  # Проверка вкладки "Система"
    page = Sidebar(browser, link)
    page.open()
    page.check_system_tab()

# @pytest.mark.skip
def test_close_all_tabs_button(browser):  # Проверка кнопки "Закрыть все вкладки"
    page = Sidebar(browser, link)
    page.open()
    page.check_close_all_tabs_button(ppk_num)


# @pytest.mark.skip
def test_ppk_add_button(browser):  # Проверка кнопки добавления ППК-Р "+"
    page = Sidebar(browser, link)
    page.open()
    page.add_ppk(29 - ppk_num)
    page.refresh_page()
    page.check_ppk_num(29, ppk_num)  # Проверка 29 ППК, что при нажатии кнопки, не добавляется 2 ППК
    page.add_ppk(2)
    page.refresh_page()
    page.check_ppk_num(30, ppk_num)  # Проверка, что 31-й ППК не добавляется


# @pytest.mark.skip
def test_ppk_settinds(browser):  # Проверка вкладки и панели конфигурация ППК
    page = Sidebar(browser, link)
    page.open()
    page.check_ppk_tab()
    page.check_delete_ppk(ppk_num)
    page.check_name_ppk()
    page.change_ppk_address()


# @pytest.mark.skip
def test_change_addresses(browser):  # Проверка адресов после очистки кэша
    page = Sidebar(browser, link)
    page.open()
    page.check_ppk_address()


# @pytest.mark.skip
def test_module_1_tab(browser):  # Проверка вкладки "#1 Области"
    page = Sidebar(browser, link)
    page.open()
    page.check_module_1_tab(ppk_num)
    page.check_module_1_sub_tabs(ppk_num)


# @pytest.mark.skip
def test_rubiring_tab(browser):  # Проверка вкладки "Rubiring"
    page = Sidebar(browser, link)
    page.open()
    page.check_rubiring_tab(ppk_num)


# @pytest.mark.skip
def test_UPS_tab(browser):  # Проверка вкладки "ИБП"
    page = Sidebar(browser, link)
    page.open()
    page.check_UPS_tab(ppk_num)
    page.check_UPS_sub_tabs(ppk_num)


# @pytest.mark.skip
def test_battery_tab(browser):  # Проверка вкладки "АКБ"
    page = Sidebar(browser, link)
    page.open()
    page.check_battery_tab(ppk_num)


# @pytest.mark.skip
def test_power_tab(browser):  # Проверка вкладки "Питание"
    page = Sidebar(browser, link)
    page.open()
    page.check_power_tab(ppk_num)

# @pytest.mark.skip
def test_logger_tab(browser):  # Проверка вкладки "Журнал"
    page = Sidebar(browser, link)
    page.open()
    page.check_logger_tab(ppk_num)