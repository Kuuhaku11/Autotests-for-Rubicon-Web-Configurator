from selenium.webdriver.common.by import By


class MainPanelLocators():
    LOGO = (By.CSS_SELECTOR, '[alt="logo"]')
    TO_PPK_BUTTON = (By.CLASS_NAME, 'css-1661jj0')
    TO_PPK_BUTTON_IS_BLINKING = (By.CLASS_NAME, 'css-638ncg')
    FROM_PPK_BUTTON = (By.ID, 'read_config_from_ppk')
    FROM_PPK_BUTTON_IS_BLINKING_DARK = (By.CLASS_NAME, 'css-1poz9ah')
    FROM_PPK_BUTTON_IS_BLINKING_LIGHT = (By.CLASS_NAME, 'css-1uq7s6e')
    SAVE_BUTTON = (By.ID, 'save_config_to_local_storage')
    RESTORE_BUTTON = (By.ID, 'restore_config_from_local_storage')
    RESTORE_MESSAGE = (By.ID, 'mui-2')
    TO_FILE_BUTTON = (By.CSS_SELECTOR, '.MuiToolbar-root :nth-child(8)')
    TO_FILE_FOR_INTELLECT_BUTTON = (By.CSS_SELECTOR, '[aria-label="В Файл для Интеллекта"]')
    FROM_FILE_BUTTON = (By.CSS_SELECTOR, '.MuiToolbar-root :nth-child(10)')
    EVENT_LOG_BUTTON = (By.CSS_SELECTOR, '[data-testid="event_log"]')
    TERMINAL_BUTTON = (By.ID, 'terminal_open')
    CLOSE_TERMINAL_ARROW = (By.ID, 'terminal_close')
    LIGHT_MODE_ICON = (By.CSS_SELECTOR, '[data-testid="LightModeIcon"]')
    DARK_MODE_ICON = (By.CSS_SELECTOR, '[data-testid="NightlightIcon"]')
    ONLINE_MARK = (By.ID, 'online_mark')
    OFFLINE_MARK = (By.CLASS_NAME, 'css-1qv5po9')
    TERMINAL_FORM = (By.CLASS_NAME, 'MuiDrawer-paperAnchorRight')
    CLOSE_EXPANDED_TABS_BUTTON = (By.ID, 'close_expanded_tabs')
    @staticmethod
    def TERMINAL_ITEMS(mess_num): return (By.CSS_SELECTOR, f'.css-1jrxq1v >p:nth-child({mess_num})')
    @staticmethod
    def CREATE_MESSAGE(object): return (By.XPATH, f'//p[contains(text(), " - created ППК-Р#1.{object}")]')
    @staticmethod
    def MODULE_CLEANING_MESSAGE(module): return (By.XPATH,
        f'//p[contains(text(), " - ППК-Р#1.{module}  Очистка конфигурации в устройстве")]')


