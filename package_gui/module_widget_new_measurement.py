########################################################################################################################
# module_new_testset
########################################################################################################################
from PyQt5.QtWidgets import QAction, QGridLayout, QWidget, QComboBox, QPushButton, QFileDialog, QLineEdit, QLabel, \
    QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QGroupBox, QMessageBox, QToolTip, QStackedLayout, QColumnView
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.Qt import *
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
# from package_gui.module_signals import *

from package_algorithms.module_fft import *
from package_algorithms.module_interface import *


from xml.etree import ElementTree as et


class Widget_New_Measurement(QWidget):
    def __init__(self):

        super().__init__()
        self.tab_index = 0

        self.lineedit_delay_test_type_individual_n_active = False
        self.lineedit_delay_dgm_delay_uniform_n_active = False

        self.messagebox_defined_parameters = QMessageBox(self)

        self.initui()

    def initui(self):

        # Window-Title of QWidget 'Widget_Check_CRC'
        self.windowname_new_measurement = 'New Measurement'
        self.setWindowTitle("%s" % self.windowname_new_measurement)
        ################################################################################################################
        # QGridLayout 'gridlayout_lv0'
        ################################################################################################################

        self.gridlayout_lv0 = QGridLayout(self)

        ################################################################################################################
        # QGroupBox 'groupbox_testset_selection'
        ################################################################################################################

        self.create_groupbox_measurement_types_selection()

        ################################################################################################################
        # QGroupBox 'groupbox_testset_editor'
        ################################################################################################################

        self.create_groupbox_measurements_specs()

        ################################################################################################################
        # QGroupBox 'groupbox_preview'
        ################################################################################################################

        self.create_groupbox_measurement_save()
        ################################################################################################################
        # QGroupBox 'groupbox_save_csv'
        ################################################################################################################

        self.create_groupbox_csv_file()

    ####################################################################################################################
    # QGroupBox 'groupbox_testset_selection'
    ####################################################################################################################

    def create_groupbox_measurement_types_selection(self):


        self.label_measurement_types = QLabel('Measurement Type:', self)

        self.combobox_measurement_types = QComboBox(self)

        for item in list_measurement_types:
            self.combobox_measurement_types.addItem(item)
        self.combobox_measurement_types.currentIndexChanged.connect(self.combobox_testset_type_index_changed)

        self.pushbutton_fft_example = QPushButton('FFT_Example', self)
        periodlength = 1
        samples = 1
        self.pushbutton_fft_example.clicked.connect(fft_example)

        self.gridlayout_lv1_measurement_types_selection = QGridLayout(self)
        self.gridlayout_lv1_measurement_types_selection.addWidget(self.label_measurement_types, 0, 0, 1, 1)
        self.gridlayout_lv1_measurement_types_selection.addWidget(self.combobox_measurement_types, 0, 1, 1, 1)
        self.gridlayout_lv1_measurement_types_selection.addWidget(self.pushbutton_fft_example, 1, 1, 1, 1)


        # QGroupBox 'groupbox_testset_selection':
        self.groupbox_measurement_types_selection = QGroupBox("Measurement Type Selection", self)
        self.groupbox_measurement_types_selection.setLayout(self.gridlayout_lv1_measurement_types_selection)

        self.gridlayout_lv0.addWidget(self.groupbox_measurement_types_selection, 0, 0, 1, 1)

    def create_groupbox_measurements_specs(self):

        ################################################################################################################
        # QStackedLayout 'stacked_layout'
        # Annotation: QStackedLayout 'stacked_layout' can show different QGroupBoxes
        ################################################################################################################

        self.gridlayout_lv1_measurements_specs = QGridLayout(self)

        #self.tabbar_measurement_specs = QTabBar(self)
        self.label1 = QLabel("Loudspeaker")
        self.label2 = QLabel("Type")
        self.label3 = QLabel("Excitation Signal")
        self.label4 = QLabel("X Coordinate")
        self.label5 = QLabel("y Coordinate")
        self.label6 = QLabel("Orientation (Angle)")
        self.label7 = QLabel('Miscellaneous')



        #self.button_add_loudspeaker()

        self.tab_loudspeakers = QTabWidget()
        #self.gridlayout_lv1_tab_loudspeakers.addWidget()
        self.gridlayout_lv1_tab_loudspeakers = QGridLayout(self)
        #for item in list_measurement_types:
        self.gridlayout_lv1_tab_loudspeakers.addWidget(self.label1, 0, 0)
        self.gridlayout_lv1_tab_loudspeakers.addWidget(self.label2, 0, 1)
        self.gridlayout_lv1_tab_loudspeakers.addWidget(self.label3, 0, 2)
        self.gridlayout_lv1_tab_loudspeakers.addWidget(self.label4, 0, 3)
        self.gridlayout_lv1_tab_loudspeakers.addWidget(self.label5, 0, 4)
        self.gridlayout_lv1_tab_loudspeakers.addWidget(self.label6, 0, 5)
        self.gridlayout_lv1_tab_loudspeakers.addWidget(self.label7, 0, 6)

        # for item in list_measurement_types:
        self.list = []
        #self.list.append()
        self.lineedit_1 = QLineEdit()
        self.lineedit_2 = QLineEdit()
        self.lineedit_3 = QLineEdit()
        self.lineedit_4 = QLineEdit()
        self.lineedit_5 = QLineEdit()
        self.lineedit_6 = QLineEdit()
        self.lineedit_7 = QLineEdit()



        number_loudspeakers = 10
        number_loudspeakers = number_loudspeakers-1
        self.item = 0
        for i in range(0, 7):

            for j in range(1, number_loudspeakers):
                self.list.append(QLineEdit())

                self.gridlayout_lv1_tab_loudspeakers.addWidget(self.list[self.item], j, i)
                self.item = self.item + 1




        self.tab_loudspeakers.setLayout(self.gridlayout_lv1_tab_loudspeakers)

        self.tab_acousticroom = QTabWidget()

        self.tab_binaural_recording_system = QTabWidget()

        self.tabbar_measurement_specs = QTabWidget(self)
        self.tabbar_measurement_specs.addTab(self.tab_loudspeakers, 'Loudspeakers')
        self.tabbar_measurement_specs.addTab(self.tab_acousticroom, 'Acoustic_Room')
        self.tabbar_measurement_specs.addTab(self.tab_binaural_recording_system, 'Binaural_Recording_System')
        #######

        self.gridlayout_lv1_measurements_specs.addWidget(self.tabbar_measurement_specs, 0, 0, 1, 1)

        self.groupbox_measurements_specs = QGroupBox("Measurement Specifications", self)
        self.groupbox_measurements_specs.setLayout( self.gridlayout_lv1_measurements_specs)



        self.gridlayout_lv0.addWidget(self.groupbox_measurements_specs, 1, 0)

    def combobox_testset_type_index_changed(self):
        print("Index Testset:     " + str(self.combobox_measurement_types.currentIndex()))
        if self.combobox_measurement_types.currentIndex() == 0:
            print("Show DELAY-Window")
            self.stacked_layout.setCurrentIndex(0)
        elif self.combobox_measurement_types.currentIndex() == 1:
            print("Show GAIN-Window")
            self.stacked_layout.setCurrentIndex(1)
        elif self.combobox_measurement_types.currentIndex() == 2:
            print("Show BIQUAD-Window")
            self.stacked_layout.setCurrentIndex(2)

    def create_groupbox_measurement_save(self):
        print('eeew')

