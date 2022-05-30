import threading
from ctypes.wintypes import MSG
from typing import Union, Tuple
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QByteArray, QRect
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QTableWidget
from win32con import WM_NCCALCSIZE, WM_NCHITTEST, HTCAPTION, HTTOPLEFT, HTBOTTOMLEFT, HTTOPRIGHT, HTBOTTOMRIGHT, HTLEFT, \
    HTRIGHT, HTTOP, HTBOTTOM, HTCLIENT, PBT_APMSUSPEND, WM_POWERBROADCAST, PBT_APMRESUMEAUTOMATIC
from modules.ui.ui_login import LoginWin
from modules.ui.ui_setting import Setting
from modules.ui.ui_winStatus import WinStatus
from modules.setting import MainSetting


class UIFunctions:
    @staticmethod
    def InitUi(widget):
        widget.ui.btn_maximize.setIcon(QIcon(u":/icons/resources/icons/win-maximize.png"))
        widget.ui.grip_icon.setStyleSheet(Setting.RESTOREGRIP_STYLE_NORMAL)
        UIFunctions.setTips(widget)
        widget.ui.btn_exit.clicked.connect(lambda: widget.close())
        widget.ui.btn_close.clicked.connect(lambda: widget.close())
        widget.ui.btn_minimize.clicked.connect(lambda: widget.showMinimized())
        widget.ui.btn_toggle.clicked.connect(widget.btnToggle)
        widget.ui.btn_exp.clicked.connect(widget.btnClicked)
        widget.ui.btn_home.clicked.connect(widget.btnClicked)
        widget.ui.btn_help.clicked.connect(widget.btnClicked)
        widget.ui.btn_maximize.clicked.connect(widget.btnClicked)
        widget.ui.btn_setting.clicked.connect(widget.btnClicked)
        widget.ui.btn_setting_return.clicked.connect(widget.btnClicked)
        widget.ui.btn_conn.clicked.connect(widget.btnClicked)
        widget.ui.btn_logout.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_graph_coor.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_graph_player.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_graph_track.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_clear_1.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_clear_2.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_clear_3.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_table.clicked.connect(widget.btnClicked)
        widget.ui.btn_table_exit.clicked.connect(widget.btnClicked)
        widget.ui.btn_table_refresh.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_remove_1.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_remove_2.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_remove_3.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_graph_fullScreen.clicked.connect(widget.btnClicked)
        widget.ui.btn_table_fullScreen.clicked.connect(widget.btnClicked)
        widget.ui.btn_exit_fullScreen_1.clicked.connect(widget.btnClicked)
        widget.ui.btn_exit_fullScreen_2.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_graph.clicked.connect(widget.btnClicked)
        widget.ui.btn_home_reset.clicked.connect(lambda: widget.resetTable())
        widget.ui.pushButton.clicked.connect(widget.btnClicked)
        widget.ui.book.setCurrentWidget(widget.returnPage("btn_home"))
        UIFunctions.resetStyle(widget, "btn_home", False)
        widget.ui.btn_setting.setStyleSheet(":hover{background-color: rgb(40, 44, 52);}")
        widget.ui.appName.setText(None)

    @staticmethod
    def maximize_restore(widget):
        if widget.isMaximized():
            widget.showNormal()
        else:
            widget.showMaximized()

    @staticmethod
    def windowStateChange(widget):
        state = widget.windowState()
        if state == Qt.WindowNoState:
            widget.ui.appBoxMargins.setContentsMargins(0, 0, 0, 0)
            widget.ui.grip_icon.show()
            widget.ui.grip_icon.setStyleSheet(Setting.RESTOREGRIP_STYLE_NORMAL)
            widget.ui.btn_maximize.setToolTip("最大化")
            widget.ui.btn_maximize.setIcon(QIcon(u":/icons/resources/icons/win-maximize.png"))
        elif state == Qt.WindowMaximized:
            # 9 is the best choice(......)
            widget.ui.appBoxMargins.setContentsMargins(9, 9, 9, 9)
            widget.ui.grip_icon.hide()
            widget.ui.btn_maximize.setToolTip("还原")
            widget.ui.btn_maximize.setIcon(QIcon(u":/icons/resources/icons/restore.png"))
            widget.ui.grip_icon.setStyleSheet(None)

    @staticmethod
    def __unselectStyle(style: str):
        return style.replace(Setting.STYLE_SELECT, "")

    @staticmethod
    def __selectStyle(style: str):
        return "".join([style, Setting.STYLE_SELECT])

    @staticmethod
    def resetStyle(widget, btnName, mode=True):
        oldName = widget.selectedBtn
        if btnName == "btn_home" or btnName == "btn_conn" or btnName == "btn_exp":
            if mode:
                if oldName != btnName:
                    newW = widget.returnBtn(btnName)
                    newW.setStyleSheet(UIFunctions.__selectStyle(newW.styleSheet()))
                    oldW = widget.returnBtn(oldName)
                    oldW.setStyleSheet(UIFunctions.__unselectStyle(oldW.styleSheet()))
                    widget.selectedBtn = btnName
            else:
                nowW = widget.returnBtn(btnName)
                if widget.toggleFold:
                    nowW.setStyleSheet(UIFunctions.__selectStyle(Setting.TOGGLEBOX_FOLD))
                else:
                    nowW.setStyleSheet(UIFunctions.__selectStyle(Setting.TOGGLEBOX_UNFOLD))

    @staticmethod
    def loginEvent(widget):
        if not WinStatus.win_showStatus["loginWidget"]:
            widget.loginWidget = LoginWin()
            widget.loginWidget.show()
            widget.loginWidget.move(widget.retCenterPos(widget.loginWidget))
            WinStatus.win_showStatus["loginWidget"] = True

    @staticmethod
    def btnClicked(widget):
        btnName = widget.sender().objectName()
        if btnName == "btn_maximize":
            UIFunctions.maximize_restore(widget)
        elif btnName == "btn_home_graph_coor":
            lock = threading.Lock()
            tableView = widget.findTbByPage(widget.ui.stackedWidget.currentWidget())
            bCoor = tableView.showCoor
            nowW = widget.returnBtn(btnName)
            othW = widget.returnBtn("btn_home_graph_track")
            try:
                lock.acquire()
                if bCoor:
                    nowW.setStyleSheet(Setting.BTN_COOR_N)
                    othW.hide()
                else:
                    nowW.setStyleSheet(Setting.BTN_COOR_Y)
                    if not tableView.timerStart:
                        othW.show()
                tableView.showCoor = not bCoor
            finally:
                lock.release()
        elif btnName == "btn_home_graph_player":
            nowW = widget.returnBtn(btnName)
            othW = widget.returnBtn("btn_home_graph_track")
            tableView = widget.findTbByPage(widget.ui.stackedWidget.currentWidget())
            if tableView.timerStart:
                nowW.setStyleSheet(Setting.BTN_PLAYER_PAUSE)
                nowW.setToolTip("开始监测")
                if tableView.showCoor:
                    othW.show()
            else:
                nowW.setStyleSheet(Setting.BTN_PLAYER_PLAY)
                nowW.setToolTip("暂停监测")
                othW.hide()
            tableView.changePlayStatus()
        elif btnName == "btn_home_graph_track":
            nowW = widget.returnBtn(btnName)
            tableView = widget.findTbByPage(widget.ui.stackedWidget.currentWidget())
            lock = threading.Lock()
            try:
                lock.acquire()
                if tableView.tracking:
                    nowW.setStyleSheet(Setting.BTN_TRACK_N)
                else:
                    nowW.setStyleSheet(Setting.BTN_TRACK_Y)
                tableView.changeTrackStatus()
            finally:
                lock.release()
        elif btnName == "btn_home_clear_1":
            UIFunctions.clearTable(widget.ui.tableWidget)
        elif btnName == "btn_home_clear_2":
            UIFunctions.clearTable(widget.ui.tableWidget_2)
        elif btnName == "btn_home_clear_3":
            UIFunctions.clearTable(widget.ui.tableWidget_4)
        elif btnName == "btn_home_table" or btnName == "btn_table_exit":
            nowW = widget.returnBtn("btn_home_table")
            lock = threading.Lock()
            try:
                lock.acquire()
                if not widget.tableVisible:
                    if widget.canResponse():
                        widget.ui.home_view.setCurrentWidget(widget.returnPage("home_normal_page"))
                        widget.ui.home_midBox.setMaximumHeight(0)
                        widget.ui.home_tableBox.setMaximumHeight(16777215)
                        UIFunctions.setCheckBoxStatus(widget)
                        nowW.setStyleSheet(Setting.BTN_TABLE_VISIBLE)
                        nowW.setToolTip("关闭表格")
                        widget.tableVisible = True
                else:
                    widget.ui.home_tableBox.setMaximumHeight(0)
                    widget.ui.home_midBox.setMaximumHeight(16777215)
                    nowW.setStyleSheet(Setting.BTN_TABLE_INVISIBLE)
                    nowW.setToolTip("显示表格")
                    widget.tableVisible = False
                    widget.ui.home_view.setCurrentWidget(widget.returnPage("home_normal_page"))
            finally:
                lock.release()
        elif btnName == "btn_table_refresh":
            UIFunctions.setCheckBoxStatus(widget)
        elif btnName == "btn_home_remove_1" or btnName == "btn_home_remove_2" or \
                btnName == "btn_home_remove_3":
            if btnName == "btn_home_remove_1":
                tb = widget.ui.tableWidget
            elif btnName == "btn_home_remove_2":
                tb = widget.ui.tableWidget_2
            else:
                tb = widget.ui.tableWidget_4
            UIFunctions.removeItems(tb)
        elif btnName == "btn_home_graph_fullScreen" or btnName == "btn_table_fullScreen":
            if btnName == "btn_home_graph_fullScreen":
                widget.tableView2.resizeView(widget.ui.home_normal_page.width(),
                                             widget.ui.home_normal_page.height() - 50)
            widget.ui.home_view.setCurrentWidget(widget.returnPage(btnName))
        elif btnName == "btn_exit_fullScreen_1" or btnName == "btn_exit_fullScreen_2":
            widget.ui.home_view.setCurrentWidget(widget.returnPage(btnName))
        elif btnName == "btn_home_graph":
            if widget.canResponse(False):
                widget.managePage()
        elif btnName == "btn_home" or btnName == "btn_conn" or btnName == "btn_exp":
            UIFunctions.resetStyle(widget, btnName)
            if (btnName == "btn_conn" or btnName == "btn_exp") \
                    and WinStatus.win_showStatus["mainWin_login"] is False:
                UIFunctions.loginEvent(widget)
            widget.ui.book.setCurrentWidget(widget.returnPage(btnName))
        elif btnName == "btn_logout":
            if WinStatus.win_showStatus["mainWin_login"]:
                widget.returnBtn(btnName).setText("登录")
                widget.statusSetting.changeIni("mainWin_login", int(False))
            else:
                UIFunctions.loginEvent(widget)
        elif btnName == "btn_help":
            from webbrowser import open
            open("https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html")
        elif btnName == "btn_setting" or btnName == "btn_setting_return":
            UIFunctions.settingBox(widget)
        else:
            widget.messageBox.information("抱歉", "施工中", btn_text3="确认",
                                          btn_func3=lambda: widget.messageBox.close())

    @staticmethod
    def btnToggle(widget):
        lock = threading.Lock()
        width = widget.ui.leftMenu.width()
        standard = Setting.LEFTMENU_STANDARD
        dur = Setting.TIME_ANIMATION_LEFTMENU
        des = Setting.BIN_DESCRIPTION1
        if widget.settingFold:
            offStyle = Setting.BTN_SETTING_FOLD
        else:
            offStyle = Setting.BTN_SETTING_UNFOLD

        try:
            lock.acquire()
            if width == standard:
                widthExtended = Setting.LEFTMENU_EXTENDED
                widget.toggleFold = False
                widget.ui.btn_toggle.setText("折叠")
                widget.ui.appName.setText("PyGibird")
                widget.ui.btn_toggle.setStyleSheet(Setting.TOGGLEBOX_UNFOLD)
                widget.ui.btn_home.setStyleSheet(Setting.TOGGLEBOX_UNFOLD)
                widget.ui.btn_conn.setStyleSheet(Setting.TOGGLEBOX_UNFOLD)
                widget.ui.btn_help.setStyleSheet(Setting.TOGGLEBOX_UNFOLD)
                widget.ui.btn_exp.setStyleSheet(Setting.TOGGLEBOX_UNFOLD)
                widget.ui.btn_exit.setStyleSheet(Setting.TOGGLEBOX_UNFOLD)
                widget.ui.btn_setting.setStyleSheet(Setting.TOGGLEBOX_UNFOLD + offStyle)
            else:
                widthExtended = standard
                widget.toggleFold = True
                widget.ui.btn_toggle.setText("展开")
                widget.ui.appName.setText(None)
                widget.ui.btn_toggle.setStyleSheet(Setting.TOGGLEBOX_FOLD)
                widget.ui.btn_home.setStyleSheet(Setting.TOGGLEBOX_FOLD)
                widget.ui.btn_conn.setStyleSheet(Setting.TOGGLEBOX_FOLD)
                widget.ui.btn_help.setStyleSheet(Setting.TOGGLEBOX_FOLD)
                widget.ui.btn_exp.setStyleSheet(Setting.TOGGLEBOX_FOLD)
                widget.ui.btn_exit.setStyleSheet(Setting.TOGGLEBOX_FOLD)
                widget.ui.btn_setting.setStyleSheet(Setting.TOGGLEBOX_FOLD + offStyle)
        finally:
            lock.release()
        UIFunctions.resetStyle(widget, widget.selectedBtn, False)
        UIFunctions.animation(widget, widget.ui.leftMenu, dur, width, widthExtended, des)

    @staticmethod
    def __btn_setting_style(widget):
        lock = threading.Lock()
        try:
            lock.acquire()
            if widget.toggleFold:
                nowStyle = Setting.TOGGLEBOX_FOLD
            else:
                nowStyle = Setting.TOGGLEBOX_UNFOLD

            if widget.settingFold:
                widget.ui.btn_setting.setStyleSheet(nowStyle + Setting.BTN_SETTING_UNFOLD)
                widget.settingFold = False
            else:
                widget.ui.btn_setting.setStyleSheet(nowStyle + Setting.BTN_SETTING_FOLD)
                widget.settingFold = True
        finally:
            lock.release()

    @staticmethod
    def settingBox(widget):
        width = widget.ui.settingBox.width()
        standard = Setting.SETTINGBOX_STANDARD
        dur = Setting.TIME_ANIMATION_SETTINGBOX
        des1 = Setting.BIN_DESCRIPTION1
        des2 = Setting.BIN_DESCRIPTION2
        if width == standard:
            widthExtended = Setting.SETTINGBOX_EXTENDED
            alpha_beg = 0
            alpha_end = 1.0
        else:
            widthExtended = standard
            alpha_beg = 1.0
            alpha_end = 0
        UIFunctions.__btn_setting_style(widget)
        UIFunctions.animation_sa(widget, widget.ui.settingBox, dur, width, widthExtended,
                                 des1, dur, alpha_beg, alpha_end, des2)

    @staticmethod
    def setTips(widget):
        widget.ui.btn_maximize.setToolTip("最大化")
        widget.ui.btn_close.setToolTip("关闭")
        widget.ui.btn_minimize.setToolTip("最小化")
        widget.ui.btn_home_graph_player.setToolTip("开始监测")

    @staticmethod
    def animation(widget, part, duration, beg, end, description):
        animation = QPropertyAnimation(part, description, widget)
        animation.setDuration(duration)
        animation.setStartValue(beg)
        animation.setEndValue(end)
        animation.setEasingCurve(QEasingCurve.InOutQuart)
        animation.start()

    @staticmethod
    # Size and Alpha
    def animation_sa(widget, part, s_duration, s_beg, s_end,
                     s_description, a_duration, a_beg, a_end, a_description):
        # Resize
        animation1 = QPropertyAnimation(part, s_description, widget)
        animation1.setDuration(s_duration)
        animation1.setStartValue(s_beg)
        animation1.setEndValue(s_end)
        animation1.setEasingCurve(QEasingCurve.InOutQuart)
        # Set Opacity
        effect = QGraphicsOpacityEffect(part)
        effect.setOpacity(a_beg)
        part.setGraphicsEffect(effect)
        animation2 = QPropertyAnimation(effect, a_description, widget)
        animation2.setDuration(a_duration)
        animation2.setStartValue(a_beg)
        animation2.setEndValue(a_end)
        animation1.start()
        animation2.start()

    @staticmethod
    def setting_HoverEvent(widget, enter: bool):
        nowW = widget.returnBtn("btn_setting")
        if widget.settingFold:
            style = Setting.BTN_SETTING_FOLD
        else:
            style = Setting.BTN_SETTING_UNFOLD
        offStyle = Setting.OFFSTYLE
        nowStyle = nowW.styleSheet()
        if enter:
            nowW.setStyleSheet(nowStyle.replace(style, offStyle))
        else:
            nowW.setStyleSheet(nowStyle.replace(offStyle, style))

    @staticmethod
    def myNativeEvent(widget, eventType: Union[QByteArray, bytes], message: int) -> Tuple[object, int]:
        msg = MSG.from_address(message.__int__())
        form = QMainWindow.find(msg.hWnd)

        if not form:
            return False
        if msg.message == WM_NCCALCSIZE:
            return True, 0
        elif msg.message == WM_NCHITTEST:
            geo = widget.frameGeometry()
            posX = (msg.lParam & 65535) - geo.x()
            posY = (msg.lParam >> 16) - geo.y()
            mousePos = QPoint(posX, posY)

            offSize = Setting.OFFSET
            rectTitlebar = QRect(widget.ui.logoBox.width() + widget.ui.settingBox.width(), offSize / 2,
                                 (widget.width() - widget.ui.topRightMenu.width() -
                                  widget.ui.logoBox.width() - widget.ui.settingBox.width()),
                                 widget.ui.topBar.height() - offSize / 2)
            rectTopLeft = QRect(0, 0, offSize / 2, offSize / 2)
            rectTopRight = QRect(widget.width() - offSize / 2, 0, offSize / 2, offSize / 2)
            rectBottomLeft = QRect(0, widget.height() - offSize / 2, offSize / 2, offSize / 2)
            rectBottomRight = QRect(widget.width() - offSize, widget.height() - offSize, offSize, offSize)
            rectLeft = QRect(0, offSize / 2, offSize / 2, widget.height() - offSize)
            rectRight = QRect(widget.width() - offSize / 2, offSize / 2, offSize / 2, widget.height() - offSize)
            rectTop = QRect(offSize / 2, 0, widget.width() - offSize, offSize / 2)
            rectBottom = QRect(offSize / 2, widget.height() - offSize / 2, widget.width() - offSize, offSize / 2)

            if rectTitlebar.contains(mousePos):
                result = HTCAPTION
            elif not widget.isMaximized():
                if rectTopLeft.contains(mousePos):
                    result = HTTOPLEFT
                elif rectTopRight.contains(mousePos):
                    result = HTTOPRIGHT
                elif rectBottomLeft.contains(mousePos):
                    result = HTBOTTOMLEFT
                elif rectBottomRight.contains(mousePos):
                    result = HTBOTTOMRIGHT
                elif rectLeft.contains(mousePos):
                    result = HTLEFT
                elif rectRight.contains(mousePos):
                    result = HTRIGHT
                elif rectTop.contains(mousePos):
                    result = HTTOP
                elif rectBottom.contains(mousePos):
                    result = HTBOTTOM
                else:
                    result = HTCLIENT
            else:
                result = HTCLIENT
            return True, result
        # Fix the problem after PC sleep or hibernate
        elif msg.wParam == PBT_APMSUSPEND and msg.message == WM_POWERBROADCAST:
            widget.showMinimized()
        elif msg.wParam == PBT_APMRESUMEAUTOMATIC:
            widget.showNormal()
        return QMainWindow.nativeEvent(widget, eventType, message)

    @staticmethod
    def clearTable(tb):
        for i in range(tb.rowCount()):
            tb.removeRow(0)

    @staticmethod
    def setCheckBoxStatus(widget):
        tb: QTableWidget = widget.ui.tableWidget
        lst = MainSetting.check_list
        for i in range(len(lst)):
            btn = widget.returnCheckBox(lst[i])
            btn.hide()
        for i in range(tb.rowCount()):
            btn = widget.returnCheckBox(tb.item(i, 0).text())
            btn.setChecked(True)
            btn.show()

    @staticmethod
    def removeItems(tb: QTableWidget):
        off = 0
        for i in range(tb.rowCount()):
            if tb.item(i - off, 0).isSelected():
                tb.removeRow(i - off)
                off += 1
