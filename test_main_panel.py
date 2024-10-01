from test_cases.main_panel import MainPanel
import pytest
from loguru import logger
from time import sleep


#===================================================================================================
'''Главная панель (DRBN-T52).
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
    page.should_be_event_log_button()
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
    recording_setting_for_modules(page)  # Запись и проверка отдельно по трем модулям


# @pytest.mark.skip
def test_from_ppk_button(browser):  # Проверка кнопки "ИЗ ППК"
    page = MainPanel(browser, link)
    unload_setting(page)  # Выгрузка конфигурации из ППК и проверка


# @pytest.mark.skip
def test_full_record_to_ppk(browser):  # Полная запись в ППК
    page = MainPanel(browser, link)
    page.open()
    for ppk in range(1, ppk_num + 1):
        page.open_ppk_objects(ppk)
        page.open_module_objects(1, ppk)  # Раскрыть объекты в соответствующем модуле
        page.add_areas(areas, ppk)  # Добавить Зоны Пожаротушения
        page.add_inputlink(inlinks, ppk)
        page.add_ouputlink(outlinks, ppk)
        page.open_module_objects(2, ppk)
        page.add_BIS_M(BIS_Ms, ppk)
        page.open_module_objects(3, ppk)
        for AL in 1, 2:
            page.open_ADDRESSABLE_LOOP(AL, ppk)
            page.add_addressable_devices(AL, addr_devs, ppk)  # На АШ добавляются АУ каждого типа
        page.get_memory_info()
        page.close_ppk_objects(ppk)
    page.save_settings()  # TODO баг, при большой конфигурации без сохранения объекты модут удалиться
    page.refresh_page()  # При обновлении у объектов активируются настройки по умолчанию
    recording_setting_for_modules(page)


# @pytest.mark.skip
def test_full_unload_from_ppk(browser):  # Полная выгрузка из ППК
    page = MainPanel(browser, link)
    unload_setting(page)
    for ppk in range(1, ppk_num + 1):
        page.open_ppk_objects(ppk)
        page.open_module_objects(1, ppk)
        page.check_number_of_areas(areas, ppk)  # Проверка количества созданных Зон Пожаротушения
        page.check_number_of_inputlink(inlinks, ppk)
        page.check_number_of_outputlink(outlinks, ppk)
        page.open_module_objects(2, ppk)
        page.check_number_of_BIS_M(BIS_Ms, ppk)
        page.open_module_objects(3, ppk)
        for AL in 1, 2:
            page.open_ADDRESSABLE_LOOP(AL, ppk)
            page.check_number_of_addressable_devices(AL, addr_devs, ppk)
        page.close_ppk_objects(ppk)


# @pytest.mark.skip
def test_save_button(browser):  # Проверка кнопки "сохранить"
    page = MainPanel(browser, link)
    unload_setting(page)
    page.check_save_settings(areas, inlinks, outlinks, BIS_Ms, addr_devs, ppk_num)


# @pytest.mark.skip
def test_restore_button(browser):  # Проверка кнопки "восстановить"
    test_full_rewrite(browser, True)  # Измение всех настроек, без сохранения
    page = MainPanel(browser, link)
    page.restore_settings()
    for ppk in range(1, ppk_num + 1):
        page.open_ppk_objects(ppk)
        page.should_not_be_areas_settings(areas, ppk)  # Проверка, что все настройки зон стоят по умолчанию
        page.should_not_be_inputlinks_settings(inlinks, ppk)
        page.should_not_be_outputlinks_settings(outlinks, ppk)
        page.should_not_be_BIS_Ms_settings(BIS_Ms, ppk)
        page.should_not_be_addressable_devices_settings(1, addr_devs, ppk)
        page.should_not_be_addressable_devices_settings(2, addr_devs, ppk)
        page.close_ppk_objects(ppk)


# @pytest.mark.skip
def test_full_rewrite(browser, call_from_another_func=False):  # Полная перезапись настроек
    page = MainPanel(browser, link)
    unload_setting(page)
    page.save_settings()  # Нажатие кнопки "сохранить" (иначе изменения стираются)
    for ppk in range(1, ppk_num + 1):
        page.open_ppk_objects(ppk)
        page.open_module_objects(1, ppk)
        page.open_module_objects(2, ppk)
        page.open_module_objects(3, ppk)
        page.open_ADDRESSABLE_LOOP(1, ppk)
        page.open_ADDRESSABLE_LOOP(2, ppk)
        page.rewrite_areas_settings(areas, ppk)
        page.rewrite_inputlinks_settings(inlinks, areas, addr_devs, ppk)  # Изменение всех настроек всех типов ТС вход
        page.rewrite_outputlinks_settings(outlinks, areas, BIS_Ms, ppk)
        page.rewrite_BIS_Ms_settings(BIS_Ms, ppk)
        page.rewrite_addressable_devices_settings(1, addr_devs, ppk)
        page.rewrite_addressable_devices_settings(2, addr_devs, ppk)
        page.close_ppk_objects(ppk)
    page.get_memory_info()
    if call_from_another_func == False:
        recording_setting_for_modules(page)


# @pytest.mark.skip
def test_check_full_rewrite(browser, call_from_another_func=False):  # Проверка перезаписи настроек
    page = MainPanel(browser, link)
    if call_from_another_func == False:
        unload_setting(page)
    for ppk in range(1, ppk_num + 1):
        page.open_ppk_objects(ppk)
        page.open_module_objects(1, ppk)
        page.open_module_objects(2, ppk)
        page.open_module_objects(3, ppk)
        page.open_ADDRESSABLE_LOOP(1, ppk)
        page.open_ADDRESSABLE_LOOP(2, ppk)
        page.should_be_areas_settings(areas, ppk)
        page.should_be_inputlinks_settings(inlinks, areas, addr_devs, ppk)
        page.should_be_outputlinks_settings(outlinks, areas, BIS_Ms, ppk)
        page.should_be_BIS_Ms_settings(BIS_Ms, ppk)
        page.should_be_addressable_devices_settings(1, addr_devs, ppk)
        page.should_be_addressable_devices_settings(2, addr_devs, ppk)
        page.close_ppk_objects(ppk)
    page.get_memory_info()


@pytest.mark.skip
def test_to_file_and_from_file_buttons(browser):  # Проверка кнопки "в файл" и кнопки "из файла"
    page = MainPanel(browser, link)
    unload_setting(page)
    page.click_to_file_button()
    page.dismiss()
    page.click_to_file_button()
    page.accept()
    page.click_from_file_button()
    page.load_configuration_from_file()
    page.delete_config_file()
    test_check_full_rewrite(browser, True)


@pytest.mark.skip
def test_to_file_for_intellect_button(browser):  # Проверка кнопки "в файл для Интеллекта"
    page = MainPanel(browser, link)
    unload_setting(page)
    page.click_to_file_for_intellect_button()
    page.dismiss()
    page.click_to_file_for_intellect_button()
    page.accept()
    page.delete_config_for_Intellect_file()


# @pytest.mark.skip
def test_terminal(browser):  # Проверка терминала
    page = MainPanel(browser, link)
    page.open()
    page.open_terminal(ppk_num)
    page.unload_settings()
    # Проверяет наличие и орфографию сообщений создания всех типов объектов
    page.should_be_object_creation_messages(areas, inlinks, outlinks, BIS_Ms, addr_devs, ppk_num)
    page.should_be_alternating_colors_in_terminal()  # Проверка чередования цветов
    page.clearing_ppk(ppk_num)


# @pytest.mark.skip
def test_event_log(browser):  # Проверка журнала
    page = MainPanel(browser, link)
    page.open()
    page.check_column_names()
    page.check_button_to_display_number_of_events()
    page.check_value_of_columns(ppk_num)
    page.check_colors_of_the_button()


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