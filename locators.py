from selenium.webdriver.common.by import By


class MainPanelLocators():
    LOGO = (By.CSS_SELECTOR, '[alt="logo"]')
    TO_PPK_BUTTON = (By.CLASS_NAME, 'css-1661jj0')
    FROM_PPK_BUTTON = (By.ID, 'read_config_from_ppk')
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
    PPK_R_FORM = (By.ID, 'ppk_1_Box')
    PPK_R_FORM_1 = (By.XPATH, '//span[contains(text(), "#1")]')
    PPK_R_ARROW = (By.CSS_SELECTOR, '#id_expand_1_Box > svg')
    ACTIVE_OBJECT = (By.CLASS_NAME, 'Mui-selected')
    RECORD_START = [(By.XPATH, f'//p[contains(text(), "- в ППК ППК-Р#1")]'),
                    (By.XPATH, f'//p[contains(text(), "- в ППК ППК-Р#1.Модуль#1(Области)")]'),
                    (By.XPATH, f'//p[contains(text(), "- в ППК ППК-Р#1.Модуль#2(Выходы)")]'),
                    (By.XPATH, f'//p[contains(text(), "- в ППК ППК-Р#1.Модуль#3(Адресные шлейфы)")]')]
    RECORD_END = (By.XPATH, '//p[contains(text(), " - stop sending to PPK: done uploading")]')
    MODULE_FORM = [(By.ID, 'id_item_text_1_Box_Module_1_'), 
                   (By.ID, 'id_item_text_1_Box_Module_2_'), 
                   (By.ID, 'id_item_text_1_Box_Module_3_')]
    MODULE_ARROW = [(By.CSS_SELECTOR, '#id_expand_1_Box_Module_1_ > svg'),
                    (By.CSS_SELECTOR, '#id_expand_1_Box_Module_2_ > svg'),
                    (By.CSS_SELECTOR, '#id_expand_1_Box_Module_3_ > svg')]
    AREA_ADD_BUTTON= (By.CSS_SELECTOR, '#id_add_1_Box_Module_1_Area path')
    INPUT_ADD_BUTTON= (By.CSS_SELECTOR, '#id_add_1_Box_Module_1_InputLink path')
    OUTPUT_ADD_BUTTON = (By.CSS_SELECTOR, '#id_add_1_Box_Module_1_OutputLink path')
