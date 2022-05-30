# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiHWlKuL.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
                               QFrame, QHBoxLayout, QHeaderView, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
                               QVBoxLayout, QWidget)
from modules.ui.ui_resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 810)
        MainWindow.setMinimumSize(QSize(1440, 810))
        MainWindow.setStyleSheet(u"QMenu{\n"
                                 "	font: 12pt \"Microsoft YaHei UI\";\n"
                                 "	color:rgb(255, 255, 255); \n"
                                 "	background-color: rgb(48, 50, 52);\n"
                                 " 	border:1px solid rgb(107, 107, 107);\n"
                                 "	width:150px\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item{\n"
                                 "	background-color:transparent;\n"
                                 "	height:25px;\n"
                                 "	padding: 3px 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator:checked{background-image: url(:/icons/resources/icons/checked_blue.png);}\n"
                                 "\n"
                                 "QMenu::item:selected{\n"
                                 "	background-color: rgb(75, 110, 175);\n"
                                 "}\n"
                                 "	\n"
                                 "QMenu::separator{\n"
                                 "	height:1px;\n"
                                 "	background-color: rgb(107, 107, 107);\n"
                                 "}")
        self.action22222 = QAction(MainWindow)
        self.action22222.setObjectName(u"action22222")
        self.action3333 = QAction(MainWindow)
        self.action3333.setObjectName(u"action3333")
        self.action44444 = QAction(MainWindow)
        self.action44444.setObjectName(u"action44444")
        self.action555 = QAction(MainWindow)
        self.action555.setObjectName(u"action555")
        self.action111 = QAction(MainWindow)
        self.action111.setObjectName(u"action111")
        self.action111.setCheckable(True)
        font = QFont()
        font.setPointSize(12)
        self.action111.setFont(font)
        self.action222 = QAction(MainWindow)
        self.action222.setObjectName(u"action222")
        self.action333 = QAction(MainWindow)
        self.action333.setObjectName(u"action333")
        self.action444 = QAction(MainWindow)
        self.action444.setObjectName(u"action444")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"/*555555555555555555555555555555555555555555555555555555*/\n"
                                      "#QWidget{\n"
                                      "	font: 14pt \"Microsoft YaHei UI\";\n"
                                      "	color: rgb(186, 186, 166);\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#appBox{\n"
                                      "	color:rgb(186, 186, 166);\n"
                                      "	background-color: rgb(60, 63, 65);\n"
                                      "	border:1px solid rgb(60, 63, 65);\n"
                                      "}\n"
                                      "\n"
                                      "/*page_home*/\n"
                                      "#home_table{\n"
                                      "	gridline: 1px solid rgb(72, 75, 78);\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#home_table::item{\n"
                                      "	color:rgb(186, 186, 166);\n"
                                      "	border:1px solid rgb(72, 75, 78);\n"
                                      "}\n"
                                      "\n"
                                      "#home_table::item:selected{\n"
                                      "	background-color: rgb(33, 66, 131);\n"
                                      "}\n"
                                      "\n"
                                      "QHeaderView::section{\n"
                                      "	background-color: rgb(60, 63, 65);\n"
                                      "	border:1px solid rgb(72, 75, 78);\n"
                                      "}\n"
                                      "/*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&*/\n"
                                      "#home_graphics{\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "/*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^*/\n"
                                      "#about_box{\n"
                                      "	border:none;\n"
                                      "	background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "#settingBox{\n"
                                      "	border:none;\n"
                                      "	border-right:1px solid rgb(109, 109, 109);\n"
                                      "	"
                                      "background-color: rgb(44, 49, 58);\n"
                                      "}\n"
                                      "\n"
                                      "#settingBar{\n"
                                      "	border:none;\n"
                                      "	border-bottom:3px solid rgb(109, 109, 109);\n"
                                      "	background-color: rgb(102, 148, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#settingBar .QLabel{\n"
                                      "	border:none;\n"
                                      "	text-align:left center;\n"
                                      "	background-color: transparent;\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	font: 12pt \"Microsoft YaHei UI\";\n"
                                      "	border-left:22px solid transparent;\n"
                                      "}\n"
                                      "\n"
                                      "#setting_label_2{\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	background-position:center;\n"
                                      "	background-image: url(:/icons/resources/icons/setting.png);\n"
                                      "}\n"
                                      "\n"
                                      "#settingBar .QPushButton{\n"
                                      "	border:none;\n"
                                      "	background-image: url(:/icons/resources/icons/close.png);\n"
                                      "	background-position:center;\n"
                                      "	background-color: transparent;\n"
                                      "	background-repeat:no-repeat;\n"
                                      "}\n"
                                      "\n"
                                      "#settingBar .QPushButton:hover{\n"
                                      "	background-color: rgb(148, 200, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#settingBar .QPushButton:pressed{\n"
                                      "	background-color: rgb(67, 67, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#setting_header .QPushButton:hover{"
                                      "\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#setting_footer .QPushButton:hover{\n"
                                      "	background-color: rgb(60, 61, 93);\n"
                                      "}\n"
                                      "\n"
                                      "#setting_header .QPushButton:pressed{\n"
                                      "	background-color: rgb(77, 144, 254);\n"
                                      "}\n"
                                      "\n"
                                      "#setting_footer .QPushButton:pressed{\n"
                                      "	background-color: rgb(77, 144, 254);\n"
                                      "}\n"
                                      "\n"
                                      "#setting_header .QPushButton{\n"
                                      "	background-position: left center;\n"
                                      "	text-align:left center;\n"
                                      "	border:none;\n"
                                      "	padding-left:40px solid transparent;\n"
                                      "	border-left:22px solid transparent;\n"
                                      "	background-color: transparent;\n"
                                      "	color:rgb(255, 255, 255);\n"
                                      "	font: 12pt \"Microsoft YaHei UI\";\n"
                                      "	background-repeat:no-repeat;\n"
                                      "}\n"
                                      "\n"
                                      "#setting_footer .QPushButton{\n"
                                      "	background-position:center;\n"
                                      "	text-align:center;\n"
                                      "	border:1px solid rgb(60, 61, 93);\n"
                                      "	border-radius:10px;\n"
                                      "	background-color: rgb(81, 82, 124);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	font: 560 12pt \"Microsoft YaHei UI\";\n"
                                      "}\n"
                                      "\n"
                                      "#setting_header,"
                                      " #setting_body, #setting_footer{\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_message{\n"
                                      "	background-image: url(:/icons/resources/icons/message.png);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_file{\n"
                                      "	background-image: url(:/icons/resources/icons/filelist.png);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_more{\n"
                                      "	background-image: url(:/icons/resources/icons/more_2.png);\n"
                                      "}\n"
                                      "/*----------------------------------------------------*/\n"
                                      "#content{\n"
                                      "	background-color:rgb(60, 63, 65);\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#leftMenu{\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QToolTip {\n"
                                      "	color: #ffffff;\n"
                                      "	font: 12pt \"Microsoft YaHei UI\";\n"
                                      "	background-color: rgba(33, 37, 43, 180);\n"
                                      "	border: 1px solid rgb(44, 49, 58);\n"
                                      "	background-image: none;\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border-left: 2px solid rgb(255, 121, 198);\n"
                                      "	padding-left: 8px;\n"
                                      "	margin: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_close{\n"
                                      "	background-image: url(:/icons/resources/icons/close.png);\n"
                                      "}\n"
                                      "\n"
                                      ""
                                      "#btn_minimize{\n"
                                      "	background-image: url(:/icons/resources/icons/win-minimize.png);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_home{\n"
                                      "	background-image: url(:/icons/resources/icons/home.png);\n"
                                      "}\n"
                                      "\n"
                                      "#bottomLog .QLabel{\n"
                                      "	font: 9pt \"Microsoft YaHei UI\";\n"
                                      "	color:rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_exit{\n"
                                      "	margin-top:20px solid transparent;\n"
                                      "	background-image: url(:/icons/resources/icons/exit.png);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_help{\n"
                                      "	background-image: url(:/icons/resources/icons/help.png);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_conn{\n"
                                      "	background-image: url(:/icons/resources/icons/RemoteConn.png);\n"
                                      "}\n"
                                      "\n"
                                      "#line{\n"
                                      "	border:none;\n"
                                      "	background-color: rgb(105, 105, 105);\n"
                                      "}\n"
                                      ".QFrame{\n"
                                      "	border:none;\n"
                                      "	\n"
                                      "	background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_setting{\n"
                                      "	background-image: url(:/icons/resources/icons/setting.png);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_toggle{\n"
                                      "	background-image: url(:/icons/resources/icons/more_1.png);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_exp{\n"
                                      "	background-image:url(:/icons/resources/icons/export.png);\n"
                                      ""
                                      "}\n"
                                      "\n"
                                      "#toggleBox{\n"
                                      "	border-top:3px solid rgb(109, 109, 109);\n"
                                      "}\n"
                                      "\n"
                                      "#logoBox{\n"
                                      "	background-position:center;\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#logo{\n"
                                      "	background-position:center;\n"
                                      "	background-repeat:no repeat;\n"
                                      "	border-right:5px solid transparent;\n"
                                      "	background-image: url(:/icons/resources/logo/logo.ico);\n"
                                      "}\n"
                                      "\n"
                                      "#appName{\n"
                                      "	font: italic 16pt \"Monotype Corsiva\";\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#appExpr{\n"
                                      "	font: 350 10pt \"Microsoft YaHei UI\";\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	margin-left:10px solid transparent;\n"
                                      "	margin-top:10px solid transparent;\n"
                                      "}\n"
                                      "\n"
                                      "#author{\n"
                                      "	font: 290 7pt \"Microsoft YaHei UI\";\n"
                                      "	color: rgb(142, 147, 218);\n"
                                      "}\n"
                                      "\n"
                                      "#leftMenu .QPushButton{\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#topBox .QPushButton{\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "/*----------------------------------------------------------------*/\n"
                                      "#toggleBox .QPushButton:hover{\n"
                                      "	backgro"
                                      "und-color:rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_home:hover{\n"
                                      "	background-color:rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_conn:hover{\n"
                                      "	background-color:rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_exp:hover{\n"
                                      "	background-color:rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_help:hover{\n"
                                      "	background-color:rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_minimize:hover{\n"
                                      "	background-color:rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_maximize:hover{\n"
                                      "	background-color:rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "#closeBox .QPushButton:pressed {	\n"
                                      "	background-color: rgb(241, 112, 122);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#toggleBox .QPushButton:pressed {	\n"
                                      "	background-color: rgb(75, 110, 175);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#menuBar .QPushButton:pressed {	\n"
                                      "	background-color: rgb(75, 110, 175);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "#exitBox .QPushButton:pressed {	\n"
                                      "	background-color: rgb(241, 112, 122);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "/*********************************************************/\n"
                                      "#bt"
                                      "n_exit:hover{\n"
                                      "	background-color: rgb(232, 17, 35);\n"
                                      "	color:rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_close:hover{\n"
                                      "	background-color: rgb(232, 17, 35);\n"
                                      "	color:rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "#btn_toggle :hover{\n"
                                      "	color:rgb(255, 255, 255);\n"
                                      "	background-color:rgb(79, 82, 84);\n"
                                      "}\n"
                                      "\n"
                                      "/*---------------------------------------------------------------------------------*/\n"
                                      "#leftMenuBox .QPushButton{\n"
                                      "	font: 12pt \"Microsoft YaHei UI\";\n"
                                      "	color:rgb(255, 255, 255);\n"
                                      "	background-position:center;\n"
                                      "	text-align:bottom center;\n"
                                      "	border-bottom: 12px solid transparent;\n"
                                      "}\n"
                                      "\n"
                                      "/*#leftMenuBox .QPushButton{\n"
                                      "	font: 9pt \"Microsoft YaHei UI\";\n"
                                      "	color:rgb(255, 255, 255);\n"
                                      "	background-position: left center;\n"
                                      "	text-align:left center;\n"
                                      "	border-left:22px solid transparent;\n"
                                      "	padding-left:48px solid transparent;\n"
                                      "}*/\n"
                                      "/*++++++++++++++++++++++++++++++++++++++++++++*/\n"
                                      "#topRightMenu .QPushButton{\n"
                                      "	background-position:center;\n"
                                      "}\n"
                                      "\n"
                                      "#viewContain"
                                      "er{\n"
                                      "	background-color: rgb(43, 43, 43);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#topBox{\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	border:none;\n"
                                      "	border-bottom:3px solid rgb(109, 109, 109);\n"
                                      "}\n"
                                      "\n"
                                      "#bottomLog{\n"
                                      "	background-color: rgb(44, 49, 58);\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "/*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ScroolBar*/\n"
                                      "QScrollBar:horizontal{\n"
                                      "	background: none;\n"
                                      "	border:none;\n"
                                      "	margin:0 0 0 5px;\n"
                                      "	border-radius:0;\n"
                                      "	height:10px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal{\n"
                                      "	min-width:25px;\n"
                                      "	background-color: rgb(169, 169, 169);\n"
                                      "	border-radius:5px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:horizontal:hover{\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-line:horizontal{\n"
                                      "	border:none;\n"
                                      "	width:0;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line:horizontal{\n"
                                      "	border:none;\n"
                                      "	width:0;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:vertical{\n"
                                      "	border:none;\n"
                                      "	background: none;\n"
                                      "	width:10px;\n"
                                      "	margin:32px 0 0 0"
                                      ";\n"
                                      "	border-radius:0px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical{\n"
                                      "	background-color: rgb(169, 169, 169);\n"
                                      "	width:10px;\n"
                                      "	border-radius:5px;\n"
                                      "	min-height:25px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:hover{\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-line:vertical{\n"
                                      "	border:none;\n"
                                      "	background-color: rgb(60, 63, 65);\n"
                                      "	height:30px;\n"
                                      "	subcontrol-origin:margin;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line:vertical{\n"
                                      "	border:none;\n"
                                      "	height:0;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-page:vertical{\n"
                                      "	background-color: rgb(59, 59, 59);\n"
                                      "	border-bottom-right-radius:5px;\n"
                                      "	border-bottom-left-radius:5px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-page:vertical{\n"
                                      "	background-color: rgb(59, 59, 59);\n"
                                      "	border-top-right-radius:5px;\n"
                                      "	border-top-left-radius:5px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-page:vertical{\n"
                                      "	background-color: rgb(59, 59, 59);\n"
                                      "	border-bottom-right-radius:5px;\n"
                                      "	border-bottom-left-radius:5px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-page:horizontal{\n"
                                      "	backg"
                                      "round-color: rgb(59, 59, 59);\n"
                                      "	border-top-right-radius:5px;\n"
                                      "	border-bottom-right-radius:5px;\n"
                                      "}\n"
                                      "QScrollBar::sub-page:horizontal{\n"
                                      "	background-color: rgb(59, 59, 59);\n"
                                      "	border-top-left-radius:5px;\n"
                                      "	border-bottom-left-radius:5px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::up-arrow:vertical,QScrollBar::down-arrow:vertical{\n"
                                      "	background:none;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal,QScrollBar::down-arrow:horizontal{\n"
                                      "	background:none;\n"
                                      "}\n"
                                      "\n"
                                      "#home_table{\n"
                                      "	border-right:1px solid rgb(65, 67, 69);\n"
                                      "	font: 12pt \"Microsoft YaHei UI\";\n"
                                      "	\n"
                                      "}\n"
                                      "/********************************************************************************/\n"
                                      "#topDragArea .QPushButton{\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_home_graph_fullScreen{\n"
                                      "	background-image: url(:/icons/resources/icons/fullscreen.png);\n"
                                      "	background-position:center;\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	margin-right:2px solid transparent;\n"
                                      "	border-radius:3px;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_home_graph_player{\n"
                                      "	background-image: url(:/i"
                                      "cons/resources/icons/play.png);\n"
                                      "	background-position:center;\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	margin-right:2px solid transparent;\n"
                                      "	border-radius:3px;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_home_graph_track{\n"
                                      "	background-image: url(:/icons/resources/icons/track_gray.png);\n"
                                      "	background-position:center;\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	margin-right:2px solid transparent;\n"
                                      "	border-radius:3px;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_home_graph_coor{\n"
                                      "	background-image: url(:/icons/resources/icons/coor_gray.png);\n"
                                      "	background-position:center;\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	margin-right:2px solid transparent;\n"
                                      "	border-radius:3px;\n"
                                      "}\n"
                                      "/*0000000000000000000000000000000000000000000000000000000*/\n"
                                      "#home_rightBox QPushButton{\n"
                                      "	border:none;\n"
                                      "	font: 12pt \"Microsoft YaHei UI\";\n"
                                      "	color: rgb(186, 186, 166);\n"
                                      "}\n"
                                      "\n"
                                      "#home_rightBox QTextEdit{\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "/*===================================================*/\n"
                                      "#home_table_rightBox QPushButton{\n"
                                      "	border:none;\n"
                                      "}\n"
                                      "\n"
                                      ""
                                      "#home_table_rightBox QCheckBox{\n"
                                      "	padding-left:20px;\n"
                                      "}\n"
                                      "\n"
                                      "#home_table_rightBox QCheckBox::indicator{\n"
                                      "	border:1px solid rgb(60, 63, 65);\n"
                                      "}\n"
                                      "#home_table_rightBox QCheckBox::indicator:hover{\n"
                                      "	border:1px solid rgb(169, 169, 169);\n"
                                      "}\n"
                                      "\n"
                                      "#home_table_rightBox QCheckBox::indicator:checked{\n"
                                      "	background-position:center;\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	background-image: url(:/icons/resources/icons/checked_blue.png);\n"
                                      "}")
        self.appBoxMargins = QVBoxLayout(self.styleSheet)
        self.appBoxMargins.setSpacing(0)
        self.appBoxMargins.setObjectName(u"appBoxMargins")
        self.appBoxMargins.setContentsMargins(0, 0, 0, 0)
        self.appBox = QFrame(self.styleSheet)
        self.appBox.setObjectName(u"appBox")
        self.appBox.setMinimumSize(QSize(940, 560))
        self.appBox.setStyleSheet(u"")
        self.appBox.setFrameShape(QFrame.NoFrame)
        self.appBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.appBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.appBox)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(0, 0))
        self.leftMenu.setMaximumSize(QSize(80, 16777215))
        self.leftMenu.setStyleSheet(u"")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logoBox = QFrame(self.leftMenu)
        self.logoBox.setObjectName(u"logoBox")
        self.logoBox.setMaximumSize(QSize(16777215, 45))
        self.logoBox.setStyleSheet(u"")
        self.logoBox.setFrameShape(QFrame.StyledPanel)
        self.logoBox.setFrameShadow(QFrame.Raised)
        self.logo = QFrame(self.logoBox)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 60, 45))
        self.logo.setMinimumSize(QSize(45, 45))
        self.logo.setMaximumSize(QSize(60, 45))
        self.logo.setLayoutDirection(Qt.LeftToRight)
        self.logo.setAutoFillBackground(False)
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.appName = QLabel(self.logoBox)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(60, 10, 101, 31))
        self.appName.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.logoBox)

        self.leftMenuBox = QFrame(self.leftMenu)
        self.leftMenuBox.setObjectName(u"leftMenuBox")
        self.leftMenuBox.setMinimumSize(QSize(80, 0))
        self.leftMenuBox.setStyleSheet(u"")
        self.leftMenuBox.setFrameShape(QFrame.StyledPanel)
        self.leftMenuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.leftMenuBox)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuBox)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMinimumSize(QSize(0, 0))
        self.toggleBox.setMaximumSize(QSize(16777215, 83))
        self.toggleBox.setStyleSheet(u"")
        self.toggleBox.setFrameShape(QFrame.StyledPanel)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.toggleBox)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(0, 83))
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_toggle)

        self.verticalLayout_8.addWidget(self.toggleBox)

        self.menuBar = QFrame(self.leftMenuBox)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setStyleSheet(u"")
        self.menuBar.setFrameShape(QFrame.StyledPanel)
        self.menuBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menuBar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.homeBox = QFrame(self.menuBar)
        self.homeBox.setObjectName(u"homeBox")
        self.homeBox.setMaximumSize(QSize(16777215, 80))
        self.homeBox.setFrameShape(QFrame.StyledPanel)
        self.homeBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.homeBox)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.homeBox)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 80))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.btn_home)

        self.verticalLayout_4.addWidget(self.homeBox)

        self.connBox = QFrame(self.menuBar)
        self.connBox.setObjectName(u"connBox")
        self.connBox.setMinimumSize(QSize(0, 80))
        self.connBox.setMaximumSize(QSize(16777215, 80))
        self.connBox.setFrameShape(QFrame.StyledPanel)
        self.connBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.connBox)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_conn = QPushButton(self.connBox)
        self.btn_conn.setObjectName(u"btn_conn")
        self.btn_conn.setMinimumSize(QSize(0, 80))
        self.btn_conn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_conn)

        self.verticalLayout_4.addWidget(self.connBox)

        self.expBox = QFrame(self.menuBar)
        self.expBox.setObjectName(u"expBox")
        self.expBox.setMinimumSize(QSize(0, 0))
        self.expBox.setMaximumSize(QSize(16777215, 80))
        self.expBox.setFrameShape(QFrame.StyledPanel)
        self.expBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.expBox)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_exp = QPushButton(self.expBox)
        self.btn_exp.setObjectName(u"btn_exp")
        self.btn_exp.setMinimumSize(QSize(0, 80))
        self.btn_exp.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_exp)

        self.verticalLayout_4.addWidget(self.expBox)

        self.helpBox = QFrame(self.menuBar)
        self.helpBox.setObjectName(u"helpBox")
        self.helpBox.setMaximumSize(QSize(16777215, 80))
        self.helpBox.setFrameShape(QFrame.StyledPanel)
        self.helpBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.helpBox)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_help = QPushButton(self.helpBox)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(0, 80))
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_help)

        self.verticalLayout_4.addWidget(self.helpBox)

        self.line = QFrame(self.menuBar)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.exitBox = QFrame(self.menuBar)
        self.exitBox.setObjectName(u"exitBox")
        self.exitBox.setMaximumSize(QSize(16777215, 100))
        self.exitBox.setFrameShape(QFrame.StyledPanel)
        self.exitBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.exitBox)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_exit = QPushButton(self.exitBox)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 100))
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_exit)

        self.verticalLayout_4.addWidget(self.exitBox)

        self.verticalLayout_8.addWidget(self.menuBar, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuBox)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(0, 0))
        self.bottomMenu.setMaximumSize(QSize(16777215, 80))
        self.bottomMenu.setStyleSheet(u"")
        self.bottomMenu.setFrameShape(QFrame.StyledPanel)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_setting = QPushButton(self.bottomMenu)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QSize(0, 80))
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setting.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_setting)

        self.verticalLayout_8.addWidget(self.bottomMenu)

        self.verticalLayout.addWidget(self.leftMenuBox)

        self.horizontalLayout.addWidget(self.leftMenu)

        self.settingBox = QFrame(self.appBox)
        self.settingBox.setObjectName(u"settingBox")
        self.settingBox.setMinimumSize(QSize(0, 0))
        self.settingBox.setMaximumSize(QSize(0, 16777215))
        self.settingBox.setFrameShape(QFrame.StyledPanel)
        self.settingBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.settingBox)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.settingBar = QFrame(self.settingBox)
        self.settingBar.setObjectName(u"settingBar")
        self.settingBar.setMinimumSize(QSize(400, 48))
        self.settingBar.setFrameShape(QFrame.StyledPanel)
        self.settingBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.settingBar)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.setting_label_2 = QLabel(self.settingBar)
        self.setting_label_2.setObjectName(u"setting_label_2")
        self.setting_label_2.setMinimumSize(QSize(45, 45))
        self.setting_label_2.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_14.addWidget(self.setting_label_2)

        self.settingBar_label = QLabel(self.settingBar)
        self.settingBar_label.setObjectName(u"settingBar_label")
        self.settingBar_label.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_14.addWidget(self.settingBar_label)

        self.btn_setting_return = QPushButton(self.settingBar)
        self.btn_setting_return.setObjectName(u"btn_setting_return")
        self.btn_setting_return.setMinimumSize(QSize(50, 45))
        self.btn_setting_return.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_14.addWidget(self.btn_setting_return)

        self.verticalLayout_22.addWidget(self.settingBar)

        self.setting_header = QFrame(self.settingBox)
        self.setting_header.setObjectName(u"setting_header")
        self.setting_header.setMaximumSize(QSize(16777215, 135))
        self.setting_header.setFrameShape(QFrame.StyledPanel)
        self.setting_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.setting_header)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.setting_header)
        self.btn_message.setObjectName(u"btn_message")
        self.btn_message.setMinimumSize(QSize(0, 45))

        self.verticalLayout_5.addWidget(self.btn_message)

        self.btn_file = QPushButton(self.setting_header)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setMinimumSize(QSize(0, 45))

        self.verticalLayout_5.addWidget(self.btn_file)

        self.btn_more = QPushButton(self.setting_header)
        self.btn_more.setObjectName(u"btn_more")
        self.btn_more.setMinimumSize(QSize(0, 45))

        self.verticalLayout_5.addWidget(self.btn_more)

        self.verticalLayout_22.addWidget(self.setting_header)

        self.setting_body = QFrame(self.settingBox)
        self.setting_body.setObjectName(u"setting_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.setting_body.sizePolicy().hasHeightForWidth())
        self.setting_body.setSizePolicy(sizePolicy1)
        self.setting_body.setFrameShape(QFrame.StyledPanel)
        self.setting_body.setFrameShadow(QFrame.Raised)
        self.about_box = QTextEdit(self.setting_body)
        self.about_box.setObjectName(u"about_box")
        self.about_box.setGeometry(QRect(10, 0, 380, 580))
        self.about_box.setMinimumSize(QSize(380, 580))
        self.about_box.setMaximumSize(QSize(339, 16777215))
        self.about_box.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.setting_body)

        self.setting_footer = QFrame(self.settingBox)
        self.setting_footer.setObjectName(u"setting_footer")
        self.setting_footer.setMaximumSize(QSize(16777215, 45))
        self.setting_footer.setFrameShape(QFrame.StyledPanel)
        self.setting_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.setting_footer)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_logout = QPushButton(self.setting_footer)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setMaximumSize(QSize(330, 16777215))

        self.horizontalLayout_13.addWidget(self.btn_logout)

        self.verticalLayout_22.addWidget(self.setting_footer)

        self.horizontalLayout.addWidget(self.settingBox)

        self.content = QFrame(self.appBox)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBox = QFrame(self.content)
        self.topBox.setObjectName(u"topBox")
        self.topBox.setMaximumSize(QSize(16777215, 48))
        self.topBox.setStyleSheet(u"")
        self.topBox.setFrameShape(QFrame.StyledPanel)
        self.topBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.topBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.topBox)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(400, 45))
        self.topBar.setStyleSheet(u"")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.topBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.topBar)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 45))
        self.topMenu.setFrameShape(QFrame.StyledPanel)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.topMenu)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.appExpr = QLabel(self.topMenu)
        self.appExpr.setObjectName(u"appExpr")
        self.appExpr.setMinimumSize(QSize(0, 0))
        self.appExpr.setMaximumSize(QSize(16777215, 45))
        self.appExpr.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.appExpr)

        self.horizontalLayout_5.addWidget(self.topMenu)

        self.horizontalLayout_3.addWidget(self.topBar)

        self.topRightMenu = QFrame(self.topBox)
        self.topRightMenu.setObjectName(u"topRightMenu")
        self.topRightMenu.setMinimumSize(QSize(0, 45))
        self.topRightMenu.setMaximumSize(QSize(180, 16777215))
        self.topRightMenu.setFrameShape(QFrame.StyledPanel)
        self.topRightMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.topRightMenu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.topRightMenu)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(60, 45))
        self.btn_minimize.setMaximumSize(QSize(60, 45))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.topRightMenu)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(60, 45))
        self.btn_maximize.setMaximumSize(QSize(60, 45))
        self.btn_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximize.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btn_maximize)

        self.closeBox = QFrame(self.topRightMenu)
        self.closeBox.setObjectName(u"closeBox")
        self.closeBox.setMaximumSize(QSize(60, 45))
        self.closeBox.setFrameShape(QFrame.StyledPanel)
        self.closeBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.closeBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.closeBox)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(60, 45))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(self.closeBox)

        self.horizontalLayout_3.addWidget(self.topRightMenu)

        self.verticalLayout_2.addWidget(self.topBox)

        self.viewContainer = QFrame(self.content)
        self.viewContainer.setObjectName(u"viewContainer")
        self.viewContainer.setStyleSheet(u"")
        self.viewContainer.setFrameShape(QFrame.StyledPanel)
        self.viewContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.viewContainer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.book = QStackedWidget(self.viewContainer)
        self.book.setObjectName(u"book")
        self.book.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
                                     "color: rgb(255, 255, 255);")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.page_home)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setStyleSheet(u"")
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.home_view = QStackedWidget(self.frame_home)
        self.home_view.setObjectName(u"home_view")
        self.home_view.setStyleSheet(u"")
        self.home_normal_page = QWidget()
        self.home_normal_page.setObjectName(u"home_normal_page")
        self.verticalLayout_16 = QVBoxLayout(self.home_normal_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.home_tableBox = QFrame(self.home_normal_page)
        self.home_tableBox.setObjectName(u"home_tableBox")
        self.home_tableBox.setMaximumSize(QSize(16777215, 0))
        self.home_tableBox.setStyleSheet(u"")
        self.horizontalLayout_21 = QHBoxLayout(self.home_tableBox)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.home_table = QTableWidget(self.home_tableBox)
        if (self.home_table.columnCount() < 30):
            self.home_table.setColumnCount(30)
        if (self.home_table.rowCount() < 30):
            self.home_table.setRowCount(30)
        self.home_table.setObjectName(u"home_table")
        self.home_table.setFocusPolicy(Qt.NoFocus)
        self.home_table.setStyleSheet(u"QHeaderView::section{\n"
                                      "	font: 12pt \"Microsoft YaHei UI\";\n"
                                      "}\n"
                                      "\n"
                                      "QTableView::item:selected{\n"
                                      "	background-color: rgb(0, 120, 215);\n"
                                      "}")
        self.home_table.setLineWidth(1)
        self.home_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.home_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.home_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.home_table.setAlternatingRowColors(False)
        self.home_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.home_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.home_table.setGridStyle(Qt.SolidLine)
        self.home_table.setSortingEnabled(False)
        self.home_table.setRowCount(30)
        self.home_table.setColumnCount(30)
        self.home_table.horizontalHeader().setHighlightSections(True)
        self.home_table.verticalHeader().setVisible(False)
        self.home_table.verticalHeader().setHighlightSections(True)
        self.home_table.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_21.addWidget(self.home_table)

        self.home_table_rightBox = QFrame(self.home_tableBox)
        self.home_table_rightBox.setObjectName(u"home_table_rightBox")
        self.home_table_rightBox.setMinimumSize(QSize(0, 0))
        self.home_table_rightBox.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        self.home_table_rightBox.setFrameShape(QFrame.StyledPanel)
        self.home_table_rightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.home_table_rightBox)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_table_exit = QPushButton(self.home_table_rightBox)
        self.btn_table_exit.setObjectName(u"btn_table_exit")
        self.btn_table_exit.setMinimumSize(QSize(120, 40))
        self.btn_table_exit.setMaximumSize(QSize(16777215, 40))
        self.btn_table_exit.setStyleSheet(u"QPushButton{\n"
                                          "	background-color: rgb(60, 63, 65);\n"
                                          "	background-repeat:no-repeat;\n"
                                          "	background-position:right;\n"
                                          "	background-image: url(:/icons/resources/icons/right_arrow.png);\n"
                                          "	border-right:25px solid transparent;\n"
                                          "}\n"
                                          ":hover{\n"
                                          "	background-color: rgb(50, 50, 50);\n"
                                          "}\n"
                                          "\n"
                                          ":pressed{\n"
                                          "	background-color: rgb(75, 110, 175);\n"
                                          "}")
        self.btn_table_exit.setCheckable(True)

        self.verticalLayout_17.addWidget(self.btn_table_exit)

        self.check_furnace = QCheckBox(self.home_table_rightBox)
        self.check_furnace.setObjectName(u"check_furnace")
        self.check_furnace.setMinimumSize(QSize(0, 40))
        self.check_furnace.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.check_furnace)

        self.check_superheater = QCheckBox(self.home_table_rightBox)
        self.check_superheater.setObjectName(u"check_superheater")
        self.check_superheater.setMinimumSize(QSize(0, 40))

        self.verticalLayout_17.addWidget(self.check_superheater)

        self.check_reheater = QCheckBox(self.home_table_rightBox)
        self.check_reheater.setObjectName(u"check_reheater")
        self.check_reheater.setMinimumSize(QSize(0, 40))

        self.verticalLayout_17.addWidget(self.check_reheater)

        self.check_economizer = QCheckBox(self.home_table_rightBox)
        self.check_economizer.setObjectName(u"check_economizer")
        self.check_economizer.setMinimumSize(QSize(0, 40))

        self.verticalLayout_17.addWidget(self.check_economizer)

        self.check_airPreheater = QCheckBox(self.home_table_rightBox)
        self.check_airPreheater.setObjectName(u"check_airPreheater")
        self.check_airPreheater.setMinimumSize(QSize(0, 40))

        self.verticalLayout_17.addWidget(self.check_airPreheater)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer)

        self.btn_table_refresh = QPushButton(self.home_table_rightBox)
        self.btn_table_refresh.setObjectName(u"btn_table_refresh")
        self.btn_table_refresh.setMinimumSize(QSize(0, 30))
        self.btn_table_refresh.setStyleSheet(u":hover{\n"
                                             "	background-color: rgb(50, 50, 50);\n"
                                             "}\n"
                                             "\n"
                                             ":pressed{\n"
                                             "	background-color: rgb(75, 110, 175);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton{\n"
                                             "	border:1px solid rgb(109, 109, 109);\n"
                                             "	border-radius:5px;\n"
                                             "}")

        self.verticalLayout_17.addWidget(self.btn_table_refresh)

        self.btn_table_fullScreen = QPushButton(self.home_table_rightBox)
        self.btn_table_fullScreen.setObjectName(u"btn_table_fullScreen")
        self.btn_table_fullScreen.setMinimumSize(QSize(0, 30))
        self.btn_table_fullScreen.setStyleSheet(u":hover{\n"
                                                "	background-color: rgb(50, 50, 50);\n"
                                                "}\n"
                                                "\n"
                                                ":pressed{\n"
                                                "	background-color: rgb(75, 110, 175);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton{\n"
                                                "	border:1px solid rgb(109, 109, 109);\n"
                                                "	border-radius:5px;\n"
                                                "}")

        self.verticalLayout_17.addWidget(self.btn_table_fullScreen)

        self.btn_table_filter = QPushButton(self.home_table_rightBox)
        self.btn_table_filter.setObjectName(u"btn_table_filter")
        self.btn_table_filter.setMinimumSize(QSize(0, 30))
        self.btn_table_filter.setAutoFillBackground(False)
        self.btn_table_filter.setStyleSheet(u":hover{\n"
                                            "	background-color: rgb(50, 50, 50);\n"
                                            "}\n"
                                            "\n"
                                            ":pressed{\n"
                                            "	background-color: rgb(75, 110, 175);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton{\n"
                                            "	border:1px solid rgb(109, 109, 109);\n"
                                            "	border-radius:5px;\n"
                                            "}")

        self.verticalLayout_17.addWidget(self.btn_table_filter)

        self.horizontalLayout_21.addWidget(self.home_table_rightBox)

        self.verticalLayout_12.addWidget(self.home_tableBox)

        self.home_midBox = QFrame(self.home_normal_page)
        self.home_midBox.setObjectName(u"home_midBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.home_midBox.sizePolicy().hasHeightForWidth())
        self.home_midBox.setSizePolicy(sizePolicy3)
        self.home_midBox.setStyleSheet(u"QLabel{\n"
                                       "	font: 16pt \"Microsoft YaHei UI\";\n"
                                       "	border-bottom:2px solid rgb(102, 104, 104);\n"
                                       "}")
        self.home_midBox.setFrameShape(QFrame.StyledPanel)
        self.home_midBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.home_midBox)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.bar1 = QFrame(self.home_midBox)
        self.bar1.setObjectName(u"bar1")
        self.bar1.setFrameShape(QFrame.StyledPanel)
        self.bar1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.bar1)

        self.bar2 = QFrame(self.home_midBox)
        self.bar2.setObjectName(u"bar2")
        self.bar2.setFrameShape(QFrame.StyledPanel)
        self.bar2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.bar2)

        self.bar3 = QFrame(self.home_midBox)
        self.bar3.setObjectName(u"bar3")
        self.bar3.setFrameShape(QFrame.StyledPanel)
        self.bar3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.bar3)

        self.bar4 = QFrame(self.home_midBox)
        self.bar4.setObjectName(u"bar4")
        self.bar4.setFrameShape(QFrame.StyledPanel)
        self.bar4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.bar4)

        self.bar5 = QFrame(self.home_midBox)
        self.bar5.setObjectName(u"bar5")
        self.bar5.setFrameShape(QFrame.StyledPanel)
        self.bar5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.bar5)

        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)

        self.textBar = QFrame(self.home_midBox)
        self.textBar.setObjectName(u"textBar")
        self.textBar.setFrameShape(QFrame.StyledPanel)
        self.textBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.textBar)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.textBox1 = QFrame(self.textBar)
        self.textBox1.setObjectName(u"textBox1")
        self.textBox1.setStyleSheet(u"#textBox1{\n"
                                    "	border-left:2px solid rgb(102, 104, 104);\n"
                                    "}")
        self.verticalLayout_20 = QVBoxLayout(self.textBox1)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.textBox1)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.label_2 = QLabel(self.textBox1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_2)

        self.label_3 = QLabel(self.textBox1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_3)

        self.label_4 = QLabel(self.textBox1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_4)

        self.label_5 = QLabel(self.textBox1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_5)

        self.horizontalLayout_25.addWidget(self.textBox1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_6 = QLabel(self.textBar)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_21.addWidget(self.label_6)

        self.label_7 = QLabel(self.textBar)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_21.addWidget(self.label_7)

        self.label_8 = QLabel(self.textBar)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_21.addWidget(self.label_8)

        self.label_9 = QLabel(self.textBar)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_21.addWidget(self.label_9)

        self.label_10 = QLabel(self.textBar)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.label_10)

        self.horizontalLayout_25.addLayout(self.verticalLayout_21)

        self.horizontalLayout_24.addWidget(self.textBar)

        self.verticalLayout_12.addWidget(self.home_midBox)

        self.verticalLayout_16.addLayout(self.verticalLayout_12)

        self.home_graphBox = QFrame(self.home_normal_page)
        self.home_graphBox.setObjectName(u"home_graphBox")
        self.verticalLayout_11 = QVBoxLayout(self.home_graphBox)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.topDragArea = QFrame(self.home_graphBox)
        self.topDragArea.setObjectName(u"topDragArea")
        self.topDragArea.setMinimumSize(QSize(0, 40))
        self.topDragArea.setMaximumSize(QSize(16777215, 40))
        self.topDragArea.setStyleSheet(u"#topDragArea{\n"
                                       "	background-color: rgb(49, 51, 53);\n"
                                       "}\n"
                                       "\n"
                                       "QFrame{\n"
                                       "	border:none;\n"
                                       "	background-color: transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "	border:none;\n"
                                       "	background-color: transparent;\n"
                                       "}\n"
                                       "")
        self.topDragArea.setFrameShape(QFrame.StyledPanel)
        self.topDragArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.topDragArea)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.topInfoArea = QFrame(self.topDragArea)
        self.topInfoArea.setObjectName(u"topInfoArea")
        self.topInfoArea.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")
        self.horizontalLayout_22 = QHBoxLayout(self.topInfoArea)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.graphBox_1 = QFrame(self.topInfoArea)
        self.graphBox_1.setObjectName(u"graphBox_1")
        self.graphBox_1.setStyleSheet(u"margin-right:10px")
        self.graphBox_1.setFrameShape(QFrame.StyledPanel)
        self.graphBox_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.graphBox_1)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.home_graph_1 = QPushButton(self.graphBox_1)
        self.home_graph_1.setObjectName(u"home_graph_1")
        sizePolicy2.setHeightForWidth(self.home_graph_1.sizePolicy().hasHeightForWidth())
        self.home_graph_1.setSizePolicy(sizePolicy2)
        self.home_graph_1.setStyleSheet(u"margin-left:10px;\n"
                                        "margin-right:10px;")

        self.horizontalLayout_32.addWidget(self.home_graph_1)

        self.home_graph_exit_1 = QPushButton(self.graphBox_1)
        self.home_graph_exit_1.setObjectName(u"home_graph_exit_1")
        self.home_graph_exit_1.setMinimumSize(QSize(20, 20))
        self.home_graph_exit_1.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_32.addWidget(self.home_graph_exit_1)

        self.horizontalLayout_22.addWidget(self.graphBox_1)

        self.graphBox_2 = QFrame(self.topInfoArea)
        self.graphBox_2.setObjectName(u"graphBox_2")
        self.graphBox_2.setFrameShape(QFrame.StyledPanel)
        self.graphBox_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.graphBox_2)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.home_graph_2 = QPushButton(self.graphBox_2)
        self.home_graph_2.setObjectName(u"home_graph_2")
        sizePolicy2.setHeightForWidth(self.home_graph_2.sizePolicy().hasHeightForWidth())
        self.home_graph_2.setSizePolicy(sizePolicy2)
        self.home_graph_2.setStyleSheet(u"margin-left:10px;\n"
                                        "margin-right:10px;")

        self.horizontalLayout_33.addWidget(self.home_graph_2)

        self.home_graph_exit_2 = QPushButton(self.graphBox_2)
        self.home_graph_exit_2.setObjectName(u"home_graph_exit_2")
        self.home_graph_exit_2.setMinimumSize(QSize(20, 20))
        self.home_graph_exit_2.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_33.addWidget(self.home_graph_exit_2)

        self.horizontalLayout_22.addWidget(self.graphBox_2)

        self.graphBox_3 = QFrame(self.topInfoArea)
        self.graphBox_3.setObjectName(u"graphBox_3")
        self.graphBox_3.setFrameShape(QFrame.StyledPanel)
        self.graphBox_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.graphBox_3)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.home_graph_3 = QPushButton(self.graphBox_3)
        self.home_graph_3.setObjectName(u"home_graph_3")
        sizePolicy2.setHeightForWidth(self.home_graph_3.sizePolicy().hasHeightForWidth())
        self.home_graph_3.setSizePolicy(sizePolicy2)
        self.home_graph_3.setStyleSheet(u"margin-left:10px;\n"
                                        "margin-right:10px;")

        self.horizontalLayout_34.addWidget(self.home_graph_3)

        self.home_graph_exit_3 = QPushButton(self.graphBox_3)
        self.home_graph_exit_3.setObjectName(u"home_graph_exit_3")
        self.home_graph_exit_3.setMinimumSize(QSize(20, 20))
        self.home_graph_exit_3.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_34.addWidget(self.home_graph_exit_3)

        self.horizontalLayout_22.addWidget(self.graphBox_3)

        self.graphBox_4 = QFrame(self.topInfoArea)
        self.graphBox_4.setObjectName(u"graphBox_4")
        self.graphBox_4.setFrameShape(QFrame.StyledPanel)
        self.graphBox_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.graphBox_4)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.home_graph_4 = QPushButton(self.graphBox_4)
        self.home_graph_4.setObjectName(u"home_graph_4")
        sizePolicy2.setHeightForWidth(self.home_graph_4.sizePolicy().hasHeightForWidth())
        self.home_graph_4.setSizePolicy(sizePolicy2)
        self.home_graph_4.setStyleSheet(u"margin-left:10px;\n"
                                        "margin-right:10px;")

        self.horizontalLayout_35.addWidget(self.home_graph_4)

        self.home_graph_exit_4 = QPushButton(self.graphBox_4)
        self.home_graph_exit_4.setObjectName(u"home_graph_exit_4")
        self.home_graph_exit_4.setMinimumSize(QSize(20, 20))
        self.home_graph_exit_4.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_35.addWidget(self.home_graph_exit_4)

        self.horizontalLayout_22.addWidget(self.graphBox_4)

        self.graphBox_5 = QFrame(self.topInfoArea)
        self.graphBox_5.setObjectName(u"graphBox_5")
        self.graphBox_5.setFrameShape(QFrame.StyledPanel)
        self.graphBox_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.graphBox_5)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.home_graph_5 = QPushButton(self.graphBox_5)
        self.home_graph_5.setObjectName(u"home_graph_5")
        sizePolicy2.setHeightForWidth(self.home_graph_5.sizePolicy().hasHeightForWidth())
        self.home_graph_5.setSizePolicy(sizePolicy2)
        self.home_graph_5.setStyleSheet(u"margin-left:10px;\n"
                                        "margin-right:10px;")

        self.horizontalLayout_36.addWidget(self.home_graph_5)

        self.home_graph_exit_5 = QPushButton(self.graphBox_5)
        self.home_graph_exit_5.setObjectName(u"home_graph_exit_5")
        self.home_graph_exit_5.setMinimumSize(QSize(20, 20))
        self.home_graph_exit_5.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_36.addWidget(self.home_graph_exit_5)

        self.horizontalLayout_22.addWidget(self.graphBox_5)

        self.graphBox_6 = QFrame(self.topInfoArea)
        self.graphBox_6.setObjectName(u"graphBox_6")
        self.graphBox_6.setFrameShape(QFrame.StyledPanel)
        self.graphBox_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.graphBox_6)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.home_graph_6 = QPushButton(self.graphBox_6)
        self.home_graph_6.setObjectName(u"home_graph_6")
        sizePolicy2.setHeightForWidth(self.home_graph_6.sizePolicy().hasHeightForWidth())
        self.home_graph_6.setSizePolicy(sizePolicy2)
        self.home_graph_6.setStyleSheet(u"margin-left:10px;\n"
                                        "margin-right:10px;")

        self.horizontalLayout_37.addWidget(self.home_graph_6)

        self.home_graph_exit_6 = QPushButton(self.graphBox_6)
        self.home_graph_exit_6.setObjectName(u"home_graph_exit_6")
        self.home_graph_exit_6.setMinimumSize(QSize(20, 20))
        self.home_graph_exit_6.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_37.addWidget(self.home_graph_exit_6)

        self.horizontalLayout_22.addWidget(self.graphBox_6)

        self.emptySpacer = QPushButton(self.topInfoArea)
        self.emptySpacer.setObjectName(u"emptySpacer")
        sizePolicy1.setHeightForWidth(self.emptySpacer.sizePolicy().hasHeightForWidth())
        self.emptySpacer.setSizePolicy(sizePolicy1)

        self.horizontalLayout_22.addWidget(self.emptySpacer)

        self.horizontalLayout_38.addWidget(self.topInfoArea)

        self.home_table_topMenu = QFrame(self.topDragArea)
        self.home_table_topMenu.setObjectName(u"home_table_topMenu")
        self.horizontalLayout_16 = QHBoxLayout(self.home_table_topMenu)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_home_graph_track = QPushButton(self.home_table_topMenu)
        self.btn_home_graph_track.setObjectName(u"btn_home_graph_track")
        self.btn_home_graph_track.setMinimumSize(QSize(40, 30))
        self.btn_home_graph_track.setMaximumSize(QSize(40, 30))
        self.btn_home_graph_track.setToolTipDuration(0)
        self.btn_home_graph_track.setStyleSheet(u":hover{\n"
                                                "	background-color:rgb(76, 80, 82);\n"
                                                "}\n"
                                                ":pressed{\n"
                                                "	background-color:rgb(92, 97, 100);\n"
                                                "}")

        self.horizontalLayout_16.addWidget(self.btn_home_graph_track)

        self.btn_home_graph_coor = QPushButton(self.home_table_topMenu)
        self.btn_home_graph_coor.setObjectName(u"btn_home_graph_coor")
        self.btn_home_graph_coor.setMinimumSize(QSize(40, 30))
        self.btn_home_graph_coor.setMaximumSize(QSize(40, 30))
        self.btn_home_graph_coor.setStyleSheet(u":hover{\n"
                                               "	background-color:rgb(76, 80, 82);\n"
                                               "}\n"
                                               ":pressed{\n"
                                               "	background-color:rgb(92, 97, 100);\n"
                                               "}")

        self.horizontalLayout_16.addWidget(self.btn_home_graph_coor)

        self.btn_home_graph_player = QPushButton(self.home_table_topMenu)
        self.btn_home_graph_player.setObjectName(u"btn_home_graph_player")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_home_graph_player.sizePolicy().hasHeightForWidth())
        self.btn_home_graph_player.setSizePolicy(sizePolicy4)
        self.btn_home_graph_player.setMinimumSize(QSize(40, 30))
        self.btn_home_graph_player.setMaximumSize(QSize(40, 30))
        self.btn_home_graph_player.setStyleSheet(u":hover{\n"
                                                 "	background-color:rgb(76, 80, 82);\n"
                                                 "}\n"
                                                 ":pressed{\n"
                                                 "	background-color:rgb(92, 97, 100);\n"
                                                 "}")

        self.horizontalLayout_16.addWidget(self.btn_home_graph_player)

        self.btn_home_graph_fullScreen = QPushButton(self.home_table_topMenu)
        self.btn_home_graph_fullScreen.setObjectName(u"btn_home_graph_fullScreen")
        sizePolicy4.setHeightForWidth(self.btn_home_graph_fullScreen.sizePolicy().hasHeightForWidth())
        self.btn_home_graph_fullScreen.setSizePolicy(sizePolicy4)
        self.btn_home_graph_fullScreen.setMinimumSize(QSize(40, 30))
        self.btn_home_graph_fullScreen.setMaximumSize(QSize(40, 30))
        self.btn_home_graph_fullScreen.setStyleSheet(u":hover{\n"
                                                     "	background-color:rgb(76, 80, 82);\n"
                                                     "}\n"
                                                     ":pressed{\n"
                                                     "	background-color:rgb(92, 97, 100);\n"
                                                     "}\n"
                                                     "")

        self.horizontalLayout_16.addWidget(self.btn_home_graph_fullScreen)

        self.horizontalLayout_38.addWidget(self.home_table_topMenu)

        self.verticalLayout_11.addWidget(self.topDragArea)

        self.stackedWidget = QStackedWidget(self.home_graphBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.tableViewPage = QWidget()
        self.tableViewPage.setObjectName(u"tableViewPage")
        self.tableViewPage.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.tableViewPage)
        self.tableViewPage1 = QWidget()
        self.tableViewPage1.setObjectName(u"tableViewPage1")
        self.tableViewPage1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.tableViewPage1)
        self.tableViewPage2 = QWidget()
        self.tableViewPage2.setObjectName(u"tableViewPage2")
        self.tableViewPage2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.tableViewPage2)
        self.tableViewPage3 = QWidget()
        self.tableViewPage3.setObjectName(u"tableViewPage3")
        self.tableViewPage3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.tableViewPage3)
        self.tableViewPage4 = QWidget()
        self.tableViewPage4.setObjectName(u"tableViewPage4")
        self.tableViewPage4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.tableViewPage4)
        self.tableViewPage5 = QWidget()
        self.tableViewPage5.setObjectName(u"tableViewPage5")
        self.tableViewPage5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.tableViewPage5)
        self.tableViewPage6 = QWidget()
        self.tableViewPage6.setObjectName(u"tableViewPage6")
        self.tableViewPage6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.tableViewPage6)

        self.verticalLayout_11.addWidget(self.stackedWidget)

        self.verticalLayout_16.addWidget(self.home_graphBox)

        self.home_view.addWidget(self.home_normal_page)
        self.home_maximize_graph_page = QWidget()
        self.home_maximize_graph_page.setObjectName(u"home_maximize_graph_page")
        self.verticalLayout_23 = QVBoxLayout(self.home_maximize_graph_page)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.home_maximize_graph_page)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"QPushButton{\n"
                                   "	border:none;\n"
                                   "	background:none;\n"
                                   "}\n"
                                   "QFrame{\n"
                                   "	background-color: rgb(49, 51, 53);\n"
                                   "}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_26.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_26.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_26.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_26.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_26.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_26.addWidget(self.pushButton_10)

        self.horizontalLayout_27.addLayout(self.horizontalLayout_26)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 50))
        self.pushButton_4.setStyleSheet(u":hover{\n"
                                        "	background-color:rgb(76, 80, 82);\n"
                                        "}\n"
                                        ":pressed{\n"
                                        "	background-color:rgb(92, 97, 100);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "	background-repeat:no repeat;\n"
                                        "	background-position:center;\n"
                                        "	background-image: url(:/icons/resources/icons/track_gray.png);\n"
                                        "}")

        self.horizontalLayout_27.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setStyleSheet(u":hover{\n"
                                        "	background-color:rgb(76, 80, 82);\n"
                                        "}\n"
                                        ":pressed{\n"
                                        "	background-color:rgb(92, 97, 100);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "	background-repeat:no repeat;\n"
                                        "	background-position:center;\n"
                                        "	background-image: url(:/icons/resources/icons/coor_gray.png);\n"
                                        "}")

        self.horizontalLayout_27.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setStyleSheet(u":hover{\n"
                                        "	background-color:rgb(76, 80, 82);\n"
                                        "}\n"
                                        ":pressed{\n"
                                        "	background-color:rgb(92, 97, 100);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "	background-repeat:no repeat;\n"
                                        "	background-position:center;\n"
                                        "	background-image: url(:/icons/resources/icons/play.png);\n"
                                        "}")

        self.horizontalLayout_27.addWidget(self.pushButton_2)

        self.btn_exit_fullScreen_1 = QPushButton(self.frame_5)
        self.btn_exit_fullScreen_1.setObjectName(u"btn_exit_fullScreen_1")
        self.btn_exit_fullScreen_1.setMinimumSize(QSize(50, 50))
        self.btn_exit_fullScreen_1.setStyleSheet(u":hover{\n"
                                                 "	background-color:rgb(76, 80, 82);\n"
                                                 "}\n"
                                                 ":pressed{\n"
                                                 "	background-color:rgb(92, 97, 100);\n"
                                                 "}\n"
                                                 "QPushButton{\n"
                                                 "	background-repeat:no repeat;\n"
                                                 "	background-position:center;\n"
                                                 "	background-image: url(:/icons/resources/icons/fullscreen-exit.png);\n"
                                                 "}")

        self.horizontalLayout_27.addWidget(self.btn_exit_fullScreen_1)

        self.horizontalLayout_28.addLayout(self.horizontalLayout_27)

        self.verticalLayout_23.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.home_maximize_graph_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_6)

        self.home_view.addWidget(self.home_maximize_graph_page)
        self.home_maximize_table_page = QWidget()
        self.home_maximize_table_page.setObjectName(u"home_maximize_table_page")
        self.verticalLayout_24 = QVBoxLayout(self.home_maximize_table_page)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.home_maximize_table_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 60))
        self.frame_7.setStyleSheet(u"QPushButton{\n"
                                   "	border:none;\n"
                                   "	background-color:transparent;\n"
                                   "	\n"
                                   "	font: 12pt \"Microsoft YaHei UI\";\n"
                                   "}\n"
                                   "\n"
                                   "QCheckBox{\n"
                                   "	font: 12pt \"Microsoft YaHei UI\";\n"
                                   "	border:none;\n"
                                   "	background-color:transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QFrame{\n"
                                   "	background-color:rgb(60, 63, 65);\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QCheckBox::indicator{\n"
                                   "	border:1px solid rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QCheckBox::indicator:hover{\n"
                                   "	border:1px solid rgb(169, 169, 169);\n"
                                   "}\n"
                                   "\n"
                                   "QCheckBox::indicator:checked{\n"
                                   "	background-position:center;\n"
                                   "	background-repeat:no-repeat;\n"
                                   "	background-image: url(:/icons/resources/icons/checked_blue.png);\n"
                                   "}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.checkBox = QCheckBox(self.frame_7)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(80, 60))
        self.checkBox.setStyleSheet(u"padding-left: 10px;")

        self.horizontalLayout_29.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_7)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(90, 60))

        self.horizontalLayout_29.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame_7)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(90, 60))

        self.horizontalLayout_29.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame_7)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(90, 60))

        self.horizontalLayout_29.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame_7)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMinimumSize(QSize(110, 60))

        self.horizontalLayout_29.addWidget(self.checkBox_5)

        self.horizontalLayout_30.addLayout(self.horizontalLayout_29)

        self.pushButton_13 = QPushButton(self.frame_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_30.addWidget(self.pushButton_13)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(65, 60))
        self.pushButton.setMaximumSize(QSize(65, 16777215))
        self.pushButton.setStyleSheet(u":hover{\n"
                                      "	background-color:rgb(76, 80, 82);\n"
                                      "}\n"
                                      ":pressed{\n"
                                      "	background-color:rgb(92, 97, 100);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{\n"
                                      "	background-repeat:no repeat;\n"
                                      "	background-position:center;\n"
                                      "	background-image: url(:/icons/resources/icons/restoreScreen.png);\n"
                                      "}")

        self.horizontalLayout_30.addWidget(self.pushButton)

        self.pushButton_11 = QPushButton(self.frame_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(65, 60))
        self.pushButton_11.setMaximumSize(QSize(65, 16777215))
        self.pushButton_11.setStyleSheet(u":hover{\n"
                                         "	background-color:rgb(76, 80, 82);\n"
                                         "}\n"
                                         ":pressed{\n"
                                         "	background-color:rgb(92, 97, 100);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "	background-repeat:no repeat;\n"
                                         "	background-position:center;\n"
                                         "	background-image: url(:/icons/resources/icons/confirm.png);\n"
                                         "}")

        self.horizontalLayout_30.addWidget(self.pushButton_11)

        self.btn_exit_fullScreen_2 = QPushButton(self.frame_7)
        self.btn_exit_fullScreen_2.setObjectName(u"btn_exit_fullScreen_2")
        self.btn_exit_fullScreen_2.setMinimumSize(QSize(80, 60))
        self.btn_exit_fullScreen_2.setStyleSheet(u":hover{\n"
                                                 "	background-color:rgb(76, 80, 82);\n"
                                                 "}\n"
                                                 ":pressed{\n"
                                                 "	background-color:rgb(92, 97, 100);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton{\n"
                                                 "	background-repeat:no repeat;\n"
                                                 "	background-position:center;\n"
                                                 "	background-image: url(:/icons/resources/icons/fullscreen-exit.png);\n"
                                                 "}")

        self.horizontalLayout_30.addWidget(self.btn_exit_fullScreen_2)

        self.verticalLayout_24.addWidget(self.frame_7)

        self.tableWidget_3 = QTableWidget(self.home_maximize_table_page)
        if (self.tableWidget_3.columnCount() < 30):
            self.tableWidget_3.setColumnCount(30)
        if (self.tableWidget_3.rowCount() < 30):
            self.tableWidget_3.setRowCount(30)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"QHeaderView::section{\n"
                                         "	font: 12pt \"Microsoft YaHei UI\";\n"
                                         "}\n"
                                         "\n"
                                         "QTableView{\n"
                                         "	border:none;\n"
                                         "	font: 12pt \"Microsoft YaHei UI\";\n"
                                         "}\n"
                                         "\n"
                                         "QTableView::item{\n"
                                         "	border:1px solid rgb(69, 72, 74);\n"
                                         "}\n"
                                         "\n"
                                         "QTableView::item:selected{\n"
                                         "	background-color: rgb(0, 120, 215);\n"
                                         "}")
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_3.setRowCount(30)
        self.tableWidget_3.setColumnCount(30)
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.verticalLayout_24.addWidget(self.tableWidget_3)

        self.home_view.addWidget(self.home_maximize_table_page)

        self.horizontalLayout_12.addWidget(self.home_view)

        self.home_rightBox = QFrame(self.frame_home)
        self.home_rightBox.setObjectName(u"home_rightBox")
        self.home_rightBox.setMinimumSize(QSize(400, 0))
        self.home_rightBox.setMaximumSize(QSize(400, 16777215))
        self.home_rightBox.setStyleSheet(u"#home_rightBox{\n"
                                         "	background-color: rgb(60, 63, 65);\n"
                                         "	border-left:3px solid rgb(109, 109, 109);\n"
                                         "}")
        self.home_rightBox.setFrameShape(QFrame.StyledPanel)
        self.home_rightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.home_rightBox)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.home_frame_right_1 = QFrame(self.home_rightBox)
        self.home_frame_right_1.setObjectName(u"home_frame_right_1")
        self.home_frame_right_1.setMinimumSize(QSize(0, 40))
        self.home_frame_right_1.setMaximumSize(QSize(16777215, 40))
        self.home_frame_right_1.setStyleSheet(u"background-color: rgb(48, 50, 52);")
        self.horizontalLayout_17 = QHBoxLayout(self.home_frame_right_1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_home_select_part = QPushButton(self.home_frame_right_1)
        self.btn_home_select_part.setObjectName(u"btn_home_select_part")
        self.btn_home_select_part.setMinimumSize(QSize(120, 30))
        self.btn_home_select_part.setMaximumSize(QSize(120, 16777215))
        self.btn_home_select_part.setStyleSheet(u":hover{\n"
                                                "	background-color:rgb(76, 80, 82);\n"
                                                "}\n"
                                                ":pressed{\n"
                                                "	background-color:rgb(92, 97, 100);\n"
                                                "}\n"
                                                "\n"
                                                "#btn_home_select_part{\n"
                                                "	border:1px solid rgb(109, 109, 109);\n"
                                                "	border-radius:5px;\n"
                                                "	background-repeat:no repeat;\n"
                                                "	background-position:right;\n"
                                                "	background-image: url(:/icons/resources/icons/inverted-triangle_16.png);\n"
                                                "}\n"
                                                "\n"
                                                "#btn_home_select_part::menu-indicator{\n"
                                                "	image:none\n"
                                                "}")

        self.horizontalLayout_17.addWidget(self.btn_home_select_part)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)

        self.btn_home_remove_1 = QPushButton(self.home_frame_right_1)
        self.btn_home_remove_1.setObjectName(u"btn_home_remove_1")
        sizePolicy2.setHeightForWidth(self.btn_home_remove_1.sizePolicy().hasHeightForWidth())
        self.btn_home_remove_1.setSizePolicy(sizePolicy2)
        self.btn_home_remove_1.setMinimumSize(QSize(40, 40))
        self.btn_home_remove_1.setStyleSheet(u"QPushButton{\n"
                                             "	border-left:1px solid rgb(109, 109, 109);\n"
                                             "	background-repeat:no repeat;\n"
                                             "	background-position:center;\n"
                                             "	background-image: url(:/icons/resources/icons/remove.png);\n"
                                             "}\n"
                                             ":hover{\n"
                                             "	background-color: rgb(58, 60, 62);\n"
                                             "}\n"
                                             ":pressed{\n"
                                             "	background-color:rgb(68, 75, 75);\n"
                                             "}")

        self.horizontalLayout_17.addWidget(self.btn_home_remove_1)

        self.btn_home_table = QPushButton(self.home_frame_right_1)
        self.btn_home_table.setObjectName(u"btn_home_table")
        self.btn_home_table.setMinimumSize(QSize(40, 40))
        self.btn_home_table.setStyleSheet(u"QPushButton{\n"
                                          "	border-left:1px solid rgb(109, 109, 109);\n"
                                          "	background-repeat:no repeat;\n"
                                          "	background-position:center;\n"
                                          "	background-image: url(:/icons/resources/icons/table_gray.png);\n"
                                          "}\n"
                                          ":hover{\n"
                                          "	background-color: rgb(58, 60, 62);\n"
                                          "}\n"
                                          ":pressed{\n"
                                          "	background-color:rgb(68, 75, 75);\n"
                                          "}")

        self.horizontalLayout_17.addWidget(self.btn_home_table)

        self.btn_home_clear_1 = QPushButton(self.home_frame_right_1)
        self.btn_home_clear_1.setObjectName(u"btn_home_clear_1")
        self.btn_home_clear_1.setMinimumSize(QSize(50, 40))
        self.btn_home_clear_1.setStyleSheet(u"QPushButton{\n"
                                            "	border-left:1px solid rgb(109, 109, 109);\n"
                                            "}\n"
                                            ":hover{\n"
                                            "	background-color: rgb(58, 60, 62);\n"
                                            "}\n"
                                            ":pressed{\n"
                                            "	background-color:rgb(68, 75, 75);\n"
                                            "}")

        self.horizontalLayout_17.addWidget(self.btn_home_clear_1)

        self.verticalLayout_19.addWidget(self.home_frame_right_1)

        self.tableWidget = QTableWidget(self.home_rightBox)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 200))
        self.tableWidget.setFocusPolicy(Qt.ClickFocus)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
                                       "	border:none;\n"
                                       "	font: 12pt \"Microsoft YaHei UI\";\n"
                                       "}\n"
                                       "\n"
                                       "QTableView::item:selected{\n"
                                       "	background-color: rgb(0, 120, 215);\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section{\n"
                                       "	border:none;\n"
                                       "	border-bottom:1px solid rgb(109, 109, 109);\n"
                                       "	border-right:1px solid rgb(109, 109, 109);\n"
                                       "	font: 12pt \"Microsoft YaHei UI\";\n"
                                       "	background-color: rgb(59, 59, 59);\n"
                                       "	color: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "")
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_19.addWidget(self.tableWidget)

        self.home_rightBox_bottom = QFrame(self.home_rightBox)
        self.home_rightBox_bottom.setObjectName(u"home_rightBox_bottom")
        sizePolicy1.setHeightForWidth(self.home_rightBox_bottom.sizePolicy().hasHeightForWidth())
        self.home_rightBox_bottom.setSizePolicy(sizePolicy1)
        self.home_rightBox_bottom.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_13 = QVBoxLayout(self.home_rightBox_bottom)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.home_frame_right_2 = QFrame(self.home_rightBox_bottom)
        self.home_frame_right_2.setObjectName(u"home_frame_right_2")
        self.home_frame_right_2.setMaximumSize(QSize(16777215, 40))
        self.home_frame_right_2.setStyleSheet(u"background-color: rgb(48, 50, 52);")
        self.horizontalLayout_18 = QHBoxLayout(self.home_frame_right_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.btn_home_select_para = QPushButton(self.home_frame_right_2)
        self.btn_home_select_para.setObjectName(u"btn_home_select_para")
        self.btn_home_select_para.setMinimumSize(QSize(120, 30))
        self.btn_home_select_para.setMaximumSize(QSize(120, 16777215))
        self.btn_home_select_para.setStyleSheet(u":hover{\n"
                                                "	background-color:rgb(76, 80, 82);\n"
                                                "}\n"
                                                ":pressed{\n"
                                                "	background-color:rgb(92, 97, 100);\n"
                                                "}\n"
                                                "\n"
                                                "#btn_home_select_para{\n"
                                                "	border:1px solid rgb(109, 109, 109);\n"
                                                "	border-radius:5px;\n"
                                                "	background-repeat:no repeat;\n"
                                                "	background-position:right;\n"
                                                "	background-image: url(:/icons/resources/icons/inverted-triangle_16.png);\n"
                                                "}\n"
                                                "\n"
                                                "#btn_home_select_para::menu-indicator{\n"
                                                "	image:none;\n"
                                                "}")

        self.horizontalLayout_18.addWidget(self.btn_home_select_para)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.btn_home_remove_2 = QPushButton(self.home_frame_right_2)
        self.btn_home_remove_2.setObjectName(u"btn_home_remove_2")
        sizePolicy2.setHeightForWidth(self.btn_home_remove_2.sizePolicy().hasHeightForWidth())
        self.btn_home_remove_2.setSizePolicy(sizePolicy2)
        self.btn_home_remove_2.setMinimumSize(QSize(40, 40))
        self.btn_home_remove_2.setStyleSheet(u"QPushButton{\n"
                                             "	border-left:1px solid rgb(109, 109, 109);\n"
                                             "	background-repeat:no repeat;\n"
                                             "	background-position:center;\n"
                                             "	background-image: url(:/icons/resources/icons/remove.png);\n"
                                             "}\n"
                                             ":hover{\n"
                                             "	background-color: rgb(58, 60, 62);\n"
                                             "}\n"
                                             ":pressed{\n"
                                             "	background-color:rgb(68, 75, 75);\n"
                                             "}")

        self.horizontalLayout_18.addWidget(self.btn_home_remove_2)

        self.btn_home_clear_2 = QPushButton(self.home_frame_right_2)
        self.btn_home_clear_2.setObjectName(u"btn_home_clear_2")
        self.btn_home_clear_2.setMinimumSize(QSize(50, 40))
        self.btn_home_clear_2.setStyleSheet(u"QPushButton{\n"
                                            "	border-left:1px solid rgb(109, 109, 109);\n"
                                            "}\n"
                                            ":hover{\n"
                                            "	background-color: rgb(58, 60, 62);\n"
                                            "}\n"
                                            ":pressed{\n"
                                            "	background-color:rgb(68, 75, 75);\n"
                                            "}")

        self.horizontalLayout_18.addWidget(self.btn_home_clear_2)

        self.verticalLayout_13.addWidget(self.home_frame_right_2)

        self.tableWidget_2 = QTableWidget(self.home_rightBox_bottom)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFocusPolicy(Qt.ClickFocus)
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
                                         "	border:none;\n"
                                         "	font: 12pt \"Microsoft YaHei UI\";\n"
                                         "}\n"
                                         "\n"
                                         "QTableView::item:selected{\n"
                                         "	background-color: rgb(0, 120, 215);\n"
                                         "}\n"
                                         "\n"
                                         "QHeaderView::section{\n"
                                         "	border:none;\n"
                                         "	border-bottom:1px solid rgb(109, 109, 109);\n"
                                         "	border-right:1px solid rgb(109, 109, 109);\n"
                                         "	font: 12pt \"Microsoft YaHei UI\";\n"
                                         "	background-color: rgb(59, 59, 59);\n"
                                         "}")
        self.tableWidget_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.verticalLayout_13.addWidget(self.tableWidget_2)

        self.home_frame_right_3 = QFrame(self.home_rightBox_bottom)
        self.home_frame_right_3.setObjectName(u"home_frame_right_3")
        self.home_frame_right_3.setMaximumSize(QSize(16777215, 40))
        self.home_frame_right_3.setStyleSheet(u"background-color: rgb(48, 50, 52);")
        self.horizontalLayout_20 = QHBoxLayout(self.home_frame_right_3)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.btn_home_graph = QPushButton(self.home_frame_right_3)
        self.btn_home_graph.setObjectName(u"btn_home_graph")
        self.btn_home_graph.setMinimumSize(QSize(120, 40))
        self.btn_home_graph.setStyleSheet(u"QPushButton{\n"
                                          "	border:1px solid rgb(109, 109, 109);\n"
                                          "	border-radius:5px;\n"
                                          "}\n"
                                          ":hover{\n"
                                          "	background-color: rgb(76, 80, 82);\n"
                                          "}\n"
                                          ":pressed{\n"
                                          "	background-color: rgb(75, 110, 175);\n"
                                          "}")

        self.horizontalLayout_20.addWidget(self.btn_home_graph)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)

        self.btn_home_reset = QPushButton(self.home_frame_right_3)
        self.btn_home_reset.setObjectName(u"btn_home_reset")
        self.btn_home_reset.setMinimumSize(QSize(40, 40))
        self.btn_home_reset.setStyleSheet(u"QPushButton{\n"
                                          "	border-left:1px solid rgb(109, 109, 109);\n"
                                          "	background-repeat:no repeat;\n"
                                          "	background-position:center;\n"
                                          "	background-image: url(:/icons/resources/icons/refresh.png);\n"
                                          "}\n"
                                          ":hover{\n"
                                          "	background-color: rgb(58, 60, 62);\n"
                                          "}\n"
                                          ":pressed{\n"
                                          "	background-color:rgb(68, 75, 75);\n"
                                          "}")

        self.horizontalLayout_20.addWidget(self.btn_home_reset)

        self.btn_home_remove_3 = QPushButton(self.home_frame_right_3)
        self.btn_home_remove_3.setObjectName(u"btn_home_remove_3")
        self.btn_home_remove_3.setMinimumSize(QSize(40, 40))
        self.btn_home_remove_3.setStyleSheet(u"QPushButton{\n"
                                             "	border-left:1px solid rgb(109, 109, 109);\n"
                                             "	background-repeat:no repeat;\n"
                                             "	background-position:center;\n"
                                             "	background-image: url(:/icons/resources/icons/remove.png);\n"
                                             "}\n"
                                             ":hover{\n"
                                             "	background-color: rgb(58, 60, 62);\n"
                                             "}\n"
                                             ":pressed{\n"
                                             "	background-color:rgb(68, 75, 75);\n"
                                             "}")

        self.horizontalLayout_20.addWidget(self.btn_home_remove_3)

        self.btn_home_clear_3 = QPushButton(self.home_frame_right_3)
        self.btn_home_clear_3.setObjectName(u"btn_home_clear_3")
        self.btn_home_clear_3.setMinimumSize(QSize(50, 40))
        self.btn_home_clear_3.setStyleSheet(u"QPushButton{\n"
                                            "	border-left:1px solid rgb(109, 109, 109);\n"
                                            "}\n"
                                            ":hover{\n"
                                            "	background-color: rgb(58, 60, 62);\n"
                                            "}\n"
                                            ":pressed{\n"
                                            "	background-color:rgb(68, 75, 75);\n"
                                            "}")

        self.horizontalLayout_20.addWidget(self.btn_home_clear_3)

        self.verticalLayout_13.addWidget(self.home_frame_right_3)

        self.verticalLayout_19.addWidget(self.home_rightBox_bottom)

        self.verticalLayout_25.addLayout(self.verticalLayout_19)

        self.frame_10 = QFrame(self.home_rightBox)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 200))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_4 = QTableWidget(self.frame_10)
        if (self.tableWidget_4.columnCount() < 4):
            self.tableWidget_4.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setFocusPolicy(Qt.ClickFocus)
        self.tableWidget_4.setStyleSheet(u"QTableWidget{\n"
                                         "	border:none;\n"
                                         "	font: 12pt \"Microsoft YaHei UI\";\n"
                                         "}\n"
                                         "\n"
                                         "QTableView::item:selected{\n"
                                         "	background-color: rgb(0, 120, 215);\n"
                                         "}\n"
                                         "\n"
                                         "QHeaderView::section{\n"
                                         "	border:none;\n"
                                         "	border-bottom:1px solid rgb(109, 109, 109);\n"
                                         "	border-right:1px solid rgb(109, 109, 109);\n"
                                         "	font: 12pt \"Microsoft YaHei UI\";\n"
                                         "	background-color: rgb(59, 59, 59);\n"
                                         "}")
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.horizontalLayout_31.addWidget(self.tableWidget_4)

        self.verticalLayout_25.addWidget(self.frame_10)

        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.horizontalLayout_12.addWidget(self.home_rightBox)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)

        self.verticalLayout_10.addWidget(self.frame_home)

        self.book.addWidget(self.page_home)
        self.page_exp = QWidget()
        self.page_exp.setObjectName(u"page_exp")
        self.page_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.book.addWidget(self.page_exp)
        self.page_conn = QWidget()
        self.page_conn.setObjectName(u"page_conn")
        self.verticalLayout_15 = QVBoxLayout(self.page_conn)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame = QFrame(self.page_conn)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_2 = QFrame(self.page_conn)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_conn)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 250))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_3)

        self.horizontalLayout_19.addLayout(self.verticalLayout_14)

        self.frame_4 = QFrame(self.page_conn)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy6.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy6)
        self.frame_4.setMinimumSize(QSize(250, 0))
        self.frame_4.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_4)

        self.verticalLayout_15.addLayout(self.horizontalLayout_19)

        self.book.addWidget(self.page_conn)

        self.horizontalLayout_6.addWidget(self.book)

        self.verticalLayout_2.addWidget(self.viewContainer)

        self.bottomLog = QFrame(self.content)
        self.bottomLog.setObjectName(u"bottomLog")
        self.bottomLog.setMinimumSize(QSize(0, 25))
        self.bottomLog.setStyleSheet(u"")
        self.bottomLog.setFrameShape(QFrame.StyledPanel)
        self.bottomLog.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottomLog)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.author = QLabel(self.bottomLog)
        self.author.setObjectName(u"author")
        self.author.setMinimumSize(QSize(70, 0))
        self.author.setMaximumSize(QSize(70, 16777215))
        self.author.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.author)

        self.msgBox = QLabel(self.bottomLog)
        self.msgBox.setObjectName(u"msgBox")
        self.msgBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.msgBox)

        self.msgBox1 = QLabel(self.bottomLog)
        self.msgBox1.setObjectName(u"msgBox1")
        self.msgBox1.setMinimumSize(QSize(150, 0))
        self.msgBox1.setMaximumSize(QSize(140, 16777215))
        self.msgBox1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.msgBox1)

        self.version = QLabel(self.bottomLog)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(80, 0))
        self.version.setMaximumSize(QSize(80, 16777215))
        self.version.setStyleSheet(u"")
        self.version.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.version)

        self.grip_icon = QFrame(self.bottomLog)
        self.grip_icon.setObjectName(u"grip_icon")
        self.grip_icon.setMaximumSize(QSize(25, 16777215))
        self.grip_icon.setFrameShape(QFrame.StyledPanel)
        self.grip_icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.grip_icon)

        self.verticalLayout_2.addWidget(self.bottomLog)

        self.horizontalLayout.addWidget(self.content)

        self.appBoxMargins.addWidget(self.appBox)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.book.setCurrentIndex(0)
        self.home_view.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action22222.setText(QCoreApplication.translate("MainWindow", u"22222", None))
        self.action3333.setText(QCoreApplication.translate("MainWindow", u"3333", None))
        self.action44444.setText(QCoreApplication.translate("MainWindow", u"44444", None))
        self.action555.setText(QCoreApplication.translate("MainWindow", u"555", None))
        self.action111.setText(QCoreApplication.translate("MainWindow", u"111", None))
        self.action222.setText(QCoreApplication.translate("MainWindow", u"222", None))
        self.action333.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.action444.setText(QCoreApplication.translate("MainWindow", u"444", None))
        self.appName.setText(QCoreApplication.translate("MainWindow", u"PyGibird", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"\u5c55\u5f00", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_conn.setText(QCoreApplication.translate("MainWindow", u"\u8fdc\u7a0b\u8fde\u63a5", None))
        self.btn_exp.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bfc\u51fa", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.setting_label_2.setText("")
        self.settingBar_label.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.btn_setting_return.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u50a8\u76ee\u5f55", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.about_box.setMarkdown(QCoreApplication.translate("MainWindow", u"**About PyGibird**\n"
                                                                            "\n"
                                                                            "       PyGibird GUI is very much based on the open source project of Mr.\n"
                                                                            "Wanderson M. Pimenta, and if you have seen his work, you will definitely find\n"
                                                                            "the style very similar. If you are a beginner like me, his work must be very\n"
                                                                            "helpful to you. Here is the link to his project: \n"
                                                                            "\n"
                                                                            "https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6.\n"
                                                                            "\n"
                                                                            "       During the experience you may find that some of the interfaces are not\n"
                                                                            "available, either because of time limit or because they involve the processing\n"
                                                                            "of some data for my thesis. I'm sorry for any trouble caused by this, and since\n"
                                                                            "the author is not a computer science major, please understand the code style.\n"
                                                                            "\n"
                                                                            "**Convert UI**\n"
                                                                            "\n"
                                                                            "pyside6-uic name.ui > ui_name.py\n"
                                                                            "\n"
                                                                            "**Convert QRC**\n"
                                                                            "\n"
                                                                            "pyside6-rcc name.qrc -o name_rc.py\n"
                                                                            "\n"
                                                                            "", None))
        self.about_box.setHtml(QCoreApplication.translate("MainWindow",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                          "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; color:#ff79c6;\">About PyGibird</span></p>\n"
                                                          "<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">      </span><span style=\" font-size:10pt; color:#ffffff;\"> PyGibird GUI"
                                                          " is very much based on the open source project of Mr. Wanderson M. Pimenta, and if you have seen his work, you will definitely find the style very similar. If you are a beginner like me, his work must be very helpful to you. Here is the link to his project: </span></p>\n"
                                                          "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6.</span></p>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">       During the experience you may find that some of the interfaces are not available, either because of time limit or because they involve the processing of some data for my thesis. I'm sorry for any trouble caused by this, and since the author is not a computer science major, please understand the "
                                                          "code style.</span></p>\n"
                                                          "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                          "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; color:#ff79c6;\">Convert UI</span></p>\n"
                                                          "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">pyside6-uic name.ui &gt; ui_name.py</span></p>\n"
                                                          "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:700; color:#ff79c6;\"><br /></p>\n"
                                                          "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                                                          "nt:0px;\"><span style=\" font-size:12pt; font-weight:700; color:#ff79c6;\">Convert QRC</span></p>\n"
                                                          "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">pyside6-rcc name.qrc -o name_rc.py</span></p>\n"
                                                          "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt; color:#ff55ff;\"><br /></p></body></html>",
                                                          None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5f55", None))
        self.appExpr.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>PyGibird App - A Graduation Project based on Python</p></body></html>",
                                                        None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_table_exit.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btn_table_exit.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009", None))
        self.check_furnace.setText(QCoreApplication.translate("MainWindow", u"\u7089\u819b", None))
        self.check_superheater.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u70ed\u5668", None))
        self.check_reheater.setText(QCoreApplication.translate("MainWindow", u"\u518d\u70ed\u5668", None))
        self.check_economizer.setText(QCoreApplication.translate("MainWindow", u"\u7701\u7164\u5668", None))
        self.check_airPreheater.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u9884\u5668", None))
        # if QT_CONFIG(tooltip)
        self.btn_table_refresh.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btn_table_refresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u9009\u62e9", None))
        # if QT_CONFIG(tooltip)
        self.btn_table_fullScreen.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btn_table_fullScreen.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f\u663e\u793a", None))
        # if QT_CONFIG(tooltip)
        self.btn_table_filter.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btn_table_filter.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u7b5b\u9009", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"#1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"#3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"#4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"#5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.home_graph_1.setText("")
        self.home_graph_exit_1.setText("")
        self.home_graph_2.setText("")
        self.home_graph_exit_2.setText("")
        self.home_graph_3.setText("")
        self.home_graph_exit_3.setText("")
        self.home_graph_4.setText("")
        self.home_graph_exit_4.setText("")
        self.home_graph_5.setText("")
        self.home_graph_exit_5.setText("")
        self.home_graph_6.setText("")
        self.home_graph_exit_6.setText("")
        self.emptySpacer.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_home_graph_track.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u8f85\u52a9\u8ffd\u8e2a", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_home_graph_track.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_home_graph_coor.setToolTip(QCoreApplication.translate("MainWindow", u"\u5750\u6807", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_home_graph_coor.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_home_graph_player.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btn_home_graph_player.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_home_graph_fullScreen.setToolTip(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_home_graph_fullScreen.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u8f85\u52a9\u8ffd\u8e2a", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u8f85\u52a9\u5750\u6807", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_exit_fullScreen_1.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u5168\u5c4f", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_exit_fullScreen_1.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u7089\u819b", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u70ed\u5668", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u518d\u70ed\u5668", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u7701\u7164\u5668", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u9884\u70ed\u5668", None))
        self.pushButton_13.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u6570\u636e", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u7b5b\u9009", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_11.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_exit_fullScreen_2.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u5168\u5c4f", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_exit_fullScreen_2.setText("")

        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)

        self.btn_home_select_part.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u90e8\u4f4d", None))
        # if QT_CONFIG(tooltip)
        self.btn_home_remove_1.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6240\u9009", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_home_remove_1.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_home_table.setToolTip(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8868\u683c", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_home_table.setText("")
        self.btn_home_clear_1.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u4f4d", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u673a\u7ec4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7", None));
        self.btn_home_select_para.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u53c2\u6570", None))
        # if QT_CONFIG(tooltip)
        self.btn_home_remove_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6240\u9009", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_home_remove_2.setText("")
        self.btn_home_clear_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee", None));
        self.btn_home_graph.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u5165\u56fe\u50cf", None))
        self.btn_home_reset.setText("")
        self.btn_home_remove_3.setText("")
        self.btn_home_clear_3.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        ___qtablewidgetitem6 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u540d", None));
        ___qtablewidgetitem7 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u540d", None));
        ___qtablewidgetitem8 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem9 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u65f6\u95f4", None));
        self.author.setText(QCoreApplication.translate("MainWindow", u"By:Yuanyue", None))
        self.msgBox.setText("")
        self.msgBox1.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.00", None))
    # retranslateUi
