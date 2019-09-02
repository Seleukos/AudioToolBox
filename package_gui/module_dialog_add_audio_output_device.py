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
        self.setWindowTitle('Dialog')
        self.setGeometry(200, 200, 200, 200)
        print("DIALOG22222222!!!!")


        gridlayout = QGridLayout(self)

        #name = test['name']
        #print(name)

        combobox = QComboBox(self)

        #for item in sd.query_devices():
            #combobox.addItem(item)

        #combobox.currentIndexChanged.connect()
        '''
        gridlayout.addWidget(QLabel("Selected Audio Device:"), 0, 0, 1, 1)
        gridlayout.addWidget(combobox, 0, 1, 1, 1)
        gridlayout.addWidget(QLabel("name_measurement"), 2, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 3, 1, 1, 1)
        gridlayout.addWidget(QLabel("filepath_audiofile"), 4, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 5, 1, 1, 1)
        gridlayout.addWidget(QLabel("id_output_device,"), 6, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 7, 1, 1, 1)
        gridlayout.addWidget(QLabel("id_input_device,"), 8, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 9, 1, 1, 1)
        gridlayout.addWidget(QLabel("filepath_recordfile"), 9, 1, 1, 1)
        gridlayout.addWidget(QLabel("filepath_recordfile"), 10, 1, 1, 1)

        '''

        self.show()



    def button_add_audio_device_clicked(self):

        audiodevice = AudioDevice()
        audiodevice.name = ''
        audiodevice.param1 = ''
        audiodevice.param2 = ''
        audiodevice.param3 = ''
        audiodevice.param4 = ''

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



