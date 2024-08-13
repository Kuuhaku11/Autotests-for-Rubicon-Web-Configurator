from test_cases.main_panel import MainPanel # type: ignore
import pytest # type: ignore
from time import sleep


'''Главная панель (DRBN-T52).
Предполагается проверка пустого ППК-Р с номером 1.
Некоторые тесты могут не работать, если конфигуратор уже отдельно открыт.
Установка необходимых пакетов: pip install -r requirements.txt
Команда для запуска через терминал: pytest -s -v -m 'test' .\test_main_panel.py
'''
link = 'http://localhost:8082/'
version = '1.0.0.268'  # Необходимо указать актуальную версию конифгуратора для проверки соотвествия
online = True  # True / False | Подключен ли ППК-Р (для проверки статуса)

# Количество объектов, которые будут проверятся
areas = 10  # Зоны пожаротушения
inlinks = 12  # ТС входы (6 типов)
outlinks = 9  # ТС выходы (3 типа)
BIS_Ms = 8  # БИС-Мы (4 типа)
addr_devs = 26  # Адресные устройства для двух шлейфов (13 типов)


# Для запуска тестов в двух браузерах
# pytestmark = pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])

# @pytest.mark.test
def test_title(browser):  # Проверка title
    page = MainPanel(browser, link)
    page.open()
    page.check_tab_name_on_title()  # Название вкладки
    page.check_version_on_title(version)  # Версия конфигуратора в title


# @pytest.mark.test
def test_logo(browser):  # Проверка логотипа "Рубикон"
    page = MainPanel(browser, link)
    page.open()
    page.should_be_logo()  # Есть ли лого?
    page.page_should_refresh_when_click_logo()  # Обновляется ли страница при клике на лого?


# @pytest.mark.test
def test_settings_panel(browser):  # Проверка панели настроек на наличие кнопок и орфографию
    page = MainPanel(browser, link)
    page.open()
    page.should_be_to_ppk_button()
    page.should_be_from_ppk_button()
    page.should_be_save_button()
    page.should_be_restore_button()
    page.should_be_to_file_button()
    page.should_be_to_file_for_intellect_button()
    page.should_be_from_file_button()
    page.should_be_log_button()
    page.should_be_terminal_button()
    page.should_be_light_mode_icon()


# @pytest.mark.test
def test_connection_status(browser):  # Проверка статуса подключения
    page = MainPanel(browser, link)
    page.open()
    if online:
        page.should_be_online_mark()
        page.status_should_be_online()
        page.online_mark_color_should_be_green()
    elif not online:
        page.should_be_offline_mark()
        page.status_should_be_offline()
        page.online_mark_color_should_be_yellow()


# @pytest.mark.test
def test_to_ppk_button(browser):  # Проверка кнопки В ППК с открытым Терминалом
    page = MainPanel(browser, link)
    page.open()
    page.open_terminal()
    page.recording_setting_for_ppk()  # Записать настройки для ППК
    page.check_record()  # Проверка начала и окончания записи в терминале
    page.open_ppk_objects()
    recording_setting_for_modules(page)


# @pytest.mark.test
def test_from_ppk_button(browser):  # Проверка кнопки ИЗ ППК
    page = MainPanel(browser, link)
    undoad_setting(page)


# @pytest.mark.test
def test_full_record_to_ppk(browser):  # Полная запись в ППК
    page = MainPanel(browser, link)
    page.open()
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.add_areas(areas)
    page.add_inputlink(inlinks)
    page.add_ouputlink(outlinks)
    page.open_module_objects(2)
    page.add_BIS_M(BIS_Ms)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.add_addressable_devices(1, addr_devs)  # Добавление на АШ 1 АУ каждого типа по 2 раза
    page.open_ADDRESSABLE_LOOP(2)
    page.add_addressable_devices(2, addr_devs)
    page.open_terminal()
    recording_setting_for_modules(page)


# @pytest.mark.test
def test_full_unload_from_ppk(browser):  # Полная выгрузка из ППК
    page = MainPanel(browser, link)
    undoad_setting(page)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.check_number_of_areas(areas)
    page.check_number_of_inputlink(inlinks)
    page.check_number_of_outputlink(outlinks)
    page.open_module_objects(2)
    page.check_number_of_BIS_M(BIS_Ms)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.check_number_of_addressable_devices(1, addr_devs)
    page.open_ADDRESSABLE_LOOP(2)
    page.check_number_of_addressable_devices(2, addr_devs)


# @pytest.mark.test
def test_full_rewrite(browser):  # Полная перезапись настроек
    page = MainPanel(browser, link)
    undoad_setting(page)
    page.save_settings()
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.rewrite_area_settings(areas)
    # page.rewrite_inputlink_settings(inlinks)
    # page.rewrite_outputlink_settings(outlinks)
    # page.open_module_objects(2)
    # page.rewrite_BIS_M_settings(BIS_Ms)
    # page.open_module_objects(3)
    # page.open_ADDRESSABLE_LOOP(1)
    # page.rewrite_addressable_devices_settings(1, addr_devs)
    # page.open_ADDRESSABLE_LOOP(2)
    # page.rewrite_addressable_devices_settings(2, addr_devs)
    page.open_terminal()
    recording_setting_for_modules(page)

@pytest.mark.test
def test_check_full_rewrite(browser):  # Проверка полной перезаписи настроек
    page = MainPanel(browser, link)
    undoad_setting(page)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.should_be_area_settings(areas)
    # clearing_ppk(page)


#---------------------------
def recording_setting_for_modules(page):
    page.recording_setting_for_module(1)  # Записать настройки для указанного модуля
    page.check_record('.Модуль#1(Области)')
    # page.refresh_page()  # TODO: расскоментить
    # page.open_terminal()
    # page.recording_setting_for_module(2)  # Записать настройки для указанного модуля
    # page.check_record('.Модуль#2(Выходы)')
    # page.refresh_page()
    # page.open_terminal()
    # page.recording_setting_for_module(3)  # Записать настройки для указанного модуля
    # page.check_record('.Модуль#3(Адресные шлейфы)')


def undoad_setting(page):
    page.open()
    page.open_terminal()
    page.unload_settings()  # Выгрузка настроек из ППК
    page.check_unload()
    page.close_terminal()


def clearing_ppk(page):
    page.clear_module_1()
    page.clear_module_2()
    page.clear_module_3()
    recording_setting_for_modules(page)