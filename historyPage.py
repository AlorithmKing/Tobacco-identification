# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historyPageWsuGrh.ui'
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
                               QLabel, QListWidget, QListWidgetItem, QPushButton,
                               QSizePolicy, QWidget)


class Ui_Form(object):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.SubForm = None

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.SubForm = Form
        Form.resize(792, 594)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(520, 40, 271, 461))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 81, 16))
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 60, 261, 151))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.com_date = QComboBox(self.frame_5)
        self.com_date.addItem("")
        self.com_date.setObjectName(u"com_date")

        self.gridLayout.addWidget(self.com_date, 2, 1, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.com_range = QComboBox(self.frame_5)
        self.com_range.addItem("")
        self.com_range.addItem("")
        self.com_range.addItem("")
        self.com_range.setObjectName(u"com_range")

        self.gridLayout.addWidget(self.com_range, 2, 3, 1, 1)

        self.com_year = QComboBox(self.frame_5)
        self.com_year.addItem("")
        self.com_year.addItem("")
        self.com_year.addItem("")
        self.com_year.setObjectName(u"com_year")

        self.gridLayout.addWidget(self.com_year, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.com_ids = QComboBox(self.frame_5)
        self.com_ids.addItem("")
        self.com_ids.addItem("")
        self.com_ids.addItem("")
        self.com_ids.addItem("")
        self.com_ids.addItem("")
        self.com_ids.setObjectName(u"com_ids")

        self.gridLayout.addWidget(self.com_ids, 3, 1, 1, 1)

        self.com_month = QComboBox(self.frame_5)
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.addItem("")
        self.com_month.setObjectName(u"com_month")

        self.gridLayout.addWidget(self.com_month, 0, 3, 1, 1)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-63, 260, 361, 20))
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 230, 75, 23))
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 230, 75, 23))
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(9, 279, 261, 201))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listWidget = QListWidget(self.frame_6)
        # QListWidgetItem(self.listWidget)
        # QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 1)

        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(20, 20, 75, 23))
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 460, 501, 43))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_spec = QPushButton(self.frame_3)
        self.btn_spec.setObjectName(u"btn_spec")

        self.gridLayout_2.addWidget(self.btn_spec, 0, 2, 1, 1)

        self.btn_nan = QPushButton(self.frame_3)
        self.btn_nan.setObjectName(u"btn_nan")

        self.gridLayout_2.addWidget(self.btn_nan, 0, 1, 1, 1)

        self.btn_org = QPushButton(self.frame_3)
        self.btn_org.setObjectName(u"btn_org")

        self.gridLayout_2.addWidget(self.btn_org, 0, 3, 1, 1)

        self.btn_history = QPushButton(self.frame_3)
        self.btn_history.setObjectName(u"btn_history")

        self.gridLayout_2.addWidget(self.btn_history, 0, 0, 1, 1)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 540, 701, 41))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 71, 16))
        self.lbl_hproInfo = QLabel(self.frame_4)
        self.lbl_hproInfo.setObjectName(u"lbl_hproInfo")
        self.lbl_hproInfo.setGeometry(QRect(100, 10, 591, 16))
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(510, 20, 20, 501))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 510, 791, 20))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(19, 49, 491, 401))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 440, 521, 20))
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(240, 30, 53, 15))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle('图片管理')
        self.label.setText('选择历史图片')
        self.label_6.setText('品牌编号')
        self.label_5.setText('班次')
        self.com_date.setItemText(0, '12月24日')

        self.label_2.setText('年份')
        self.com_range.setItemText(0, '1')
        self.com_range.setItemText(1, '2')
        self.com_range.setItemText(2, '3')

        self.com_year.setItemText(0, '2011')
        self.com_year.setItemText(1, '2012')
        self.com_year.setItemText(2, '2013')

        self.label_4.setText('日期')
        self.com_ids.setItemText(0, '1')
        self.com_ids.setItemText(1, '02202')
        self.com_ids.setItemText(2, '02180')
        self.com_ids.setItemText(3, '02179')
        self.com_ids.setItemText(4, '02162')

        self.com_month.setItemText(0, '1')
        self.com_month.setItemText(1, '2')
        self.com_month.setItemText(2, '3')
        self.com_month.setItemText(3, '4')
        self.com_month.setItemText(4, '5')
        self.com_month.setItemText(5, '6')
        self.com_month.setItemText(6, '7')
        self.com_month.setItemText(7, '8')
        self.com_month.setItemText(8, '9')
        self.com_month.setItemText(9, '10')
        self.com_month.setItemText(10, '11')
        self.com_month.setItemText(11, '12')

        self.pushButton.setText('搜索')
        self.pushButton_2.setText('当前班次')

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.btn_back.setText('回退')
        self.btn_spec.setText('特殊班次')
        self.btn_nan.setText('缺省班次')
        self.btn_org.setText('浏览原图')
        self.btn_history.setText('历史图片')
        self.label_7.setText('产品信息：')
        self.lbl_hproInfo.setText("")
        self.label_8.setText("")
        self.label_9.setText('历史图片')
        # 设置标签项的选中样式
        selected_style = '''
            QLabel {
                background-color: blue;
                color: red;
                font-weight: bold;
            }
        '''
        self.listWidget.setStyleSheet(selected_style)

    # retranslateUi

    def connect_next_page(self):
        self.Form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.HideWindow()
        self.ui.btn_back.clicked.connect(self.ShowWindow)

    def HideWindow(self):
        self.MainForm.hide()

    def ShowWindow(self):
        self.MainForm.show()
        self.ui.SubForm.hide()
