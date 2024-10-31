# -*- coding: utf-8 -*-

from classes.function import calculate_function
from classes.triang import create_sides_array
from classes.max import calculate_max

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(760, 479)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-30, 10, 781, 481))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 10, 331, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.btnRun = QPushButton(self.tab)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(290, 70, 121, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.btnRun.setFont(font1)
        self.txtResult = QTextEdit(self.tab)
        self.txtResult.setObjectName(u"txtResult")
        self.txtResult.setGeometry(QRect(120, 150, 481, 241))
        self.txtResult.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lblNotes = QLabel(self.tab_3)
        self.lblNotes.setObjectName(u"lblNotes")
        self.lblNotes.setGeometry(QRect(310, 20, 121, 41))
        self.lblNotes.setFont(font)
        self.btnRunNotes = QPushButton(self.tab_3)
        self.btnRunNotes.setObjectName(u"btnRunNotes")
        self.btnRunNotes.setGeometry(QRect(300, 80, 121, 51))
        self.btnRunNotes.setFont(font1)
        self.txtResultNotes = QTextEdit(self.tab_3)
        self.txtResultNotes.setObjectName(u"txtResultNotes")
        self.txtResultNotes.setGeometry(QRect(120, 190, 481, 161))
        self.txtResultNotes.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.btnRunCoins = QPushButton(self.tab_2)
        self.btnRunCoins.setObjectName(u"btnRunCoins")
        self.btnRunCoins.setGeometry(QRect(610, 320, 121, 51))
        self.btnRunCoins.setFont(font1)
        self.lblNotes_2 = QLabel(self.tab_2)
        self.lblNotes_2.setObjectName(u"lblNotes_2")
        self.lblNotes_2.setGeometry(QRect(220, 20, 321, 41))
        self.lblNotes_2.setFont(font)
        self.txtFirst = QTextEdit(self.tab_2)
        self.txtFirst.setObjectName(u"txtFirst")
        self.txtFirst.setGeometry(QRect(160, 90, 481, 41))
        self.txtFirst.setFont(font1)
        self.txtResultCoins = QTextEdit(self.tab_2)
        self.txtResultCoins.setObjectName(u"txtResultCoins")
        self.txtResultCoins.setGeometry(QRect(90, 230, 481, 161))
        self.txtResultCoins.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)

        self.btnRun.clicked.connect(self.run_function)
        self.btnRunNotes.clicked.connect(self.run_triang)
        self.btnRunCoins.clicked.connect(self.run_max)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0447\u0451\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.btnRun.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.lblNotes.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u0440\u043e\u043d\u044b", None))
        self.btnRunNotes.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u0440\u043e\u043d\u044b", None))
        self.btnRunCoins.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.lblNotes_2.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.txtFirst.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043f\u0438\u0441\u043e\u043a \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Max", None))
    # retranslateUi
    def run_function(self):
        array = calculate_function()
        self.txtResult.setText(str(array))

    def run_triang(self):
        array = create_sides_array()
        self.txtResultNotes.setText(str(array))

    def run_max(self):
        array = calculate_max([int(i) for i in self.txtFirst.toPlainText().split(' ')])
        self.txtResultCoins.setText(str(array))