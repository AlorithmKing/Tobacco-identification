# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'totalNQOmsF.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class Ui_total(object):
    def __init__(self):
        super(Ui_total, self).__init__()
        self.Total_Form = None

    def setupUi(self, total):
        if not total.objectName():
            total.setObjectName(u"total")
        self.Total_Form = total
        total.resize(458, 308)
        self.line = QFrame(total)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 240, 461, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(total)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 260, 321, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.layoutWidget1 = QWidget(total)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 70, 343, 85))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.layoutWidget1)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(self.layoutWidget1)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout.addWidget(self.comboBox_3)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.comboBox_4 = QComboBox(self.layoutWidget1)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_2.addWidget(self.comboBox_4)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.comboBox_5 = QComboBox(self.layoutWidget1)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_2.addWidget(self.comboBox_5)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.comboBox_6 = QComboBox(self.layoutWidget1)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_2.addWidget(self.comboBox_6)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.comboBox_7 = QComboBox(self.layoutWidget1)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_3.addWidget(self.comboBox_7)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.lineEdit = QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(total)

        QMetaObject.connectSlotsByName(total)
        self.pushButton_2.clicked.connect(total.close)

    # setupUi

    def retranslateUi(self, total):
        total.setWindowTitle('统计界面')
        self.pushButton.setText('统计')
        self.pushButton_2.setText('退出')
        self.label.setText('从')
        self.comboBox.setItemText(0, '2011')
        self.comboBox.setItemText(1, '2012')
        self.comboBox.setItemText(2, '2013')

        self.label_2.setText('年')
        self.comboBox_2.setItemText(0, '1')
        self.comboBox_2.setItemText(1, '2')
        self.comboBox_2.setItemText(2, '3')
        self.comboBox_2.setItemText(3, '4')
        self.comboBox_2.setItemText(4, '5')
        self.comboBox_2.setItemText(5, '6')
        self.comboBox_2.setItemText(6, '7')
        self.comboBox_2.setItemText(7, '8')
        self.comboBox_2.setItemText(8, '9')
        self.comboBox_2.setItemText(9, '10')
        self.comboBox_2.setItemText(10, '11')
        self.comboBox_2.setItemText(11, '12')

        self.label_3.setText('月')
        self.comboBox_3.setItemText(0, '1')
        self.comboBox_3.setItemText(1, '2')
        self.comboBox_3.setItemText(2, '3')
        self.comboBox_3.setItemText(3, '4')
        self.comboBox_3.setItemText(4, '5')
        self.comboBox_3.setItemText(5, '6')
        self.comboBox_3.setItemText(6, '7')
        self.comboBox_3.setItemText(7, '8')
        self.comboBox_3.setItemText(8, '9')
        self.comboBox_3.setItemText(9, '10')
        self.comboBox_3.setItemText(10, '11')
        self.comboBox_3.setItemText(11, '12')
        self.comboBox_3.setItemText(12, '13')
        self.comboBox_3.setItemText(13, '14')
        self.comboBox_3.setItemText(14, '15')
        self.comboBox_3.setItemText(15, '16')
        self.comboBox_3.setItemText(16, '17')
        self.comboBox_3.setItemText(17, '18')
        self.comboBox_3.setItemText(18, '19')
        self.comboBox_3.setItemText(19, '20')
        self.comboBox_3.setItemText(20, '21')
        self.comboBox_3.setItemText(21, '22')
        self.comboBox_3.setItemText(22, '23')
        self.comboBox_3.setItemText(23, '24')
        self.comboBox_3.setItemText(24, '25')
        self.comboBox_3.setItemText(25, '26')
        self.comboBox_3.setItemText(26, '27')
        self.comboBox_3.setItemText(27, '28')
        self.comboBox_3.setItemText(28, '29')
        self.comboBox_3.setItemText(29, '30')
        self.comboBox_3.setItemText(30, '31')

        self.label_4.setText('日')
        self.label_5.setText('到')
        self.comboBox_4.setItemText(0, '2011')
        self.comboBox_4.setItemText(1, '2012')
        self.comboBox_4.setItemText(2, '2013')

        self.label_6.setText('年')
        self.comboBox_5.setItemText(0, '1')
        self.comboBox_5.setItemText(1, '2')
        self.comboBox_5.setItemText(2, '3')
        self.comboBox_5.setItemText(3, '4')
        self.comboBox_5.setItemText(4, '5')
        self.comboBox_5.setItemText(5, '6')
        self.comboBox_5.setItemText(6, '7')
        self.comboBox_5.setItemText(7, '8')
        self.comboBox_5.setItemText(8, '9')
        self.comboBox_5.setItemText(9, '10')
        self.comboBox_5.setItemText(10, '11')
        self.comboBox_5.setItemText(11, '12')

        self.label_7.setText('月')
        self.comboBox_6.setItemText(0, '1')
        self.comboBox_6.setItemText(1, '2')
        self.comboBox_6.setItemText(2, '3')
        self.comboBox_6.setItemText(3, '4')
        self.comboBox_6.setItemText(4, '5')
        self.comboBox_6.setItemText(5, '6')
        self.comboBox_6.setItemText(6, '7')
        self.comboBox_6.setItemText(7, '8')
        self.comboBox_6.setItemText(8, '9')
        self.comboBox_6.setItemText(9, '10')
        self.comboBox_6.setItemText(10, '11')
        self.comboBox_6.setItemText(11, '12')
        self.comboBox_6.setItemText(12, '13')
        self.comboBox_6.setItemText(13, '14')
        self.comboBox_6.setItemText(14, '15')
        self.comboBox_6.setItemText(15, '16')
        self.comboBox_6.setItemText(16, '17')
        self.comboBox_6.setItemText(17, '18')
        self.comboBox_6.setItemText(18, '19')
        self.comboBox_6.setItemText(19, '20')
        self.comboBox_6.setItemText(20, '21')
        self.comboBox_6.setItemText(21, '22')
        self.comboBox_6.setItemText(22, '23')
        self.comboBox_6.setItemText(23, '24')
        self.comboBox_6.setItemText(24, '25')
        self.comboBox_6.setItemText(25, '26')
        self.comboBox_6.setItemText(26, '27')
        self.comboBox_6.setItemText(27, '28')
        self.comboBox_6.setItemText(28, '29')
        self.comboBox_6.setItemText(29, '30')
        self.comboBox_6.setItemText(30, '31')

        self.label_8.setText('日')
        self.label_9.setText('品牌')
        self.comboBox_7.setItemText(0, '06103')
        self.comboBox_7.setItemText(1, '02202')
        self.comboBox_7.setItemText(2, '02180')
        self.comboBox_7.setItemText(3, '02179')
        self.comboBox_7.setItemText(4, '02162')

        self.label_10.setText('数量')
        self.label_11.setText('箱')

    # retranslateUi

    def close_event(self):
        self.Total_Form.close()
