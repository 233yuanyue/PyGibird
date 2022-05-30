import threading
import _ctypes
from PySide6.QtCore import QEvent
from PySide6.QtGui import QMouseEvent, QHoverEvent
from modules.ui.ui_setting import Setting
from modules.ui.ui_style_login import *
from modules.data import Db
from modules.ui.ui_winStatus import WinStatus, status_opn
from modules.setting import MainSetting


class LoginWin(QWidget):
    def __init__(self):
        super(LoginWin, self).__init__()
        self.ui = Ui_loginWidget()
        self.ui.setupUi(self)
        # Call the object through pointer(id)
        self.parentWin = _ctypes.PyObj_FromPtr(MainSetting.widget)
        self.statusSetting = status_opn()
        self.pwd_invisible = True
        self.isPressed = False
        self.btnName = None
        self.prePos = None
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint |
                            Qt.SubWindow | Qt.WindowStaysOnTopHint)
        self.ui.btn_visible.installEventFilter(self)
        self.ui.acc_text.installEventFilter(self)
        self.ui.pwd_text.installEventFilter(self)
        self.ui.btn_visible.setAttribute(Qt.WA_Hover)
        self.uiInit()

    def uiInit(self):
        self.ui.msg_label.setText(None)
        self.ui.msg_label.setStyleSheet(None)
        self.ui.btn_login.clicked.connect(self.btnClicked)
        self.ui.btn_exit.clicked.connect(self.btnClicked)
        self.ui.acc_icon.clicked.connect(self.btnClicked)
        self.ui.btn_visible.clicked.connect(self.btnClicked)
        self.ui.checkBox.clicked.connect(lambda: self.statusSetting.changeIni(
            "rememberAcc", int(self.ui.checkBox.isChecked())))
        self.ui.btn_visible.setStyleSheet(Setting.LOGIN_BTN_INVISIBLE_OUT_STYLE)
        self.setTopEvent()
        self.ui.acc_text.setFocus()
        self.ui.checkBox.setChecked(self.statusSetting.retVal("rememberAcc"))
        self.setAccBottom()
        self.ui.acc_bottom.activated.connect(self.acc_bottom_indChange)
        # I don't know why they cannot properly work
        # LoginWin.setPlaceholderTextColor(self.ui.acc_text)
        # LoginWin.setPlaceholderTextColor(self.ui.pwd_text)

    # @staticmethod
    # def setPlaceholderTextColor(_lineEdit):
    #     lineEdit = QLineEdit(_lineEdit)
    #     pal = lineEdit.palette()
    #     pal.setColor(QPalette.Normal, QPalette.PlaceholderText, QColor(255, 255, 255))
    #     lineEdit.setPalette(pal)

    def acc_bottom_indChange(self):
        num = self.ui.acc_bottom.count()
        if self.ui.acc_bottom.currentIndex() == num - 1:
            self.statusSetting.clearCache()
            while num > 1:
                self.ui.acc_bottom.removeItem(0)
                num -= 1
            self.ui.acc_text.setText(None)
        else:
            self.ui.acc_text.setText(self.ui.acc_bottom.currentText())

    def setAccBottom(self):
        info = self.statusSetting.retAcc_cacheInfo()
        if info is not None:
            for acc in info:
                self.ui.acc_bottom.insertItem(0, acc[0])
                self.ui.acc_text.setText(acc[0])

    def setTopEvent(self):
        def topPress(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton:
                self.prePos = event.globalPos()
                self.isPressed = True
            event.accept()

        self.ui.topMoveArea.mousePressEvent = topPress

        def topRelease(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton:
                self.isPressed = False
            event.accept()

        self.ui.topMoveArea.mouseReleaseEvent = topRelease

        def topMovement(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton and self.isPressed:
                self.move(event.globalPos() + self.pos() - self.prePos)
                self.prePos = event.globalPos()
            event.accept()

        self.ui.topMoveArea.mouseMoveEvent = topMovement

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        objName = watched.objectName()
        if event.type() == QHoverEvent.HoverEnter and objName == "btn_visible":
            self.pwdHoverEvent(True)
            return True
        elif event.type() == QHoverEvent.HoverLeave and objName == "btn_visible":
            self.pwdHoverEvent(False)
            return True
        elif event.type() == QHoverEvent.FocusIn and objName == "acc_text":
            QLineEdit.focusInEvent(self.ui.acc_text, event)
            self.ui.AccountBox.setStyleSheet(Setting.LOGIN_QLINEEDIT_FOCUSIN_STYLE)
            return True
        elif event.type() == QHoverEvent.FocusOut and objName == "acc_text":
            QLineEdit.focusOutEvent(self.ui.acc_text, event)
            self.ui.AccountBox.setStyleSheet(Setting.LOGIN_QLINEEDIT_FOCUSOUT_STYLE)
            return True
        elif event.type() == QHoverEvent.FocusIn and objName == "pwd_text":
            QLineEdit.focusInEvent(self.ui.pwd_text, event)
            self.ui.PasswordBox.setStyleSheet(Setting.LOGIN_QLINEEDIT_FOCUSIN_STYLE)
            return True
        elif event.type() == QHoverEvent.FocusOut and objName == "pwd_text":
            QLineEdit.focusOutEvent(self.ui.pwd_text, event)
            self.ui.PasswordBox.setStyleSheet(Setting.LOGIN_QLINEEDIT_FOCUSOUT_STYLE)
            return True
        return QWidget.eventFilter(self, watched, event)

    def pwdHoverEvent(self, enter: bool):
        if self.pwd_invisible:
            if enter:
                self.ui.btn_visible.setStyleSheet(Setting.LOGIN_BTN_INVISIBLE_IN_STYLE)
            else:
                self.ui.btn_visible.setStyleSheet(Setting.LOGIN_BTN_INVISIBLE_OUT_STYLE)
        else:
            if enter:
                self.ui.btn_visible.setStyleSheet(Setting.LOGIN_BTN_VISIBLE_IN_STYLE)
            else:
                self.ui.btn_visible.setStyleSheet(Setting.LOGIN_BTN_VISIBLE_OUT_STYLE)

    def btnClicked(self):
        btnName = self.sender().objectName()
        if btnName == "btn_login":
            self.loginMsg()
        elif btnName == "acc_icon":
            self.ui.acc_bottom.showPopup()
        elif btnName == "btn_visible":
            self.visibleChange()
        elif btnName == "btn_exit":
            self.close()
            WinStatus.win_showStatus[self.objectName()] = False

    def loginMsg(self):
        accText = self.ui.acc_text.text()
        pwdText = self.ui.pwd_text.text()
        if accText == "":
            msg = "账号不能为空!"
        elif accText != "" and pwdText == "":
            msg = "密码不能为空!"
        elif LoginWin.check_acc_pwd(accText, pwdText):
            self.parentWin.messageBox.information(
                "提示", "登陆成功!!!", btn_text3="确认",
                btn_func3=lambda: self.parentWin.messageBox.close())
            self.close()
            WinStatus.win_showStatus[self.objectName()] = False
            self.statusSetting.changeIni("mainWin_login", int(True))
            self.parentWin.set_btn_logout_text()
            if self.statusSetting.retVal("rememberAcc"):
                self.statusSetting.insertCache(accText)
            return
        else:
            msg = "账号或密码错误!"
        self.ui.msg_label.setText(msg)
        self.ui.msg_label.setStyleSheet(Setting.LOGIN_MSG_LABEL_STYLE)

    @staticmethod
    def check_acc_pwd(accText, pwdText):
        sqlAcc = MainSetting.sqlAcc
        sqlPwd = MainSetting.sqlPwd
        sqlHost = MainSetting.sqlHost
        sqlPort = int(MainSetting.sqlPort)
        try:
            db = Db(sqlAcc, sqlPwd, "user", sqlHost, sqlPort)
            ret = db.select_opn("select * from master where accountNum = '%s'" % accText, False)
            if ret is not None:
                if ret[0] == accText and ret[1] == pwdText:
                    return True
        except Exception as err:
            print(err)
            try:
                db = Db(sqlAcc, sqlPwd, "mysql", sqlHost, sqlPort)
                db.create_db("user")
                db.close()
                db = Db(sqlAcc, sqlPwd, "user", sqlHost, sqlPort)
                db.create_tb("create table if not exists cache(accountNum varchar(11) primary key not null)")
                db.create_tb("create table if not exists master("
                             "accountNum varchar(11) primary key not null,"
                             "password varchar(11) not null)")
            except Exception as err:
                print(str(err) + "\n ERROR: MySQL")
        return False

    def visibleChange(self):
        lock = threading.Lock()
        try:
            lock.acquire()
            if self.pwd_invisible:
                self.ui.btn_visible.setStyleSheet(Setting.LOGIN_BTN_VISIBLE_OUT_STYLE)
                self.ui.pwd_text.setEchoMode(QLineEdit.EchoMode.Normal)
                self.pwd_invisible = False
            else:
                self.ui.btn_visible.setStyleSheet(Setting.LOGIN_BTN_INVISIBLE_OUT_STYLE)
                self.ui.pwd_text.setEchoMode(QLineEdit.EchoMode.Password)
                self.pwd_invisible = True
        finally:
            lock.release()
