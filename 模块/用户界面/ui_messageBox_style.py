# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messageBoxRzALRu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from modules.ui.ui_resources_rc import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(560, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                 "border-radius:5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.frame)
        self.top.setObjectName(u"top")
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.top)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        self.label.setMaximumSize(QSize(16777215, 70))
        self.label.setStyleSheet(u"font:14pt \"Microsoft YaHei UI\";\n"
                                 "margin-left:10px solid transparent;")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addWidget(self.top)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"margin-left:10px solid transparent;\n"
                                   "font: 12pt \"Microsoft YaHei UI\";")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setStyleSheet(u"margin-left:10px solid transparent;\n"
                                   "font: 12pt \"Microsoft YaHei UI\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.spacer = QLabel(self.frame)
        self.spacer.setObjectName(u"spacer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spacer.sizePolicy().hasHeightForWidth())
        self.spacer.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.spacer)

        self.bottom = QFrame(self.frame)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 70))
        self.bottom.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.bottom)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 36))
        self.pushButton.setMaximumSize(QSize(16777215, 36))
        self.pushButton.setStyleSheet(u"background-color: rgb(66, 139, 202);\n"
                                      "font: 14pt \"Microsoft YaHei UI\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "margin-left:10px solid transparent;\n"
                                      "padding-left:10px solid transparent;\n"
                                      "padding-right:10px solid transparent;\n"
                                      "border:none;")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.bottom)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 36))
        self.pushButton_2.setMaximumSize(QSize(16777215, 36))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
                                        "font: 14pt \"Microsoft YaHei UI\";\n"
                                        "margin-left:5px solid transparent;\n"
                                        "padding-left:10px solid transparent;\n"
                                        "padding-right:10px solid transparent;\n"
                                        "border:none;")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.spacer_2 = QLabel(self.bottom)
        self.spacer_2.setObjectName(u"spacer_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spacer_2.sizePolicy().hasHeightForWidth())
        self.spacer_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.spacer_2)

        self.pushButton_3 = QPushButton(self.bottom)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 36))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
                                        "font: 14pt \"Microsoft YaHei UI\";\n"
                                        "border:none;\n"
                                        "padding-left:10px solid transparent;\n"
                                        "padding-right:10px solid transparent;\n"
                                        "margin-right:10px solid transparent;")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.verticalLayout_2.addWidget(self.bottom)

        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u662f\u5426\u4fdd\u5b58\u66f4\u6539\uff1f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog",
                                                        u"\u5982\u679c\u4e0d\u4fdd\u5b58\uff0c\u60a8\u7684\u66f4\u6539\u5c06\u4f1a\u4e22\u5931\u3002",
                                                        None))
        self.spacer.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u4e22\u5f03", None))
        self.spacer_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi
