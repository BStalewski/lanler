#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QAction, QApplication, QCheckBox, QDialog,
                         QMainWindow, QMessageBox, QRadioButton, )

from commons import CLICKED_SIGNAL, NotImplementedException
from model.main_model import Model
from dictionary_frame import ChooseDictionaryFrame
from options_frame import OptionsFrame
from pos_frame import AddPoSFrame
from test_frame import TestParamsFrame

from py_ui.main_ui import Ui_MainWindow
from py_ui.choose_user_ui import Ui_ChooseUserDialog
from py_ui.new_user_ui import Ui_NewUserDialog


class Gui(QMainWindow, Ui_MainWindow):

    def __init__(self, model):
        QMainWindow.__init__(self, None)
        self.setupUi(self)

        self.connect(self.addPoSButton, CLICKED_SIGNAL, self.add_pos)
        self.connect(self.testButton, CLICKED_SIGNAL, self.test)
        self.connect(self.dictionaryButton, CLICKED_SIGNAL, self.dictionary)
        self.connect(self.optionsButton, CLICKED_SIGNAL, self.options)

        self.model = model

        self.right_frame = None
        self.init_menu_bar()
        self.statusBar()

        self.center_on_screen()
        self.show()

    def init_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu(u'&Plik')
        exit_action = self.create_action(u'Zakończ', u'Ctrl+Q', u'Zakończ program', self.close)
        file_menu.addAction(exit_action)

    def center_on_screen(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2
        self.move(x, y)

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
        return TestParamsFrame(self)

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


class ChooseUserDialog(QDialog, Ui_ChooseUserDialog):
    def __init__(self, model, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.radio_buttons = []
        self.connect(self.newUserButton, CLICKED_SIGNAL, self.create_new_user)
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
