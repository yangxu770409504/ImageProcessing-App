# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_sub_window_4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1269, 752)
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(30, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_image_2 = QtWidgets.QLabel(Form)
        self.label_image_2.setGeometry(QtCore.QRect(740, 10, 480, 480))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_image_2.setFont(font)
        self.label_image_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_image_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_image_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_2.setObjectName("label_image_2")
        self.pushButton_open_file = QtWidgets.QPushButton(Form)
        self.pushButton_open_file.setGeometry(QtCore.QRect(40, 90, 111, 28))
        self.pushButton_open_file.setCheckable(False)
        self.pushButton_open_file.setDefault(True)
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.groupBox_sobel_filter = QtWidgets.QGroupBox(Form)
        self.groupBox_sobel_filter.setGeometry(QtCore.QRect(10, 230, 171, 151))
        self.groupBox_sobel_filter.setObjectName("groupBox_sobel_filter")
        self.pushButton_sobel_filter = QtWidgets.QPushButton(self.groupBox_sobel_filter)
        self.pushButton_sobel_filter.setGeometry(QtCore.QRect(40, 110, 93, 28))
        self.pushButton_sobel_filter.setObjectName("pushButton_sobel_filter")
        self.radioButton_sobel_dx = QtWidgets.QRadioButton(self.groupBox_sobel_filter)
        self.radioButton_sobel_dx.setGeometry(QtCore.QRect(30, 20, 121, 19))
        self.radioButton_sobel_dx.setObjectName("radioButton_sobel_dx")
        self.radioButton_sobel_dy = QtWidgets.QRadioButton(self.groupBox_sobel_filter)
        self.radioButton_sobel_dy.setGeometry(QtCore.QRect(30, 50, 121, 19))
        self.radioButton_sobel_dy.setObjectName("radioButton_sobel_dy")
        self.radioButton_sobel_dx_dy = QtWidgets.QRadioButton(self.groupBox_sobel_filter)
        self.radioButton_sobel_dx_dy.setGeometry(QtCore.QRect(30, 80, 121, 19))
        self.radioButton_sobel_dx_dy.setObjectName("radioButton_sobel_dx_dy")
        self.groupBox_laplace_filter = QtWidgets.QGroupBox(Form)
        self.groupBox_laplace_filter.setGeometry(QtCore.QRect(10, 400, 171, 111))
        self.groupBox_laplace_filter.setObjectName("groupBox_laplace_filter")
        self.pushButton_laplace_filter = QtWidgets.QPushButton(self.groupBox_laplace_filter)
        self.pushButton_laplace_filter.setGeometry(QtCore.QRect(40, 60, 93, 28))
        self.pushButton_laplace_filter.setObjectName("pushButton_laplace_filter")
        self.spinBox_laplace_ksize = QtWidgets.QSpinBox(self.groupBox_laplace_filter)
        self.spinBox_laplace_ksize.setGeometry(QtCore.QRect(100, 30, 46, 22))
        self.spinBox_laplace_ksize.setMinimum(1)
        self.spinBox_laplace_ksize.setSingleStep(2)
        self.spinBox_laplace_ksize.setProperty("value", 1)
        self.spinBox_laplace_ksize.setObjectName("spinBox_laplace_ksize")
        self.label_title_9 = QtWidgets.QLabel(self.groupBox_laplace_filter)
        self.label_title_9.setGeometry(QtCore.QRect(30, 30, 51, 21))
        self.label_title_9.setObjectName("label_title_9")
        self.label_image_1 = QtWidgets.QLabel(Form)
        self.label_image_1.setGeometry(QtCore.QRect(220, 10, 480, 480))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_image_1.setFont(font)
        self.label_image_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_image_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_image_1.setScaledContents(False)
        self.label_image_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_1.setObjectName("label_image_1")
        self.groupBox_custom_filter = QtWidgets.QGroupBox(Form)
        self.groupBox_custom_filter.setGeometry(QtCore.QRect(10, 530, 271, 211))
        self.groupBox_custom_filter.setObjectName("groupBox_custom_filter")
        self.doubleSpinBox_custom_filter_1 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_1.setGeometry(QtCore.QRect(40, 40, 51, 22))
        self.doubleSpinBox_custom_filter_1.setDecimals(1)
        self.doubleSpinBox_custom_filter_1.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_1.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_1.setObjectName("doubleSpinBox_custom_filter_1")
        self.doubleSpinBox_custom_filter_2 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_2.setGeometry(QtCore.QRect(110, 40, 51, 22))
        self.doubleSpinBox_custom_filter_2.setDecimals(1)
        self.doubleSpinBox_custom_filter_2.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_2.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_2.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_2.setObjectName("doubleSpinBox_custom_filter_2")
        self.doubleSpinBox_custom_filter_3 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_3.setGeometry(QtCore.QRect(180, 40, 51, 22))
        self.doubleSpinBox_custom_filter_3.setDecimals(1)
        self.doubleSpinBox_custom_filter_3.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_3.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_3.setObjectName("doubleSpinBox_custom_filter_3")
        self.doubleSpinBox_custom_filter_4 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_4.setGeometry(QtCore.QRect(40, 80, 51, 22))
        self.doubleSpinBox_custom_filter_4.setDecimals(1)
        self.doubleSpinBox_custom_filter_4.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_4.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_4.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_4.setObjectName("doubleSpinBox_custom_filter_4")
        self.doubleSpinBox_custom_filter_5 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_5.setGeometry(QtCore.QRect(110, 80, 51, 22))
        self.doubleSpinBox_custom_filter_5.setDecimals(1)
        self.doubleSpinBox_custom_filter_5.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_5.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_5.setProperty("value", 5.0)
        self.doubleSpinBox_custom_filter_5.setObjectName("doubleSpinBox_custom_filter_5")
        self.doubleSpinBox_custom_filter_6 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_6.setGeometry(QtCore.QRect(180, 80, 51, 22))
        self.doubleSpinBox_custom_filter_6.setDecimals(1)
        self.doubleSpinBox_custom_filter_6.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_6.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_6.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_6.setObjectName("doubleSpinBox_custom_filter_6")
        self.doubleSpinBox_custom_filter_7 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_7.setGeometry(QtCore.QRect(40, 120, 51, 22))
        self.doubleSpinBox_custom_filter_7.setDecimals(1)
        self.doubleSpinBox_custom_filter_7.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_7.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_7.setObjectName("doubleSpinBox_custom_filter_7")
        self.doubleSpinBox_custom_filter_8 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_8.setGeometry(QtCore.QRect(110, 120, 51, 22))
        self.doubleSpinBox_custom_filter_8.setDecimals(1)
        self.doubleSpinBox_custom_filter_8.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_8.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_8.setProperty("value", -1.0)
        self.doubleSpinBox_custom_filter_8.setObjectName("doubleSpinBox_custom_filter_8")
        self.doubleSpinBox_custom_filter_9 = QtWidgets.QDoubleSpinBox(self.groupBox_custom_filter)
        self.doubleSpinBox_custom_filter_9.setGeometry(QtCore.QRect(180, 120, 51, 22))
        self.doubleSpinBox_custom_filter_9.setDecimals(1)
        self.doubleSpinBox_custom_filter_9.setMinimum(-100.0)
        self.doubleSpinBox_custom_filter_9.setSingleStep(0.5)
        self.doubleSpinBox_custom_filter_9.setObjectName("doubleSpinBox_custom_filter_9")
        self.pushButton_custom_filter = QtWidgets.QPushButton(self.groupBox_custom_filter)
        self.pushButton_custom_filter.setGeometry(QtCore.QRect(90, 160, 93, 28))
        self.pushButton_custom_filter.setObjectName("pushButton_custom_filter")
        self.comboBox_selector = QtWidgets.QComboBox(Form)
        self.comboBox_selector.setGeometry(QtCore.QRect(40, 180, 111, 31))
        self.comboBox_selector.setObjectName("comboBox_selector")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 140, 111, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像锐化"))
        self.label_title.setText(_translate("Form", "图像锐化"))
        self.label_image_2.setText(_translate("Form", "处理后的图像"))
        self.pushButton_open_file.setText(_translate("Form", "打开图片"))
        self.groupBox_sobel_filter.setTitle(_translate("Form", "Sobel算子"))
        self.pushButton_sobel_filter.setText(_translate("Form", "确定"))
        self.radioButton_sobel_dx.setText(_translate("Form", "X方向梯度"))
        self.radioButton_sobel_dy.setText(_translate("Form", "Y方向梯度"))
        self.radioButton_sobel_dx_dy.setText(_translate("Form", "X和Y方向梯度"))
        self.groupBox_laplace_filter.setTitle(_translate("Form", "Laplace算子"))
        self.pushButton_laplace_filter.setText(_translate("Form", "确定"))
        self.label_title_9.setText(_translate("Form", "核大小："))
        self.label_image_1.setText(_translate("Form", "原图"))
        self.groupBox_custom_filter.setTitle(_translate("Form", "自定义3*3卷积核"))
        self.pushButton_custom_filter.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "选择锐化类型："))

