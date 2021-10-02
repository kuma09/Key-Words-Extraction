# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(707, 545)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 500, 321, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 50, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(270, 10, 411, 161))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 111, 31))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 380, 111, 31))
        self.pushButton_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(270, 250, 411, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 181, 41))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(270, 180, 151, 41))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 320, 111, 31))
        self.pushButton_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 250, 111, 31))
        self.pushButton_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 55, 41, 21))
        self.label.setStyleSheet("image: url(:/newPrefix/e.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 380, 31, 31))
        self.label_4.setStyleSheet("image: url(:/newPrefix/d.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 320, 31, 31))
        self.label_5.setStyleSheet("image: url(:/newPrefix/d.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(140, 250, 31, 31))
        self.label_6.setStyleSheet("image: url(:/newPrefix/d.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Ouvrir"))
        self.label_2.setText(_translate("Dialog", "Choisir un Text"))
        self.pushButton_3.setText(_translate("Dialog", "Mot-Clés"))
        self.label_3.setText(_translate("Dialog", "Choisir le nombre de Mot Clés"))
        self.pushButton_4.setText(_translate("Dialog", "Pos-Tag"))
        self.pushButton_5.setText(_translate("Dialog", "Lemma"))

import f
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

