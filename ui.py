# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'req.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(865, 644)
        self.verticalLayout_4 = QVBoxLayout(main)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.method_list = QComboBox(main)
        self.method_list.addItem("")
        self.method_list.addItem("")
        self.method_list.addItem("")
        self.method_list.addItem("")
        self.method_list.setObjectName(u"method_list")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_list.sizePolicy().hasHeightForWidth())
        self.method_list.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.method_list.setFont(font)

        self.horizontalLayout.addWidget(self.method_list)

        self.lineEdit = QLineEdit(main)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(14)
        self.lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.choose_1 = QPushButton(main)
        self.choose_1.setObjectName(u"choose_1")
        self.choose_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.choose_1)

        self.save_1 = QPushButton(main)
        self.save_1.setObjectName(u"save_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_1.sizePolicy().hasHeightForWidth())
        self.save_1.setSizePolicy(sizePolicy1)
        self.save_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.save_1)

        self.lineEdit_2 = QLineEdit(main)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.choose_2 = QPushButton(main)
        self.choose_2.setObjectName(u"choose_2")
        sizePolicy1.setHeightForWidth(self.choose_2.sizePolicy().hasHeightForWidth())
        self.choose_2.setSizePolicy(sizePolicy1)
        self.choose_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.choose_2)

        self.save_2s = QPushButton(main)
        self.save_2s.setObjectName(u"save_2s")
        self.save_2s.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.save_2s)

        self.pushButton = QPushButton(main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(4, 5)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 9, -1)
        self.label = QLabel(main)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_2 = QPushButton(main)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.pushButton_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(main)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(main)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.line = QFrame(main)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(main)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(18)
        self.label_2.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.checkBox = QCheckBox(main)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_5.addWidget(self.checkBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.textEdit = QTextEdit(main)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(main)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textBrowser = QTextBrowser(main)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_6.addWidget(self.textBrowser)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.resbodylabel = QLabel(main)
        self.resbodylabel.setObjectName(u"resbodylabel")
        self.resbodylabel.setFont(font3)

        self.verticalLayout_3.addWidget(self.resbodylabel)

        self.res_body = QTextBrowser(main)
        self.res_body.setObjectName(u"res_body")

        self.verticalLayout_3.addWidget(self.res_body)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_4 = QPushButton(main)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButton_4.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"http\u8bf7\u6c42", None))
        self.method_list.setItemText(0, QCoreApplication.translate("main", u"GET", None))
        self.method_list.setItemText(1, QCoreApplication.translate("main", u"POST", None))
        self.method_list.setItemText(2, QCoreApplication.translate("main", u"DELETE", None))
        self.method_list.setItemText(3, QCoreApplication.translate("main", u"PUT", None))

        self.lineEdit.setPlaceholderText(QCoreApplication.translate("main", u"\u8bf7\u8f93\u5165URL", None))
        self.choose_1.setText(QCoreApplication.translate("main", u"\u9009\u62e9", None))
        self.save_1.setText(QCoreApplication.translate("main", u"\u4fdd\u5b58", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("main", u"\u8f93\u5165\u7aef\u70b9", None))
        self.choose_2.setText(QCoreApplication.translate("main", u"\u9009\u62e9", None))
        self.save_2s.setText(QCoreApplication.translate("main", u"\u4fdd\u5b58", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"\u53d1\u9001\u8bf7\u6c42", None))
        self.label.setText(QCoreApplication.translate("main", u"Header", None))
        self.pushButton_2.setText(QCoreApplication.translate("main", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("main", u"-", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main", u"value", None));
        self.label_2.setText(QCoreApplication.translate("main", u"Request Body", None))
        self.checkBox.setText(QCoreApplication.translate("main", u"Send/No", None))
        self.resbodylabel.setText(QCoreApplication.translate("main", u"Response Body", None))
        self.pushButton_4.setText(QCoreApplication.translate("main", u"Clear", None))
    # retranslateUi

