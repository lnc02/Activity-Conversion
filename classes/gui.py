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
from datetime import datetime
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Sets the system date as the reference and request date value.
        self.ui.dateEdit_startDate.setDate(QtCore.QDate.currentDate())
        self.ui.dateEdit_mesDate.setDate((QtCore.QDate.currentDate()))

        # Button activate
        self.ui.button_calculate.clicked.connect(self.on_button_click)

    # Calculate Button
    def on_button_click(self):
        # Function variables
        # Read and reformat date from form
        mes_date = self.ui.dateEdit_mesDate.date().toString('dd.MM.yyyy')
        # Read start-value from form
        start_value = self.ui.doubleSpinBox_startValue.value()
        # Set requested date in output
        self.ui.label_date.setText(str(mes_date))

        self.calc_activity()

    def calc_activity(self):

        # Function variables
        # Date format that is expected
        date_format = "%d.%m.%Y"
        # half-life Iodine 125
        hwz = 59.49
        n_zero = self.ui.doubleSpinBox_startValue.value()
        # conversion factor U to mCi
        u_to_mci = 1.2699
        # Read and reformat date from form
        ref_date = self.ui.dateEdit_startDate.date().toString('dd.MM.yyyy')
        mes_date = self.ui.dateEdit_mesDate.date().toString('dd.MM.yyyy')
        ref_date_calc = datetime.strptime(ref_date, date_format)
        mes_date_calc = datetime.strptime(mes_date, date_format)
        # Read combo Box from form
        unit = self.ui.comboBox_mesUnit.currentText()

        # Calculating the date difference
        diff_date = (ref_date_calc - mes_date_calc).days

        # Calculate activity on requested date - Basis Unit
        n_t = round(n_zero * np.exp((np.log(2) / hwz) * diff_date), 4)
        mci_u_t = round((n_t / u_to_mci), 4)
        mbq_t = round((mci_u_t * 37), 4)
        # Calculate activity on requested date - Basis MBq
        mci_mbq_t = round((n_t / 37), 4)
        u_mbq_t = round((mci_mbq_t * u_to_mci), 4)
        # Calculate activity on requested date - Basis mCi
        u_mci_t = round((n_t * u_to_mci), 4)
        mbq_mci_t = round((n_t * 37), 4)

        # Output in the form
        if unit == "Unit":
            self.ui.label_resUnit.setText(str(n_t))
            self.ui.label_resMBq.setText(str(mbq_t))
            self.ui.label_resmCi.setText(str(mci_u_t))
        elif unit == "MBq":
            self.ui.label_resUnit.setText(str(u_mbq_t))
            self.ui.label_resMBq.setText(str(n_t))
            self.ui.label_resmCi.setText(str(mci_mbq_t))
        elif unit == "mCi":
            self.ui.label_resUnit.setText(str(u_mci_t))
            self.ui.label_resMBq.setText(str(mbq_mci_t))
            self.ui.label_resmCi.setText(str(n_t))
