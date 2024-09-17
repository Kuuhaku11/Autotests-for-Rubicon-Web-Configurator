from test_cases.main_panel import MainPanel
import pytest
from time import sleep


#===================================================================================================
'''Главная панель (DRBN-T52).
Предполагается проверка пустого ППК-Р с номером 1.
Некоторые тесты не будут работать, если конфигуратор уже отдельно открыт.
Установка необходимых пакетов: pip install -r requirements.txt
Команда для запуска через терминал: pytest -s -v --tb=short .\test_main_panel.py
Для запуска запуска тестов в firefox добавить параметр: --browser_name=firefox
Для повторной проверки упавших тестов рекомендуется добавить параметр: --reruns 1
Для пропуска отдельных тестов можно раскомментировать фикстуру: @pytest.mark.skip
'''
link = 'http://localhost:8082/'
version = '1.0.0.268'  # Необходимо указать актуальную версию конифгуратора для проверки соотвествия
online = True  # True / False | Подключен ли ППК-Р? (для проверки статуса)
headless = False  # True / False | Запуск тестов без отображения в браузере
                 # (test_from_file_button не будет работать тк дилоговое окно windows не отобразится)

ppk_num = 2  # Количество подключенных ППК-Р

# Количество объектов, которые будут проверятся
areas = 10  # Зоны пожаротушения | по умолчания 10 | максимум 255
inlinks = 12  # ТС входы (6 типов) | по умолчания 12 | максимум 511
outlinks = 9  # ТС выходы (3 типа) | по умолчания 9 | максимум 511
BIS_Ms = 12  # БИС-Мы (4 типа) | по умолчания 12 | максимум 15
addr_devs = 26  # Адресные устройства для двух шлейфов (13 типов) | по умолчания 26 | максимум 255
#===================================================================================================


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
    page.open_ppk_objects()
    recording_setting_for_modules(page)  # Запись и проверка отдельно по трем модулям


# @pytest.mark.skip
def test_from_ppk_button(browser):  # Проверка кнопки "ИЗ ППК"
    page = MainPanel(browser, link)
    unload_setting(page)  # Выгрузка конфигурации из ППК и проверка


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
    page.save_settings()  # TODO баг, при большой конфигурации без сохранения объекты модут удалиться
    page.refresh_page()  # При обновлении у объектов активируются настройки по умолчанию
    recording_setting_for_modules(page)


# @pytest.mark.skip
def test_full_unload_from_ppk(browser):  # Полная выгрузка из ППК
    page = MainPanel(browser, link)
    unload_setting(page)
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
    unload_setting(page)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.open_module_objects(2)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.open_ADDRESSABLE_LOOP(2)
    page.check_save_settings(areas, inlinks, outlinks, BIS_Ms, addr_devs)


# @pytest.mark.skip
def test_restore_button(browser):  # Проверка кнопки "восстановить"
    test_full_rewrite(browser, True)  # Измение всех настроек, без сохранения
    page = MainPanel(browser, link)
    page.restore_settings()
    page.should_not_be_areas_settings(areas)  # Проверка, что все настройки зон стоят по умолчанию
    page.should_not_be_inputlinks_settings(inlinks)
    page.should_not_be_outputlinks_settings(outlinks)
    page.should_not_be_BIS_Ms_settings(BIS_Ms)
    page.should_not_be_addressable_devices_settings(1, addr_devs)
    page.should_not_be_addressable_devices_settings(2, addr_devs)


# @pytest.mark.skip
def test_full_rewrite(browser, call_from_another_func=False):  # Полная перезапись настроек
    page = MainPanel(browser, link)
    unload_setting(page)
    page.save_settings()  # Нажатие кнопки "сохранить" (иначе изменения стираются)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.open_module_objects(2)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.open_ADDRESSABLE_LOOP(2)
    page.rewrite_areas_settings(areas)
    page.rewrite_inputlinks_settings(inlinks, areas, addr_devs)  # Изменение всех настроек всех типов ТС вход
    page.rewrite_outputlinks_settings(outlinks, areas, BIS_Ms)
    page.rewrite_BIS_Ms_settings(BIS_Ms)
    page.rewrite_addressable_devices_settings(1, addr_devs)
    page.rewrite_addressable_devices_settings(2, addr_devs)
    if call_from_another_func == False:
        recording_setting_for_modules(page)


# @pytest.mark.skip
def test_check_full_rewrite(browser, call_from_another_func=False):  # Проверка перезаписи настроек
    page = MainPanel(browser, link)
    if call_from_another_func == False:
        unload_setting(page)
    page.open_ppk_objects()
    page.open_module_objects(1)
    page.open_module_objects(2)
    page.open_module_objects(3)
    page.open_ADDRESSABLE_LOOP(1)
    page.open_ADDRESSABLE_LOOP(2)
    page.should_be_areas_settings(areas)
    page.should_be_inputlinks_settings(inlinks, areas, addr_devs)
    page.should_be_outputlinks_settings(outlinks, areas, BIS_Ms)
    page.should_be_BIS_Ms_settings(BIS_Ms)
    page.should_be_addressable_devices_settings(1, addr_devs)
    page.should_be_addressable_devices_settings(2, addr_devs)


# @pytest.mark.skip
def test_to_file_button(browser):  # Проверка кнопки "в файл"
    page = MainPanel(browser, link)
    unload_setting(page)
    page.click_to_file_button()
    page.dismiss()
    page.click_to_file_button()
    page.accept()


# @pytest.mark.skip
def test_to_file_for_intellect_button(browser):  # Проверка кнопки "в файл для Интеллекта"
    page = MainPanel(browser, link)
    unload_setting(page)
    page.click_to_file_for_intellect_button()
    page.dismiss()
    page.click_to_file_for_intellect_button()
    page.accept()
    page.delete_config_for_Intellect_file()


# @pytest.mark.skip
def test_from_file_button(browser):  # Проверка кнопки "из файла"
    page = MainPanel(browser, link)
    page.open()
    page.click_from_file_button()
    page.load_configuration_from_file()
    page.delete_config_file()
    test_check_full_rewrite(browser, True)


# @pytest.mark.skip
def test_terminal(browser):  # Проверка терминала
    page = MainPanel(browser, link)
    unload_setting(page)
    # Проверяет наличие и орфографию сообщений создания всех типов объектов
    page.should_be_object_creation_messages(areas, inlinks, outlinks, BIS_Ms, addr_devs)
    page.should_be_alternating_colors_in_terminal()  # Проверка чередования цветов
    page.clearing_ppk()


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
    page.save_settings()  # TODO баг, при большой конфигурации без сохранения объекты модут удалиться
    page.refresh_page()
    page.open_terminal()
    page.recording_setting_for_module(1)  # Записать настройки для указанного модуля
    page.check_record('Модуль#1(Области)', (areas + inlinks + outlinks) * 2)
    page.refresh_page()
    page.open_terminal()
    page.recording_setting_for_module(2)  # Записать настройки для указанного модуля
    page.check_record('Модуль#2(Выходы)', BIS_Ms * 8)
    page.refresh_page()
    page.open_terminal()
    page.recording_setting_for_module(3)  # Записать настройки для указанного модуля
    page.check_record('Модуль#3(Адресные шлейфы)', addr_devs * 12)


def unload_setting(page):
    page.open()
    page.open_terminal()
    page.unload_settings()  # Выгрузка настроек из ППК
    page.check_unload((areas + inlinks + outlinks) * 2, BIS_Ms * 2, addr_devs * 3)
    page.close_terminal()