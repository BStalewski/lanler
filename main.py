#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import QApplication

from gui.main_gui import Gui
from model.main_model import Model


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
