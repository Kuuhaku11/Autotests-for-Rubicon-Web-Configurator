from main_page import Page # type: ignore
from locators import MainPanelLocators, SystemObjectsLocators, AreaSettingsLocators # type: ignore
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


class MainPanel(Page):  # Класс для тестирования по тест-кейсу "Главная панель" (DRBN-T52)

# Общие функции
    def check_presence_and_spelling(self, locator, button_name):
        assert self.is_element_present(*locator), \
            f'Button "{button_name}" is not presented'
        button_text = self.browser.find_element(*locator).text
        assert button_text == button_name, \
            f'Button "{button_name}" has a spelling error, button text: {button_text}'

    # Проверка на наличие элемента и орфографические ошибки
    def presence_and_spelling(self, locator, button_name):
        print(f'Checking the button "{button_name}"...')
        try:
            self.check_presence_and_spelling(locator, button_name)
        except StaleElementReferenceException:  # Firefox выдает ошибку из-за обновления элементов
            self.check_presence_and_spelling(locator, button_name)

    def refresh_page(self):
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого

    def open_terminal(self):
        sleep(0.3)  # f
        self.browser.find_element(*MainPanelLocators.TERMINAL_BUTTON).click()
        assert self.is_element_present(*MainPanelLocators.TERMINAL_FORM), \
            'Terminal does not open'
    
    def close_terminal(self):
        sleep(1)
        self.browser.find_element(*MainPanelLocators.CLOSE_TERMINAL_ARROW).click()
        assert self.is_element_present(*MainPanelLocators.CLOSE_TERMINAL_ARROW), \
            'Terminal does not close'

    def open_ppk_objects(self):
        self.browser.find_element(*SystemObjectsLocators.PPK_R_ARROW).click()

    def open_module_objects(self, module_num):
        self.browser.find_element(*SystemObjectsLocators.MODULE_ARROW(module_num)).click()

    def close_expanded_tabs(self):  # Закрыть все вкладки
        self.browser.find_element(*MainPanelLocators.CLOSE_EXPANDED_TABS_BUTTON).click()

    def save_settings(self):
        self.browser.find_element(*MainPanelLocators.SAVE_BUTTON).click()


# Проверка title
    def check_tab_name_on_title(self):  # Название вкладки
        print('Checking the title...')
        title = self.browser.title
        assert title.split()[0] == 'Веб-конфигуратор', \
            f'The tab name in the title does not match, expected "Веб-конфигуратор"'

    def check_version_on_title(self, version):  # Номер версии конфигуратора в title
        title = self.browser.title
        assert title.split()[1] == version, \
            f'The configurator version in the title does not match, expected "{version}"'


# Проверка логотипа "Рубикон"
    def should_be_logo(self):
        print('Checking the logo...')
        assert self.is_element_present(*MainPanelLocators.LOGO), 'Logo is not presented'
        assert self.is_element_visible(*MainPanelLocators.LOGO), \
            'Logo is not displayed'
    
    def page_should_refresh_when_click_logo(self):  # Обновляется ли страница при клике на лого?
        self.close_expanded_tabs()  # Закрыть все вкладки
        self.browser.find_element(*SystemObjectsLocators.SYSTEM_ARROW).click()  # Скрываем объекты
        self.browser.find_element(*MainPanelLocators.LOGO).click()  # Нажимаем на лого
        assert self.browser.find_element(*SystemObjectsLocators.PPK_R_FORM_NUMB_1).is_displayed(), \
            'Page has not been refresh, system elements are visible'


