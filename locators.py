from selenium.webdriver.common.by import By


class MainPanelLocators():
    LOGO = (By.CSS_SELECTOR, '[alt="logo"]')
    TO_PPK_BUTTON = (By.CLASS_NAME, 'css-1661jj0')
    TO_PPK_BUTTON_IS_BLINKING = (By.CLASS_NAME, 'css-638ncg')
    FROM_PPK_BUTTON = (By.ID, 'read_config_from_ppk')
    FROM_PPK_BUTTON_IS_BLINKING = (By.CLASS_NAME, 'css-1poz9ah')
    SAVE_BUTTON = (By.ID, 'save_config_to_local_storage')
    RESTORE_BUTTON = (By.ID, 'restore_config_from_local_storage')
    TO_FILE_BUTTON = (By.CSS_SELECTOR, '.MuiToolbar-root :nth-child(8)')
    TO_FILE_FOR_INTELLECT_BUTTON = (By.CSS_SELECTOR, '[aria-label="В Файл для Интеллекта"]')
    FROM_FILE_BUTTON = (By.CSS_SELECTOR, '.MuiToolbar-root :nth-child(10)')
    LOG_BUTTON = (By.CSS_SELECTOR, '[data-testid="event_log"]')
    TERMINAL_BUTTON = (By.ID, 'terminal_open')
    CLOSE_TERMINAL_ARROW = (By.ID, 'terminal_close')
    LIGHT_MODE_ICON = (By.CSS_SELECTOR, '[data-testid="LightModeIcon"]')
    ONLINE_MARK = (By.ID, 'online_mark')
    OFFLINE_MARK = (By.CLASS_NAME, 'css-1qv5po9')
    TERMINAL_FORM = (By.CLASS_NAME, 'MuiDrawer-paperAnchorRight')
    CLOSE_EXPANDED_TABS_BUTTON = (By.ID, 'close_expanded_tabs')


