import esp


def is_4mb():
    return True if esp.flash_size() <= 4194304 else False


if is_4mb():
    _attrs = {
        "BATTERY_BLACK_CHARGE_IMG": "res/basic/Battery/battery_Black_Charge.jpg",
        "BATTERY_BLACK_IMG": "res/basic/Battery/battery_Black.jpg",
        "BATTERY_GRAY_IMG": "res/basic/Battery/battery_Gray.jpg",
        "BATTERY_GREEN_CHARGE_IMG": "res/basic/Battery/battery_Green_Charge.jpg",
        "BATTERY_GREEN_IMG": "res/basic/Battery/battery_Green.jpg",
        "BATTERY_RED_CHARGE_IMG": "res/basic/Battery/battery_Red_Charge.jpg",
        "BATTERY_RED_IMG": "res/basic/Battery/battery_Red.jpg",
        "BATTERY_YELLOW_IMG": "res/basic/Battery/battery_Yellow.jpg",
        "SERVER_BLUE_IMG": "res/basic/Server/server_blue.jpg",
        "SERVER_EMPTY_IMG": "res/basic/Server/server_empty.jpg",
        "SERVER_ERROR_IMG": "res/basic/Server/server_error.jpg",
        "SERVER_GREEN_IMG": "res/basic/Server/Server_Green.jpg",
        "WIFI_DISCONNECTED_IMG": "res/basic/WiFi/wifi_disconnected.jpg",
        "WIFI_EMPTY_IMG": "res/basic/WiFi/wifi_empty.jpg",
        "WIFI_GOOD_IMG": "res/basic/WiFi/wifi_good.jpg",
        "WIFI_MID_IMG": "res/basic/WiFi/wifi_mid.jpg",
        "WIFI_WORSE_IMG": "res/basic/WiFi/wifi_worse.jpg",
        "APPLIST_SELECTED_IMG": "res/basic/appList_selected.jpg",
        "APPLIST_UNSELECTED_IMG": "res/basic/appList_unselected.jpg",
        "APPLIST_IMG": "res/basic/applist.jpg",
        "APPLIST_LEFT_IMG": "res/basic/applistLeft.jpg",
        "APPLIST_RIGHT_IMG": "res/basic/applistRight.jpg",
        "APPRUN_SELECTED_IMG": "res/basic/appRun_selected.jpg",
        "APPRUN_UNSELECTED_IMG": "res/basic/appRun_unselected.jpg",
        "BAR1_IMG": "res/basic/bar1.jpg",
        "BAR2_IMG": "res/basic/bar2.jpg",
        "BAR3_IMG": "res/basic/bar3.jpg",
        "BAR4_IMG": "res/basic/bar4.jpg",
        "BAR5_IMG": "res/basic/bar5.jpg",
        "BOOT_NO_IMG": "res/basic/boot_No.jpg",
        "BOOT_YES_IMG": "res/basic/boot_Yes.jpg",
        "DEVELOP_SELECTED_IMG": "res/basic/develop_selected.jpg",
        "DEVELOP_UNSELECTED_IMG": "res/basic/develop_unselected.jpg",
        "DEVELOP_PRIVATE_IMG": "res/basic/developPrivate.jpg",
        "DEVELOP_PUBLIC_IMG": "res/basic/developPublic.jpg",
        "EZDATA_SELECTED_IMG": "res/basic/ezdata_selected.jpg",
        "EZDATA_UNSELECTED_IMG": "res/basic/ezdata_unselected.jpg",
        "LOGO_IMG": "res/basic/logo.jpg",
        "RUN_IMG": "res/basic/run.jpg",
        "SCREEN25_IMG": "res/basic/screen25.jpg",
        "SCREEN50_IMG": "res/basic/screen50.jpg",
        "SCREEN75_IMG": "res/basic/screen75.jpg",
        "SCREEN100_IMG": "res/basic/screen100.jpg",
        "SETTING_SELECTED_IMG": "res/basic/setting_selected.jpg",
        "SETTING_UNSELECTED_IMG": "res/basic/setting_unselected.jpg",
        "SETTING_SELECT_IMG": "res/basic/settingSelect.jpg",
        "SETTING_UNSELECT_IMG": "res/basic/settingUnselect.jpg",
        "SETTING_WIFI_IMG": "res/basic/SettingWifi.jpg",
        "AVATAR_IMG": "res/img/avatar.jpg",
        "USER_AVATAR_PATH": "res/img/",
    }
