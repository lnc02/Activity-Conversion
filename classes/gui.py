# Filename: gui.py
#
# Created by A. Gierich at 09.08.2019
#
# Description:
#
# Last chances: 
#

from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)