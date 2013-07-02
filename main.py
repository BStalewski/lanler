#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QAction, QApplication, QCheckBox, QDialog,
QFrame, QMainWindow, QMessageBox, QRadioButton,)

from model import Model, PtPlDictionaryModel, PlPtDictionaryModel

from py_ui.main_ui import Ui_MainWindow
from py_ui.choose_user_ui import Ui_ChooseUserDialog
from py_ui.new_user_ui import Ui_NewUserDialog

from py_ui.choose_add_pos_ui import Ui_AddPoSFrame
from py_ui.add_noun_ui import Ui_AddNounDialog

from py_ui.choose_dictionary_ui import Ui_ChooseDictionaryFrame
from py_ui.pt_pl_dictionary_ui import Ui_PtPlDictionaryFrame
from py_ui.options_ui import Ui_OptionsFrame

from py_ui.pt_pl_dictionary_ui import _translate


class Gui(QMainWindow, Ui_MainWindow):

    def __init__(self, model):
        QMainWindow.__init__(self, None)
        self.setupUi(self)

        self.connect(self.addPoSButton, QtCore.SIGNAL('clicked()'), self.add_pos)
        self.connect(self.testButton, QtCore.SIGNAL('clicked()'), self.test)
        self.connect(self.dictionaryButton, QtCore.SIGNAL('clicked()'), self.dictionary)
        self.connect(self.optionsButton, QtCore.SIGNAL('clicked()'), self.options)

        self.model = model

        self.right_frame = None
        self.init_menu_bar()
        self.statusBar()

        self.show()

    def init_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu(u'&Plik')
        exit_action = self.create_action(u'Zakończ', u'Ctrl+Q', u'Zakończ program', self.close)
        file_menu.addAction(exit_action)

    def create_action(self, name, shortcut, status_tip, callback, enabled=True):
        action = QAction(name, self)
        action.setShortcut(shortcut)
        action.setStatusTip(status_tip)
        action.triggered.connect(callback)
        action.setEnabled(enabled)
        return action

    def choose_user(self):
        dialog = ChooseUserDialog(self.model, self)

        if dialog.exec_():
            user_name = dialog.get_chosen_user()
            self.show_logged_user(user_name)
            self.model.set_current_user(user_name)
            return True

        return False

    def change_right_frame(fun):
        def wrapper(self, *args, **kwargs):
            if self.right_frame:
                self.right_frame.close()
            self.right_frame = fun(self, *args, **kwargs)
            self.horizontalLayout.addWidget(self.right_frame)

        return wrapper

    @change_right_frame
    def add_pos(self):
        return AddPoSFrame(self.model, self)

    @change_right_frame
    def test(self):
        raise NotImplementedException('test')

    @change_right_frame
    def dictionary(self):
        return ChooseDictionaryFrame(self.model, self)

    @change_right_frame
    def options(self):
        return OptionsFrame(self)

    @change_right_frame
    def show_frame(self, frame):
        return frame

    def show_logged_user(self, user_name):
        msg = u'Użytkownik: ' + user_name
        self.userName.showMessage(msg)


class RightFrame():
    def __init__(self, main_window):
        self.main_window = main_window