# Проверка панели настроек
    def should_be_to_ppk_button(self):
        self.presence_and_spelling(MainPanelLocators.TO_PPK_BUTTON, 'В ППК')

    def should_be_from_ppk_button(self):
        self.presence_and_spelling(MainPanelLocators.FROM_PPK_BUTTON, 'ИЗ ППК')
    
    def should_be_save_button(self):
        self.presence_and_spelling(MainPanelLocators.SAVE_BUTTON, 'СОХРАНИТЬ')

    def should_be_restore_button(self):
        self.presence_and_spelling(MainPanelLocators.RESTORE_BUTTON, 'ВОССТАНОВИТЬ')

    def should_be_to_file_button(self):
        self.presence_and_spelling(MainPanelLocators.TO_FILE_BUTTON, 'В ФАЙЛ')

    def should_be_to_file_for_intellect_button(self):
        print('Checking the button "В Файл для Интеллекта"...')
        assert self.is_element_present(*MainPanelLocators.TO_FILE_FOR_INTELLECT_BUTTON), \
            'Button "В Файл для Интеллекта" is not presented'

    def should_be_from_file_button(self):
        self.presence_and_spelling(MainPanelLocators.FROM_FILE_BUTTON, 'ИЗ ФАЙЛА')
    
    def should_be_log_button(self):
        self.presence_and_spelling(MainPanelLocators.LOG_BUTTON, 'ЖУРНАЛ')
        
    def should_be_terminal_button(self):
        self.presence_and_spelling(MainPanelLocators.TERMINAL_BUTTON, 'ТЕРМИНАЛ')

    def should_be_light_mode_icon(self):
        print('Checking the light mode icon...')
        assert self.is_element_present(*MainPanelLocators.LIGHT_MODE_ICON), \
            'Icon "Light Mode" is not presented'


# Проверка статуса подключения
    def should_be_online_mark(self):
        print('Checking online status...')
        assert self.is_element_present(*MainPanelLocators.ONLINE_MARK), \
            'Online mark is not presented'
    
    def status_should_be_online(self):
        status = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).text
        assert status == 'online', f'Connection status not "online", status: {status}'

    def online_mark_color_should_be_green(self):
        color = self.browser.find_element(*MainPanelLocators.ONLINE_MARK).value_of_css_property('color')
        assert '0, 230, 118' in color, \
            f'Connection status color is not green: "rgb(0, 230, 118)", color: {color}'
    
    def should_be_offline_mark(self):
        print('Checking offline status...')
        assert self.is_element_present(*MainPanelLocators.OFFLINE_MARK), \
            'Offline mark is not presented'
    
    def status_should_be_offline(self):
        status = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).text
        assert status == 'offline', f'Connection status not "offline", status: {status}'

    def online_mark_color_should_be_yellow(self):
        color = self.browser.find_element(*MainPanelLocators.OFFLINE_MARK).value_of_css_property('color')
        assert color == 'rgba(255, 215, 64, 1)', \
            f'Connection status color is not yellow: "rgba(255, 215, 64, 1)", color: {color}'


# Проверка кнопки В ППК с открытым Терминалом
    def recording_setting_for_ppk(self):
        print('Checking recording setting for ppk...')
        self.browser.find_element(*SystemObjectsLocators.PPK_R_FORM_NUMB_1).click()  # ППК стал активным
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК

    def recording_setting_for_module(self, module_num):  # Модуль Области стал активным
        print(f'Checking recording setting for module {module_num}...')
        self.browser.find_element(*SystemObjectsLocators.MODULE_FORM(module_num)).click()
        assert self.is_element_clickable(*MainPanelLocators.TO_PPK_BUTTON), \
            'Nutton "В ППК" is not clickable'
        self.browser.find_element(*MainPanelLocators.TO_PPK_BUTTON).click()  # Начать запись В ППК
        assert self.is_element_present(*MainPanelLocators.TO_PPK_BUTTON_IS_BLINKING), \
            'Nutton "В ППК" does not blink'

    def check_record(self, module=''):
        print(f'Checking start and finish of recording for {'ppk' if module == '' else module[1:]}...')
        assert self.is_element_present(*SystemObjectsLocators.RECORD_START(module)), \
            f'Recording for {'ppk' if module == '' else module[1:]} has not started'
        flag = self.is_element_visible(*SystemObjectsLocators.RECORD_FINISH, 180)  # Ожидание 3 мин
        assert flag, f'Recording for {'ppk' if module == '' else module[1:]} has not finished'


