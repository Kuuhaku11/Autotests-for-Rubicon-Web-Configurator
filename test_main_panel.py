from test_cases.main_panel import MainPanel # type: ignore
import pytest # type: ignore
from time import sleep


link = 'http://localhost:8082/'
version = '1.0.0.267'  # Необходимо указать актуальную версию конифгуратора для првоерки соотвествия
online = True  # True / False | Подключен ли ППК-Р (для проверки статуса)

# pytestmark = pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])

@pytest.mark.test
def test_check_tab(browser):  # Проверка title
    page = MainPanel(browser, link)
    page.open()
    sleep(3)
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
    page.close_expanded_tabs()  # Закрыть все вкладки
    page.recording_setting_for_ppk()  # Записать настройки для ППК
    page.check_record()  # Проверка начала и окончания записи в терминале
    page.open_ppk_objects()
    for i in 1, 2, 3:
        page.recording_setting_for_module(i)  # Записать настройки для указанного модуля
        page.check_record(i)

# @pytest.mark.test
def test_from_ppk_button_with_terminal(browser):  # Проверка кнопки ИЗ ППК с открытым Терминалом
    page = MainPanel(browser, link)
    page.open()


# @pytest.mark.test
def test_full_record(browser):  # Проверка полной записи в ППК
    page = MainPanel(browser, link)
    page.open()
    page.open_terminal()
    page.close_expanded_tabs()  # Закрыть все вкладки
    page.open_ppk_objects()
    page.open_module_objects(1)

    page.open_module_objects(2)

    page.open_module_objects(3)