class ChooseUserDialog(QDialog, Ui_ChooseUserDialog):
    def __init__(self, model, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.radio_buttons = []
        self.connect(self.newUserButton, QtCore.SIGNAL('clicked()'), self.create_new_user)
        self.model = model
        names = self.model.get_users_names()
        self.user_names = names

        for name in names:
            self.add_user(name)

    def add_user(self, name):
        radio_button = QRadioButton(name, self)
        if not len(self.radio_buttons):
            radio_button.setChecked(True)

        self.groupBoxLayout.addWidget(radio_button)
        self.radio_buttons.append(radio_button)

    def get_chosen_user(self):
        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                return radio_button.text()

    def create_new_user(self):
        new_user_dialog = NewUserDialog(self.model, self)

        if new_user_dialog.exec_():
            new_user_name = new_user_dialog.get_user_name()
            import_users = new_user_dialog.get_import_users()
            self.model.create_user(new_user_name, import_users)
            self.add_user(new_user_name)
            self.radio_buttons[-1].setChecked(True)


class NewUserDialog(QDialog, Ui_NewUserDialog):
    def __init__(self, model, current_users_names, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.check_boxes = []
        self.model = model
        for name in self.model.get_users_names():
            check_box = QCheckBox(name, self)
            self.importGroupBoxLayout.addWidget(check_box)
            self.check_boxes.append(check_box)

    def get_user_name(self):
        return self.userNameLineEdit.text()

    def get_import_users(self):
        return [checkbox.text().__str__() for checkbox in self.check_boxes if checkbox.isChecked()]

    def accept(self):
        if self.model.is_user_name_unique(self.get_user_name()):
            QDialog.accept(self)
        else:
            QMessageBox.warning(self, u'Błąd', u'Błąd: nazwa użytkownika musi być unikalna')


class AddPoSFrame(QFrame, Ui_AddPoSFrame, RightFrame):
    def __init__(self, model, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.addNounButton, QtCore.SIGNAL('clicked()'), self.add_noun)
        self.connect(self.addVerbButton, QtCore.SIGNAL('clicked()'), self.add_verb)
        self.connect(self.addAdjectiveButton, QtCore.SIGNAL('clicked()'), self.add_adjective)
        self.connect(self.addPronounButton, QtCore.SIGNAL('clicked()'), self.add_pronoun)
        self.model = model

    def add_noun(self):
        dialog = AddNounDialog(self)
        if dialog.exec_():
            self.model.add_noun(**dialog.get_fields())

    def add_verb(self):
        print 'add_verb'
        raise NotImplementedException('add verb')

    def add_adjective(self):
        print 'add adjective'
        raise NotImplementedException('add adjective')

    def add_pronoun(self):
        print 'add pronoun'
        raise NotImplementedException('add pronoun')


class OptionsFrame(QFrame, Ui_OptionsFrame, RightFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.changeUserButton, QtCore.SIGNAL('clicked()'), self.change_user)
        self.connect(self.removeUserButton, QtCore.SIGNAL('clicked()'), self.remove_user)

    def change_user(self):
        print 'change user'
        raise NotImplementedException('change user')

    def remove_user(self):
        print 'remove user'
        raise NotImplementedException('remove user')


class ChooseDictionaryFrame(QFrame, Ui_ChooseDictionaryFrame, RightFrame):
    def __init__(self, model, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.plPtDictionaryButton, QtCore.SIGNAL('clicked()'), self.pl_pt_dictionary)
        self.connect(self.ptPlDictionaryButton, QtCore.SIGNAL('clicked()'), self.pt_pl_dictionary)
        self.model = model

    def pl_pt_dictionary(self):
        self.main_window.show_frame(PlPtDictionaryFrame(self.model, self.parent()))

    def pt_pl_dictionary(self):
        self.main_window.show_frame(PtPlDictionaryFrame(self.model, self.parent()))


class PtPlDictionaryFrame(QFrame, Ui_PtPlDictionaryFrame, RightFrame):
    def __init__(self, model, parent):
        QFrame.__init__(self, parent)
        RightFrame.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.backButton, QtCore.SIGNAL('clicked()'), self.back)
        self.model = model

        tablemodel = PtPlDictionaryModel(self.model.get_current_user(), self)
        self.dictionaryTableView.setModel(tablemodel)

    def back(self):
        raise NotImplementedException('back')


class PlPtDictionaryFrame(PtPlDictionaryFrame):
    def __init__(self, model, parent):
        PtPlDictionaryFrame.__init__(self, model, parent)

        tablemodel = PlPtDictionaryModel(self.model.get_current_user(), self)
        self.dictionaryTableView.setModel(tablemodel)
    
    def retranslateUi(self, frame):
        Ui_PtPlDictionaryFrame.retranslateUi(self, frame)
        frame.setWindowTitle(_translate("PlPtDictionaryFrame", "Frame", None))
        self.label.setText(_translate("PlPtDictionaryFrame", "Słownik polsko - portugalski", None))

    def back(self):
        raise NotImplementedException('back')


class AddNounDialog(QDialog, Ui_AddNounDialog):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
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


class NotImplementedException(Exception):
    pass


def main():
    app = QApplication(sys.argv)
    model = Model()
    gui = Gui(model)
    if not gui.choose_user():
        gui.close()
    else:
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
