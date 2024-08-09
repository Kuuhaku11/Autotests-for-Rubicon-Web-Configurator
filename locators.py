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
    LIGHT_MODE_ICON = (By.CSS_SELECTOR, '[data-testid="LightModeIcon"]')
    ONLINE_MARK = (By.ID, 'online_mark')
    OFFLINE_MARK = (By.CLASS_NAME, 'css-1qv5po9')
    TERMINAL_FORM = (By.CLASS_NAME, 'MuiDrawer-paperAnchorRight')
    CLOSE_EXPANDED_TABS_BUTTON = (By.ID, 'close_expanded_tabs')


class SystemObjectsLocators():
    SYSTEM_ARROW = (By.CLASS_NAME, 'css-1v19ibo')
    ACTIVE_OBJECT = (By.CLASS_NAME, 'Mui-selected')

    PPK_R_FORM = (By.ID, 'ppk_1_Box')  # Первый ППК по списку (не используется)
    PPK_R_FORM_NUMB_1 = (By.XPATH, '//span[contains(text(), "#1")]')
    PPK_R_ARROW = (By.ID, 'id_expand_1_Box')

    MODULE_FORM = (By.ID, 'id_item_text_1_Box_Module_')  # + {num}_
    MODULE_ARROW = (By.ID, 'id_expand_1_Box_Module_')  # + {num}_

    AREA_ADD_ICON = (By.ID, 'id_add_1_Box_Module_1_Area')
    NUMBER_OF_AREAS = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_Area > span')
    DELETE_AREAS = (By.ID, 'delete_group_1_Box_Module_1_Area')

    INPUTLINK_ADD_ICON =(By.ID, 'id_add_1_Box_Module_1_InputLink')
    INPUTLINK_ARROW = (By.ID, 'id_expand_1_Box_Module_1_InputLink')
    INPUTLINK_ITEMS = (By.ID, 'id_item_text_1_Box_Module_1_InputLink_')  # + {num}_
    NUMBER_OF_INPUTLINK = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_InputLink > span')
    DELETE_INPUTLINKS = (By.ID, 'delete_group_1_Box_Module_1_InputLink')

    OUTPUTLINK_ADD_ICON =(By.ID, 'id_add_1_Box_Module_1_OutputLink')
    OUTPUTLINK_ARROW = (By.ID, 'id_expand_1_Box_Module_1_OutputLink')
    OUTPUTLINK_ITEMS = (By.ID, 'id_item_text_1_Box_Module_1_OutputLink_')  # + {num}_
    NUMBER_OF_OUTPUTLINK = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_OutputLink > span')
    DELETE_OUTPUTLINKS = (By.ID, 'delete_group_1_Box_Module_1_OutputLink')

    RS_485_ADD_ICON = (By.ID, 'id_add_1_Box_Module_2_SK')
    RS_485_ARROW = (By.ID, 'id_expand_1_Box_Module_2_SK')
    RS_485_ITEMS = (By.ID, 'id_item_text_1_Box_Module_2_SK_')  # + {num}_
    NUMBER_OF_RS_485 = (By.CSS_SELECTOR, '#badge_1_Box_Module_2_SK > span')
    DELETE_RS_485 = (By.ID, 'delete_group_1_Box_Module_2_SK')

    ADDRESSABLE_LOOP = (By.ID, 'id_expand_1_Box_Module_3_AL_')  # + {num}_
    ADDRESSABLE_DEVICES_ADD_ICON = (By.CSS_SELECTOR, '#badge_1_Box_Module_3_AL_')  # + {num}_AU
    ADDRESSABLE_DEVICES_ARROW = (By.ID, 'id_expand_1_Box_Module_3_AL_')  # + {num}_AU
    ADDRESSABLE_DEVICES_ITEMS = (By.ID, 'id_item_text_1_Box_Module_3_AL_')  # + {num}_AU_{num}_
    DELETE_ADDRESSABLE_DEVICES = (By.ID, 'delete_group_1_Box_Module_3_AL_')  # + {num}_AU

    SELECT_TYPE_ICON = (By.CSS_SELECTOR, '.css-sckop7 span')
    TYPES = (By.CSS_SELECTOR, '.css-r8u8y9 :nth-child(')  # + {num})

    RECORD_START = (By.XPATH, '//p[contains(text(), "- в ППК ППК-Р#1')  # + {module}")]
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



