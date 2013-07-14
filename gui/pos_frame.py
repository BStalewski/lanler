#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog, QFrame, QMessageBox

from commons import CLICKED_SIGNAL, RightFrame
from py_ui.choose_add_pos_ui import Ui_AddPoSFrame
from py_ui.add_noun_ui import Ui_AddNounDialog
from py_ui.add_pos_ui import Ui_AddPoSDialog


class AddPoSFrame(QFrame, Ui_AddPoSFrame, RightFrame):
    def __init__(self, model, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.addNounButton, CLICKED_SIGNAL, self.add_noun)
        self.connect(self.addVerbButton, CLICKED_SIGNAL, self.add_verb)
        self.connect(self.addAdjectiveButton, CLICKED_SIGNAL, self.add_adjective)
        self.connect(self.addPronounButton, CLICKED_SIGNAL, self.add_pronoun)
        self.model = model

    def add_noun(self):
        dialog = AddNounDialog(self)
        if dialog.exec_():
            self.model.add_noun(**dialog.get_fields())

    def add_verb(self):
        dialog = AddPoSDialog(self)
        if dialog.exec_():
            self.model.add_verb(**dialog.get_fields())

    def add_adjective(self):
        dialog = AddPoSDialog(self)
        if dialog.exec_():
            self.model.add_adjective(**dialog.get_fields())

    def add_pronoun(self):
        dialog = AddPoSDialog(self)
        if dialog.exec_():
            self.model.add_pronoun(**dialog.get_fields())


class AddNounDialog(QDialog, Ui_AddNounDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)

    def accept(self):
        if self.validate():
            QDialog.accept(self)

    def get_gender(self):
        return 'M' if self.masculineRadioButton.isChecked() else 'F'

    def get_polish(self):
        return self.polishLineEdit.text().trimmed()

    def get_portuguese(self):
        return self.portugueseLineEdit.text().trimmed()

    def validate(self):
        polish = self.get_polish()
        portuguese = self.get_portuguese()
        gender = self.get_gender()
        if not polish or not portuguese:
            QMessageBox.warning(self, u'Błąd', u'Błąd: wszystkie pola muszą być uzupełnione')
            return False

        if not gender:
            QMessageBox.warning(self, u'Błąd', u'Błąd: niewybrany rodzaj rzeczownika')
            return False

        return True

    def get_fields(self):
        return {
            u'polish': self.get_polish(),
            u'portuguese': self.get_portuguese(),
            u'gender': self.get_gender(),
        }


class AddPoSDialog(QDialog, Ui_AddPoSDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)

    def accept(self):
        if self.validate():
            QDialog.accept(self)

    def get_polish(self):
        return self.polishLineEdit.text().trimmed()

    def get_portuguese(self):
        return self.portugueseLineEdit.text().trimmed()

    def validate(self):
        polish = self.get_polish()
        portuguese = self.get_portuguese()
        if not polish or not portuguese:
            QMessageBox.warning(self, u'Błąd', u'Błąd: wszystkie pola muszą być uzupełnione')
            return False

        return True

    def get_fields(self):
        return {
            u'polish': self.get_polish(),
            u'portuguese': self.get_portuguese(),
        }