# Проверка кнопки ИЗ ППК
    def unload_settings(self):
        print(f'Checking unloading settings from ppk...')
        sleep(1)
        self.browser.find_element(*MainPanelLocators.FROM_PPK_BUTTON).click()
        assert self.is_element_present(*MainPanelLocators.FROM_PPK_BUTTON_IS_BLINKING), \
            'Button "ИЗ ППК" does not blink'

    def check_unload(self):
        print(f'Checking start and finish of unloading for ppk and moduls...')
        assert self.is_element_present(*SystemObjectsLocators.UNLOAD_START), \
            f'Unload for all ppkr has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_1, 30), \
            f'Unload for module 1 has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH_MODULE_1, 30), \
            f'Unload for module 1 has not finished or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_2, 30), \
            f'Unload for module 2 has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH_MODULE_2, 30), \
            f'Unload for module 2 has not finished or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_START_MODULE_3, 30), \
            f'Unload for module 3 has not started or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH_MODULE_3, 30), \
            f'Unload for module 3 has not finished or there is a spelling error'
        assert self.is_element_visible(*SystemObjectsLocators.UNLOAD_FINISH, 30), \
            f'Unload for all ppkr has not finished or there is a spelling error'


# Проверка полной записи в ППК
    def add_areas(self, areas):
        print(f'Creating {areas} areas...')
        for _ in range(areas):  # Создать Зоны пожаротушения
            self.browser.find_element(*SystemObjectsLocators.AREA_ADD_ICON).click()

    def add_inputlink(self, inlinks):
        print(f'Creating {inlinks} inputlinks...')
        for i in range(inlinks):  # Создать ТС входы
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ARROW).click()  # Список входов
        for i in range(inlinks):  # Сделать ТС входы каждого типа
            self.browser.find_element(*SystemObjectsLocators.INPUTLINK_ITEMS(i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 6 + 1)).click()  # Изменить тип входа
            sleep(0.1)  # f

    def add_ouputlink(self, outlinks):
        print(f'Creating {outlinks} outputlinks...')
        for i in range(outlinks):  # Создать ТС выходы
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ARROW).click()  # Список выходов
        for i in range(outlinks):  # Сделать ТС выходы каждого типа
            self.browser.find_element(*SystemObjectsLocators.OUTPUTLINK_ITEMS(i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 3 + 1)).click()  # Изменить тип выхода
            sleep(0.1)  # f
        
    
    def add_BIS_M(self, BIS_Ms):
        print(f'Creating {BIS_Ms} BIS M...')
        for i in range(BIS_Ms):  # Создать БИС-Мы
            self.browser.find_element(*SystemObjectsLocators.RS_485_ADD_ICON).click()
        self.browser.find_element(*SystemObjectsLocators.RS_485_ARROW).click()  # Список БИС-М
        for i in range(BIS_Ms):  # Сделать БИС-Мы каждого типа
            self.browser.find_element(*SystemObjectsLocators.RS_485_ITEMS(i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 4 + 1)).click()  # Изменить тип выхода
            sleep(0.1)  # f
    
    def open_ADDRESSABLE_LOOP(self, AL):
        assert self.is_element_clickable(*SystemObjectsLocators.ADDRESSABLE_LOOP(AL)), \
            'Addressable loop arrow is not clickable'
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_LOOP(AL)).click()

    def add_addressable_devices(self, AL, addr_devs):
        print(f'Creating {addr_devs} addressable devices on addressable loop {AL}...')
        for i in range(addr_devs):  # Создать АУ
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL)).click()
        self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ARROW(AL)).click()
        for i in range(addr_devs):  # Сделать АУ каждого типа
            self.browser.find_element(*SystemObjectsLocators.ADDRESSABLE_DEVICES_ITEMS(AL, i + 1)).click()
            self.browser.find_element(*SystemObjectsLocators.SELECT_TYPE_ICON).click()
            self.browser.find_element(*SystemObjectsLocators.TYPES(i % 13 + 1)).click()  # Изменить тип выхода
            sleep(0.15)  # f


