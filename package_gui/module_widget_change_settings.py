########################################################################################################################
# module_widget_change_settings
########################################################################################################################
from PyQt5.QtWidgets import QAction, QGridLayout, QWidget, QComboBox, QPushButton, QFileDialog, QLineEdit, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QGroupBox, QMessageBox, QToolTip, QStackedLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
##from TestsetCreator.package_gui.module_signals import *
#from TestsetCreator.package_algorithms.module_testset import *
#from TestsetCreator.package_algorithms.module_testset_delay import *
#from TestsetCreator.package_algorithms.module_testset_gain import *


class Widget_Change_Settings(QWidget):
    def __init__(self):

        super().__init__()

        self.lineedit_testtyp_individual_n_active = False
        self.lineedit_dgm_delay_uniform_n_active = False

        self.messagebox_defined_parameters = QMessageBox(self)


        self.initui()

    def initui(self):

        # Window-Title of QWidget 'Widget_Check_CRC'
        self.windowname = 'Change Settings'
        self.setWindowTitle("%s" % self.windowname)
        ################################################################################################################
        # QGridLayout 'gridlayout_lv0'
        ################################################################################################################

        self.gridlayout_lv0 = QGridLayout(self)
        self.setLayout(self.gridlayout_lv0)

        self.pushbutton = QPushButton("PUSH", self)
        self.label = QLabel(self)
        self.movie = QMovie('TestsetCreator/graphics/tenor.gif')
        self.movie.setCacheMode(QMovie.CacheAll)
        self.label.setMovie(self.movie)
        self.gridlayout_lv0.addWidget(self.pushbutton)
        self.gridlayout_lv0.addWidget(self.label)
        self.movie.start()
