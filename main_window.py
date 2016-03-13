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
        PyRGGGWindow.resize(742, 256)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PyRGGGWindow.sizePolicy().hasHeightForWidth())
        PyRGGGWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(PyRGGGWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbLastGame = QtGui.QLabel(self.centralwidget)
        self.lbLastGame.setGeometry(QtCore.QRect(0, 150, 739, 31))
        self.lbLastGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLastGame.setObjectName(_fromUtf8("lbLastGame"))
        self.bRoll = QtGui.QPushButton(self.centralwidget)
        self.bRoll.setGeometry(QtCore.QRect(460, 210, 281, 41))
        self.bRoll.setObjectName(_fromUtf8("bRoll"))
        self.lbForthGame = QtGui.QLabel(self.centralwidget)
        self.lbForthGame.setGeometry(QtCore.QRect(0, 120, 739, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbForthGame.setFont(font)
        self.lbForthGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbForthGame.setObjectName(_fromUtf8("lbForthGame"))
        self.lbTheGame = QtGui.QLabel(self.centralwidget)
        self.lbTheGame.setGeometry(QtCore.QRect(0, 70, 739, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbTheGame.setFont(font)
        self.lbTheGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTheGame.setObjectName(_fromUtf8("lbTheGame"))
        self.lbSecondGame = QtGui.QLabel(self.centralwidget)
        self.lbSecondGame.setGeometry(QtCore.QRect(0, 40, 739, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbSecondGame.setFont(font)
        self.lbSecondGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSecondGame.setObjectName(_fromUtf8("lbSecondGame"))
        self.lbFirstGame = QtGui.QLabel(self.centralwidget)
        self.lbFirstGame.setGeometry(QtCore.QRect(0, 20, 739, 31))
        self.lbFirstGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFirstGame.setObjectName(_fromUtf8("lbFirstGame"))
        self.cbPlatforms = QtGui.QComboBox(self.centralwidget)
        self.cbPlatforms.setGeometry(QtCore.QRect(0, 210, 451, 41))
        self.cbPlatforms.setObjectName(_fromUtf8("cbPlatforms"))
        self.lbCurPlatform = QtGui.QLabel(self.centralwidget)
        self.lbCurPlatform.setGeometry(QtCore.QRect(10, 10, 311, 21))
        self.lbCurPlatform.setObjectName(_fromUtf8("lbCurPlatform"))
        self.lbTotlaGames = QtGui.QLabel(self.centralwidget)
        self.lbTotlaGames.setGeometry(QtCore.QRect(600, 10, 141, 20))
        self.lbTotlaGames.setObjectName(_fromUtf8("lbTotlaGames"))
        self.lbCurPlatformIcon = QtGui.QLabel(self.centralwidget)
        self.lbCurPlatformIcon.setGeometry(QtCore.QRect(10, 30, 57, 51))
        self.lbCurPlatformIcon.setText(_fromUtf8(""))
        self.lbCurPlatformIcon.setObjectName(_fromUtf8("lbCurPlatformIcon"))
        PyRGGGWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyRGGGWindow)
        QtCore.QMetaObject.connectSlotsByName(PyRGGGWindow)

    def retranslateUi(self, PyRGGGWindow):
        PyRGGGWindow.setWindowTitle(_translate("PyRGGGWindow", "MainWindow", None))
        self.lbLastGame.setText(_translate("PyRGGGWindow", "------", None))
        self.bRoll.setText(_translate("PyRGGGWindow", "Roll", None))
        self.lbForthGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbTheGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbSecondGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbFirstGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbCurPlatform.setText(_translate("PyRGGGWindow", "Current platform: ----", None))
        self.lbTotlaGames.setText(_translate("PyRGGGWindow", "Games in DB: ---", None))

