from PySide6.QtWidgets import QGraphicsDropShadowEffect
from modules.ui.ui_messageBox_style import *


class MessageBox(QDialog):
    def __init__(self, parent):
        super(MessageBox, self).__init__()
        self.parent = parent
        self.setParent(parent)
        self.dic = {"information":190}
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.initUi()

    def initUi(self):
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor((QColor(0, 0, 0, 150)))
        self.ui.frame.setGraphicsEffect(self.shadow)

    def information(self, title, text1, text2=None,
                    btn_text1=None, btn_text2=None, btn_text3=None,
                    btn_func1=None, btn_func2=None, btn_func3=None) -> None:
        self.ui.label.setText(title)
        self.ui.label_2.setText(text1)
        off = 0
        if text2:
            self.ui.label_3.setText(text2)
            off = 70
        else:
            self.ui.label_3.hide()
            self.ui.spacer.hide()

        if btn_text1:
            self.ui.pushButton.setText(btn_text1)
            self.ui.pushButton.clicked.connect(btn_func1)
        else:
            self.ui.pushButton.hide()

        if btn_text2:
            self.ui.pushButton_2.setText(btn_text2)
            self.ui.pushButton_2.clicked.connect(btn_func2)
        else:
            self.ui.pushButton_2.hide()

        if btn_text3:
            self.ui.pushButton_3.setText(btn_text3)
            self.ui.pushButton_3.clicked.connect(btn_func3)
        else:
            self.ui.pushButton_3.hide()

        self.setMaximumHeight(self.dic["information"] + off)
        self.followEvent(self.parent)
        # cannot operate MianWindow
        # self.setModal(True)
        self.show()

    def followEvent(self, leader):
        globalPos = leader.mapToGlobal(QPoint(0, 0))
        self.move(globalPos.x() + leader.width() / 2 - self.width() / 2,
                  globalPos.y() + leader.height() / 4 - self.height() / 2)
