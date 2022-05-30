from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QMenu
from win32api import SetWindowLong, GetWindowLong
from win32con import GWL_STYLE, WS_MAXIMIZEBOX, WS_THICKFRAME, WS_CAPTION
from modules.ui.ui_messageBox import MessageBox
from modules.ui.ui_style import *
from modules.ui.ui_winStatus import status_opn
from modules.ui.ui_setting import Setting
from modules.setting import MainSetting
from modules.graph import TableView


class MainWindow_base(QMainWindow):
    def __init__(self):
        super(MainWindow_base, self).__init__()
        self.statusSetting = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.preWidth = self.width()
        self.pageList = [[self.ui.tableViewPage1, False, None],
                         [self.ui.tableViewPage2, False, None],
                         [self.ui.tableViewPage3, False, None],
                         [self.ui.tableViewPage4, False, None],
                         [self.ui.tableViewPage5, False, None],
                         [self.ui.tableViewPage6, False, None]]
        self.btn_page = [["home_graph_1", None], ["home_graph_2", None],
                         ["home_graph_3", None], ["home_graph_4", None],
                         ["home_graph_5", None], ["home_graph_6", None]]
        self.pageSelect = None
        self.selectedBtn = "btn_home"
        self.toggleFold = True
        self.settingFold = True
        self.tableVisible = False
        # flash will occur when you drag window if set the attribute, you may need it to set shadow
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.hWnd = self.winId()
        SetWindowLong(self.hWnd, GWL_STYLE, GetWindowLong(self.hWnd, GWL_STYLE) | WS_MAXIMIZEBOX |
                      WS_THICKFRAME | WS_CAPTION)
        self.messageBox = MessageBox(self)
        self.initUi()

    def initUi(self):
        self.ui.btn_setting.installEventFilter(self)
        self.ui.btn_setting.setAttribute(Qt.WA_Hover)
        self.statusSetting = status_opn()
        self.set_btn_logout_text()
        MainSetting.widget = id(self)
        self.setBtnMenu()
        self.ui.home_table.setSortingEnabled(True)
        self.ui.home_table.sortItems(0)
        self.ui.home_table.horizontalHeader().setSortIndicatorShown(True)
        self.ui.home_table.horizontalHeader().setSortIndicator(0, Qt.SortOrder.AscendingOrder)
        self.ui.btn_home_graph_track.hide()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.home_table_topMenu.hide()

    def returnBtn(self, name):
        if name == "btn_home":
            return self.ui.btn_home
        elif name == "btn_conn":
            return self.ui.btn_conn
        elif name == "btn_exp":
            return self.ui.btn_exp
        elif name == "btn_setting":
            return self.ui.btn_setting
        elif name == "btn_logout":
            return self.ui.btn_logout
        elif name == "btn_home_graph_track":
            return self.ui.btn_home_graph_track
        elif name == "btn_home_graph_player":
            return self.ui.btn_home_graph_player
        elif name == "btn_home_graph_coor":
            return self.ui.btn_home_graph_coor
        elif name == "btn_home_clear_1":
            return self.ui.btn_home_clear_1
        elif name == "btn_home_clear_2":
            return self.ui.btn_home_clear_2
        elif name == "btn_home_table":
            return self.ui.btn_home_table
        elif name == "btn_table_filter":
            return self.ui.btn_table_filter
        elif name == "btn_table_fullScreen":
            return self.ui.btn_table_fullScreen
        elif name == "btn_table_refresh":
            return self.ui.btn_table_refresh
        elif name == "btn_home_remove_1":
            return self.ui.btn_home_remove_1
        elif name == "btn_home_remove_2":
            return self.ui.btn_home_remove_2
        elif name == "btn_exit_fullScreen_1":
            return self.ui.btn_exit_fullScreen_1
        elif name == "btn_exit_fullScreen_2":
            return self.ui.btn_exit_fullScreen_2
        elif name == "home_graph_1":
            return [self.ui.home_graph_1, self.ui.graphBox_1, self.ui.home_graph_exit_1]
        elif name == "home_graph_2":
            return [self.ui.home_graph_2, self.ui.graphBox_2, self.ui.home_graph_exit_2]
        elif name == "home_graph_3":
            return [self.ui.home_graph_3, self.ui.graphBox_3, self.ui.home_graph_exit_3]
        elif name == "home_graph_4":
            return [self.ui.home_graph_4, self.ui.graphBox_4, self.ui.home_graph_exit_4]
        elif name == "home_graph_5":
            return [self.ui.home_graph_5, self.ui.graphBox_5, self.ui.home_graph_exit_5]
        elif name == "home_graph_6":
            return [self.ui.home_graph_6, self.ui.graphBox_6, self.ui.home_graph_exit_6]

    def returnCheckBox(self, name):
        if name == "炉膛":
            return self.ui.check_furnace
        elif name == "过热器":
            return self.ui.check_superheater
        elif name == "再热器":
            return self.ui.check_reheater
        elif name == "省煤器":
            return self.ui.check_economizer
        elif name == "空气预热器":
            return self.ui.check_airPreheater

    def returnPage(self, name):
        if name == "btn_home":
            return self.ui.page_home
        elif name == "btn_conn":
            return self.ui.page_conn
        elif name == "btn_exp":
            return self.ui.page_exp
        elif name == "btn_home_graph_fullScreen":
            return self.ui.home_maximize_graph_page
        elif name == "btn_table_fullScreen":
            return self.ui.home_maximize_table_page
        elif name == "btn_exit_fullScreen_1" or name == "btn_exit_fullScreen_2" \
                or name == "home_normal_page":
            return self.ui.home_normal_page
        elif name == "tableViewPage":
            return self.ui.tableViewPage
        elif name == "tableViewPage1":
            return self.ui.tableViewPage1
        elif name == "tableViewPage2":
            return self.ui.tableViewPage2
        elif name == "tableViewPage3":
            return self.ui.tableViewPage3
        elif name == "tableViewPage4":
            return self.ui.tableViewPage4
        elif name == "tableViewPage5":
            return self.ui.tableViewPage5
        elif name == "tableViewPage6":
            return self.ui.tableViewPage6

    def retCenterPos(self, widget):
        geo = self.geometry()
        x = geo.x() + (self.width() - widget.width()) / 2
        y = geo.y() + (self.height() - widget.height()) / 2
        return QPoint(x, y)

    def set_btn_logout_text(self):
        self.ui.btn_logout.setText(
            "退出登录" if self.statusSetting.retVal("mainWin_login") else "登录")

    def setBtnMenu(self):
        menu_1 = QMenu(self)
        menu_opn1 = BtnActions()
        menu_opn1.addActions(self, ["炉膛", "过热器", "再热器", "省煤器", "空气预热器"])
        menu_1.addActions(menu_opn1.actions)
        menu_1.addSeparator()
        btn_1 = QAction("添加所选", self)
        btn_2 = QAction("添加全部", self)
        menu_1.addAction(btn_1)
        menu_1.addAction(btn_2)
        menu_1.setStyleSheet(Setting.MENU_STYLE)
        self.ui.btn_home_select_part.setMenu(menu_1)

        menu_2 = QMenu(self)
        menu_opn2 = BtnActions()
        menu_opn2.addAction("灰污系数", self)
        menu_2.addActions(menu_opn2.actions)
        menu_2.addAction(QAction("其他暂无", self))
        menu_2.addSeparator()
        btn_3 = QAction("添加所选", self)
        btn_4 = QAction("添加全部", self)
        menu_2.addAction(btn_3)
        menu_2.addAction(btn_4)
        menu_2.setStyleSheet(Setting.MENU_STYLE)
        self.ui.btn_home_select_para.setMenu(menu_2)

        def mouseRelease_1(e: QMouseEvent):
            action = menu_1.actionAt(e.pos())
            if action and not menu_opn1.notIn(action):
                action.activate(QAction.Trigger)
            else:
                QMenu.mouseReleaseEvent(menu_1, e)

        menu_1.mouseReleaseEvent = mouseRelease_1

        def mouseRelease_2(e: QMouseEvent):
            action = menu_2.actionAt(e.pos())
            if action and not menu_opn2.notIn(action):
                action.activate(QAction.Trigger)
            else:
                QMenu.mouseReleaseEvent(menu_2, e)

        menu_2.mouseReleaseEvent = mouseRelease_2
        dic_1 = MainSetting.btn1_dic
        dic_2 = MainSetting.btn2_dic
        tb_1 = self.ui.tableWidget
        tb_2 = self.ui.tableWidget_2
        btn_1.triggered.connect(lambda: BtnActions.btnActionEvent(tb_1, dic_1, True, menu_opn1, self))
        btn_2.triggered.connect(lambda: BtnActions.btnActionEvent(tb_1, dic_1, False, menu_opn1, self))
        btn_3.triggered.connect(lambda: BtnActions.btnActionEvent(tb_2, dic_2, True, menu_opn2, self))
        btn_4.triggered.connect(lambda: BtnActions.btnActionEvent(tb_2, dic_2, False, menu_opn2, self))

    def canResponse(self, bTable=True):
        if bTable:
            if self.ui.tableWidget.item(0, 0) is not None:
                return True
            self.messageBox.information("提示", "未选择 [选择部位] ", btn_text3="确认",
                                        btn_func3=lambda: self.messageBox.close())
        else:
            if self.ui.tableWidget.item(0, 0) is not None and \
                    self.ui.tableWidget_2.item(0, 0) is not None:
                return True
            self.messageBox.information("提示", "未选择 [选择部位] 或 [选择参数] ", btn_text3="确认",
                                        btn_func3=lambda: self.messageBox.close())
        return False

    def resetTable(self):
        tb = self.ui.tableWidget_4
        for i in range(tb.rowCount()):
            tb.removeRow(0)
        tb1 = self.ui.tableWidget
        tb2 = self.ui.tableWidget_2
        row = tb2.rowCount()
        for j in range(tb1.rowCount()):
            text1 = tb1.item(j, 0).text()
            for k in range(row):
                text2 = tb2.item(k, 0).text()
                row2 = row * j + k
                tb.insertRow(row2)
                for m in range(tb.columnCount()):
                    if m == 0:
                        item = QTableWidgetItem("".join([text1, MainWindow_base.returnOffStr(text2)]))
                    elif m == 1:
                        item = QTableWidgetItem(text2)
                    elif m == 2:
                        item = QTableWidgetItem("00:00")
                    else:
                        item = QTableWidgetItem("30:00")
                    item.setFlags(item.flags() & (~Qt.ItemIsEditable))
                    tb.setItem(row2, m, item)

    def managePage(self):
        lst1 = []
        lst2 = []
        for page in self.pageList:
            if not page[1]:
                lst1.append(page)
            else:
                lst2.append(page)
        ret = self.__realSize(lst2)
        if ret[0] != 0:
            repeatLst = [ret[i] for i in range(1, len(ret))]
            if len(lst1) - ret[0] < 0:
                def continueEvent():
                    self.__insertGraph(lst1, repeatLst)
                    self.messageBox.close()

                self.messageBox.information(
                    "警告", "图像将超过限制 [6] ", "请选择 [继续添加] 或 [取消添加]",
                    "继续添加", btn_text3="取消添加", btn_func1=continueEvent,
                    btn_func3=lambda: self.messageBox.close())
            else:
                self.__insertGraph(lst1, repeatLst)

    def __realSize(self, lst):
        tb = self.ui.tableWidget_4
        repeatSize = 0
        ret = [0]
        for row in range(tb.rowCount()):
            for page in lst:
                if page[2].id == "".join([tb.item(row, 0).text(), tb.item(row, 1).text()]):
                    repeatSize += 1
                    ret.append(row)
        ret[0] = tb.rowCount() - repeatSize
        return ret

    def __insertGraph(self, lst, repeatLst):
        tb = self.ui.tableWidget_4
        restLst = [i for i in range(tb.rowCount()) if repeatLst.count(i) == 0]
        page_iter = lst.__iter__()
        for row in restLst:
            try:
                pageLst = page_iter.__next__()
                parent = pageLst[0]
                pageLst[1] = True
                text1 = tb.item(row, 0).text()
                text2 = tb.item(row, 1).text()
                pageLst[2] = TableView(parent, text1, "", text2, self.ui.tableViewPage.width(),
                                       self.ui.tableViewPage.height(), scatter=True, subline=True)
                self.__availableBtn(pageLst[0], text1, text2)
            except StopIteration:
                return

    def __availableBtn(self, page, text1, text2):
        for btnLst in self.btn_page:
            if btnLst[1] is None:
                btnLst[1] = page
                self.__setPageBtnStyle(self.returnBtn(btnLst[0]), page.objectName(), text1, text2)
                return

    def __setPageBtnStyle(self, btnList, page, text1, text2):
        btn = btnList[0]
        frame = btnList[1]
        exitBtn = btnList[2]
        p = self.returnPage(page)
        if self.pageSelect is None:
            frame.setStyleSheet(Setting.BTN_GRAPH_SELECTED)
            self.ui.stackedWidget.setCurrentWidget(p)
            self.pageSelect = frame
            self.menuVisible()
        else:
            frame.setStyleSheet(Setting.BTN_GRAPH_VISIBLE)
        btn.setText("".join([text1, MainWindow_base.returnOffStr(text2)]))
        exitBtn.setStyleSheet(Setting.BTN_GRAPH_EXIT)

        def func():
            self.ui.stackedWidget.setCurrentWidget(p)
            self.resizePage(p)
            if self.pageSelect != frame:
                frame.setStyleSheet(Setting.BTN_GRAPH_SELECTED)
                if self.pageSelect is not None:
                    self.pageSelect.setStyleSheet(Setting.BTN_GRAPH_VISIBLE)
                    # You can inherit previous state, but I choose to reset them for convenience's sake
                    self.findTbByPage(p).changePlayStatus(True)
                    self.refreshStatus()
                self.pageSelect = frame

        btn.clicked.connect(func)
        exitBtn.clicked.connect(lambda: self.messageBox.information(
            "抱歉", "施工中......", "计划中有 [移除] 与 [位置交换] 操作", btn_text3="确定",
            btn_func3=lambda: self.messageBox.close()))

    def resizePage(self, page):
        for p in self.pageList:
            parent = p[0]
            if parent == page:
                tb = p[2]
                tb.view.setGeometry(0, 0, parent.width(), parent.height())
                tb.chartView.setGeometry(0, 0, parent.width(), parent.height())
                return

    def menuVisible(self):
        if self.pageSelect is None:
            self.ui.home_table_topMenu.hide()
        else:
            self.ui.home_table_topMenu.show()

    def findTbByPage(self, page):
        for p in self.pageList:
            if p[0] == page:
                return p[2]
        return None

    def refreshStatus(self):
        self.ui.btn_home_graph_track.setStyleSheet(Setting.BTN_TRACK_N)
        self.ui.btn_home_graph_player.setStyleSheet(Setting.BTN_PLAYER_PAUSE)
        self.ui.btn_home_graph_coor.setStyleSheet(Setting.BTN_COOR_N)
        self.ui.btn_home_graph_track.hide()

    @staticmethod
    def returnOffStr(text):
        if text == "灰污系数":
            return ""
        return ""

    @staticmethod
    def exist(tb: QTableWidget, text, originalRows):
        for i in range(originalRows):
            if tb.item(i, 0).text() == text:
                return True
        return False

    @staticmethod
    def exist_override(tb: QTableWidget, text1, text2, originalRows):
        for i in range(originalRows):
            if tb.item(i, 0).text() == text1 and tb.item(i, 1) == text2:
                return True
        return False

    @staticmethod
    def setMySQLInfo(host, port, uid, pwd):
        MainSetting.sqlHost = host
        MainSetting.sqlPort = port
        MainSetting.sqlAcc = uid
        MainSetting.sqlPwd = pwd