else:
    _attrs = {
        "BATTERY_BLACK_CHARGE_IMG": "/system/basic/Battery/battery_Black_Charge.jpg",
        "BATTERY_BLACK_IMG": "/system/basic/Battery/battery_Black.jpg",
        "BATTERY_GRAY_IMG": "/system/basic/Battery/battery_Gray.jpg",
        "BATTERY_GREEN_CHARGE_IMG": "/system/basic/Battery/battery_Green_Charge.jpg",
        "BATTERY_GREEN_IMG": "/system/basic/Battery/battery_Green.jpg",
        "BATTERY_RED_CHARGE_IMG": "/system/basic/Battery/battery_Red_Charge.jpg",
        "BATTERY_RED_IMG": "/system/basic/Battery/battery_Red.jpg",
        "BATTERY_YELLOW_IMG": "/system/basic/Battery/battery_Yellow.jpg",
        "SERVER_EMPTY_IMG": "/system/basic/Server/server_empty.jpg",
        "SERVER_ERROR_IMG": "/system/basic/Server/server_error.jpg",
        "SERVER_GREEN_IMG": "/system/basic/Server/Server_Green.jpg",
        "WIFI_DISCONNECTED_IMG": "/system/basic/WiFi/wifi_disconnected.jpg",
        "WIFI_EMPTY_IMG": "/system/basic/WiFi/wifi_empty.jpg",
        "WIFI_GOOD_IMG": "/system/basic/WiFi/wifi_good.jpg",
        "WIFI_MID_IMG": "/system/basic/WiFi/wifi_mid.jpg",
        "WIFI_WORSE_IMG": "/system/basic/WiFi/wifi_worse.jpg",
        "APPLIST_SELECTED_IMG": "/system/basic/appList_selected.jpg",
        "APPLIST_UNSELECTED_IMG": "/system/basic/appList_unselected.jpg",
        "APPLIST_IMG": "/system/basic/applist.jpg",
        "APPLIST_LEFT_IMG": "/system/basic/applistLeft.jpg",
        "APPLIST_RIGHT_IMG": "/system/basic/applistRight.jpg",
        "APPRUN_SELECTED_IMG": "/system/basic/appRun_selected.jpg",
        "APPRUN_UNSELECTED_IMG": "/system/basic/appRun_unselected.jpg",
        "BAR1_IMG": "/system/basic/bar1.jpg",
        "BAR2_IMG": "/system/basic/bar2.jpg",
        "BAR3_IMG": "/system/basic/bar3.jpg",
        "BAR4_IMG": "/system/basic/bar4.jpg",
        "BAR5_IMG": "/system/basic/bar5.jpg",
        "BOOT_NO_IMG": "/system/basic/boot_No.jpg",
        "BOOT_YES_IMG": "/system/basic/boot_Yes.jpg",
        "DEVELOP_SELECTED_IMG": "/system/basic/develop_selected.jpg",
        "DEVELOP_UNSELECTED_IMG": "/system/basic/develop_unselected.jpg",
        "DEVELOP_PRIVATE_IMG": "/system/basic/developPrivate.jpg",
        "DEVELOP_PUBLIC_IMG": "/system/basic/developPublic.jpg",
        "EZDATA_SELECTED_IMG": "/system/basic/ezdata_selected.jpg",
        "EZDATA_UNSELECTED_IMG": "/system/basic/ezdata_unselected.jpg",
        "LOGO_IMG": "/system/basic/logo.jpg",
        "RUN_IMG": "/system/basic/run.jpg",
        "SCREEN25_IMG": "/system/basic/screen25.jpg",
        "SCREEN50_IMG": "/system/basic/screen50.jpg",
        "SCREEN75_IMG": "/system/basic/screen75.jpg",
        "SCREEN100_IMG": "/system/basic/screen100.jpg",
        "SETTING_SELECTED_IMG": "/system/basic/setting_selected.jpg",
        "SETTING_UNSELECTED_IMG": "/system/basic/setting_unselected.jpg",
        "SETTING_SELECT_IMG": "/system/basic/settingSelect.jpg",
        "SETTING_UNSELECT_IMG": "/system/basic/settingUnselect.jpg",
        "SETTING_WIFI_IMG": "/system/basic/SettingWifi.jpg",
        "AVATAR_IMG": "/system/common/img/avatar.jpg",
        "USER_AVATAR_PATH": "/system/common/img/",
    }


def __getattr__(attr):
    value = _attrs.get(attr, None)
    if value is None:
        raise AttributeError(attr)
    globals()[attr] = value
    return value
