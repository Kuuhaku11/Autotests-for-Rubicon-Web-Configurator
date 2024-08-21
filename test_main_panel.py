from test_cases.main_panel import MainPanel # type: ignore
import pytest # type: ignore
from time import sleep


#___________________________________________________________________________________________________
'''Главная панель (DRBN-T52).
Предполагается проверка пустого ППК-Р с номером 1.
Некоторые тесты не будут работать, если конфигуратор уже отдельно открыт.
Установка необходимых пакетов: pip install -r requirements.txt
Команда для запуска через терминал: pytest -s -v .\test_main_panel.py
Для запуска запуска тестов в firefox добавить параметр: --browser_name=firefox
Для пропуска отдельных тестов можно раскомментировать фикстуру: @pytest.mark.skip
'''
link = 'http://localhost:8082/'
version = '1.0.0.268'  # Необходимо указать актуальную версию конифгуратора для проверки соотвествия
online = True  # True / False | Подключен ли ППК-Р? (для проверки статуса)
headless = False  # True / False | Запуск тестов без отображения в браузере
display_cursor = True  # True / False | Отображение движений курсора

# Количество объектов, которые будут проверятся
areas = 10  # Зоны пожаротушения | по умолчания 10
inlinks = 12  # ТС входы (6 типов) | по умолчания 12
outlinks = 9  # ТС выходы (3 типа) | по умолчания 9
BIS_Ms = 12  # БИС-Мы (4 типа) | по умолчания 12
addr_devs = 26  # Адресные устройства для двух шлейфов (13 типов) | по умолчания 26
#___________________________________________________________________________________________________


pytestmark = pytest.mark.parametrize('headless', [headless])

# @pytest.mark.skip
def test_title(browser):  # Проверка title
    page = MainPanel(browser, link)
    page.open()
    page.check_tab_name_on_title()  # Название вкладки
    page.check_version_on_title(version)  # Версия конфигуратора в title


# @pytest.mark.skip
def test_logo(browser):  # Проверка логотипа "Рубикон"
    page = MainPanel(browser, link)
    page.open()
    page.should_be_logo()  # Есть ли лого?
    page.page_should_refresh_when_click_logo()  # Обновляется ли страница при клике на лого?


# @pytest.mark.skip
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


# @pytest.mark.skip
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


# @pytest.mark.skip
def test_to_ppk_button(browser):  # Проверка кнопки "В ППК" с открытым Терминалом
    page = MainPanel(browser, link)
    page.open()
    page.open_terminal()
    page.recording_setting_for_ppk()  # Запись настроек для ППК
    page.close_terminal()
    page.check_record()  # Проверка начала и окончания записи в терминале
    page.open_ppk_objects()
    recording_setting_for_modules(page)  # Запись и проверка отдельно по трем модулям


# @pytest.mark.skip
def test_from_ppk_button(browser):  # Проверка кнопки "ИЗ ППК"
    page = MainPanel(browser, link)
    undoad_setting(page)  # Выгрузка конфигурации из ППК и проверка


# @pytest.mark.skip
def test_full_record_to_ppk(browser):  # Полная запись в ППК
    page = MainPanel(browser, link)
    page.open()
    page.open_ppk_objects()  # Раскрыть объекты в ППК
    page.open_module_objects(1)  # Раскрыть объекты в соответствующем модуле
    page.add_areas(areas)  # Добавить Зоны Пожаротушения
    page.add_inputlink(inlinks)
    page.add_ouputlink(outlinks)
    page.open_module_objects(2)
    page.add_BIS_M(BIS_Ms)
    page.open_module_objects(3)
    for AL in 1, 2:
        page.open_ADDRESSABLE_LOOP(AL)
        page.add_addressable_devices(AL, addr_devs)  # На АШ добавляются АУ каждого типа
    recording_setting_for_modules(page)


# @pytest.mark.skip
def test_full_unload_from_ppk(browser):  # Полная выгрузка из ППК
    page = MainPanel(browser, link)
    undoad_setting(page)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.check_number_of_areas(areas)  # Проверка количества созданных Зон Пожаротушения
    page.check_number_of_inputlink(inlinks)
    page.check_number_of_outputlink(outlinks)
    page.open_module_objects(2)
    page.check_number_of_BIS_M(BIS_Ms)
    page.open_module_objects(3)
    for AL in 1, 2:
        page.open_ADDRESSABLE_LOOP(AL)
        page.check_number_of_addressable_devices(AL, addr_devs)


# @pytest.mark.skip
def test_save_button(browser):  # Проверка кнопки "сохранить"
    page = MainPanel(browser, link)
    undoad_setting(page)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.open_module_objects(2)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.open_ADDRESSABLE_LOOP(2)
    page.check_save_settings()


# @pytest.mark.skip
def test_restore_button(browser):  # Проверка кнопки "восстановить"
    page = test_full_rewrite(browser, 1)
    page.restore_settings()
    page.should_not_be_areas_settings(areas)
    page.should_not_be_inputlinks_settings(inlinks)
    page.should_not_be_outputlinks_settings(outlinks)
    page.should_not_be_BIS_Ms_settings(BIS_Ms)
    page.should_not_be_addressable_devices_settings(1, addr_devs)
    page.should_not_be_addressable_devices_settings(2, addr_devs)


# @pytest.mark.skip
def test_full_rewrite(browser, flag=0):  # Полная перезапись настроек
    page = MainPanel(browser, link)
    undoad_setting(page)
    page.save_settings()  # Нажатие кнопки "сохранить" (иначе изменения стираются)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.open_module_objects(2)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.open_ADDRESSABLE_LOOP(2)
    page.rewrite_areas_settings(areas)
    page.rewrite_inputlinks_settings(inlinks, areas)  # Измение всех настроек всех типов ТС вход
    page.rewrite_outputlinks_settings(outlinks, areas)
    page.rewrite_BIS_Ms_settings(BIS_Ms)
    page.rewrite_addressable_devices_settings(1, addr_devs)
    page.rewrite_addressable_devices_settings(2, addr_devs)
    if flag == 0:
        recording_setting_for_modules(page)
    else:
        return page


# @pytest.mark.skip
def test_check_full_rewrite(browser):  # Проверка полной перезаписи настроек
    page = MainPanel(browser, link)
    undoad_setting(page)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.open_module_objects(2)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.open_ADDRESSABLE_LOOP(2)
    page.should_be_areas_settings(areas)
    page.should_be_inputlinks_settings(inlinks, areas)
    page.should_be_outputlinks_settings(outlinks, areas)
    page.should_be_BIS_Ms_settings(BIS_Ms)
    page.should_be_addressable_devices_settings(1, addr_devs)
    page.should_be_addressable_devices_settings(2, addr_devs)
    clearing_ppk(page)


#___________________________________________________________________________________________________
def recording_setting_for_modules(page):
    page.refresh_page()
    page.open_terminal()
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


def undoad_setting(page):
    page.open()
    page.open_terminal()
    page.unload_settings()  # Выгрузка настроек из ППК
    page.check_unload()  # Проверка выгрузки (сообщения о начале и окончании выгрузки всех модулей)
    page.close_terminal()


def clearing_ppk(page):
    page.open_terminal()
    page.clear_module_1()
    page.clear_module_2()
    page.clear_module_3()
    recording_setting_for_modules(page)