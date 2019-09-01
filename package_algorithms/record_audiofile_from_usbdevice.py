import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

import matplotlib.pyplot as plt
import soundfile as sf
import subprocess
import argparse

def test_sounddevice_record(path):

    fs = 44100  # sample rate
    seconds = 5  # duration of recording

    myrecording = sd.rec(int(seconds * fs),
                         samplerate=fs,
                         channels=2)

    sd.wait()  # wait until recording is finished

    write('output.wav', fs, myrecording)  # save as wav.-file

    plt.plot(myrecording)