# Полная выгрузка из ППК
    def check_number_of_areas(self, areas):
        print(f'Checking number of areas...')
        assert str(areas) == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_AREAS).text, \
            f'Number of areas is not equal {areas}'

    def check_number_of_inputlink(self, inlinks):
        print(f'Checking number of inlinks...')
        assert str(inlinks) == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_INPUTLINK).text, \
            f'Number of inputlinks is not equal {inlinks}'

    def check_number_of_outputlink(self, outlinks):
        print(f'Checking number of outlinks...')
        assert str(outlinks) == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_OUTPUTLINK).text, \
            f'Number of outputlinks is not equal {outlinks}'

    def check_number_of_BIS_M(self, BIS_Ms):
        print(f'Checking number of BIS_Ms...')
        assert str(BIS_Ms) == self.browser.find_element(*SystemObjectsLocators.NUMBER_OF_RS_485).text, \
            f'Number of BIS_M is not equal {BIS_Ms}'

    def check_number_of_addressable_devices(self, AL, addr_devs):
        print(f'Checking number of addr_devs...')
        assert str(addr_devs) == self.browser.find_element(
            *SystemObjectsLocators.ADDRESSABLE_DEVICES_ADD_ICON(AL)).text, \
            f'Number of addressable_devices on {AL} loop is not equal {addr_devs}'


# Полной перезаписи настроек ранее добавленных объектов
    def rewrite_area_settings(self, areas):
        print(f'Rewrite settings in {areas} areas...')
        self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()
        for area_num in range(1, areas):
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(area_num)).click()
            self.browser.execute_script("window.scrollBy(0, -500);")  # Прокрутка страницы
            self.browser.find_element(*AreaSettingsLocators.ENTERS_THE_AREA(area_num)).click()
            self.browser.find_element(*SystemObjectsLocators.DROP_DOWN_LIST(areas - 1)).click()
            self.browser.find_element(*AreaSettingsLocators.DISABLE(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.DELAY_IN_EVACUATION(area_num)
                                      ).send_keys(123456)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING_START_TIME(area_num)
                                      ).send_keys(123456)
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.GAS_OUTPUT_SIGNAL(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR_ARROW).click()
            self.browser.find_element(*SystemObjectsLocators.DROP_DOWN_LIST(2)).click()
            self.browser.find_element(*AreaSettingsLocators.EXTINGUISHING_BY_MFA(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.FORWARD_IN_RING(area_num)).click()
            self.browser.find_element(*AreaSettingsLocators.RETRY_DELAY(area_num)
                                      ).send_keys(123456)
            self.browser.find_element(*AreaSettingsLocators.LAUNCH_ALGORITHM_ARROW).click()
            self.browser.find_element(*SystemObjectsLocators.DROP_DOWN_LIST(3)).click()
            self.browser.find_element(*AreaSettingsLocators.RESET_DELAY(area_num)
                                      ).send_keys(123456)


# Проверка полной перезаписи настроек
    def should_be_area_settings(self, areas):
        print(f'Check settings in {areas} areas...')
        self.browser.find_element(*SystemObjectsLocators.AREA_ARROW).click()
        for area_num in range(1, areas):
            self.browser.find_element(*SystemObjectsLocators.AREA_ITEMS(area_num)).click()
            value = self.browser.find_element(
                *AreaSettingsLocators.ENTERS_THE_AREA(area_num)).get_attribute('value')
            assert f'#{areas} Зона Пожаротушения ' == value, \
                f'"входит в область" setting in area {area_num} does not match, expected ' \
                f'"#{areas} Зона Пожаротушения ", value received "{value}"'
            assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
                AreaSettingsLocators.CHECKBOX_CHECKED[1] + AreaSettingsLocators.DISABLE(area_num)[1]), \
                f'Checkbox "отключен" in area {area_num} is unchecked, expected to be checked'
            value = self.browser.find_element(
                *AreaSettingsLocators.DELAY_IN_EVACUATION(area_num)).get_attribute('value')
            assert f'1800' == value, f'"задержка эвакуации" setting in area {area_num} '\
                f'does not match, expected "1800", value received "{value}"'
            value = self.browser.find_element(
                *AreaSettingsLocators.EXTINGUISHING_START_TIME(area_num)).get_attribute('value')
            assert f'255' == value, f'"время пуска тушения" setting in area {area_num} '\
                f'does not match, expected "255", value received "{value}"'
            assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
                AreaSettingsLocators.CHECKBOX_CHECKED[1] + AreaSettingsLocators.EXTINGUISHING(area_num)[1]), \
                f'Checkbox "есть пожаротушение" in area {area_num} is unchecked, expected to be checked'     
            assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
                AreaSettingsLocators.CHECKBOX_CHECKED[1] + AreaSettingsLocators.GAS_OUTPUT_SIGNAL(area_num)[1]), \
                f'Checkbox "требуется сигнал выхода газа" in area {area_num} is unchecked, expected to be checked'
            value = self.browser.find_element(
                *AreaSettingsLocators.MUTUALLY_EXCLUSIVE_SR(area_num)).get_attribute('value')
            assert f'интерлок' == value, f'"взаимно исключает ДУ" setting in area {area_num} '\
                f'does not match, expected "интерлок", value received "{value}"'
            assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
                AreaSettingsLocators.CHECKBOX_CHECKED[1] + 
                AreaSettingsLocators.EXTINGUISHING_BY_MFA(area_num)[1]), \
                f'Checkbox "тушение по ИПР" in area {area_num} is unchecked, expected to be checked'
            assert self.is_element_present(AreaSettingsLocators.CHECKBOX_CHECKED[0],
                AreaSettingsLocators.CHECKBOX_CHECKED[1] + AreaSettingsLocators.FORWARD_IN_RING(area_num)[1]), \
                f'Checkbox "пересылать по кольцу" in area {area_num} is unchecked, expected to be checked'
            value = self.browser.find_element(
                *AreaSettingsLocators.RETRY_DELAY(area_num)).get_attribute('value')
            assert f'16383' == value, f'"задержка перезапроса" setting in area {area_num} '\
                f'does not match, expected "16383", value received "{value}"'
            value = self.browser.find_element(
                *AreaSettingsLocators.LAUNCH_ALGORITHM(area_num)).get_attribute('value')
            assert f'C1 (две сработки)' == value, f'"алгоритм ЗКПС" setting in area {area_num} '\
                f'does not match, expected "C1 (две сработки)", value received "{value}"'
            value = self.browser.find_element(
                *AreaSettingsLocators.RESET_DELAY(area_num)).get_attribute('value')
            assert f'16383' == value, f'"задержка сброса" setting in area {area_num} '\
                f'does not match, expected "16383", value received "{value}"'


    
