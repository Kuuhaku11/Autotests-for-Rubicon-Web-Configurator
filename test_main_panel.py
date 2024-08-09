from test_cases.main_panel import MainPanel # type: ignore
import pytest # type: ignore
from time import sleep


'''DRBN-T52.
Предполагается проверка пустого ППК с номером 1.
Некоторые тесты могут не работать, если конфигуратор уже отдельно открыт.
Команда для запуска через консоль: pytest -s -v -m 'test' .\test_main_panel.py
'''
link = 'http://localhost:8082/'
version = '1.0.0.268'  # Необходимо указать актуальную версию конифгуратора для проверки соотвествия
online = True  # True / False | Подключен ли ППК-Р (для проверки статуса)

# Для запуска тестов в нескольких браузерах
# pytestmark = pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])

# @pytest.mark.test
def test_check_tab(browser):  # Проверка title
    page = MainPanel(browser, link)
    page.open()
    page.check_tab_name_on_title()  # Название вкладки
    page.check_version_on_title(version)  # Версия конфигуратора в title

# @pytest.mark.test
def test_logo(browser):  # Проверка логотипа "Рубикон"
    page = MainPanel(browser, link)
    page.open()
    page.should_be_logo()  # Есть ли лого?
    page.does_page_refresh_when_click_logo()  # Обновляется ли страница при клике на лого?

# @pytest.mark.test
def test_check_settings_panel(browser):  # Проверка панели настроек на наличие кнопок и орфографию
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
def test_check_connection_status(browser):  # Проверка статуса подключения
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
def test_to_ppk_button_with_terminal(browser):  # Проверка кнопки В ППК с открытым Терминалом
    page = MainPanel(browser, link)
    page.open()
    page.open_terminal()
    page.recording_setting_for_ppk()  # Записать настройки для ППК
    page.check_record()  # Проверка начала и окончания записи в терминале
    page.open_ppk_objects()
    recording_setting_for_modules(page)

# @pytest.mark.test
def test_check_unload(browser):
    page = MainPanel(browser, link)
    page.open()
    page.open_terminal()
    page.unload_settings()  # Выгрузка настроек из ППК
    page.check_unload()

@pytest.mark.test
class TestFullRecord():
    def test_full_record(self, browser):  # Проверка полной записи в ППК
        page = MainPanel(browser, link)
        page.open()
        page.open_ppk_objects()
        page.open_module_objects(1)
        page.add_10_areas()
        page.add_12_inputlink()
        page.add_9_ouputlink()
        page.open_module_objects(2)
        page.add_8_BIS_M()
        page.open_module_objects(3)
        page.open_ADDRESSABLE_LOOP(1)
        page.add_26_addressable_devices(1)  # Добавление на АШ 1 АУ каждого типа по 2 раза
        page.open_ADDRESSABLE_LOOP(2)
        page.add_26_addressable_devices(2)
        page.open_terminal()
        recording_setting_for_modules(page)

    def test_update_and_check_unload_and_clear(self, browser):
        page = MainPanel(browser, link)
        page.open()
        page.open_terminal()
        page.unload_settings()  # Выгрузка настроек из ППК
        page.check_unload()
        page.open_ppk_objects()
        page.open_module_objects(1)
        page.open_module_objects(2)
        page.open_module_objects(3)
        page.open_ADDRESSABLE_LOOP(1)
        page.open_ADDRESSABLE_LOOP(2)
        page.check_number_of_objects()
        page.clear_module_1()
        page.clear_module_2()
        page.clear_module_3()
        recording_setting_for_modules(page)


def recording_setting_for_modules(page):
    page.recording_setting_for_module(1)  # Записать настройки для указанного модуля
    page.check_record('.Модуль#1(Области)')
    page.refresh_page()
    page.open_terminal()
    page.recording_setting_for_module(2)  # Записать настройки для указанного модуля
    page.check_record('.Модуль#2(Выходы)')
    page.refresh_page()
    page.open_terminal()
    page.recording_setting_for_module(3)  # Записать настройки для указанного модуля
    page.check_record('.Модуль#3(Адресные шлейфы)')