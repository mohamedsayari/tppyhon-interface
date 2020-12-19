# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(811, 476)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.t = QtWidgets.QLineEdit(Dialog)
        self.t.setGeometry(QtCore.QRect(140, 100, 113, 20))
        self.t.setObjectName("t")
        self.q = QtWidgets.QLineEdit(Dialog)
        self.q.setGeometry(QtCore.QRect(140, 140, 113, 20))
        self.q.setObjectName("q")
        self.aj = QtWidgets.QPushButton(Dialog)
        self.aj.setGeometry(QtCore.QRect(84, 290, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.aj.setFont(font)
        self.aj.setObjectName("aj")
        self.res = QtWidgets.QTableWidget(Dialog)
        self.res.setGeometry(QtCore.QRect(290, 220, 511, 192))
        self.res.setObjectName("res")
        self.res.setColumnCount(4)
        self.res.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(3, item)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.r = QtWidgets.QLineEdit(Dialog)
        self.r.setGeometry(QtCore.QRect(140, 170, 113, 20))
        self.r.setObjectName("r")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Gestion de question"))
        self.label_2.setText(_translate("Dialog", "titre"))
        self.label_3.setText(_translate("Dialog", "question"))
        self.aj.setText(_translate("Dialog", "ajouter"))
        item = self.res.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        item = self.res.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "titre"))
        item = self.res.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "question"))
        item = self.res.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "reponce"))
        self.label_5.setText(_translate("Dialog", "reponce"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
