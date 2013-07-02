# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/choose_add_pos.ui'
#
# Created: Tue Jul  2 08:29:12 2013
#      by: PyQt4 UI code generator 4.10.2-snapshot-74ade0e1faf2
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

class Ui_AddPoSFrame(object):
    def setupUi(self, AddPoSFrame):
        AddPoSFrame.setObjectName(_fromUtf8("AddPoSFrame"))
        AddPoSFrame.resize(133, 160)
        AddPoSFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        AddPoSFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(AddPoSFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.addNounButton = QtGui.QPushButton(AddPoSFrame)
        self.addNounButton.setObjectName(_fromUtf8("addNounButton"))
        self.verticalLayout.addWidget(self.addNounButton)
        self.addVerbButton = QtGui.QPushButton(AddPoSFrame)
        self.addVerbButton.setObjectName(_fromUtf8("addVerbButton"))
        self.verticalLayout.addWidget(self.addVerbButton)
        self.addAdjectiveButton = QtGui.QPushButton(AddPoSFrame)
        self.addAdjectiveButton.setObjectName(_fromUtf8("addAdjectiveButton"))
        self.verticalLayout.addWidget(self.addAdjectiveButton)
        self.addPronounButton = QtGui.QPushButton(AddPoSFrame)
        self.addPronounButton.setObjectName(_fromUtf8("addPronounButton"))
        self.verticalLayout.addWidget(self.addPronounButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(AddPoSFrame)
        QtCore.QMetaObject.connectSlotsByName(AddPoSFrame)

    def retranslateUi(self, AddPoSFrame):
        AddPoSFrame.setWindowTitle(_translate("AddPoSFrame", "Dodaj wyraz", None))
        self.addNounButton.setText(_translate("AddPoSFrame", "Rzeczownik", None))
        self.addVerbButton.setText(_translate("AddPoSFrame", "Czasownik", None))
        self.addAdjectiveButton.setText(_translate("AddPoSFrame", "Przymiotnik", None))
        self.addPronounButton.setText(_translate("AddPoSFrame", "Zaimek", None))

