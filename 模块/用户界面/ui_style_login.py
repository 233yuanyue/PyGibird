# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginRRGPck.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from modules.ui.ui_resources_rc import *


class Ui_loginWidget(object):
    def setupUi(self, loginWidget):
        if not loginWidget.objectName():
            loginWidget.setObjectName(u"loginWidget")
        loginWidget.resize(411, 485)
        loginWidget.setStyleSheet(u"QWidget{\n"
                                  "	border:none;\n"
                                  "	background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QWidget .QLabel, .QPushButton, .QCheckBox{\n"
                                  "	color: rgb(128, 128, 128);\n"
                                  "	font: 12pt \"Microsoft YaHei UI\";\n"
                                  "}\n"
                                  "\n"
                                  ".QPushBotton{\n"
                                  "	border:none;\n"
                                  "	background-color: transparent;\n"
                                  "}\n"
                                  "\n"
                                  "QFrame{\n"
                                  "	border:none;\n"
                                  "}\n"
                                  "\n"
                                  "#welcome_label{\n"
                                  "	font: 550 18pt \"Microsoft YaHei UI\";\n"
                                  "	color: rgb(33, 36, 40);\n"
                                  "}\n"
                                  "\n"
                                  "#btn_login{\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "	background-color: rgb(38, 112, 234);\n"
                                  "	border-radius:5px;\n"
                                  "	font: 12pt \"Microsoft YaHei UI\";\n"
                                  "}\n"
                                  "\n"
                                  "#btn_register{\n"
                                  "	color: rgb(63, 133, 255);\n"
                                  "}\n"
                                  "\n"
                                  "#btn_exit{\n"
                                  "	background-repeat:no-repeat;\n"
                                  "	background-position:center;\n"
                                  "	background-image: url(:/icons/resources/icons/close_gray.png);\n"
                                  "}\n"
                                  "#btn_exit:hover{\n"
                                  "	background-image: url(:/icons/resources/icons/close_blue.png);\n"
                                  "}\n"
                                  "/*-----------------------------------------------------*/\n"
                                  "#bottom_problem{\n"
                                  "	text-align:left;\n"
                                  ""
                                  "}\n"
                                  "\n"
                                  "#bottom_problem:hover{\n"
                                  "	\n"
                                  "	color: rgb(38, 112, 234);\n"
                                  "}\n"
                                  "\n"
                                  "#bottom_botBox .QLabel{\n"
                                  "	color: rgb(196, 196, 196);\n"
                                  "}\n"
                                  "\n"
                                  "#bottom_botBox .QPushButton:hover{\n"
                                  "	color: rgb(38, 112, 234);\n"
                                  "}\n"
                                  "\n"
                                  "#bottom_topBox{	\n"
                                  "	margin-bottom:30px;\n"
                                  "}\n"
                                  "/*---------------------------------------------------------------*/\n"
                                  "#btn_forgetPwd{\n"
                                  "	text-align:right;\n"
                                  "}\n"
                                  "\n"
                                  "#checkBox{\n"
                                  "	padding-left:5px;\n"
                                  "}\n"
                                  "\n"
                                  "#checkBox::indicator{\n"
                                  "	border:1px solid rgb(196, 206, 226);\n"
                                  "	width:14px;\n"
                                  " 	height:14px;\n"
                                  "}\n"
                                  "\n"
                                  "#checkBox::indicator:hover{\n"
                                  "	border:1px solid rgb(38, 112, 234);\n"
                                  "}\n"
                                  "\n"
                                  "#checkBox::indicator:checked{\n"
                                  "	border:1px solid rgb(38, 112, 234);\n"
                                  "	background-repeat:no-repeat;\n"
                                  "	background-position:center;\n"
                                  "	background-image: url(:/icons/resources/icons/checked_blue.png);\n"
                                  "}\n"
                                  "\n"
                                  "#btn_forgetPwd:hover{\n"
                                  "	color: rgb(38, 112, 234);\n"
                                  "}\n"
                                  "/*----------------------------------------------------------*/\n"
                                  "#Account"
                                  "Box{\n"
                                  "	border:1px solid rgb(219, 219, 219);\n"
                                  "	border-radius:6px;\n"
                                  "	margin-bottom:10px solid transparent;\n"
                                  "}\n"
                                  "\n"
                                  "#AccountBox QListView::item{\n"
                                  "	background-color: rgb(0, 0, 0);\n"
                                  "}\n"
                                  "\n"
                                  "#AccountBox .QLineEdit{\n"
                                  "	border:none;\n"
                                  "	background-color: transparent;\n"
                                  "	padding-left:10px solid transparent;\n"
                                  "	/*color:rgb(196, 196, 196);*/\n"
                                  "	font: 13pt \"Microsoft YaHei UI\";\n"
                                  "}\n"
                                  "\n"
                                  "#AccountBox .QComboBox{\n"
                                  "	border:1px solid rgb(242, 242, 242);\n"
                                  "	font: 12pt \"Microsoft YaHei UI\";\n"
                                  "	background-color: transparent;\n"
                                  "}\n"
                                  "\n"
                                  "#acc_icon{\n"
                                  "	background-repeat:no-repeat;\n"
                                  "	background-position:center;\n"
                                  "	background-image: url(:/icons/resources/icons/invertedTriangle.png);\n"
                                  "}\n"
                                  "\n"
                                  "#acc_icon:hover{\n"
                                  "	background-image: url(:/icons/resources/icons/invertedTriangle_blue.png);\n"
                                  "}\n"
                                  "\n"
                                  "#acc_bottom{\n"
                                  "	color: rgb(0, 0, 0);\n"
                                  "	background-color:rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "#acc_bottom QAbstractItemView{\n"
                                  "	border:1px solid rgb(237, 237, 237);\n"
                                  ""
                                  "	outline:0px;\n"
                                  "}\n"
                                  "\n"
                                  "#acc_bottom QAbstractItemView::item{\n"
                                  "	color: rgb(128, 128, 128);\n"
                                  "	height:27px;\n"
                                  "	padding-left:10px;\n"
                                  "	background-color: transparent;\n"
                                  "}\n"
                                  "\n"
                                  "#acc_bottom QAbstractItemView::item:hover{\n"
                                  "	color: rgb(38, 112, 234);\n"
                                  "}\n"
                                  "/*=========================================*/\n"
                                  "#PasswordBox{\n"
                                  "	border:1px solid rgb(219, 219, 219);\n"
                                  "	border-radius:6px;\n"
                                  "	margin-bottom:10px solid transparent;\n"
                                  "	margin-left:1px;\n"
                                  "	margin-right:1px;\n"
                                  "}\n"
                                  "\n"
                                  "#PasswordBox .QLineEdit{\n"
                                  "	border:none;\n"
                                  "	background-color: transparent;\n"
                                  "	padding-left:10px solid transparent;\n"
                                  "	/*color: rgb(196, 196, 196);*/\n"
                                  "	font: 13pt \"Microsoft YaHei UI\";\n"
                                  "}\n"
                                  "\n"
                                  "#btn_visible{\n"
                                  "	background-repeat:no-repeat;\n"
                                  "	background-position:center;\n"
                                  "}")
        self.shadowArea = QVBoxLayout(loginWidget)
        self.shadowArea.setSpacing(0)
        self.shadowArea.setObjectName(u"shadowArea")
        self.shadowArea.setContentsMargins(10, 10, 10, 10)
        self.widgetBox = QFrame(loginWidget)
        self.widgetBox.setObjectName(u"widgetBox")
        self.verticalLayout_4 = QVBoxLayout(self.widgetBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topBox = QFrame(self.widgetBox)
        self.topBox.setObjectName(u"topBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topBox.sizePolicy().hasHeightForWidth())
        self.topBox.setSizePolicy(sizePolicy)
        self.topBox.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_7 = QHBoxLayout(self.topBox)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.topMoveArea = QFrame(self.topBox)
        self.topMoveArea.setObjectName(u"topMoveArea")
        self.topMoveArea.setFrameShape(QFrame.StyledPanel)
        self.topMoveArea.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.topMoveArea)

        self.btn_exit = QPushButton(self.topBox)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(40, 40))
        self.btn_exit.setMaximumSize(QSize(40, 40))
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btn_exit)

        self.verticalLayout_4.addWidget(self.topBox)

        self.welcome_label = QLabel(self.widgetBox)
        self.welcome_label.setObjectName(u"welcome_label")
        sizePolicy.setHeightForWidth(self.welcome_label.sizePolicy().hasHeightForWidth())
        self.welcome_label.setSizePolicy(sizePolicy)
        self.welcome_label.setMinimumSize(QSize(0, 70))
        self.welcome_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.welcome_label)

        self.mainBody = QFrame(self.widgetBox)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.AccountBox = QFrame(self.mainBody)
        self.AccountBox.setObjectName(u"AccountBox")
        sizePolicy.setHeightForWidth(self.AccountBox.sizePolicy().hasHeightForWidth())
        self.AccountBox.setSizePolicy(sizePolicy)
        self.AccountBox.setMaximumSize(QSize(16777215, 70))
        self.AccountBox.setFrameShape(QFrame.StyledPanel)
        self.AccountBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.AccountBox)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.acc_text = QLineEdit(self.AccountBox)
        self.acc_text.setObjectName(u"acc_text")
        self.acc_text.setMinimumSize(QSize(0, 55))

        self.horizontalLayout.addWidget(self.acc_text)

        self.acc_icon = QPushButton(self.AccountBox)
        self.acc_icon.setObjectName(u"acc_icon")
        self.acc_icon.setMinimumSize(QSize(45, 45))
        self.acc_icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.acc_icon.setFlat(True)

        self.horizontalLayout.addWidget(self.acc_icon)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.acc_bottom = QComboBox(self.AccountBox)
        self.acc_bottom.addItem("")
        self.acc_bottom.setObjectName(u"acc_bottom")
        sizePolicy.setHeightForWidth(self.acc_bottom.sizePolicy().hasHeightForWidth())
        self.acc_bottom.setSizePolicy(sizePolicy)
        self.acc_bottom.setMinimumSize(QSize(0, 0))
        self.acc_bottom.setMaximumSize(QSize(16777215, 0))
        self.acc_bottom.setEditable(False)
        self.acc_bottom.setInsertPolicy(QComboBox.InsertAtTop)

        self.verticalLayout.addWidget(self.acc_bottom)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2.addWidget(self.AccountBox)

        self.PasswordBox = QFrame(self.mainBody)
        self.PasswordBox.setObjectName(u"PasswordBox")
        sizePolicy.setHeightForWidth(self.PasswordBox.sizePolicy().hasHeightForWidth())
        self.PasswordBox.setSizePolicy(sizePolicy)
        self.PasswordBox.setMaximumSize(QSize(16777215, 70))
        self.PasswordBox.setFrameShape(QFrame.StyledPanel)
        self.PasswordBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.PasswordBox)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.pwd_text = QLineEdit(self.PasswordBox)
        self.pwd_text.setObjectName(u"pwd_text")
        self.pwd_text.setMinimumSize(QSize(0, 60))
        self.pwd_text.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.pwd_text)

        self.btn_visible = QPushButton(self.PasswordBox)
        self.btn_visible.setObjectName(u"btn_visible")
        self.btn_visible.setMinimumSize(QSize(45, 45))
        self.btn_visible.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visible.setIconSize(QSize(32, 32))
        self.btn_visible.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_visible)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.addWidget(self.PasswordBox)

        self.forgetPwdBox = QFrame(self.mainBody)
        self.forgetPwdBox.setObjectName(u"forgetPwdBox")
        sizePolicy.setHeightForWidth(self.forgetPwdBox.sizePolicy().hasHeightForWidth())
        self.forgetPwdBox.setSizePolicy(sizePolicy)
        self.forgetPwdBox.setMinimumSize(QSize(0, 65))
        self.verticalLayout_5 = QVBoxLayout(self.forgetPwdBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pwd_layout = QFrame(self.forgetPwdBox)
        self.pwd_layout.setObjectName(u"pwd_layout")
        sizePolicy.setHeightForWidth(self.pwd_layout.sizePolicy().hasHeightForWidth())
        self.pwd_layout.setSizePolicy(sizePolicy)
        self.pwd_layout.setMaximumSize(QSize(16777215, 40))
        self.pwd_layout.setStyleSheet(u"margin-bottom:10px;")
        self.layout_pwd = QHBoxLayout(self.pwd_layout)
        self.layout_pwd.setSpacing(0)
        self.layout_pwd.setObjectName(u"layout_pwd")
        self.layout_pwd.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.pwd_layout)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 30))

        self.layout_pwd.addWidget(self.checkBox)

        self.btn_forgetPwd = QPushButton(self.pwd_layout)
        self.btn_forgetPwd.setObjectName(u"btn_forgetPwd")
        self.btn_forgetPwd.setMinimumSize(QSize(0, 30))
        self.btn_forgetPwd.setCheckable(False)
        self.btn_forgetPwd.setAutoRepeat(False)
        self.btn_forgetPwd.setAutoExclusive(False)
        self.btn_forgetPwd.setAutoDefault(False)
        self.btn_forgetPwd.setFlat(True)

        self.layout_pwd.addWidget(self.btn_forgetPwd)

        self.verticalLayout_5.addWidget(self.pwd_layout)

        self.msg_label = QLabel(self.forgetPwdBox)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy)
        self.msg_label.setMinimumSize(QSize(0, 20))
        self.msg_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.msg_label)

        self.verticalLayout_2.addWidget(self.forgetPwdBox)

        self.btn_login = QPushButton(self.mainBody)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 50))
        self.btn_login.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_login)

        self.bottomBox = QFrame(self.mainBody)
        self.bottomBox.setObjectName(u"bottomBox")
        sizePolicy.setHeightForWidth(self.bottomBox.sizePolicy().hasHeightForWidth())
        self.bottomBox.setSizePolicy(sizePolicy)
        self.bottomBox.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_6 = QVBoxLayout(self.bottomBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bottom_topBox = QFrame(self.bottomBox)
        self.bottom_topBox.setObjectName(u"bottom_topBox")
        sizePolicy.setHeightForWidth(self.bottom_topBox.sizePolicy().hasHeightForWidth())
        self.bottom_topBox.setSizePolicy(sizePolicy)
        self.bottom_topBox.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_topBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bottom_problem = QPushButton(self.bottom_topBox)
        self.bottom_problem.setObjectName(u"bottom_problem")
        self.bottom_problem.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.bottom_problem)

        self.bottom_account = QLabel(self.bottom_topBox)
        self.bottom_account.setObjectName(u"bottom_account")
        self.bottom_account.setMinimumSize(QSize(0, 50))
        self.bottom_account.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.bottom_account)

        self.btn_register = QPushButton(self.bottom_topBox)
        self.btn_register.setObjectName(u"btn_register")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_register.sizePolicy().hasHeightForWidth())
        self.btn_register.setSizePolicy(sizePolicy1)
        self.btn_register.setMinimumSize(QSize(0, 50))
        self.btn_register.setMaximumSize(QSize(70, 16777215))
        self.btn_register.setCheckable(False)
        self.btn_register.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_register)

        self.verticalLayout_6.addWidget(self.bottom_topBox)

        self.bottom_botBox = QFrame(self.bottomBox)
        self.bottom_botBox.setObjectName(u"bottom_botBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bottom_botBox.sizePolicy().hasHeightForWidth())
        self.bottom_botBox.setSizePolicy(sizePolicy2)
        self.bottom_botBox.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.bottom_botBox)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.bottom_botBox)
        self.label_1.setObjectName(u"label_1")
        sizePolicy2.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_1)

        self.btn_userAgreement = QPushButton(self.bottom_botBox)
        self.btn_userAgreement.setObjectName(u"btn_userAgreement")
        sizePolicy2.setHeightForWidth(self.btn_userAgreement.sizePolicy().hasHeightForWidth())
        self.btn_userAgreement.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.btn_userAgreement)

        self.label_2 = QLabel(self.bottom_botBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.btn_privacyAgreement = QPushButton(self.bottom_botBox)
        self.btn_privacyAgreement.setObjectName(u"btn_privacyAgreement")
        sizePolicy2.setHeightForWidth(self.btn_privacyAgreement.sizePolicy().hasHeightForWidth())
        self.btn_privacyAgreement.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.btn_privacyAgreement)

        self.verticalLayout_6.addWidget(self.bottom_botBox)

        self.verticalLayout_2.addWidget(self.bottomBox)

        self.verticalLayout_4.addWidget(self.mainBody, 0, Qt.AlignTop)

        self.shadowArea.addWidget(self.widgetBox)

        self.retranslateUi(loginWidget)

        self.btn_forgetPwd.setDefault(False)

        QMetaObject.connectSlotsByName(loginWidget)

    # setupUi

    def retranslateUi(self, loginWidget):
        loginWidget.setWindowTitle(QCoreApplication.translate("loginWidget", u"Form", None))
        self.btn_exit.setText("")
        self.welcome_label.setText(QCoreApplication.translate("loginWidget", u"\u6b22\u8fce\u767b\u5f55PyGibird", None))
        self.acc_text.setPlaceholderText(
            QCoreApplication.translate("loginWidget", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.acc_icon.setText("")
        self.acc_bottom.setItemText(0,
                                    QCoreApplication.translate("loginWidget", u"\u6e05\u9664\u5386\u53f2\u6570\u636e",
                                                               None))

        self.acc_bottom.setCurrentText(
            QCoreApplication.translate("loginWidget", u"\u6e05\u9664\u5386\u53f2\u6570\u636e", None))
        self.acc_bottom.setPlaceholderText("")
        self.pwd_text.setPlaceholderText(
            QCoreApplication.translate("loginWidget", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.btn_visible.setText("")
        self.checkBox.setText(QCoreApplication.translate("loginWidget", u"\u8bb0\u4f4f\u8d26\u53f7", None))
        self.btn_forgetPwd.setText(QCoreApplication.translate("loginWidget", u"\u5fd8\u8bb0\u5bc6\u7801?", None))
        self.msg_label.setText("")
        self.btn_login.setText(QCoreApplication.translate("loginWidget", u"\u767b\u5f55", None))
        self.bottom_problem.setText(
            QCoreApplication.translate("loginWidget", u"\u767b\u5f55\u9047\u5230\u95ee\u9898\uff1f", None))
        self.bottom_account.setText(QCoreApplication.translate("loginWidget", u"\u6ca1\u6709\u8d26\u53f7\uff1f", None))
        self.btn_register.setText(QCoreApplication.translate("loginWidget", u"\u7acb\u5373\u6ce8\u518c", None))
        self.label_1.setText(QCoreApplication.translate("loginWidget", u"\u767b\u5f55\u5373\u540c\u610f", None))
        self.btn_userAgreement.setText(
            QCoreApplication.translate("loginWidget", u"\u300a\u7528\u6237\u534f\u8bae\u300b", None))
        self.label_2.setText(QCoreApplication.translate("loginWidget", u"\u53ca", None))
        self.btn_privacyAgreement.setText(
            QCoreApplication.translate("loginWidget", u"\u300a\u9690\u79c1\u534f\u8bae\u300b", None))
    # retranslateUi
