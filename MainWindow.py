# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget, QFileDialog,QListWidgetItem)
from historyPage import Ui_Form
from total import Ui_total
import sys
from Img_operation import *
import json
import time
from data_collect import *


class MainWindow(object):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.MainForm = None
        self.Form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.current_product = None
        self.count = 0
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.MainForm = Form
        Form.resize(830, 652)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 51, 541, 491))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 551, 511))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(599, 49, 960, 680))
        self.frame_2.setMinimumSize(QSize(960, 680))
        self.frame_2.setMaximumSize(QSize(960, 680))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-20, 230, 401, 20))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(56, 320, 121, 191))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # 添加按钮
        self.btn_import = QPushButton(self.layoutWidget)
        self.btn_import.setObjectName(u"btn_import")
        self.verticalLayout.addWidget(self.btn_import)

        self.btn_pre = QPushButton(self.layoutWidget)
        self.btn_pre.setObjectName(u"btn_pre")
        self.verticalLayout.addWidget(self.btn_pre)

        self.btn_connect = QPushButton(self.layoutWidget)
        self.btn_connect.setObjectName(u"btn_connect")
        self.verticalLayout.addWidget(self.btn_connect)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.layoutWidget1 = QWidget(self.frame_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 60, 191, 83))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 600, 821, 43))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit_5 = QLineEdit(self.frame_3)
        self.lineEdit_5.setStyleSheet("font size: 20px")
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_4.addWidget(self.lineEdit_5)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(210, 10, 341, 21))
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(580, 50, 20, 531))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 570, 821, 20))
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.btn_connect.clicked.connect(self.connect_next_page)
        self.pushButton_2.clicked.connect(self.connect_total_page)
        self.btn_import.clicked.connect(self.import_picture)
        self.btn_pre.clicked.connect(self.pre_process_image)
        self.ui.btn_org.clicked.connect(self.show_org)
        self.ui.pushButton_2.clicked.connect(self.current_item)

        # 设置文本颜色
        palette = QPalette()
        text_color = QColor(255, 0, 0)  # 设置文本颜色为红色
        palette.setColor(QPalette.ColorRole.Text, text_color)
        self.lineEdit_5.setPalette(palette)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle('主界面')
        self.label_5.setText("")
        self.btn_import.setText('导入图片')
        self.btn_pre.setText('处理图片')
        self.btn_connect.setText('历史图片')
        self.pushButton_2.setText('统计')
        self.label_4.setText('当前年份')
        self.lineEdit_3.setText(time.strftime('%Y', time.localtime()))
        self.label_3.setText('当前月份')
        self.lineEdit_2.setText(time.strftime('%m-%d', time.localtime()))
        self.label_2.setText('当前时间')
        self.lineEdit.setText(time.strftime('%H-%M', time.localtime()))
        self.label.setText('产品信息')
        self.lineEdit_4.setText('烟箱品牌视觉分拣系统')

    # retranslateUi

    def connect_next_page(self):
        self.Form.show()
        self.HideWindow()
        self.ui.btn_back.clicked.connect(self.ShowWindow)


    def connect_total_page(self):
        self.Form1 = QWidget()
        self.ui1 = Ui_total()
        self.ui1.setupUi(self.Form1)
        self.Form1.show()

    def HideWindow(self):
        self.MainForm.hide()

    def ShowWindow(self):
        self.MainForm.show()
        self.ui.SubForm.hide()

    def import_picture(self):
        self.file_name, _ = QFileDialog.getOpenFileName(None, "选择图片文件", "", "*.jpg *.jpeg *.png *.bmp")
        if self.file_name:
            print(self.file_name)
            self.name = get_filepath_Name(self.file_name)
            self.current_product=self.name
            pixmap = QPixmap(self.file_name)
            self.label_5.setPixmap(pixmap)
            self.label_5.setScaledContents(True)
            self.label_5.setAlignment(Qt.AlignCenter)
            QListWidgetItem(self.ui.listWidget)
            ___qlistwidgetitem = self.ui.listWidget.item(self.count)
            ___qlistwidgetitem.setText(self.name)
            self.count += 1
    def show_product_info(self, file_name):

        # self.pix = preprocess_image(file_name)
        # self.pix = img_rotate(self.pix,90)
        self.pix = Image.open(file_name)
        content = pytesseract.image_to_string(self.pix, lang='eng',
                                              config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789').splitlines()
        if content[0]:
            info = get_product_name(content[0])
            self.lineEdit_5.setText(info)
        else:
            print("Can't Recognize the information")

    def pre_process_image(self):
        self.pre_img = preprocess_image(self.file_name)
        new_path = f'process_img/+{format(self.name)}.jpg'
        Image.fromarray(self.pre_img).save(new_path)
        pixmap = QPixmap(new_path)
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.show_product_info(new_path)

    def show_current_time(self):
        self.lineEdit.setText(time.strftime('%H:%M:%S', time.localtime()))

    def show_org(self):
        pixmap = QPixmap(self.file_name)
        self.ui.label_8.setPixmap(pixmap)
        self.ui.label_8.setScaledContents(True)
        self.ui.label_8.setAlignment(Qt.AlignCenter)
    def current_item(self):
        print("f{当前产品：self.current_product}",self.current_product)
def get_product_name(id):
    json_data = json.load(open('info.json', 'r', encoding='utf-8'))
    if json_data:
        for data in json_data:
            if data['id'] == id:
                return data['info']
    else:
        return "缺省产品"


def main():
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
