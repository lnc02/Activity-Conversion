# Filename: main.py
#
# Created by A. Gierich at 09.08.2019
#
# Description:
# Program for calculating the activity of radioactive substances
# Last chances: 
#

import sys
from qtpy import QtWidgets
from classes import gui

app = QtWidgets.QApplication(sys.argv)

# starts the GUI
window = gui.MainWindow()
window.show()

sys.exit(app.exec_())