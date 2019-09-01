########################################################################################################################
# module_widget_new_audio_measurement
########################################################################################################################

from PyQt5.Qt import *

# imports for sounddevice
import sounddevice as sd

# import of moduls
from package_algorithms.module_audiofile_functions import*
from package_algorithms.module_audio_measurement import *
from package_algorithms.module_sounddevice import *
from package_gui.module_dialog_add_audio_output_device import *


class Widget_New_Audio_Measurement(QWidget):
    def __init__(self):

        super().__init__()
        #self.tab_index = 0

        #self.messagebox_defined_parameters = QMessageBox(self)


        # Important:
        self.indices_audiodevice = []

        self.initui()

    def initui(self):

        # Window-Title of QWidget 'Widget_Check_CRC'
        self.windowname_new_audiodevicetest = 'New Audio Device Test'
        self.setWindowTitle("%s" % self.windowname_new_audiodevicetest)
        ################################################################################################################
        # QGridLayout 'gridlayout_lv0'
        ################################################################################################################

        self.gridlayout_lv0 = QGridLayout(self)
        self.gridlayout_lv0.addWidget(self.create_groupbox_measurement_settings())
        self.gridlayout_lv0.addWidget(self.create_groupbox_dut_settings())
        self.gridlayout_lv0.addWidget(self.create_groupbox_audio_output_devices())
        self.gridlayout_lv0.addWidget(self.create_groupbox_audio_input_devices())
        self.gridlayout_lv0.addWidget(self.create_groupox_audio_measurement_control_board())


        ################################################################################################################
        # QGroupBox 'groupbox_testset_selection'
        ################################################################################################################

        #self.create_groupbox_audio_devices_testing()

        ###### test



        #self.link_playback_audiofile_from_usbdevice(self.indices_audiodevice)

        ####################################################################################################################
        # QGroupBox 'groupbox_testset_selection'
        ####################################################################################################################

    def link_playback_audiofile_from_usbdevice(self, indices_audiodevice):
        playback_audiofile_from_usbdevice(indices_audiodevice)

        return 0

    def create_groupbox_measurement_settings(self):
        groupbox = QGroupBox(self)
        groupbox.setTitle('Measurement Settings')

        return groupbox

    def create_groupbox_measurement_settings(self):
        groupbox = QGroupBox(self)
        groupbox.setTitle('Measurement Settings')

        return groupbox

    def create_groupbox_dut_settings(self):
        groupbox = QGroupBox(self)
        groupbox.setTitle('DUT Settings')

        return groupbox

    def create_groupbox_audio_output_devices(self):
        groupbox = QGroupBox(self)
        groupbox.setTitle('Audio Output Devices')

        number_audio_output_devices = 10

        gridlayout = QGridLayout(self)
        list_headers = ["Sequence Number",
                        "Name",
                        "Starting Time",
                        "Ending Time",
                        "Playback Settings",
                        "Playback",
                        "Delete"]

        for index in range(len(list_headers)):
            gridlayout.addWidget(QLabel(list_headers[index]), 0, index, 1, 1)

        for i in range(number_audio_output_devices):
            gridlayout.addWidget(QLabel("Sequence Number"), i+1, 0, 1, 1)

        for i in range(number_audio_output_devices):
            gridlayout.addWidget(QLineEdit("Name"), i+1, 1, 1, 1)

        for i in range(number_audio_output_devices):
            gridlayout.addWidget(QLineEdit("Starting Time"), i+1, 2, 1, 1)

        for i in range(number_audio_output_devices):
            gridlayout.addWidget(QLineEdit("Ending Time"), i+1, 3, 1, 1)

        #pushbuttons_playback_settings = []

        for i in range(number_audio_output_devices):
            #pushbuttons_playback_settings.append(QPushButton("Playback Settings"))
            gridlayout.addWidget(QPushButton("Playback Settings"), i+1, 4, 1, 1)

        for i in range(number_audio_output_devices):
            gridlayout.addWidget(QPushButton("Playback"), i+1, 5, 1, 1)

        for i in range(number_audio_output_devices):
            gridlayout.addWidget(QPushButton("Delete"), i+1, 6, 1, 1)

        pushbutton_add_audio_output_device = QPushButton("Add Audio Output Device")
        pushbutton_add_audio_output_device.clicked.connect(self.pushbutton_add_audio_output_device_clicked)
        gridlayout.addWidget(pushbutton_add_audio_output_device, number_audio_output_devices+1, 6, 1, 1)

        '''
        #list_dev = get_device_number_if_audio_outputdevice_all(dict_devices)
        print("Output_devices")
        list_output_devices = sd.query_devices()
        print(list_output_devices)

        #for dict_audiodevice in list_output_devices:
         #   print(dict_audiodevice)

        # Ausgabe der Spalte mit allen Output Devices:
        i = 0
        for dict_audiodevice in list_output_devices:
            print('test')
            print(dict_audiodevice)
            device_name = dict_audiodevice['']

            print('test')
            test = QLabel(device_name)
            self.gridlayout_output_devices.addWidget(test, i, 0, 1, 1)
            i = i+1
        '''

        groupbox.setLayout(gridlayout)



        '''
                print(self.list_audiodevices)
        
                # list -> transform given input (tuple) into a list
                # filter -> sorts the given tuple or lsit
                # map -> (function which takes everey item of the list, list)
                # get_device_number_if_usb_soundcard _> thats the function which is used for every item of index_info)
                # index_info
                # sounddevice.query_devices()
                audio_outputdevice_indices = list(filter(lambda x: x is not False,
                                                         map(get_device_number_if_audio_outputdevice_all,
                                                             [index_info for index_info in
                                                              enumerate(sounddevice.query_devices())])))
        
        
        
                print("Discovered the following audio output devices", audio_outputdevice_indices)
        '''

        return groupbox

    def create_groupbox_audio_input_devices(self):
        groupbox = QGroupBox(self)
        groupbox.setTitle('Audio Input Devices')

        number_audio_output_devices = 10

        gridlayout = QGridLayout(self)

        for i in range(10):
            gridlayout.addWidget(QLabel("Index"), i+1, 1, 1, 1)

        for i in range(10):
            gridlayout.addWidget(QLineEdit("Name"), i+1, 2, 1, 1)

        for i in range(10):
            gridlayout.addWidget(QLineEdit(""), i+1, 3, 1, 1)

        for i in range(10):
            gridlayout.addWidget(QPushButton("Output File Save Path"), i+1, 4, 1, 1)

        for i in range(10):
            gridlayout.addWidget(QPushButton("Record Settings"), i+1, 5, 1, 1)

        for i in range(10):
            gridlayout.addWidget(QPushButton("Record"), i+1, 6, 1, 1)

        for i in range(10):
            gridlayout.addWidget(QPushButton("Delete"), i+1, 7, 1, 1)

        groupbox.setLayout(gridlayout)

        return groupbox

    def create_groupox_audio_measurement_control_board(self):
        groupbox = QGroupBox(self)
        groupbox.setTitle('Audio Measurement Control Board')

        gridlayout = QGridLayout(self)
        gridlayout.addWidget(QLabel("Load Audio Measurement"), 0, 0, 1, 1)
        gridlayout.addWidget(QLabel("Save Audio Measurement"), 1, 0, 1, 1)
        gridlayout.addWidget(QLabel("3"), 2, 0, 1, 1)
        gridlayout.addWidget(QLineEdit("1"), 0, 1, 1, 1)
        gridlayout.addWidget(QLineEdit("2"), 1, 1, 1, 1)
        gridlayout.addWidget(QLineEdit("3"), 2, 1, 1, 1)



        gridlayout.addWidget(QLabel("Delay before Start"), 3, 0, 1, 1)
        gridlayout.addWidget(QLineEdit("1 sec"), 3, 1, 1, 1)

        gridlayout.addWidget(QPushButton("Load Audio Measurement"), 0, 2, 1, 1)
        gridlayout.addWidget(QPushButton("Save Audio Measurement"), 1, 2, 1, 1)
        gridlayout.addWidget(QPushButton("Start Audio Measurement"), 3, 2, 1, 1)

        groupbox.setLayout(gridlayout)

        return groupbox

    def button_xy_clicked(self):

        self.dialog = QDialog(self)

    def button_playback_clicked(self):

        playback_audiofile(filepath_audiofile='1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav',
                       samplerate=None,
                       mapping=None,
                       blocking=False,
                       loop=False,
                       length=0)

        return 0

    @pyqtSlot()
    def button_start_audio_measurement_clicked(self):

        start_audio_measurement()
        return 0

    @pyqtSlot()
    def pushbuttons_playback_settings_clicked(self):
        print("Test...hat funktioniert!")
        return 0

    @pyqtSlot()
    def pushbutton_add_audio_output_device_clicked(self):
        print("Test...hat funktioniert!")
        test = sd.query_devices('output')
        print(test)
        self.dialog = Dialog_Add_Audio_Output_Device(self)
        self.dialog.show()
        return 0

    @pyqtSlot()
    def pushbutton_load_audio_measurement(self):


        pass

    @pyqtSlot()
    def pushbutton_save_audio_measurement(self):


        pass





