#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QMainWindow, QAction, QDialog, QApplication,
QRadioButton, QCheckBox)

from model import Model

from py_ui.main_ui import Ui_MainWindow
from py_ui.choose_user_ui import Ui_ChooseUserDialog
from py_ui.new_user_ui import Ui_NewUserDialog


class Gui(QMainWindow, Ui_MainWindow):

    def __init__(self, model):
        QMainWindow.__init__(self, None)
        self.model = model

        self.setupUi(self)
        self.init_menu_bar()
        self.statusBar()

        self.show()

    def init_menu_bar(self):
        '''
        menubar = self.menuBar()
        file_menu = menubar.addMenu(u'&Plik')
        run_menu = menubar.addMenu(u'&Wykonaj')

        open_image_action = self.create_action(u'Otwórz obraz', u'Ctrl+O',
                                               u'Wczytaj nowy obraz', self.open_image)
        exit_action = self.create_action(u'Exit', u'Ctrl+Q', u'Zakończ program', self.close)
        file_menu.addActions([open_image_action, exit_action])

        thresholding_action = self.create_action(u'Progowanie', u'Ctrl+P', u'Wykonaj algorytm progowania',
                                                 self.thresholding, False)
        ml_em_action = self.create_action(u'Algorytm ML-EM', u'Ctrl+M',
                                          u'Wykonaj algorytm ML-EM', self.ml_em, False)
        repeat_action = self.create_action(u'Powtórz ostatni algorytm', u'Ctrl+R',
                                           u'Wykonaj ponownie poprzedni algorytm z tym samymi ustawieniami',
                                           self.repeat, False)
        run_menu.addActions([thresholding_action, ml_em_action, repeat_action])

        self.actions = {
            u'open': open_image_action,
            u'exit': exit_action,
            u'thresholding': thresholding_action,
            u'ml_em': ml_em_action,
            u'repeat': repeat_action,
        }
        '''

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
            user_name = dialog.get_chosen_user().__str__()
            self.show_logged_user(user_name)
            return True

        return False

    def show_logged_user(self, user_name):
        msg = u'Użytkownik: ' + user_name
        self.userName.showMessage(msg)


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
        new_user_dialog = NewUserDialog(model, self)

        if new_user_dialog.exec_():
            print 'import from: '
            print new_user_dialog.get_import_users()
            new_user_name = new_user_dialog.get_user_name()
            import_users = new_user_dialog.get_import_users()
            self.model.create_user(new_user_name, import_users)
            self.add_user(new_user_name)
            self.radio_buttons[-1].setChecked(True)
        else:
            print 'no_add_new_user'


class NewUserDialog(QDialog, Ui_NewUserDialog):
    def __init__(self, model, current_users_names, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.check_boxes = []
        for name in self.model.get_users_names():
            check_box = QCheckBox(name, self)
            self.importGroupBoxLayout.addWidget(check_box)
            self.check_boxes.append(check_box)

    def get_user_name(self):
        return self.userNameLineEdit.text()

    def get_import_users(self):
        return [checkbox.text().__str__() for checkbox in self.check_boxes if checkbox.isChecked()]


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
