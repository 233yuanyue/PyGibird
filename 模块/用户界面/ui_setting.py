class Setting:
    RESTOREGRIP_STYLE_NORMAL = "background-position:right bottom;\n" \
                               "background-repeat:no repeat;\n" \
                               "background-image: url(:/icons/resources/icons/resizeGrip.png);"
    TOGGLEBOX_FOLD = "font: 12pt \"Microsoft YaHei UI\";\n" \
                     "color:rgb(255, 255, 255);\n" \
                     "background-position:center;\n" \
                     "text-align:bottom center;\n" \
                     "border-bottom: 12px solid transparent;"
    TOGGLEBOX_UNFOLD = "background-position:left center;\n" \
                       "border-left:22px solid transparent;\n" \
                       "border-top:12px solid transparent;\n" \
                       "text-align:left center;\n" \
                       "padding-left:50px;\n" \
                       "font: 12pt \"Microsoft YaHei UI\";\n" \
                       "color:rgb(255, 255, 255);"
    STYLE_SELECT = "color: rgb(255, 255, 255);\n" \
                   "background-color: rgb(75, 110, 175);"
    BTN_SETTING_FOLD = "QPushButton{background-color: rgb(33, 37, 43);}"
    BTN_SETTING_UNFOLD = "background-color: rgb(44, 49, 58);"
    OFFSTYLE = "background-color: rgb(40, 44, 52);"

    """======================================================================================================"""
    LOGIN_MSG_LABEL_STYLE = "color: rgb(255, 130, 104);\n" \
                            "font: 12pt \"Microsoft YaHei UI\";\n" \
                            "background-repeat:no-repeat;\n" \
                            "background-position:left;\n" \
                            "text-align:left;\n" \
                            "background-image: url(:/icons/resources/icons/error_red.png);\n" \
                            "padding-left:15px;\n"
    LOGIN_BTN_VISIBLE_IN_STYLE = "background-image: url(:/icons/resources/icons/visible_blue.png);"
    LOGIN_BTN_VISIBLE_OUT_STYLE = "background-image: url(:/icons/resources/icons/visible.png);"
    LOGIN_BTN_INVISIBLE_IN_STYLE = "background-image: url(:/icons/resources/icons/invisible_blue.png);"
    LOGIN_BTN_INVISIBLE_OUT_STYLE = "background-image: url(:/icons/resources/icons/invisible.png);"
    LOGIN_QLINEEDIT_FOCUSOUT_STYLE = ".QFrame{border:1px solid rgb(219, 219, 219);\n" \
                                     "border-radius:6px;\n" \
                                     "margin-bottom:10px solid transparent;}"
    LOGIN_QLINEEDIT_FOCUSIN_STYLE = ".QFrame{border:1px solid rgb(38, 112, 234);\n" \
                                    "border-radius:6px;\n" \
                                    "margin-bottom:10px solid transparent;}"
    ACC_INPUT_STYLE = "color"
    """================================================================================================"""
    MENU_STYLE = "QMenu{font: 12pt \"Microsoft YaHei UI\";\n" \
                 "color:rgb(255, 255, 255);\n" \
                 "background-color: rgb(48, 50, 52);\n" \
                 "border:1px solid rgb(107, 107, 107);\n" \
                 "width:150px}\n" \
                 "QMenu::item{background-color:transparent;\n" \
                 "height:25px;\n" \
                 "padding:5px 20px;}\n" \
                 "QMenu::indicator:checked{background-image: url(:/icons/resources/icons/checked_blue.png);}\n" \
                 "QMenu::item:selected{background-color: rgb(75, 110, 175);}\n" \
                 "QMenu::separator{height:1px;\n" \
                 "background-color: rgb(107, 107, 107);}"
    """==============================================================================================="""
    BTN_TRACK_Y = "QPushButton{background-image: url(:/icons/resources/icons/track_blue.png);\n" \
                  "background-position:center;\n" \
                  "background-repeat:no-repeat;\n" \
                  "margin-right:2px solid transparent;\n" \
                  "border-radius:3px;}\n" \
                  "QPushButton:hover{background-color: rgb(76, 80, 82);}\n" \
                  "QPushButton:pressed{background-color: rgb(92, 97, 100);}"
    BTN_TRACK_N = "QPushButton{background-image: url(:/icons/resources/icons/track_gray.png);\n" \
                  "background-position:center;\n" \
                  "background-repeat:no-repeat;\n" \
                  "margin-right:2px solid transparent;\n" \
                  "border-radius:3px;}\n" \
                  "QPushButton:hover{background-color: rgb(76, 80, 82);}\n" \
                  "QPushButton:pressed{background-color: rgb(92, 97, 100);}"
    """======================================================================================================"""
    BTN_COOR_Y = "QPushButton{background-image: url(:/icons/resources/icons/coor_blue.png);\n" \
                 "background-position:center;\n" \
                 "background-repeat:no-repeat;\n" \
                 "margin-right:2px solid transparent;\n" \
                 "border-radius:3px;}\n" \
                 "QPushButton:hover{background-color: rgb(76, 80, 82);}\n" \
                 "QPushButton:pressed{background-color: rgb(92, 97, 100);}"
    BTN_COOR_N = "QPushButton{background-image: url(:/icons/resources/icons/coor_gray.png);\n" \
                 "background-position:center;\n" \
                 "background-repeat:no-repeat;\n" \
                 "margin-right:2px solid transparent;\n" \
                 "border-radius:3px;}\n" \
                 "QPushButton:hover{background-color: rgb(76, 80, 82);}\n" \
                 "QPushButton:pressed{background-color: rgb(92, 97, 100);}"
    """==================================================================================================="""
    BTN_PLAYER_PAUSE = "QPushButton{background-image: url(:/icons/resources/icons/play.png);\n" \
                       "background-position:center;\n" \
                       "background-repeat:no-repeat;\n" \
                       "margin-right:2px solid transparent;\n" \
                       "border-radius:3px;}\n" \
                       "QPushButton:hover{background-color: rgb(76, 80, 82);}\n" \
                       "QPushButton:pressed{background-color: rgb(92, 97, 100);}"
    BTN_PLAYER_PLAY = "QPushButton{background-image: url(:/icons/resources/icons/pause.png);\n" \
                      "background-position:center;\n" \
                      "background-repeat:no-repeat;\n" \
                      "margin-right:2px solid transparent;\n" \
                      "border-radius:3px;}\n" \
                      "QPushButton:hover{background-color: rgb(76, 80, 82);}\n" \
                      "QPushButton:pressed{background-color: rgb(92, 97, 100);}"
    """===================================================================================================="""
    BTN_TABLE_VISIBLE = "QPushButton{border-left:1px solid rgb(109, 109, 109);\n" \
                        "background-repeat:no repeat;background-position:center;\n" \
                        "background-image: url(:/icons/resources/icons/table_blue.png);}\n" \
                        ":hover{background-color: rgb(58, 60, 62);}\n" \
                        ":pressed{background-color:rgb(68, 75, 75);}"
    BTN_TABLE_INVISIBLE = "QPushButton{border-left:1px solid rgb(109, 109, 109);\n" \
                          "background-repeat:no repeat;background-position:center;\n" \
                          "background-image: url(:/icons/resources/icons/table_gray.png);}\n" \
                          ":hover{background-color: rgb(58, 60, 62);}\n" \
                          ":pressed{background-color:rgb(68, 75, 75);}"
    """====================================================================================================="""
    BTN_GRAPH_EXIT = "QPushButton{background-repeat:no repeat;\n" \
                     "background-position:center;\nborder-radius:10px;\n" \
                     "background-image: url(:/icons/resources/icons/close_small_gray.png);}\n" \
                     ":hover{background-color: rgb(92, 97, 100);\n" \
                     "background-image: url(:/icons/resources/icons/close_small_black.png);}"
    BTN_GRAPH_SELECTED = "QFrame{padding-left:10px;\n" \
                         "padding-right:10px;\n" \
                         "background-color: rgb(78, 82, 84);}"
    BTN_GRAPH_VISIBLE = ":hover{background-color: rgb(33, 37, 43);}\n" \
                        "QFrame{padding-left:10px;\n" \
                        "padding-right:10px}"
    """======================================================================================================"""
    TIME_ANIMATION_LEFTMENU = 0
    TIME_ANIMATION_SETTINGBOX = 400
    LEFTMENU_STANDARD = 80
    LEFTMENU_EXTENDED = 160
    SETTINGBOX_STANDARD = 0
    SETTINGBOX_EXTENDED = 400
    BIN_DESCRIPTION1 = b"minimumWidth"
    BIN_DESCRIPTION2 = b"opacity"
    OFFSET = 10
