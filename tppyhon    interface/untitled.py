# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
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
        self.label_2.setGeometry(QtCore.QRect(16, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.n = QtWidgets.QLineEdit(Dialog)
        self.n.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.n.setObjectName("n")
        self.p = QtWidgets.QLineEdit(Dialog)
        self.p.setGeometry(QtCore.QRect(120, 130, 113, 20))
        self.p.setObjectName("p")
        self.t = QtWidgets.QLineEdit(Dialog)
        self.t.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.t.setObjectName("t")
        self.n_2 = QtWidgets.QComboBox(Dialog)
        self.n_2.setGeometry(QtCore.QRect(120, 200, 111, 22))
        self.n_2.setObjectName("n_2")
        self.n_2.addItem("")
        self.n_2.addItem("")
        self.n_2.addItem("")
        self.n_2.addItem("")
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
        self.res.setColumnCount(5)
        self.res.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.res.setHorizontalHeaderItem(4, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Gestion de condidat"))
        self.label_2.setText(_translate("Dialog", "nom"))
        self.label_3.setText(_translate("Dialog", "prenom"))
        self.label_4.setText(_translate("Dialog", "tel"))
        self.label_5.setText(_translate("Dialog", "niveau"))
        self.n_2.setItemText(0, _translate("Dialog", "bac"))
        self.n_2.setItemText(1, _translate("Dialog", "bac+3"))
        self.n_2.setItemText(2, _translate("Dialog", "bac+5"))
        self.n_2.setItemText(3, _translate("Dialog", "sans bac"))
        self.aj.setText(_translate("Dialog", "ajouter"))
        item = self.res.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        item = self.res.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "nom"))
        item = self.res.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "prenom"))
        item = self.res.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "tel"))
        item = self.res.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "niveau"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
