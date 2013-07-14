# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/choose_dictionary.ui'
#
# Created: Mon Jul 15 00:43:26 2013
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

class Ui_ChooseDictionaryFrame(object):
    def setupUi(self, ChooseDictionaryFrame):
        ChooseDictionaryFrame.setObjectName(_fromUtf8("ChooseDictionaryFrame"))
        ChooseDictionaryFrame.resize(212, 174)
        ChooseDictionaryFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        ChooseDictionaryFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(ChooseDictionaryFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.plPtDictionaryButton = QtGui.QPushButton(ChooseDictionaryFrame)
        self.plPtDictionaryButton.setObjectName(_fromUtf8("plPtDictionaryButton"))
        self.verticalLayout.addWidget(self.plPtDictionaryButton)
        self.ptPlDictionaryButton = QtGui.QPushButton(ChooseDictionaryFrame)
        self.ptPlDictionaryButton.setObjectName(_fromUtf8("ptPlDictionaryButton"))
        self.verticalLayout.addWidget(self.ptPlDictionaryButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(ChooseDictionaryFrame)
        QtCore.QMetaObject.connectSlotsByName(ChooseDictionaryFrame)

    def retranslateUi(self, ChooseDictionaryFrame):
        ChooseDictionaryFrame.setWindowTitle(_translate("ChooseDictionaryFrame", "Frame", None))
        self.plPtDictionaryButton.setText(_translate("ChooseDictionaryFrame", "Polsko - portugalski", None))
        self.ptPlDictionaryButton.setText(_translate("ChooseDictionaryFrame", "Portugalsko - polski", None))