# Очистка ППК от объектов
    def clear_module_1(self):  # Полное независимое удаление всех объектов модуля Области
        print(f'Clearing module 1...')
        if self.is_element_present(*SystemObjectsLocators.DELETE_AREAS):
            self.browser.find_element(*SystemObjectsLocators.DELETE_AREAS).click()
        if self.is_element_present(*SystemObjectsLocators.DELETE_INPUTLINKS):
            self.browser.find_element(*SystemObjectsLocators.DELETE_INPUTLINKS).click()
        if self.is_element_present(*SystemObjectsLocators.DELETE_OUTPUTLINKS):
            self.browser.find_element(*SystemObjectsLocators.DELETE_OUTPUTLINKS).click()
    
    def clear_module_2(self):  # Полное независимое удаление всех объектов модуля Выходы
        print(f'Clearing module 2...')
        if self.is_element_present(*SystemObjectsLocators.DELETE_RS_485):
            self.browser.find_element(*SystemObjectsLocators.DELETE_RS_485).click()
    
    def clear_module_3(self):  # Полное независимое удаление всех объектов модуля Адресные шлейфы
        print(f'Clearing module 3...')
        if self.is_element_present(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(1)):
            self.browser.find_element(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(1)).click()
        if self.is_element_present(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(2)):
            self.browser.find_element(*SystemObjectsLocators.DELETE_ADDRESSABLE_DEVICES(2)).click()