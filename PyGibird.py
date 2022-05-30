import os
import sys
from typing import Union, Tuple
from PySide6.QtCore import QByteArray, QEvent, QObject, Qt
from PySide6.QtGui import QHoverEvent, QColor, QMouseEvent, QMoveEvent, QResizeEvent
from PySide6.QtWidgets import QApplication
from modules.ui.ui_base import MainWindow_base
from modules.ui.ui_opn import UIFunctions
from modules.graph import Meter, TableView

# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"


class MainWindow(MainWindow_base):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tableView1 = None
        self.tableView2 = None
        self.meter1 = None
        self.meter2 = None
        self.meter3 = None
        self.meter4 = None
        self.meter5 = None
        self.initGraph()
        UIFunctions.InitUi(self)
        self.show()

    def initGraph(self):
        self.tableView1 = TableView(self.ui.tableViewPage, "", "", "", 956, 325)
        self.tableView2 = TableView(self.ui.frame_6, "", "", "", 958, 685)
        self.meter1 = Meter(self.ui.bar1, QColor(229, 229, 229), 20, 340,
                            0.8, 0, 1, showPct=50, scale_LSize=5, label=self.ui.label_6)
        self.meter2 = Meter(self.ui.bar2, QColor(229, 229, 229), 20, 340,
                            0.8, 0, 1, showPct=50, scale_LSize=5, label=self.ui.label_7)
        self.meter3 = Meter(self.ui.bar3, QColor(229, 229, 229), 20, 340,
                            0.8, 0, 1, showPct=50, scale_LSize=5, label=self.ui.label_8)
        self.meter4 = Meter(self.ui.bar4, QColor(229, 229, 229), 20, 340,
                            0.8, 0, 1, showPct=50, scale_LSize=5, label=self.ui.label_9)
        self.meter5 = Meter(self.ui.bar5, QColor(229, 229, 229), 20, 340,
                            0.8, 0, 1, showPct=50, scale_LSize=5, label=self.ui.label_10)

    def btnClicked(self):
        UIFunctions.btnClicked(self)

    def btnToggle(self):
        UIFunctions.btnToggle(self)

    def nativeEvent(self, eventType: Union[QByteArray, bytes], message: int) -> Tuple[object, int]:
        return UIFunctions.myNativeEvent(self, eventType, message)

    def changeEvent(self, event: QEvent) -> None:
        if event.type() == QEvent.WindowStateChange:
            UIFunctions.windowStateChange(self)

    def moveEvent(self, event: QMoveEvent) -> None:
        try:
            if not self.messageBox.isHidden():
                self.messageBox.followEvent(self)
        except AttributeError:
            print("it can work well")

    def resizeEvent(self, event: QResizeEvent) -> None:
        if not self.messageBox.isHidden():
            self.messageBox.followEvent(self)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            # deselect table items
            self.ui.tableWidget.setCurrentItem(None)
            self.ui.tableWidget_2.setCurrentItem(None)
            self.ui.home_table.setCurrentItem(None)
            self.ui.tableWidget_4.setCurrentItem(None)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QHoverEvent.HoverEnter and watched == self.ui.btn_setting:
            self.btn_setting_hoverEvent(True)
            return True
        elif event.type() == QHoverEvent.HoverLeave and watched == self.ui.btn_setting:
            self.btn_setting_hoverEvent(False)
            return True
        return MainWindow_base.eventFilter(self, watched, event)

    def btn_setting_hoverEvent(self, enter: bool):
        UIFunctions.setting_HoverEvent(self, enter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow()
    sys.exit(app.exec())
