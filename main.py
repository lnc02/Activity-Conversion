# Filename: main.py
#
# Created by A. Gierich at 09.08.2019
#
# Description:
# Programm zur Berechnung der Aktivität von radioaktiven Stoffen
# Last chances: 
#

import sys
from qtpy import QtWidgets
from classes import gui

app = QtWidgets.QApplication(sys.argv)

window = gui.MainWindow()

window.show()

sys.exit(app.exec_())