class SystemObjectsLocators():
    SYSTEM_ARROW = (By.CLASS_NAME, 'css-1v19ibo')
    ACTIVE_OBJECT = (By.CLASS_NAME, 'Mui-selected')

    PPK_R_FORM_NUMB_1 = (By.XPATH, '//span[contains(text(), "#1")]')
    PPK_R_ARROW = (By.ID, 'id_expand_1_Box')

    @staticmethod
    def MODULE_FORM(module_num): return (By.ID, f'id_item_text_1_Box_Module_{module_num}_')
    @staticmethod
    def MODULE_ARROW(module_num): return (By.ID, f'id_expand_1_Box_Module_{module_num}_')

    AREA_ADD_ICON = (By.ID, 'id_add_1_Box_Module_1_Area')
    AREA_ARROW = (By.ID, 'id_expand_1_Box_Module_1_Area')
    @staticmethod
    def AREA_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_1_Area_{num}_')
    NUMBER_OF_AREAS = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_Area > span')
    DELETE_AREAS = (By.ID, 'delete_group_1_Box_Module_1_Area')

    INPUTLINK_ADD_ICON =(By.ID, 'id_add_1_Box_Module_1_InputLink')
    INPUTLINK_ARROW = (By.ID, 'id_expand_1_Box_Module_1_InputLink')
    @staticmethod
    def INPUTLINK_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_1_InputLink_{num}_')
    NUMBER_OF_INPUTLINK = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_InputLink > span')
    DELETE_INPUTLINKS = (By.ID, 'delete_group_1_Box_Module_1_InputLink')

    OUTPUTLINK_ADD_ICON =(By.ID, 'id_add_1_Box_Module_1_OutputLink')
    OUTPUTLINK_ARROW = (By.ID, 'id_expand_1_Box_Module_1_OutputLink')
    @staticmethod
    def OUTPUTLINK_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_1_OutputLink_{num}_')
    NUMBER_OF_OUTPUTLINK = (By.CSS_SELECTOR, '#badge_1_Box_Module_1_OutputLink > span')
    DELETE_OUTPUTLINKS = (By.ID, 'delete_group_1_Box_Module_1_OutputLink')

    RS_485_ADD_ICON = (By.ID, 'id_add_1_Box_Module_2_SK')
    RS_485_ARROW = (By.ID, 'id_expand_1_Box_Module_2_SK')
    @staticmethod
    def RS_485_ITEMS(num): return (By.ID, f'id_item_text_1_Box_Module_2_SK_{num}_')
    NUMBER_OF_RS_485 = (By.CSS_SELECTOR, '#badge_1_Box_Module_2_SK > span')
    DELETE_RS_485 = (By.ID, 'delete_group_1_Box_Module_2_SK')

    @staticmethod
    def ADDRESSABLE_LOOP(AL): return (By.ID, f'id_expand_1_Box_Module_3_AL_{AL}_')
    @staticmethod
    def ADDRESSABLE_DEVICES_ADD_ICON(AL): return (By.CSS_SELECTOR, f'#badge_1_Box_Module_3_AL_{AL}_AU')
    @staticmethod
    def ADDRESSABLE_DEVICES_ARROW(AL): return (By.ID, f'id_expand_1_Box_Module_3_AL_{AL}_AU')
    @staticmethod
    def ADDRESSABLE_DEVICES_ITEMS(AL, num): return (By.ID, f'id_item_text_1_Box_Module_3_AL_{AL}_AU_{num}_')
    @staticmethod
    def DELETE_ADDRESSABLE_DEVICES(AL): return (By.ID, f'delete_group_1_Box_Module_3_AL_{AL}_AU')

    UNIT_MENU_CONFIG = (By.ID, 'unit-menu-config')
    SELECT_TYPE_ICON = (By.CSS_SELECTOR, '.css-sckop7 span')
    @staticmethod
    def TYPES(num): return (By.CSS_SELECTOR, f'.css-r8u8y9 :nth-child({num})')

    @staticmethod
    def DROP_DOWN_LIST(num): return (By.XPATH, f'//div[@role="presentation"]//*[{num}]')

    AREA_SAVE_ICON = (By.CSS_SELECTOR, '#id_item_1_Box_Module_1_Area_1_ .css-1fsho2b')
    INPUTLINK_SAVE_ICON = (By.CSS_SELECTOR, '#id_item_1_Box_Module_1_InputLink_1_ .css-1fsho2b')
    OUTPUTLINK_SAVE_ICON = (By.CSS_SELECTOR, '#id_item_1_Box_Module_1_OutputLink_1_ .css-1fsho2b')
    BIS_M_SAVE_ICON = (By.CSS_SELECTOR, '#id_item_1_Box_Module_2_SK_1_ .css-1fsho2b')
    @staticmethod
    def ADDRESSABLE_DEVICE_SAVE_ICON(AL): return (By.CSS_SELECTOR, 
        f'#id_item_1_Box_Module_3_AL_{AL}_AU_1_ .css-1fsho2b')


    @staticmethod
    def RECORD_START(module): return (By.XPATH, f'//p[contains(text(), "- в ППК ППК-Р#1.{module}")]')
    RECORD_FINISH = (By.XPATH, '//p[contains(text(), " - stop sending to PPK: done uploading")]')

    UNLOAD_START = (By.XPATH, '//p[contains(text(), " - start read CFG from ALL PPKR")]')
    UNLOAD_START_MODULE_1 = (By.XPATH,
        '//p[contains(text(), "- start read CFG from ППК-Р#1.Модуль#1(Области)")]')
    UNLOAD_START_MODULE_2 = (By.XPATH, 
        '//p[contains(text(), " - start read CFG from ППК-Р#1.Модуль#2(Выходы)")]')
    UNLOAD_START_MODULE_3 = (By.XPATH, 
        '//p[contains(text(), " - start read CFG from ППК-Р#1.Модуль#3(Адресные шлейфы)")]')
    UNLOAD_FINISH = (By.XPATH, '//p[contains(text(), " - stop read CFG from ALL PPKR")]')

    CLEAR_MODULE_BUTTON = (By.CLASS_NAME, 'css-174aos4')


