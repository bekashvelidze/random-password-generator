# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'random_pass.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setStyleSheet("background-color: #22222e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 550, 100))
        self.frame.setStyleSheet("background-color: rgb(251, 91, 95)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(69, 23, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(111, 116, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(111, 243, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.length = QtWidgets.QLineEdit(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(97, 170, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.length.setFont(font)
        self.length.setStyleSheet("color: white; \n"
"border: 2px solid;\n"
"border-color: white;\n"
"border-radius: 10;")
        self.length.setAlignment(QtCore.Qt.AlignCenter)
        self.length.setObjectName("length")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(10, 290, 480, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("color: white; \n"
"border: 2px solid;\n"
"border-color: white;\n"
"border-radius: 10;")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.generate_pass = QtWidgets.QPushButton(self.centralwidget)
        self.generate_pass.setGeometry(QtCore.QRect(10, 370, 411, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_pass.sizePolicy().hasHeightForWidth())
        self.generate_pass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.generate_pass.setFont(font)
        self.generate_pass.setStyleSheet("background-color: #fb5b5d;\n"
"color: white;")
        self.generate_pass.setObjectName("generate_pass")
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(430, 370, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.copy.setFont(font)
        self.copy.setStyleSheet("background-color: #fb5b5d;\n"
"color: white;")
        self.copy.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("copy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy.setIcon(icon)
        self.copy.setIconSize(QtCore.QSize(32, 32))
        self.copy.setObjectName("copy")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Random Password Generator"))
        self.label_3.setText(_translate("MainWindow", "Enter password length"))
        self.label_2.setText(_translate("MainWindow", "Your random password"))
        self.generate_pass.setText(_translate("MainWindow", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())