# Filename: gui.py
#
# Created by A. Gierich at 09.08.2019
#
# Description:
# Configures the main window
# Last chances: 
#

from qtpy import QtWidgets, QtCore
from ui.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Sets the system date as the start value.
        self.ui.dateEdit_startDate.setDate(QtCore.QDate.currentDate())
        self.ui.dateEdit_mesDate.setDate((QtCore.QDate.currentDate()))

        # Test
        # self.ui.groupBox_result.hide()