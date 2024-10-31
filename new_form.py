from venv import create

from classes.function import calculate_function
from classes.triang import create_sides_array
from classes.max import calculate_max

# -*- coding: utf-8 -*-

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
    QPalette, QPixmap, QRadialGradient, QTransform,)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QTextEdit, QWidget, QDialogButtonBox, QVBoxLayout, QDialog)

from notes import create_two_dimensional_array


class AlertBox(QDialog):
    def __init__(self, error):
        super().__init__()
        self.setWindowTitle("Ошибка!")

        q_btn = QDialogButtonBox.StandardButton.Ok
        self.button_box = QDialogButtonBox(q_btn)
        self.button_box.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message = QLabel(error)
        layout.addWidget(message)
        layout.addWidget(self.button_box)
        self.setLayout(layout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(760, 479)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-10, 30, 781, 481))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.txtCount = QTextEdit(self.tab)
        self.txtCount.setObjectName(u"txtCount")
        self.txtCount.setGeometry(QRect(120, 260, 481, 41))
        font = QFont()
        font.setPointSize(14)
        self.txtCount.setFont(font)
        self.txtMinWide = QTextEdit(self.tab)
        self.txtMinWide.setObjectName(u"txtMinWide")
        self.txtMinWide.setGeometry(QRect(120, 160, 481, 41))
        self.txtMinWide.setFont(font)
        self.txtMaxWide = QTextEdit(self.tab)
        self.txtMaxWide.setObjectName(u"txtMaxWide")
        self.txtMaxWide.setGeometry(QRect(120, 210, 481, 41))
        self.txtMaxWide.setFont(font)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 10, 121, 41))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.label.setFont(font1)
        self.txtMinLength = QTextEdit(self.tab)
        self.txtMinLength.setObjectName(u"txtMinLength")
        self.txtMinLength.setGeometry(QRect(120, 60, 481, 41))
        self.txtMinLength.setFont(font)
        self.txtMaxLength = QTextEdit(self.tab)
        self.txtMaxLength.setObjectName(u"txtMaxLength")
        self.txtMaxLength.setGeometry(QRect(120, 110, 481, 41))
        self.txtMaxLength.setFont(font)
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(120, 310, 231, 20))
        self.checkBox.setFont(font)
        self.btnRun = QPushButton(self.tab)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(630, 370, 121, 51))
        self.btnRun.setFont(font)
        self.txtResult = QTextEdit(self.tab)
        self.txtResult.setObjectName(u"txtResult")
        self.txtResult.setGeometry(QRect(120, 350, 481, 64))
        self.txtResult.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lblNotes = QLabel(self.tab_3)
        self.lblNotes.setObjectName(u"lblNotes")
        self.lblNotes.setGeometry(QRect(310, 20, 121, 41))
        self.lblNotes.setFont(font1)
        self.txtA = QTextEdit(self.tab_3)
        self.txtA.setObjectName(u"txtA")
        self.txtA.setGeometry(QRect(130, 140, 481, 41))
        self.txtA.setFont(font)
        self.txtMinLength_2 = QTextEdit(self.tab_3)
        self.txtMinLength_2.setObjectName(u"txtMinLength_2")
        self.txtMinLength_2.setGeometry(QRect(130, 90, 481, 41))
        self.txtMinLength_2.setFont(font)
        self.txtB = QTextEdit(self.tab_3)
        self.txtB.setObjectName(u"txtB")
        self.txtB.setGeometry(QRect(130, 190, 481, 41))
        self.txtB.setFont(font)
        self.btnRunNotes = QPushButton(self.tab_3)
        self.btnRunNotes.setObjectName(u"btnRunNotes")
        self.btnRunNotes.setGeometry(QRect(600, 320, 121, 51))
        self.btnRunNotes.setFont(font)
        self.txtResultNotes = QTextEdit(self.tab_3)
        self.txtResultNotes.setObjectName(u"txtResultNotes")
        self.txtResultNotes.setGeometry(QRect(100, 250, 481, 161))
        self.txtResultNotes.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.btnRunCoins = QPushButton(self.tab_2)
        self.btnRunCoins.setObjectName(u"btnRunCoins")
        self.btnRunCoins.setGeometry(QRect(610, 320, 121, 51))
        self.btnRunCoins.setFont(font)
        self.lblNotes_2 = QLabel(self.tab_2)
        self.lblNotes_2.setObjectName(u"lblNotes_2")
        self.lblNotes_2.setGeometry(QRect(320, 20, 121, 41))
        self.lblNotes_2.setFont(font1)
        self.txtFirst = QTextEdit(self.tab_2)
        self.txtFirst.setObjectName(u"txtFirst")
        self.txtFirst.setGeometry(QRect(160, 90, 481, 41))
        self.txtFirst.setFont(font)
        self.txtSecond = QTextEdit(self.tab_2)
        self.txtSecond.setObjectName(u"txtSecond")
        self.txtSecond.setGeometry(QRect(160, 150, 481, 41))
        self.txtSecond.setFont(font)
        self.txtResultCoins = QTextEdit(self.tab_2)
        self.txtResultCoins.setObjectName(u"txtResultCoins")
        self.txtResultCoins.setGeometry(QRect(90, 230, 481, 161))
        self.txtResultCoins.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)

        self.checkBox.stateChanged.connect(self.checkbox_changed)
        self.btnRun.clicked.connect(self.btnRun_click)
        self.btnRunNotes.clicked.connect(self.btnRunNotes_click)
        self.btnRunCoins.clicked.connect(self.btnRunCoins_click)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txtCount.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u044b\u0432\u043e\u0434\u0438\u043c\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.txtMinWide.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0443\u044e \u0448\u0438\u0440\u0438\u043d\u0443", None))
        self.txtMaxWide.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0443\u044e \u0448\u0438\u0440\u0438\u043d\u0443", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u043b\u043e\u0449\u0430\u0434\u0438", None))
        self.txtMinLength.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0443\u044e \u0434\u043b\u0438\u043d\u0443", None))
        self.txtMaxLength.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0443\u044e \u0434\u043b\u0438\u043d\u0443", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.btnRun.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u041f\u043b\u043e\u0449\u0430\u0434\u0438", None))
        self.lblNotes.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0442\u044b", None))
        self.txtA.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a", None))
        self.txtMinLength_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u043b\u0438\u043d\u0443 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.txtB.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432", None))
        self.btnRunNotes.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u041d\u043e\u0442\u044b", None))
        self.btnRunCoins.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u043d\u0435\u0442\u043a\u0438", None))
        self.lblNotes_2.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u043d\u0435\u0442\u043a\u0438", None))
        self.txtFirst.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.txtSecond.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u043e\u0439 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u041c\u043e\u043d\u0435\u0442\u043a\u0438", None))
    # retranslateUi

    def checkbox_changed(self, state):
        if state == 2:
            self.txtMinLength.setReadOnly(True)
            self.txtMaxLength.setReadOnly(True)
            self.txtMinWide.setReadOnly(True)
            self.txtMaxWide.setReadOnly(True)
            self.txtCount.setReadOnly(True)
        else:
            self.txtMinLength.setReadOnly(False)
            self.txtMaxLength.setReadOnly(False)
            self.txtMinWide.setReadOnly(False)
            self.txtMaxWide.setReadOnly(False)
            self.txtCount.setReadOnly(False)

    def btnRun_click(self):
        squares = None
        if self.checkBox.isChecked():
            squares = calculate_squares()
        else:
            try:
                min_length = int(self.txtMinLength.toPlainText())
                max_length = int(self.txtMaxLength.toPlainText())
                min_wide = int(self.txtMinWide.toPlainText())
                max_wide = int(self.txtMaxWide.toPlainText())
                count = int(self.txtCount.toPlainText())
                if min_length <= 0 or max_length <= 0 or min_wide <= 0 or max_wide <= 0 or count <= 0:
                    raise Exception("Отрицательное число!")
                if min_length > max_length or min_wide > max_wide:
                    raise Exception("Максимальное меньше минимального!")
            except Exception as error:
                dlg = AlertBox(str(error))
                dlg.exec()
                return
            squares = calculate_squares(min_length, max_length, min_wide, max_wide, count)

        self.txtResult.setText(str(squares))

    def btnRunNotes_click(self):
        try:
            n = int(self.txtMinLength_2.toPlainText())
            a = int(self.txtA.toPlainText())
            b = int(self.txtB.toPlainText())
            if n <= 0 or a <= 0 or b <= 0:
                raise Exception("Отрицательное число!")
            if a > b:
                raise Exception("Максимальное меньше минимального!")
        except Exception as error:
            dlg = AlertBox(str(error))
            dlg.exec()
            return

        array = create_two_dimensional_array(n, a, b)
        self.txtResultNotes.setText(str(array))

    def btnRunCoins_click(self):
        try:
            first = [int(x) for x in self.txtFirst.toPlainText().split(" ")]
            second = [int(x) for x in self.txtSecond.toPlainText().split(" ")]
            if any(num <= 0 for num in first) or any(num <= 0 for num in second):
                raise Exception("Отрицательные числа")
        except Exception as error:
            dlg = AlertBox(str(error))
            dlg.exec()
            return
        self.txtResultCoins.setText(str(calculate_result(first, second)))


