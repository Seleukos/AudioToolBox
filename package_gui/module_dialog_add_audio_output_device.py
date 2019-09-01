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
    def __init__(self, test):

        super().__init__()

        self.initui(test)

    def initui(self, test):

        gridlayout = QGridLayout(self)

        #name = test['name']
        #print(name)

        combobox = QComboBox(self)
        combobox.addItem('Test')
        combobox.addItem('Test')
        combobox.addItem('Test')
        combobox.addItem('Test')
        #combobox.currentIndexChanged.connect()

        gridlayout.addWidget(QLabel("Selected Audio Device:"), 0, 0, 1, 1)
        gridlayout.addWidget(combobox, 0, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 2, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 3, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 4, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 5, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 6, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 7, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 8, 1, 1, 1)
        gridlayout.addWidget(QLabel(""), 9, 1, 1, 1)



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
        pass


