########################################################################################################################
# module_mainwindow
########################################################################################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, qApp, QApplication, QTabWidget, QMenuBar, QMenu, QToolBar, \
    QToolBox, QStatusBar, QDockWidget, QProgressBar, QInputDialog
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon


from package_gui.module_widget_new_measurement import *
from package_gui.module_widget_change_settings import *
from package_gui.module_widget_new_audio_measurement import *

#from package_algorithms.module_soundmeasurement import *



#from package_interface_soundcard.module_interface_asio import *

from package_algorithms.module_sounddevice import *
from package_algorithms.module_audiofile_functions import *

#from pyaudio import *


class Mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # set title of mainwindow
        self.setWindowTitle("AuToBo")
        self.setWindowIcon(QIcon(r'directory_pictures/loudspeaker_symbol.png'))

        # Set size of mainwindow

        self.setGeometry(200, 200, 2000, 1600)
        self.setMinimumSize(1000, 800)

        # Create the QMenuBar "menubar_mainwindow"
        self.create_menubar()

        # Create QToolBar "toolbar_mainwindow"
        self.create_toolbar()

        # Create QStatusBar "statusbar_mainwindow"
        self.create_statusbar()

        # Adding QTabWidget
        self.tabwidget_mainwindow = QTabWidget(self)
        self.tabwidget_mainwindow.setMovable(True)
        self.tabwidget_mainwindow.setTabsClosable(True)
        self.tabwidget_mainwindow.usesScrollButtons()
        # i = self.tabwidget_mainwindow.currentIndex()
        self.tabwidget_mainwindow.tabCloseRequested.connect(self.remove_tab)
        self.tabwidget_mainwindow.tabBarDoubleClicked.connect(self.rename_tab)
        # hat keine auswirkung

        # Adding QTabWidget
        # dockwidgetcontent = QWidget(self)
        # dockwidgetcontent.setWindowTitle("Widget")
        # self.create_dockwidget(dockwidgetcontent)

        # Defining and adding QCentralWidget
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("CentralWidget")
        self.setCentralWidget(self.tabwidget_mainwindow)

        #
        self.create_grid_moduls()

        self.show()
        #self.showFullScreen()

    def create_grid_moduls(self):
        self.widget_moduls = QWidget()

        self.tabwidget_mainwindow.addTab(self.widget_moduls, "Moduls")

        self.grid_moduls = QGridLayout(self)

        self.button_GUI_Sitian = QPushButton("GUI Sitian", self)
        self.button_GUI_Sitian.clicked.connect(self.button_guisitian_clicked)
        self.grid_moduls.addWidget(self.button_GUI_Sitian)

        self.button_soundmeasurement = QPushButton("Sound Measurement", self)
        self.button_soundmeasurement.clicked.connect(self.button_soundmeasurement_clicked)
        self.grid_moduls.addWidget(self.button_soundmeasurement)

        self.button_soundrecord= QPushButton("Sound Record", self)
        self.button_soundrecord.clicked.connect(self.button_soundrecord_clicked)
        self.grid_moduls.addWidget(self.button_soundrecord)

        self.button_sounddevice_test = QPushButton("Sounddevice Test", self)
        self.button_sounddevice_test.clicked.connect(self.button_sounddevice_test_clicked)
        self.grid_moduls.addWidget(self.button_sounddevice_test)

        #self.groupbox_ = QGroupBox("Module", self)
        #self.groupbox_.setLayout(self.grid_moduls)
        self.widget_moduls.setLayout(self.grid_moduls)
        #self.tabwidget_mainwindow.add

    def button_soundmeasurement_clicked(self):
        print("Button 'Soundmeasurement' has been clicked!")
        #soundmeasurement()

    def button_soundrecord_clicked(self):
        print("Button 'Record Sound' has been clicked!")
        #soundrecord(self)

    def button_guisitian_clicked(self):
        print("Button 'Soundmeasurement' has been clicked!")
        #gui_sitian()


    def button_sounddevice_test_clicked(self):
        print("Button 'Sounddevice Test ' has been clicked!")
        x = None

        print(sd.query_devices())

        print(sd.query_hostapis())

        print(sd.get_portaudio_version())

        #p = pyaudio.PyAudio()
        #host_info = p.get_host_api_info_by_index(0)
        #device_count = host_info.get('deviceCount')

        #print(host_info)

        #print(device_count)

        #sd.AsioSettings()

        while True:

            while x == None:
                x = input("Welche Sounddevice-Funktion soll getestet werden?\n")
            if x == '0':
                x = None
                print('Eingabe 0')
                filepath_audiofile = ""
                samplerate = 48000
                mapping = None
                blocking = False
                loop = False
                length = 10.0
                '''
                playback_audiofile(filepath_audiofile,
                                   samplerate,
                                   mapping,
                                   blocking,
                                   loop,
                                   length)
                '''
                print("Test")
                filepath_of_wavfile = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav'
                playback_audiofile_from_usbdevice(filepath_of_wavfile)

            elif x == '1':
                path_folder = "delete_me"
                test_sounddevice_record(path_folder, duration_in_sec=20)
                return 0

            elif x == '2':
                list_1 = query_devices()
                print(list_1)




    def create_menubar(self):
        # Defining QMenuBar "menubar_mainwindow"
        self.menubar_mainwindow = QMenuBar(self)
        self.setMenuBar(self.menubar_mainwindow)

        # Adding menu
        # self.menuFile = self.menubar_mainwindow.addMenu(self)
        # self.menu_settings = QMenu(self)

        # Adding menu "File":
        self.menu_file = QMenu("File", self)
        self.menubar_mainwindow.addMenu(self.menu_file)
        # self.action_new_project.setShortcut("Ctrl+S")

        '''
        NewTestsetAct = QAction(QIcon('exit.png'), '&New Testset', self)
        NewTestsetAct.setShortcut('Ctrl+N')
        NewTestsetAct.setStatusTip('New Testset application')
        # NewTestsetAct.triggered.connect(qApp.quit)
        '''

        # Defining QAction "action_new_testset", "action_open_testset" and "action_quit_program"
        self.action_new_measurement = QAction("New Measurement", self)
        self.action_new_measurement.setShortcut('Ctrl+M')
        self.action_new_measurement.setStatusTip('Open editor for a new Testset')

        self.action_open_measurement = QAction("Open Measurement", self)
        self.action_open_measurement.setShortcut('Ctrl+O')
        self.action_open_measurement.setStatusTip('Open existing Testset')


        self.action_quit_program = QAction("Quit Program", self)
        self.action_quit_program.setShortcut('Ctrl+Q')
        self.action_quit_program.setStatusTip('Close AuToBo')

        # Adding QAction "action_new_testset", "action_open_testset" and "action_quit_program" to the QMenu "menu_file"
        self.menu_file.addAction(self.action_new_measurement)
        self.menu_file.addAction(self.action_open_measurement)

        self.menu_file.addAction(self.action_quit_program)

        # Open QDialog "NewProjectConfigurator":
        # self.action_new_project.triggered.connect(self.action_triggered_new_project)
        # Open QDialog "LoadExistingProjectConfigurator":
        # self.action_open_project.triggered.connect(self.action_triggered_open_project)
        # Close the program with the "Quit_Program"-Action:
        # self.action_quit_program.triggered.connect(self.action_triggered_quit_program)

        self.action_new_measurement.triggered.connect(self.action_triggered_new_audio_measurement)


        #self.action_check_crc.triggered.connect(self.action_triggered_check_crc)
        self.action_quit_program.triggered.connect(self.action_triggered_quit_program)

        # Adding menu "Settings":
        self.menu_settings = self.menubar_mainwindow.addMenu("Settings")
        self.action_settings = QAction("Change Settings", self)

        self.menu_settings.addAction(self.action_settings)
        self.action_settings.triggered.connect(self.action_triggered_change_settings)
        # Open QDialog "Change_Settings_MainWindow":
        # self.action_settings.triggered.connect(self.action_triggered_change_settings)

        # Adding menu "Help":
        self.menu_help = QMenu("Help", self)
        self.menubar_mainwindow.addMenu(self.menu_help)
        self.action_documentation = QAction("Documentation", self)
        self.action_version = QAction("Version", self)
        self.action_sourcecode = QAction("Source Code", self)
        self.action_debug = QAction("Debug", self)
        self.menu_help.addAction(self.action_documentation)
        self.menu_help.addAction(self.action_version)
        self.menu_help.addAction(self.action_sourcecode)
        self.menu_help.addAction(self.action_debug)

    ####################################################################################################################
    # Initialisizing all Mainwindow 'mainwindow' elements:
    ####################################################################################################################

    def create_toolbar(self):
        self.toolbar_mainwindow = QToolBar(self)
        self.addToolBar(self.toolbar_mainwindow)
        self.toolbar_mainwindow.addAction("Tool1")

    def create_statusbar(self):
        self.statusbar_mainwindow = QStatusBar(self)
        self.statusbar_mainwindow.showMessage("V0.0 - 23.08.2018")
        self.setStatusBar(self.statusbar_mainwindow)

    def create_dockwidget(self, dockwidgetcontent):
        self.dockwidget_mainwindow = QDockWidget("DockWidget", self)
        self.dockwidget_mainwindow.setMinimumSize(500, 400)
        self.dockwidget_mainwindow.setAllowedAreas(Qt.TopDockWidgetArea)
        self.dockwidget_mainwindow.setWidget(dockwidgetcontent)
        self.addDockWidget(Qt.TopDockWidgetArea, self.dockwidget_mainwindow)



    ####################################################################################################################
    # Methods related to QMenu 'menu_file'
    ####################################################################################################################

    def action_triggered_new_audio_measurement(self):

        self.widget_new_audio_measurement = Widget_New_Audio_Measurement()

        # Dialog einbauen, der eine Instanz von Audio_Measurement erstellt:
        dialog_add_audio_measurement = Dialog_Add_Audio_Measurement()

        self.tabwidget_mainwindow.addTab(self.widget_new_audio_measurement, "New Measurement")

    def action_triggered_quit_program(self):
        # This method closes the program
        sys.exit(0)

    ####################################################################################################################
    # Methods related to QMenu 'menu_settings'
    ####################################################################################################################

    def action_triggered_change_settings(self):
        self.widget_change_settings = Widget_Change_Settings()
        self.tabwidget_mainwindow.addTab(self.widget_change_settings, "Change Settings")

    ####################################################################################################################
    # Methods related to QTabWidget
    ####################################################################################################################

    def remove_tab(self, index, tab_title=''):
        message_box = QMessageBox()
        message_box.setWindowTitle('AuToBo - Audio Toolbox')
        # message_box.setWindowIcon()

        tab_text = self.tabwidget_mainwindow.tabText(self.tabwidget_mainwindow.currentIndex())
        message_box.setText('Do you certainly want to close the tab \'' + tab_text + '\' ?')
        message_box.addButton(QMessageBox.No)
        message_box.addButton(QMessageBox.Yes)
        message_box.setDefaultButton(QMessageBox.No)
        if message_box.exec() == QMessageBox.Yes:
            # The QTabWidget '' will be closed:
            self.tabwidget_mainwindow.removeTab(index)
        else:
            message_box.close()

    def rename_tab(self, index):
        input_dialog = QInputDialog(self)
        input_dialog.setGeometry(3000, 200, 2000, 100)

        tab_title = input_dialog.getText(self, 'Tab Renaming', 'New Tab Title:')
        # tab_title.setValidator()

        self.tabwidget_mainwindow.setTabText(self.tabwidget_mainwindow.currentIndex(), tab_title[0])

















