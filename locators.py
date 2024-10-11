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
    def CREATE_MESSAGE(object, ppk): return (By.XPATH, f'//p[contains(text(), " - created ППК-Р#{ppk}.{object}")]')
    @staticmethod
    def MODULE_CLEANING_MESSAGE(module, ppk): return (By.XPATH,
        f'//p[contains(text(), " - ППК-Р#{ppk}.{module}  Очистка конфигурации в устройстве")]')


class SystemObjectsLocators():
    SEARCH_ITEM = (By.CLASS_NAME, 'css-1yj2jwg')
    SEARCH_FIELD = (By.ID, 'search_by_label')
    SEARCH_CLEAR_ICON = (By.CSS_SELECTOR, '[data-testid="ClearRoundedIcon"]')
    @staticmethod
    def SEARCH_ELEMENT(element): return (By.XPATH, f'//u[.="{element}"]')
    @staticmethod
    def SEARCH_BY_NAME(name): return (By.XPATH, f'//span[.="{name}"]')

    SYSTEM_FORM = (By.CSS_SELECTOR, '.css-1sct4f5 > div')
    SYSTEM_ARROW = (By.CSS_SELECTOR, '[data-testid="ExpandMoreIcon"]')
    ACTIVE_OBJECT = (By.CLASS_NAME, 'Mui-selected')
    ACTIVE_OBJECT_ADDRESS = (By.CLASS_NAME, 'css-16qv2i2')

    PPK_ADD_ICON = (By.ID, 'ppk_add_button')
    @staticmethod
    def PPK_R_FORM(ppk): return (By.XPATH, f'//span[contains(text(), "#{ppk} ППК-Р")]')
    PPK_R_BOX_1 = (By.ID, 'ppk_1_Box')
    @staticmethod
    def PPK_R_ARROW(ppk): return (By.ID, f'id_expand_{ppk}_Box')
    PPK_R_SN_FORM = (By.ID, 'id__0_SN')
    PPK_R_NAME_SETTING = (By.ID, 'id__0_name')
    PPk_R_1_NAME = (By.ID, 'name_of_ppk_1')

    @staticmethod
    def MODULE_FORM(module_num, ppk): return (By.ID, f'id_item_text_{ppk}_Box_Module_{module_num}_')
    @staticmethod
    def MODULE_ARROW(module_num, ppk): return (By.ID, f'id_expand_{ppk}_Box_Module_{module_num}_')

    @staticmethod
    def AREA_ADD_ICON(ppk): return (By.ID, f'id_add_{ppk}_Box_Module_1_Area')
    @staticmethod
    def AREA_ARROW(ppk): return (By.ID, f'id_expand_{ppk}_Box_Module_1_Area')
    @staticmethod
    def AREA_ITEMS(num, ppk): return (By.ID, f'id_item_text_{ppk}_Box_Module_1_Area_{num}_')
    @staticmethod
    def NUMBER_OF_AREAS(ppk): return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_1_Area > span')
    @staticmethod
    def DELETE_AREAS(ppk): return (By.ID, f'delete_group_{ppk}_Box_Module_1_Area')
    @staticmethod
    def RESTORE_AREAS(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_1_Area .css-84se36')
    @staticmethod
    def INVISIBILITY_AREAS_NUM(ppk): 
        return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_1_Area > .MuiBadge-invisible')

    @staticmethod
    def INPUTLINK_ADD_ICON(ppk): return (By.ID, f'id_add_{ppk}_Box_Module_1_InputLink')
    @staticmethod
    def INPUTLINK_ARROW(ppk): return (By.ID, f'id_expand_{ppk}_Box_Module_1_InputLink')
    @staticmethod
    def INPUTLINK_ITEMS(num, ppk): return (By.ID, f'id_item_text_{ppk}_Box_Module_1_InputLink_{num}_')
    @staticmethod
    def NUMBER_OF_INPUTLINK(ppk): return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_1_InputLink > span')
    @staticmethod
    def DELETE_INPUTLINKS(ppk): return (By.ID, f'delete_group_{ppk}_Box_Module_1_InputLink')
    @staticmethod
    def RESTORE_INPUTLINKS(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_1_InputLink .css-84se36')
    @staticmethod
    def INVISIBILITY_INPUTLINKS_NUM(ppk):
        return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_1_InputLink > .MuiBadge-invisible')

    @staticmethod
    def OUTPUTLINK_ADD_ICON(ppk): return (By.ID, f'id_add_{ppk}_Box_Module_1_OutputLink')
    @staticmethod
    def OUTPUTLINK_ARROW(ppk): return (By.ID, f'id_expand_{ppk}_Box_Module_1_OutputLink')
    @staticmethod
    def OUTPUTLINK_ITEMS(num, ppk): return (By.ID, f'id_item_text_{ppk}_Box_Module_1_OutputLink_{num}_')
    @staticmethod
    def NUMBER_OF_OUTPUTLINK(ppk): return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_1_OutputLink > span')
    @staticmethod
    def DELETE_OUTPUTLINKS(ppk): return (By.ID, f'delete_group_{ppk}_Box_Module_1_OutputLink')
    @staticmethod
    def RESTORE_OUTPUTLINKS(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_1_OutputLink .css-84se36')
    @staticmethod
    def INVISIBILITY_OUTPUTLINKS_NUM(ppk):
        return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_1_OutputLink > .MuiBadge-invisible')

    @staticmethod
    def RS_485_ADD_ICON(ppk): return (By.ID, f'id_add_{ppk}_Box_Module_2_SK')
    @staticmethod
    def RS_485_ARROW(ppk): return (By.ID, f'id_expand_{ppk}_Box_Module_2_SK')
    @staticmethod
    def RS_485_ITEMS(num, ppk): return (By.ID, f'id_item_text_{ppk}_Box_Module_2_SK_{num}_')
    @staticmethod
    def NUMBER_OF_RS_485(ppk): return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_2_SK > span')
    @staticmethod
    def DELETE_RS_485(ppk): return (By.ID, f'delete_group_{ppk}_Box_Module_2_SK')
    @staticmethod
    def RESTORE_RS_485(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_2_SK .css-84se36')
    @staticmethod
    def INVISIBILITY_RS_485_NUM(ppk):
        return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_2_SK > .MuiBadge-invisible')

    @staticmethod
    def ADDRESSABLE_LOOP(ppk, AL): return (By.ID, f'id_expand_{ppk}_Box_Module_3_AL_{AL}_')
    @staticmethod
    def ADDRESSABLE_DEVICES_ADD_ICON(AL, ppk): return (By.ID, f'badge_{ppk}_Box_Module_3_AL_{AL}_AU')
    @staticmethod
    def ADDRESSABLE_DEVICES_ARROW(AL, ppk): return (By.ID, f'id_expand_{ppk}_Box_Module_3_AL_{AL}_AU')
    @staticmethod
    def ADDRESSABLE_DEVICES_ITEMS(AL, num, ppk):
        return (By.ID, f'id_item_text_{ppk}_Box_Module_3_AL_{AL}_AU_{num}_')
    @staticmethod
    def DELETE_ADDRESSABLE_DEVICES(AL, ppk): return (By.ID, f'delete_group_{ppk}_Box_Module_3_AL_{AL}_AU')
    @staticmethod
    def RESTORE_ADDRESSABLE_DEVICES(AL, ppk): 
        return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_3_AL_{AL}_AU .css-84se36')
    @staticmethod
    def INVISIBILITY_ADDRESSABLE_DEVICES_NUM(AL, ppk):
        return (By.CSS_SELECTOR, f'#badge_{ppk}_Box_Module_3_AL_{AL}_AU > .MuiBadge-invisible')

    UNIT_MENU_CONFIG = (By.ID, 'unit-menu-config')
    SELECT_TYPE_ICON = (By.CSS_SELECTOR, '.css-sckop7 span')
    @staticmethod
    def TYPES(num): return (By.CSS_SELECTOR, f'.css-r8u8y9 :nth-child({num})')

    @staticmethod
    def DROP_DOWN_LIST(num): return (By.XPATH, f'//div[@role="presentation"]//*[{num}]')

    @staticmethod
    def AREA_SAVE_ICON(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_1_Area_1_ .css-1fsho2b')
    @staticmethod
    def INPUTLINK_SAVE_ICON(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_1_InputLink_1_ .css-1fsho2b')
    @staticmethod
    def OUTPUTLINK_SAVE_ICON(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_1_OutputLink_1_ .css-1fsho2b')
    @staticmethod
    def BIS_M_SAVE_ICON(ppk): return (By.CSS_SELECTOR, f'#id_item_{ppk}_Box_Module_2_SK_1_ .css-1fsho2b')
    @staticmethod
    def ADDRESSABLE_DEVICE_SAVE_ICON(AL, ppk): return (By.CSS_SELECTOR, 
        f'#id_item_{ppk}_Box_Module_3_AL_{AL}_AU_1_ .css-1fsho2b')

    @staticmethod
    def RECORD_START(ppk, module): return (By.XPATH, f'//p[contains(text(), "- в ППК ППК-Р#{ppk}.{module}")]')
    RECORD_FINISH = (By.XPATH, '//p[contains(text(), " - stop sending to PPK: done uploading")]')

    UNLOAD_START = (By.XPATH, '//p[contains(text(), " - start read CFG from ALL PPKR")]')
    @staticmethod
    def UNLOAD_START_MODULE(ppk, module): return (By.XPATH,
        f'//p[contains(text(), "- start read CFG from ППК-Р#{ppk}.Модуль#{module}")]')
    UNLOAD_FINISH = (By.XPATH, '//p[contains(text(), " - stop read CFG from ALL PPKR")]')

    CLEAR_MODULE_BUTTON = (By.CLASS_NAME, 'css-174aos4')


class ConfigurationLocators():
    DELETE_BUTTON = (By.ID, 'delete_unit')
    RESTORE_BUTTON = (By.CLASS_NAME, 'css-kuxjgv')
    DELETE_MARK = (By.CLASS_NAME, 'css-1m703jz')
    CHANGE_ADDRESS_BUTTON = (By.CSS_SELECTOR, '[data-testid="ppkr_sun_chip"]')
    CHANGE_ADDRESS_INPUT = (By.ID, 'ppkr_sun_change_input')
    CHANGE_ADDRESS_OK = (By.CSS_SELECTOR, '[data-testid="confirm_change_sun"]')

    PATH = (By.CLASS_NAME, 'css-1isemmb')
    CONFIGURATION_PANEL = (By.XPATH, '//p[.="конфигурация"]')
    STATUS_PANEL = (By.XPATH, '//p[.="статус"]')
    COMMAND_PANEL = (By.XPATH, '//p[.="команда"]')
    INFORMATION_PANEL = (By.XPATH, '//p[.="информация"]')


class AreaSettingsLocators():
    @staticmethod
    def _generate_id(ppk_num, area_num, suffix):
        return (By.ID, f'id_{ppk_num}_Box_Module_1_Area_{area_num}_{suffix}')

    @staticmethod
    def ENTERS_THE_AREA(area, ppk): return AreaSettingsLocators._generate_id(ppk, area, 'parent area')
    @staticmethod
    def DISABLE(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'ignore')
    @staticmethod
    def DELAY_IN_EVACUATION(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'delay1')
    @staticmethod
    def EXTINGUISHING_START_TIME(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'delay2')
    @staticmethod
    def EXTINGUISHING(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'extPresent')
    @staticmethod
    def GAS_OUTPUT_SIGNAL(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'needGasOk')
    @staticmethod
    def MUTUALLY_EXCLUSIVE_SR(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'interlock')
    @staticmethod
    @staticmethod
    def MUTUALLY_EXCLUSIVE_SR_ARROW(num, ppk):
        return (By.CSS_SELECTOR, f'#id_{ppk}_Box_Module_1_Area_{num}_interlock + div')
    @staticmethod
    def EXTINGUISHING_BY_MFA(num, ppk): return (By.ID, f'id_{ppk}_Box_Module_1_Area_{num}_extOnMCP')
    @staticmethod
    def FORWARD_IN_RING(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'sendOnRing')
    @staticmethod
    def RETRY_DELAY(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'reQueryDelay')
    @staticmethod
    def LAUNCH_ALGORITHM(num, ppk): return AreaSettingsLocators._generate_id(ppk, num, 'algorithm')
    @staticmethod
    def LAUNCH_ALGORITHM_ARROW(num, ppk):
        return (By.CSS_SELECTOR, f'#id_{ppk}_Box_Module_1_Area_{num}_algorithm + div')
    @staticmethod
    def RESET_DELAY(num, ppk): return (By.ID, f'id_{ppk}_Box_Module_1_Area_{num}_resetDelay')
    @staticmethod
    def CHECKBOX_CHECKED(checkbox_id): return (By.CSS_SELECTOR, f'.Mui-checked > #{checkbox_id}')


class InputLinkSettingsLocators():
    @staticmethod
    def _generate_id(ppk_num, inputlink_num, suffix):
        return (By.ID, f'id_{ppk_num}_Box_Module_1_InputLink_{inputlink_num}_{suffix}')
    
    @staticmethod
    def UNIT_ID(num, ppk): return InputLinkSettingsLocators._generate_id(ppk, num, 'unitID')
    @staticmethod
    def PARENT_AREA(num, ppk): return InputLinkSettingsLocators._generate_id(ppk, num, 'parent area')
    @staticmethod
    def DISABLE(num, ppk): return InputLinkSettingsLocators._generate_id(ppk, num, 'ignore')

    @staticmethod
    def COMMAND(num, ppk): return InputLinkSettingsLocators._generate_id(ppk, num, 'flavour')
    @staticmethod
    def COMMAND_ARROW(num, ppk): return (By.CSS_SELECTOR, f'#id_{ppk}_Box_Module_1_InputLink_{num}_flavour + div')

    @staticmethod
    def CHANNEL(num, ppk): return InputLinkSettingsLocators._generate_id(ppk, num, 'channel')
    @staticmethod
    def FIX(num, ppk): return InputLinkSettingsLocators._generate_id(ppk, num, 'fixed')


class OutputLinkSettingsLocators():
    @staticmethod
    def _generate_id(ppk_num, outputlink_num, suffix):
        return (By.ID, f'id_{ppk_num}_Box_Module_1_OutputLink_{outputlink_num}_{suffix}')
    
    @staticmethod
    def _generate_css(ppk_num, outputlink_num, suffix):
        return (By.CSS_SELECTOR, f'#id_{ppk_num}_Box_Module_1_OutputLink_{outputlink_num}_{suffix} + div')
    
    @staticmethod
    def UNIT_ID(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'unitID')
    @staticmethod
    def PARENT_AREA(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'parent area')
    @staticmethod
    def DISABLE(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'ignore')

    @staticmethod
    def TURN_ON_DELAY(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'delayOn')
    @staticmethod
    def TURN_OFF_DELAY(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'delayOff')
    @staticmethod
    def NO_STOP(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'noStopOnOff')
    @staticmethod
    def NO_RESTART_DELAY_ON(num, ppk):
        return OutputLinkSettingsLocators._generate_id(ppk, num, 'noRestartDelayOn')
    @staticmethod
    def NO_RESTART_DELAY_OFF(num, ppk):
        return OutputLinkSettingsLocators._generate_id(ppk, num, 'noRestartDelayOff')
    @staticmethod
    def SINGLE_PULSE(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'singlePulse')

    # Настройки реагирования выхода на реле
    @staticmethod
    def ON_FIRE1(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onFire1')
    @staticmethod
    def ON_FIRE1_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onFire1')
    @staticmethod
    def ON_FIRE2(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onFire2')
    @staticmethod
    def ON_FIRE2_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onFire2')
    @staticmethod
    def ON_FAULT(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onFault')
    @staticmethod
    def ON_FAULT_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onFault')
    @staticmethod
    def ON_REPAIR(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onRepair')
    @staticmethod
    def ON_REPAIR_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onRepair')
    @staticmethod
    def ON_EVACUATION(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onEvacuation')
    @staticmethod
    def ON_EVACUATION_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onEvacuation')
    @staticmethod
    def ON_EXTINGUICHING(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onExtinguiching')
    @staticmethod
    def ON_EXTINGUICHING_ARROW(num, ppk):
        return OutputLinkSettingsLocators._generate_css(ppk, num, 'onExtinguiching')
    @staticmethod
    def ON_AFTER_EXTINGUICHING(num, ppk):
        return OutputLinkSettingsLocators._generate_id(ppk, num, 'onAfterExtinguishing')
    @staticmethod
    def ON_AFTER_EXTINGUICHING_ARROW(num, ppk):
        return OutputLinkSettingsLocators._generate_css(ppk, num, 'onAfterExtinguishing')
    @staticmethod
    def ON_EXTINGUICHING_FAILED(num, ppk):
        return OutputLinkSettingsLocators._generate_id(ppk, num, 'onExtinguishingFailed')
    @staticmethod
    def ON_EXTINGUICHING_FAILED_ARROW(num, ppk):
        return OutputLinkSettingsLocators._generate_css(ppk, num, 'onExtinguishingFailed')
    @staticmethod
    def ON_AUTO_OFF(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onAutoOff')
    @staticmethod
    def ON_AUTO_OFF_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onAutoOff')
    @staticmethod
    def ON_RESET(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onReset')
    @staticmethod
    def ON_RESET_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onReset')
    @staticmethod
    def ON_DOOR(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onDoor')
    @staticmethod
    def ON_DOOR_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onDoor')
    @staticmethod
    def ON_BLOCKED(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onBlocked')
    @staticmethod
    def ON_BLOCKED_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onBlocked')
    @staticmethod
    def ON_EVACUATION_PAUSE(num, ppk):
        return OutputLinkSettingsLocators._generate_id(ppk, num, 'onEvacuationPause')
    @staticmethod
    def ON_EVACUATION_PAUSE_ARROW(num, ppk):
        return OutputLinkSettingsLocators._generate_css(ppk, num, 'onEvacuationPause')
    @staticmethod
    def ON_DOOR_PAUSE(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onDoorPause')
    @staticmethod
    def ON_DOOR_PAUSE_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onDoorPause')
    @staticmethod
    def ON_CANCELLED(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'onCancelled')
    @staticmethod
    def ON_CANCELLED_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'onCancelled')
    @staticmethod
    def ON_TECH(num, tech_num, ppk):
        return OutputLinkSettingsLocators._generate_id(ppk, num, f'onTech{tech_num}')
    @staticmethod
    def ON_TECH_ARROW(num, tech_num, ppk):
        return OutputLinkSettingsLocators._generate_css(ppk, num, f'onTech{tech_num}')
    @staticmethod
    def AND_OR(num, ppk): return OutputLinkSettingsLocators._generate_id(ppk, num, 'andOr')
    @staticmethod
    def AND_OR_ARROW(num, ppk): return OutputLinkSettingsLocators._generate_css(ppk, num, 'andOr')
    

class RS_485_SettingsLocators():
    @staticmethod
    def _generate_id(ppk_num, BIS_M_num, suffix):
        return (By.ID, f'id_{ppk_num}_Box_Module_2_SK_{BIS_M_num}_{suffix}')

    @staticmethod
    def DISABLE(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'ignore')
    @staticmethod
    def BRIGHTNESS(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'brightness')
    @staticmethod
    def TIMEOUT(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'keyTimeout')
    @staticmethod
    def NO_SOUND(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'noSound')
    @staticmethod
    def NO_ALARM_SOUND(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'noAlarmSound')
    @staticmethod
    def KEY_SENSITIVE(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'keySensitive')
    @staticmethod
    def DEFAULT_ID(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'defaultID')
    @staticmethod
    def SN(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'SN')

    @staticmethod
    def DEFAULT_GREEN(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'allGrin')
    @staticmethod
    def BACKLIGHT(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'backlight')

    @staticmethod
    def FIRE(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'fire2')
    @staticmethod
    def ATTENTION(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'fire1')
    @staticmethod
    def FAULT(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'fault')
    @staticmethod
    def AUTO_OFF(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'autoOff')
    @staticmethod
    def LEVEL_CONFIRM(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'levelConfirm')
    @staticmethod
    def LENGTH_CONFIRM(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'lengthConfirm')
    @staticmethod
    def PULSE_DIAL(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'pulseDial')
    @staticmethod
    def NO_CONFIRM(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'noConfirm')
    @staticmethod
    def PHONE_NUMBER(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'phoneNumber')
    @staticmethod
    def ACCOUNT(num, ppk): return RS_485_SettingsLocators._generate_id(ppk, num, 'Account')


class AddressableLoopSettingsLocators():
    @staticmethod
    def _generate_id(ppk_num, AL, addr_device_num, suffix):
        return (By.ID, f'id_{ppk_num}_Box_Module_3_AL_{AL}_AU_{addr_device_num}_{suffix}')
    
    @staticmethod
    def _generate_css(ppk_num, AL, addr_device_num, suffix):
        return (By.CSS_SELECTOR, f'#id_{ppk_num}_Box_Module_3_AL_{AL}_AU_{addr_device_num}_{suffix} + div')
    
    @staticmethod
    def DISABLE(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'ignore')
    @staticmethod
    def SN(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'SN')

    @staticmethod
    def MODE(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'mode')
    @staticmethod
    def MODE_ARROW(AL, num, ppk): return AddressableLoopSettingsLocators._generate_css(ppk, AL, num, 'mode')

    @staticmethod
    def TWO_INPUTS(AL, num, ppk):
        return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'use2inputs')

    @staticmethod
    def DIFFERENTIAL(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'diff')

    @staticmethod
    def THRESHOLD(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'threshold')
    @staticmethod
    def GROUP(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'group')

    @staticmethod
    def MODE220(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'mode220')
    @staticmethod
    def MODE220_ARROW(AL, num, ppk):
        return AddressableLoopSettingsLocators._generate_css(ppk, AL, num, 'mode220')
    @staticmethod
    def MOTOR(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'DC\\ motor')

    @staticmethod
    def MODE24(AL, num, ppk): return AddressableLoopSettingsLocators._generate_id(ppk, AL, num, 'mode24')
    @staticmethod
    def MODE24_ARROW(AL, num, ppk): return AddressableLoopSettingsLocators._generate_css(ppk, AL, num, 'mode24')
    

class EventLogLocators():
    @staticmethod
    def NAME_COLUMN(num): return (By.XPATH, f'//tr//th[{num}]')

    DATE_TIME = (By.XPATH, '//tr[1]//td[1]')
    EVENT = (By.XPATH, '//tr[1]//td[2]')
    ADDRESS = (By.XPATH, '//tr[1]//td[3]')
    AREA = (By.XPATH, '//tr[1]//td[4]')

    EVENTS_NUMBER = (By.ID, 'mui-4')
    EVENTS_100 = (By.XPATH, '//li[3]')