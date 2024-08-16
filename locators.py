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
    def DISABLE(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_ignore')
    def DELAY_IN_EVACUATION(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_delay1')
    def EXTINGUISHING_START_TIME(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_delay2')
    def EXTINGUISHING(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_extPresent')
    def GAS_OUTPUT_SIGNAL(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_needGasOk')
    def MUTUALLY_EXCLUSIVE_SR(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_interlock')
    def MUTUALLY_EXCLUSIVE_SR_ARROW(num): return (By.CSS_SELECTOR, 
        f'#id_1_Box_Module_1_Area_{num}_interlock + div')
    def EXTINGUISHING_BY_MFA(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_extOnMCP')
    def FORWARD_IN_RING(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_sendOnRing')
    def RETRY_DELAY(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_reQueryDelay')
    def LAUNCH_ALGORITHM(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_algorithm')
    def LAUNCH_ALGORITHM_ARROW(num): return (By.CSS_SELECTOR, 
        f'#id_1_Box_Module_1_Area_{num}_algorithm + div')
    def RESET_DELAY(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_resetDelay')
    CHECKBOX_CHECKED = (By.CSS_SELECTOR, f'.Mui-checked > #')  # + {checkbox id}


class InputLinkSettingsLocators():
    def UNIT_ID(inlink_num): return (By.ID, f'id_1_Box_Module_1_InputLink_{inlink_num}_unitID')
    def PARENT_AREA(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_parent area')
    def DISABLE(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_ignore')

    def COMMAND(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_flavour')
    def COMMAND_ARROW(num): return (By.CSS_SELECTOR, f'#id_1_Box_Module_1_InputLink_{num}_flavour + div')

    def CHANNEL(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_channel')
    def FIX(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_fixed')


class OutputLinkSettingsLocators():
    def UNIT_ID(outlink_num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{outlink_num}_unitID')
    def PARENT_AREA(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_parent area')
    def DISABLE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_ignore')

    def TURN_ON_DELAY(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_delayOn')
    def TURN_OFF_DELAY(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_delayOff')
    def NO_STOP(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_noStopOnOff')
    def NO_RESTART_DELAY_ON(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_noRestartDelayOn')
    def NO_RESTART_DELAY_OFF(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_noRestartDelayOff')
    def SINGLE_PULSE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_singlePulse')

    # Настройки реагирования выхода на реле
    def ON_FIRE1(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onFire1')
    def ON_FIRE1_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onFire1 + div')
    def ON_FIRE2(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onFire2')
    def ON_FIRE2_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onFire2 + div')
    def ON_FAULT(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onFault')
    def ON_FAULT_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onFault + div')
    def ON_REPAIR(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onRepair')
    def ON_REPAIR_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onRepair + div')
    def ON_EVACUATION(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onEvacuation')
    def ON_EVACUATION_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onEvacuation + div')
    def ON_EXTINGUICHING(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onExtinguiching')
    def ON_EXTINGUICHING_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onExtinguiching + div')
    def ON_AFTER_EXTINGUICHING(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onAfterExtinguishing')
    def ON_AFTER_EXTINGUICHING_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onAfterExtinguishing + div')
    def ON_EXTINGUICHING_FAILED(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onExtinguishingFailed')
    def ON_EXTINGUICHING_FAILED_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onExtinguishingFailed + div')
    def ON_AUTO_OFF(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onAutoOff')
    def ON_AUTO_OFF_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onAutoOff + div')
    def ON_RESET(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onReset')
    def ON_RESET_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onReset + div')
    def ON_DOOR(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onDoor')
    def ON_DOOR_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onDoor + div')
    def ON_BLOCKED(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onBlocked')
    def ON_BLOCKED_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onBlocked + div')
    def ON_EVACUATION_PAUSE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onEvacuationPause')
    def ON_EVACUATION_PAUSE_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onEvacuationPause + div')
    def ON_DOOR_PAUSE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onDoorPause')
    def ON_DOOR_PAUSE_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onDoorPause + div')
    def ON_CANCELLED(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onCancelled')
    def ON_CANCELLED_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onCancelled + div')
    def ON_TECH(num, tech_num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onTech{tech_num}')
    def ON_TECH_ARROW(num, tech_num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onTech{tech_num} + div')
    def AND_OR(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_andOr')
    def AND_OR_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_andOr + div')
    

class RS_485_SettingsLocators():
    def DISABLE(BIS_M_num): return (By.ID, f'id_1_Box_Module_2_SK_{BIS_M_num}_ignore')
    def BRIGHTNESS(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_brightness')
    def TIMEOUT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_keyTimeout')
    def NO_SOUND(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_noSound')
    def NO_ALARM_SOUND(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_noAlarmSound')
    def KEY_SENSITIVE(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_keySensitive')
    def DEFAULT_ID(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_defaultID')
    def SN(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_SN')

    def DEFAULT_GREEN(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_allGrin')
    def BACKLIGHT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_backlight')

    def FIRE(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_fire2')
    def ATTENTION(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_fire1')
    def FAULT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_fault')
    def AUTO_OFF(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_autoOff')
    def LEVEL_CONFIRM(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_levelConfirm')
    def LENGTH_CONFIRM(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_lengthConfirm')
    def PULSE_DIAL(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_pulseDial')
    def NO_CONFIRM(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_noConfirm')
    def PHONE_NUMBER(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_phoneNumber')
    def ACCOUNT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_Account')


class AddressableLoopSettingsLocators():
    def DISABLE(AL, device_num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{device_num}_ignore')
    def SN(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_SN')

    def MODE(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_mode')
    def MODE_ARROW(AL, num): return (By.CSS_SELECTOR, f'#id_1_Box_Module_3_AL_{AL}_AU_{num}_mode + div')

    def TWO_INPUTS(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_use2inputs')

    def DIFFERENTIAL(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_diff')

    def THRESHOLD(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_threshold')
    def GROUP(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_group')

    def MODE220(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_mode220')
    def MODE220_ARROW(AL, num): return (By.CSS_SELECTOR, f'#id_1_Box_Module_3_AL_{AL}_AU_{num}_mode220 + div')
    def MOTOR(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_DC\\ motor')

    def MODE24(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_mode24')
    def MODE24_ARROW(AL, num): return (By.CSS_SELECTOR, f'#id_1_Box_Module_3_AL_{AL}_AU_{num}_mode24 + div')