class AreaSettingsLocators():
    @staticmethod
    def ENTERS_THE_AREA(area_num): return (By.ID, f'id_1_Box_Module_1_Area_{area_num}_parent area')
    @staticmethod
    def DISABLE(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_ignore')
    @staticmethod
    def DELAY_IN_EVACUATION(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_delay1')
    @staticmethod
    def EXTINGUISHING_START_TIME(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_delay2')
    @staticmethod
    def EXTINGUISHING(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_extPresent')
    @staticmethod
    def GAS_OUTPUT_SIGNAL(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_needGasOk')
    @staticmethod
    def MUTUALLY_EXCLUSIVE_SR(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_interlock')
    @staticmethod
    def MUTUALLY_EXCLUSIVE_SR_ARROW(num): return (By.CSS_SELECTOR, 
        f'#id_1_Box_Module_1_Area_{num}_interlock + div')
    @staticmethod
    def EXTINGUISHING_BY_MFA(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_extOnMCP')
    @staticmethod
    def FORWARD_IN_RING(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_sendOnRing')
    @staticmethod
    def RETRY_DELAY(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_reQueryDelay')
    @staticmethod
    def LAUNCH_ALGORITHM(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_algorithm')
    @staticmethod
    def LAUNCH_ALGORITHM_ARROW(num): return (By.CSS_SELECTOR, 
        f'#id_1_Box_Module_1_Area_{num}_algorithm + div')
    @staticmethod
    def RESET_DELAY(num): return (By.ID, f'id_1_Box_Module_1_Area_{num}_resetDelay')
    CHECKBOX_CHECKED = (By.CSS_SELECTOR, f'.Mui-checked > #')  # + {checkbox id}


class InputLinkSettingsLocators():
    @staticmethod
    def UNIT_ID(inlink_num): return (By.ID, f'id_1_Box_Module_1_InputLink_{inlink_num}_unitID')
    @staticmethod
    def PARENT_AREA(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_parent area')
    @staticmethod
    def DISABLE(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_ignore')

    @staticmethod
    def COMMAND(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_flavour')
    @staticmethod
    def COMMAND_ARROW(num): return (By.CSS_SELECTOR, f'#id_1_Box_Module_1_InputLink_{num}_flavour + div')

    @staticmethod
    def CHANNEL(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_channel')
    @staticmethod
    def FIX(num): return (By.ID, f'id_1_Box_Module_1_InputLink_{num}_fixed')


class OutputLinkSettingsLocators():
    @staticmethod
    def UNIT_ID(outlink_num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{outlink_num}_unitID')
    @staticmethod
    def PARENT_AREA(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_parent area')
    @staticmethod
    def DISABLE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_ignore')

    @staticmethod
    def TURN_ON_DELAY(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_delayOn')
    @staticmethod
    def TURN_OFF_DELAY(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_delayOff')
    @staticmethod
    def NO_STOP(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_noStopOnOff')
    @staticmethod
    def NO_RESTART_DELAY_ON(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_noRestartDelayOn')
    @staticmethod
    def NO_RESTART_DELAY_OFF(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_noRestartDelayOff')
    @staticmethod
    def SINGLE_PULSE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_singlePulse')

    # Настройки реагирования выхода на реле
    @staticmethod
    def ON_FIRE1(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onFire1')
    @staticmethod
    def ON_FIRE1_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onFire1 + div')
    @staticmethod
    def ON_FIRE2(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onFire2')
    @staticmethod
    def ON_FIRE2_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onFire2 + div')
    @staticmethod
    def ON_FAULT(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onFault')
    @staticmethod
    def ON_FAULT_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onFault + div')
    @staticmethod
    def ON_REPAIR(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onRepair')
    @staticmethod
    def ON_REPAIR_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onRepair + div')
    @staticmethod
    def ON_EVACUATION(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onEvacuation')
    @staticmethod
    def ON_EVACUATION_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onEvacuation + div')
    @staticmethod
    def ON_EXTINGUICHING(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onExtinguiching')
    @staticmethod
    def ON_EXTINGUICHING_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onExtinguiching + div')
    @staticmethod
    def ON_AFTER_EXTINGUICHING(num):
        return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onAfterExtinguishing')
    @staticmethod
    def ON_AFTER_EXTINGUICHING_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onAfterExtinguishing + div')
    @staticmethod
    def ON_EXTINGUICHING_FAILED(num):
        return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onExtinguishingFailed')
    @staticmethod
    def ON_EXTINGUICHING_FAILED_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onExtinguishingFailed + div')
    @staticmethod
    def ON_AUTO_OFF(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onAutoOff')
    @staticmethod
    def ON_AUTO_OFF_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onAutoOff + div')
    @staticmethod
    def ON_RESET(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onReset')
    @staticmethod
    def ON_RESET_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onReset + div')
    @staticmethod
    def ON_DOOR(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onDoor')
    @staticmethod
    def ON_DOOR_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onDoor + div')
    @staticmethod
    def ON_BLOCKED(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onBlocked')
    @staticmethod
    def ON_BLOCKED_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onBlocked + div')
    @staticmethod
    def ON_EVACUATION_PAUSE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onEvacuationPause')
    @staticmethod
    def ON_EVACUATION_PAUSE_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onEvacuationPause + div')
    @staticmethod
    def ON_DOOR_PAUSE(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onDoorPause')
    @staticmethod
    def ON_DOOR_PAUSE_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onDoorPause + div')
    @staticmethod
    def ON_CANCELLED(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onCancelled')
    @staticmethod
    def ON_CANCELLED_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onCancelled + div')
    @staticmethod
    def ON_TECH(num, tech_num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_onTech{tech_num}')
    @staticmethod
    def ON_TECH_ARROW(num, tech_num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_onTech{tech_num} + div')
    @staticmethod
    def AND_OR(num): return (By.ID, f'id_1_Box_Module_1_OutputLink_{num}_andOr')
    @staticmethod
    def AND_OR_ARROW(num): return (By.CSS_SELECTOR,
        f'#id_1_Box_Module_1_OutputLink_{num}_andOr + div')
    

class RS_485_SettingsLocators():
    @staticmethod
    def DISABLE(BIS_M_num): return (By.ID, f'id_1_Box_Module_2_SK_{BIS_M_num}_ignore')
    @staticmethod
    def BRIGHTNESS(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_brightness')
    @staticmethod
    def TIMEOUT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_keyTimeout')
    @staticmethod
    def NO_SOUND(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_noSound')
    @staticmethod
    def NO_ALARM_SOUND(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_noAlarmSound')
    @staticmethod
    def KEY_SENSITIVE(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_keySensitive')
    @staticmethod
    def DEFAULT_ID(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_defaultID')
    @staticmethod
    def SN(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_SN')

    @staticmethod
    def DEFAULT_GREEN(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_allGrin')
    @staticmethod
    def BACKLIGHT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_backlight')

    @staticmethod
    def FIRE(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_fire2')
    @staticmethod
    def ATTENTION(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_fire1')
    @staticmethod
    def FAULT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_fault')
    @staticmethod
    def AUTO_OFF(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_autoOff')
    @staticmethod
    def LEVEL_CONFIRM(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_levelConfirm')
    @staticmethod
    def LENGTH_CONFIRM(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_lengthConfirm')
    @staticmethod
    def PULSE_DIAL(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_pulseDial')
    @staticmethod
    def NO_CONFIRM(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_noConfirm')
    @staticmethod
    def PHONE_NUMBER(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_phoneNumber')
    @staticmethod
    def ACCOUNT(num): return (By.ID, f'id_1_Box_Module_2_SK_{num}_Account')


class AddressableLoopSettingsLocators():
    @staticmethod
    def DISABLE(AL, device_num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{device_num}_ignore')
    @staticmethod
    def SN(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_SN')

    @staticmethod
    def MODE(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_mode')
    @staticmethod
    def MODE_ARROW(AL, num): return (By.CSS_SELECTOR, f'#id_1_Box_Module_3_AL_{AL}_AU_{num}_mode + div')

    @staticmethod
    def TWO_INPUTS(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_use2inputs')

    @staticmethod
    def DIFFERENTIAL(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_diff')

    @staticmethod
    def THRESHOLD(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_threshold')
    @staticmethod
    def GROUP(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_group')

    @staticmethod
    def MODE220(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_mode220')
    @staticmethod
    def MODE220_ARROW(AL, num):
        return (By.CSS_SELECTOR, f'#id_1_Box_Module_3_AL_{AL}_AU_{num}_mode220 + div')
    @staticmethod
    def MOTOR(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_DC\\ motor')

    @staticmethod
    def MODE24(AL, num): return (By.ID, f'id_1_Box_Module_3_AL_{AL}_AU_{num}_mode24')
    @staticmethod
    def MODE24_ARROW(AL, num):
        return (By.CSS_SELECTOR, f'#id_1_Box_Module_3_AL_{AL}_AU_{num}_mode24 + div')
    

class EventLogLocators():
    @staticmethod
    def NAME_COLUMN(num): return (By.XPATH, f'//tr//th[{num}]')

    DATE_TIME = (By.XPATH, '//tr[1]//td[1]')
    EVENT = (By.XPATH, '//tr[1]//td[2]')
    ADDRESS = (By.XPATH, '//tr[1]//td[3]')
    AREA = (By.XPATH, '//tr[1]//td[4]')

    EVENTS_NUMBER = (By.ID, 'mui-4')
    EVENTS_100 = (By.XPATH, '//li[3]')