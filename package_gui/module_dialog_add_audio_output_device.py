########################################################################################################################
# module_dialog_add_audio_output_device
########################################################################################################################

from PyQt5.Qt import *

# imports for sounddevice
import sounddevice as sd

# import of moduls
from package_algorithms.module_audiofile_functions import*
from package_algorithms.module_audio_measurement import *
from package_algorithms.module_sounddevice import *


class Dialog_Add_Audio_Output_Device(QDialog):
    def __init__(self):

        super().__init__()

        self.initui()

    def initui(self):
        #self.setWindowTitle('Dialog')
        #self.setGeometry(200, 200, 200, 200)
        print("DIALOG Add Audio Device")


        self.gridlayout = QGridLayout(self)

        combobox = QComboBox(self)

        list_devices = sd.query_devices()

        for dict_device_index in range(len(list_devices)):
            dict_device = list_devices[dict_device_index]
            name = dict_device["name"]
            print(name)
            combobox.addItem(name)

        combobox.currentIndexChanged.connect(self.indexchanged)

        self.gridlayout.addWidget(QLabel("Selected Audio Device:"), 0, 0, 1, 1)
        self.gridlayout.addWidget(combobox, 0, 1, 1, 1)
        self.gridlayout.addWidget(QLabel("name_measurement"), 2, 0, 1, 1)
        self.gridlayout.addWidget(QLabel(""), 3, 1, 1, 1)
        self.gridlayout.addWidget(QLabel("filepath_audiofile"), 4, 0, 1, 1)
        self.gridlayout.addWidget(QLabel(""), 5, 1, 1, 1)
        self.gridlayout.addWidget(QLabel("id_output_device,"), 6, 0, 1, 1)
        self.gridlayout.addWidget(QLabel(""), 7, 1, 1, 1)
        self.gridlayout.addWidget(QLabel("id_input_device,"), 8, 0, 1, 1)
        self.gridlayout.addWidget(QLabel(""), 9, 1, 1, 1)
        self.gridlayout.addWidget(QLabel("filepath_recordfile"), 9, 0, 1, 1)
        self.gridlayout.addWidget(QLabel("filepath_recordfile"), 10, 1, 1, 1)

        self.show()
        
    def indexchanged(self):
        print("Eererer")

    '''
    def button_add_audio_device_clicked(self):

        audiodevice = AudioMeasurement.AudioDevice()
        self.x_position = 0
        self.y_position = 0
        self.settings = 0
        self.infos = ''
        
    '''


class Dialog_Add_Audio_Measurement(QDialog):
    def __init__(self):

        super().__init__()

        self.initui()

    def initui(self):
        self.setWindowTitle('Dialog')
        self.setWindowModality(Qt.ApplicationModal)
        print("DIALOG1111111!!!!")
        #self.setGeometry(200, 200, 200, 200)

        gridlayout = QGridLayout(self)

        combobox = QComboBox(self)

        #for item in sd.query_devices():
            #combobox.addItem(item)

        #combobox.currentIndexChanged.connect()

        gridlayout.addWidget(QLabel("Selected Audio Device:"), 0, 0, 1, 1)
        gridlayout.addWidget(combobox, 0, 1, 1, 1)
        gridlayout.addWidget(QLineEdit("Textblock"), 1, 1, 1, 2)
        gridlayout.addWidget(QLabel("name_measurement"), 2, 0, 1, 1)
        gridlayout.addWidget(QLineEdit(""), 2, 1, 1, 1)
        gridlayout.addWidget(QLabel("filepath_audiofile"), 4, 0, 1, 1)
        gridlayout.addWidget(QLineEdit(""), 4, 1, 1, 1)
        gridlayout.addWidget(QLabel("id_output_device,"), 6, 0, 1, 1)
        gridlayout.addWidget(QLineEdit(""), 6, 1, 1, 1)
        gridlayout.addWidget(QLabel("id_input_device,"), 7, 0, 1, 1)
        gridlayout.addWidget(QLineEdit(""), 7, 1, 1, 1)
        gridlayout.addWidget(QLabel("filepath_recordfile"), 9, 0, 1, 1)
        gridlayout.addWidget(QLineEdit(""), 9, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 10, 0, 1, 1)
        gridlayout.addWidget(QPushButton("Ok"), 10, 1, 1, 1)

        self.show()



