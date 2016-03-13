# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PyRGGGWindow(object):
    def setupUi(self, PyRGGGWindow):
        PyRGGGWindow.setObjectName(_fromUtf8("PyRGGGWindow"))
        PyRGGGWindow.resize(746, 243)
        self.centralwidget = QtGui.QWidget(PyRGGGWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 741, 222))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbFirstGame = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbFirstGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFirstGame.setObjectName(_fromUtf8("lbFirstGame"))
        self.verticalLayout.addWidget(self.lbFirstGame)
        self.lbSecondGame = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbSecondGame.setFont(font)
        self.lbSecondGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSecondGame.setObjectName(_fromUtf8("lbSecondGame"))
        self.verticalLayout.addWidget(self.lbSecondGame)
        self.lbTheGame = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbTheGame.setFont(font)
        self.lbTheGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTheGame.setObjectName(_fromUtf8("lbTheGame"))
        self.verticalLayout.addWidget(self.lbTheGame)
        self.lbForthGame = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbForthGame.setFont(font)
        self.lbForthGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbForthGame.setObjectName(_fromUtf8("lbForthGame"))
        self.verticalLayout.addWidget(self.lbForthGame)
        self.lbLastGame = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbLastGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLastGame.setObjectName(_fromUtf8("lbLastGame"))
        self.verticalLayout.addWidget(self.lbLastGame)
        self.bRoll = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bRoll.setObjectName(_fromUtf8("bRoll"))
        self.verticalLayout.addWidget(self.bRoll)
        PyRGGGWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyRGGGWindow)
        QtCore.QMetaObject.connectSlotsByName(PyRGGGWindow)

    def retranslateUi(self, PyRGGGWindow):
        PyRGGGWindow.setWindowTitle(_translate("PyRGGGWindow", "MainWindow", None))
        self.lbFirstGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbSecondGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbTheGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbForthGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbLastGame.setText(_translate("PyRGGGWindow", "------", None))
        self.bRoll.setText(_translate("PyRGGGWindow", "Roll", None))