class BtnActions:
    def __init__(self):
        self.actions = []

    def addAction(self, name: str, parent, checkable=True):
        action = QAction(name, parent)
        action.setCheckable(checkable)
        self.actions.append(action)

    def addActions(self, parent, lst, checkable=True):
        for name in lst:
            self.addAction(name, parent, checkable)

    def retActions(self, bChecked=True):
        if bChecked:
            return [act for act in self.actions if act.isChecked()]
        else:
            return self.actions

    def notIn(self, action):
        for act in self.actions:
            if act == action:
                return False
        return True

    @staticmethod
    def btnActionEvent(nowTb, dic, check, menu_opn, widget):
        lst = menu_opn.retActions(check)
        rows = nowTb.rowCount()
        originalRows = rows
        for act in lst:
            text = act.text()
            if not MainWindow_base.exist(nowTb, text, originalRows):
                nowTb.insertRow(rows)
                item_first = QTableWidgetItem(text)
                item_first.setFlags(item_first.flags() & (~Qt.ItemIsEditable))
                nowTb.setItem(rows, 0, item_first)
                columns = 1
                for item in dic[text]:
                    item_other = QTableWidgetItem(item)
                    item_other.setFlags(item_other.flags() & (~Qt.ItemIsEditable))
                    nowTb.setItem(rows, columns, item_other)
                    columns += 1
                rows += 1
        if not widget.ui.tableWidget_4.item(0, 0) and \
                widget.ui.tableWidget.item(0, 0) and \
                widget.ui.tableWidget_2.item(0, 0):
            widget.resetTable()
