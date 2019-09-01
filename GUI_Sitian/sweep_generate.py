# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:09:22 2019
    sweep generator
@author: s01li
"""

import numpy as np
import matplotlib.pyplot as plt

import os.path
import scipy.io.wavfile
import soundfile as sf


def Read_sweep_file(filename):
    eval_file, fs    =   sf.read(filename,dtype='float32')
    return([eval_file.T, fs])
    

def sweep_generator(L, f0, f1, fs):
    # input: L:  signal length in sec
    #        f0: start freq
    #        f1: stop freq
    #        fs: sampling freq
    
    num = fs*L
    t = np.linspace(0,L,num)
    #beta = (f1-f0)/(L**2)
    #f = f0 + beta*t**2
    beta = (f1/f0)**(1/L)
    f = f0 + beta**t
    out_sig = np.sin(2*np.pi*f*t)
    plt.plot(out_sig)
    
    filename_write = 'sweep.wav'
    path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\try_sweep_generator'
    scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_sig.T)
    
    out_sig_f = np.fft.rfft(out_sig)
    plt.plot(out_sig_f)
    
    return out_sig


f0 = 20
f1 = 20000
L  = 10
fs = 48000


#### test with one sweep

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Filter'
file = 'sweepSignal_log_4s_24000.wav'
input_sweep = Read_sweep_file(os.path.join(path,file))[:-1][0]

input_sweep_f = np.fft.rfft(input_sweep)

plt.plot(input_sweep_f)