class SystemObjectsLocators():
    SYSTEM_ARROW = (By.CLASS_NAME, 'css-1v19ibo')
    ACTIVE_OBJECT = (By.CLASS_NAME, 'Mui-selected')

    PPK_R_FORM_NUMB_1 = (By.XPATH, '//span[contains(text(), "#1")]')
    PPK_R_ARROW = (By.ID, 'id_expand_1_Box')

    def MODULE_FORM(module_num): return (By.ID, f'id_item_text_1_Box_Module_{module_num}_')
    def MODULE_ARROW(module_num): return (By.ID, f'id_expand_1_Box_Module_{module_num}_')

    AREA_ADD_ICON = (By.ID, 'id_add_1_Box_Module_1_Area')
    AREA_ARROW = (By.ID, 'id_expand_1_Box_Module_1_Area')
    def AREA_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_1_Area_{num}_')
    NUMBER_OF_AREAS = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_Area > span')
    DELETE_AREAS = (By.ID, 'delete_group_1_Box_Module_1_Area')

    INPUTLINK_ADD_ICON =(By.ID, 'id_add_1_Box_Module_1_InputLink')
    INPUTLINK_ARROW = (By.ID, 'id_expand_1_Box_Module_1_InputLink')
    def INPUTLINK_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_1_InputLink_{num}_')
    NUMBER_OF_INPUTLINK = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_InputLink > span')
    DELETE_INPUTLINKS = (By.ID, 'delete_group_1_Box_Module_1_InputLink')

    OUTPUTLINK_ADD_ICON =(By.ID, 'id_add_1_Box_Module_1_OutputLink')
    OUTPUTLINK_ARROW = (By.ID, 'id_expand_1_Box_Module_1_OutputLink')
    def OUTPUTLINK_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_1_OutputLink_{num}_')
    NUMBER_OF_OUTPUTLINK = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_OutputLink > span')
    DELETE_OUTPUTLINKS = (By.ID, 'delete_group_1_Box_Module_1_OutputLink')

    RS_485_ADD_ICON = (By.ID, 'id_add_1_Box_Module_2_SK')
    RS_485_ARROW = (By.ID, 'id_expand_1_Box_Module_2_SK')
    def RS_485_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_2_SK_{num}_')
    NUMBER_OF_RS_485 = (By.CSS_SELECTOR, '#badge_1_Box_Module_2_SK > span')
    DELETE_RS_485 = (By.ID, 'delete_group_1_Box_Module_2_SK')

    def ADDRESSABLE_LOOP(AL): return (By.ID, f'id_expand_1_Box_Module_3_AL_{AL}_')
    def ADDRESSABLE_DEVICES_ADD_ICON(AL): return (By.CSS_SELECTOR, f'#badge_1_Box_Module_3_AL_{AL}_AU')
    def ADDRESSABLE_DEVICES_ARROW(AL): return (By.ID, f'id_expand_1_Box_Module_3_AL_{AL}_AU')
    def ADDRESSABLE_DEVICES_ITEMS(AL, num): return (By.ID, f'id_item_text_1_Box_Module_3_AL_{AL}_AU_{num}_')
    def DELETE_ADDRESSABLE_DEVICES(AL): return (By.ID, f'delete_group_1_Box_Module_3_AL_{AL}_AU')

    SELECT_TYPE_ICON = (By.CSS_SELECTOR, '.css-sckop7 span')
    def TYPES(num): return (By.CSS_SELECTOR, f'.css-r8u8y9 :nth-child({num})')

    def DROP_DOWN_LIST(num): return (By.XPATH, f'//div[@role="presentation"]//*[{num}]')

    def RECORD_START(module): return (By.XPATH, f'//p[contains(text(), "- в ППК ППК-Р#1{module}")]')
    RECORD_FINISH = (By.XPATH, '//p[contains(text(), " - stop sending to PPK: done uploading")]')

    UNLOAD_START = (By.XPATH, '//p[contains(text(), " - start read CFG from ALL PPKR")]')
    UNLOAD_START_MODULE_1 = (By.XPATH,
        '//p[contains(text(), "- start read CFG from ППК-Р#1.Модуль#1(Области)")]')
    UNLOAD_FINISH_MODULE_1 = (By.XPATH, 
        '//p[contains(text(), " - got CFG from ППК-Р#1.Модуль#1(Области)")]')
    UNLOAD_START_MODULE_2 = (By.XPATH, 
        '//p[contains(text(), " - start read CFG from ППК-Р#1.Модуль#2(Выходы)")]')
    UNLOAD_FINISH_MODULE_2 = (By.XPATH, 
        '//p[contains(text(), " - got CFG from ППК-Р#1.Модуль#2(Выходы)")]')
    UNLOAD_START_MODULE_3 = (By.XPATH, 
        '//p[contains(text(), " - start read CFG from ППК-Р#1.Модуль#3(Адресные шлейфы)")]')
    UNLOAD_FINISH_MODULE_3 = (By.XPATH, 
        '//p[contains(text(), " - got CFG from ППК-Р#1.Модуль#3(Адресные шлейфы)")]')
    UNLOAD_FINISH = (By.XPATH, '//p[contains(text(), " - stop read CFG from ALL PPKR")]')


class AreaSettingsLocators():
    def ENTERS_THE_AREA(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_parent area')
    def DISABLE(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_ignore')
    def DELAY_IN_EVACUATION(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_delay1')
    def EXTINGUISHING_START_TIME(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_delay2')
    def EXTINGUISHING(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_extPresent')
    def GAS_OUTPUT_SIGNAL(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_needGasOk')
    def MUTUALLY_EXCLUSIVE_SR(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_interlock')
    MUTUALLY_EXCLUSIVE_SR_ARROW = (By.CSS_SELECTOR, f'input[value="нет"] + div')
    def EXTINGUISHING_BY_MFA(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_extOnMCP')
    def FORWARD_IN_RING(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_sendOnRing')
    def RETRY_DELAY(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_reQueryDelay')
    def LAUNCH_ALGORITHM(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_algorithm')
    LAUNCH_ALGORITHM_ARROW = (By.CSS_SELECTOR, f'input[value="B (перезапрос)"] + div')
    def RESET_DELAY(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_resetDelay')
    CHECKBOX_CHECKED = (By.CSS_SELECTOR, f'.Mui-checked > #')  # + {checkbox id}