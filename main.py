#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui

from py_ui.main_ui import Ui_MainWindow

class Gui(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self, None)
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
        action = QtGui.QAction(name, self)
        action.setShortcut(shortcut)
        action.setStatusTip(status_tip)
        action.triggered.connect(callback)
        action.setEnabled(enabled)
        return action

    def choose_user(self):
        print 'cu'
        pass


class ChooseUserDialog(QtGui.QMainWindow, Ui_):

def main():
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    gui.choose_user()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
