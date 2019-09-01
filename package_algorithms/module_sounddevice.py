import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

import matplotlib.pyplot as plt
import soundfile as sf
import subprocess
import argparse

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def playback_audiofile(filepath_audiofile='1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav',
                       samplerate=None,
                       mapping=None,
                       blocking=False,
                       loop=False,
                       length=0):

    audio_data, _ = sf.read(filepath_audiofile, dtype=DATA_TYPE)
    index = 3
    DATA_TYPE = '' #############################
    output = sd.OutputStream(
        device=index,
        dtype=DATA_TYPE
    )
    output.start()
    filepath_audiofile = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav'

    with open('1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav', 'rb') as f:
        data, samplerate = sf.read(f)

    dict_device_information = sd.query_devices()

    tesblblbalt=sd.query_hostapis()

    length= len(dict_device_information)

    #sd.check_output_settings(device=, channels=)

    print("test")
    mapping = [None, None, None, None, 4]
    print(mapping)
    sd.play(data, samplerate=samplerate, mapping=mapping, blocking=blocking, loop=loop)
    print("Geschafft")
    sd.wait()
    sd.stop()
    print("Finished!")

    return None



def test_sounddevice_record(path, duration_in_sec):

    fs = 44100  # sample rate
    duration_in_sec = 20  # duration of recording

    myrecording = sd.rec(int(duration_in_sec * fs),
                         samplerate=fs,
                         channels=2)

    sd.wait()  # wait until recording is finished

    write('output.wav', fs, myrecording)  # save as wav.-file

    plt.plot(myrecording)




def query_devices(device=None, kind=None):

    dict_device_information = sd.query_devices()

    print(dict_device_information)




def test_sounddevice_status():
    sd.get_status()



def check_input_settings(device=None,
                         channels=None,
                         dtype=None,
                         extra_settings=None,
                         samplerate=None):

    input_settings = sd.check_input_settings(device=device,
                                             channels=channels,
                                             dtype=dtype,
                                             extra_settings=extra_settings,
                                             samplerate=samplerate)

    print(input_settings)
    
    #sd.check_output_settings()
        
    #sd.get_portaudio_version()
        
    #sd.get_stream()
    
    
    
    #sd._check_mapping()


def measure_latency_dut():
    print("...")
    pass

def measure_latency_mesauringchain():
    print("...")
    pass

def measurement(filepath_mixingprogram):

    def define_metadata():
        pass

    def open_totalmix_rme():
        pass

    def output():
        pass

    def input():

        pass



    filepath_mixingprogram = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\Visio 2016.lnk'
    filepath_snapshot_rme= r''
    subprocess.Popen("%s %s" % (filepath_mixingprogram, filepath_snapshot_rme))





























