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
version = '1.0.0.24'  # Необходимо указать актуальную версию конифгуратора для проверки соотвествия
online = True  # True / False | Подключен ли ППК-Р? (для проверки статуса)
headless = False  # True / False | Запуск тестов без отображения в браузере
                 # (test_from_file_button не будет работать тк дилоговое окно windows не отобразится)

ppk_num = 2  # Количество подключенных ППК-Р (Если меньше, чем по факту, остальные не будет проверяться)

# Количество объектов, которые будут проверятся
areas = 10      # Зоны пожаротушения                              | по умолчания 10 | максимум 255
inlinks = 12    # ТС входы (6 типов)                              | по умолчания 12 | максимум 511
outlinks = 9    # ТС выходы (3 типа)                              | по умолчания 9  | максимум 511
BIS_Ms = 12     # БИС-Мы (4 типа)                                 | по умолчания 12 | максимум 15
addr_devs = 26  # Адресные устройства для двух шлейфов (13 типов) | по умолчания 26 | максимум 255
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


#===================================================================================================
def recording_setting_for_modules(page):
    logger.info('Checking recording setting for all ppk')
    for ppk in range(1, ppk_num + 1):
        page.open_ppk_objects(ppk)  # Раскрыть объекты в текущем ППК
        page.save_settings()  # TODO баг, при большой конфигурации без сохранения объекты могут удалиться
        page.refresh_page()
        page.open_terminal()
        page.recording_setting_for_module(1, ppk)  # Записать настройки для указанного модуля
        page.check_record(ppk, 'Модуль#1(Области)', (areas + inlinks + outlinks) * 2)
        page.refresh_page()
        page.open_terminal()
        page.recording_setting_for_module(2, ppk)
        page.check_record(ppk, 'Модуль#2(Выходы)', BIS_Ms * 8)
        page.refresh_page()
        page.open_terminal()
        page.recording_setting_for_module(3, ppk)
        page.check_record(ppk, 'Модуль#3(Адресные шлейфы)', addr_devs * 12)
        page.close_ppk_objects(ppk)  # Свернуть объекты в текущем ППК


def unload_setting(page):
    page.open()
    page.open_terminal(ppk_num)
    page.unload_settings()  # Выгрузка настроек из ППК
    page.check_unload(areas + inlinks + outlinks, BIS_Ms * 2, addr_devs * 3, ppk_num)
    page.close_terminal()