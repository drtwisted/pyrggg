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
        PyRGGGWindow.setWindowModality(QtCore.Qt.WindowModal)
        PyRGGGWindow.resize(992, 273)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PyRGGGWindow.sizePolicy().hasHeightForWidth())
        PyRGGGWindow.setSizePolicy(sizePolicy)
        PyRGGGWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(PyRGGGWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 991, 271))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbCurrPlatformIcon = QtGui.QLabel(self.layoutWidget)
        self.lbCurrPlatformIcon.setText(_fromUtf8(""))
        self.lbCurrPlatformIcon.setObjectName(_fromUtf8("lbCurrPlatformIcon"))
        self.horizontalLayout.addWidget(self.lbCurrPlatformIcon)
        self.lbCurPlatform = QtGui.QLabel(self.layoutWidget)
        self.lbCurPlatform.setObjectName(_fromUtf8("lbCurPlatform"))
        self.horizontalLayout.addWidget(self.lbCurPlatform)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbTotlaGames = QtGui.QLabel(self.layoutWidget)
        self.lbTotlaGames.setObjectName(_fromUtf8("lbTotlaGames"))
        self.horizontalLayout.addWidget(self.lbTotlaGames)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbFirstGame = QtGui.QLabel(self.layoutWidget)
        self.lbFirstGame.setMinimumSize(QtCore.QSize(0, 27))
        self.lbFirstGame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(200, 200, 200, 240));\n"
"color: rgb(100, 100, 100);"))
        self.lbFirstGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFirstGame.setObjectName(_fromUtf8("lbFirstGame"))
        self.verticalLayout.addWidget(self.lbFirstGame)
        self.lbSecondGame = QtGui.QLabel(self.layoutWidget)
        self.lbSecondGame.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbSecondGame.setFont(font)
        self.lbSecondGame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 230));\n"
"color: rgb(50, 50, 50);"))
        self.lbSecondGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSecondGame.setObjectName(_fromUtf8("lbSecondGame"))
        self.verticalLayout.addWidget(self.lbSecondGame)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lbTheGameIconLeft = QtGui.QLabel(self.layoutWidget)
        self.lbTheGameIconLeft.setMinimumSize(QtCore.QSize(0, 0))
        self.lbTheGameIconLeft.setMaximumSize(QtCore.QSize(0, 16777215))
        self.lbTheGameIconLeft.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(230, 230, 230, 220), stop: 0.5 rgba(250, 250, 250, 230), stop:1 rgba(230, 230, 230, 220));"))
        self.lbTheGameIconLeft.setText(_fromUtf8(""))
        self.lbTheGameIconLeft.setObjectName(_fromUtf8("lbTheGameIconLeft"))
        self.horizontalLayout_3.addWidget(self.lbTheGameIconLeft)
        self.lbTheGame = QtGui.QLabel(self.layoutWidget)
        self.lbTheGame.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbTheGame.setFont(font)
        self.lbTheGame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(230, 230, 230, 220), stop: 0.5 rgba(250, 250, 250, 230), stop:1 rgba(230, 230, 230, 220));"))
        self.lbTheGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTheGame.setObjectName(_fromUtf8("lbTheGame"))
        self.horizontalLayout_3.addWidget(self.lbTheGame)
        self.lbTheGameIconRight = QtGui.QLabel(self.layoutWidget)
        self.lbTheGameIconRight.setMinimumSize(QtCore.QSize(0, 0))
        self.lbTheGameIconRight.setMaximumSize(QtCore.QSize(0, 16777215))
        self.lbTheGameIconRight.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(230, 230, 230, 220), stop: 0.5 rgba(250, 250, 250, 230), stop:1 rgba(230, 230, 230, 220));"))
        self.lbTheGameIconRight.setText(_fromUtf8(""))
        self.lbTheGameIconRight.setObjectName(_fromUtf8("lbTheGameIconRight"))
        self.horizontalLayout_3.addWidget(self.lbTheGameIconRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lbForthGame = QtGui.QLabel(self.layoutWidget)
        self.lbForthGame.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbForthGame.setFont(font)
        self.lbForthGame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 230));\n"
"color: rgb(50, 50, 50);"))
        self.lbForthGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbForthGame.setObjectName(_fromUtf8("lbForthGame"))
        self.verticalLayout.addWidget(self.lbForthGame)
        self.lbLastGame = QtGui.QLabel(self.layoutWidget)
        self.lbLastGame.setMinimumSize(QtCore.QSize(0, 27))
        self.lbLastGame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(200, 200, 200, 240));\n"
"color: rgb(100, 100, 100);"))
        self.lbLastGame.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLastGame.setObjectName(_fromUtf8("lbLastGame"))
        self.verticalLayout.addWidget(self.lbLastGame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbPlatforms = QtGui.QComboBox(self.layoutWidget)
        self.cbPlatforms.setMinimumSize(QtCore.QSize(400, 40))
        self.cbPlatforms.setObjectName(_fromUtf8("cbPlatforms"))
        self.horizontalLayout_2.addWidget(self.cbPlatforms)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bRoll = QtGui.QPushButton(self.layoutWidget)
        self.bRoll.setMinimumSize(QtCore.QSize(0, 40))
        self.bRoll.setObjectName(_fromUtf8("bRoll"))
        self.horizontalLayout_2.addWidget(self.bRoll)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        PyRGGGWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyRGGGWindow)
        QtCore.QMetaObject.connectSlotsByName(PyRGGGWindow)

    def retranslateUi(self, PyRGGGWindow):
        PyRGGGWindow.setWindowTitle(_translate("PyRGGGWindow", "MainWindow", None))
        self.lbCurPlatform.setText(_translate("PyRGGGWindow", "Current platform: ----", None))
        self.lbTotlaGames.setText(_translate("PyRGGGWindow", "Games in DB: ---", None))
        self.lbFirstGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbSecondGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbTheGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbForthGame.setText(_translate("PyRGGGWindow", "------", None))
        self.lbLastGame.setText(_translate("PyRGGGWindow", "------", None))
        self.bRoll.setText(_translate("PyRGGGWindow", "Roll", None))

