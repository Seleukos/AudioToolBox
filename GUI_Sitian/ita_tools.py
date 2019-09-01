# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:10:18 2018

@author: s01li

This code is based on 
https://git.rwth-aachen.de/ita/toolbox/blob/master/kernel/DSP/Arithmetic/ita_invert_spk_regularization.m

rewrite in Python
deal with only single channel
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

import os.path
import scipy.io.wavfile
import soundfile as sf

def ita_xfade_spk(a, b, x_fade_vec, fs, Args_beta):
    # input: x_fade_vec, range of smoothing the amp change
    # prep
    f0 = x_fade_vec[0]
    f1 = x_fade_vec[1]
    nBins = len(a)
    
    bin_dist = fs/(2*(nBins-1))
    bin0 = int(round(f0/bin_dist)+1)
    bin1 = int(round(f1/bin_dist)+1)
    bins = bin1 - bin0
    # hanning window
    win = np.hanning(2*bins+1)
    leftwin  = win[0: int(np.ceil((2*bins+1)/2))]
    rightwin = win[int(np.ceil((2*bins+1)/2)-1):] 
    # crossfading
    a[bin0-1:bin1]   =   a[bin0-1:bin1]*rightwin
    a[bin1:]         =   0
    b[0:bin0]        =   0
    b[bin0-1:bin1]   =   b[bin0-1:bin1]*leftwin
    
    # return epsilon
    return a+b

def ita_conj(data):
    return np.conjugate(data)

def ita_amplify(data, amp_factor):
    return data*amp_factor

def ita_invert_spk_regularization(data, freq_vec, fs):
    # data: freq domain signal
    Args_beta = 1e-10
    
    f_low  = freq_vec[0]
    f_high = freq_vec[1]
    
    nBins = len(data)
    a = np.zeros(nBins) + 1
    b = np.zeros(nBins) + Args_beta
    
    epsilon = ita_xfade_spk(a,b, [f_low/np.sqrt(2), f_low], fs, Args_beta)
    
    c = np.zeros(nBins) + 1
    if f_high < min(f_high*np.sqrt(2),fs/2):
        epsilon = ita_xfade_spk(epsilon,c,[f_high, min(f_high*np.sqrt(2),fs/2)], fs, Args_beta)
    epsilon = epsilon**2
    epsilon = ita_amplify(epsilon, np.abs(data).max()**2 *50 / 100 )
    result = ita_conj(data) / (ita_conj(data)*data + epsilon);
    return result


