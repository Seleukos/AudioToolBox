# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:56:16 2018

@author: s01li
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

import os.path
import scipy.io.wavfile
import soundfile as sf


def Read_sweep_file(filename):
    eval_file, fs    =   sf.read(filename,dtype='float32')
    return([eval_file.T, fs])
    
### Fullscale ###
### Input Sweep Signal ###
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Filter'
file = 'sweepSignal_log_4s_24000.wav'
input_sweep = Read_sweep_file(os.path.join(path,file))[:-1][0]


### Output Signal m90 ###
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Messung'
file = '03_FL_P-90.wav'
out_put_m90 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([528294,528294+191941+1])
out_put_m90 = out_put_m90[:, cut_range[0]:cut_range[1]]

### Output Signal 0 ###
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Messung'
file = '07_FL_P0.wav'
out_put_0 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([539409,539409+191941+1])
out_put_0 = out_put_0[:, cut_range[0]:cut_range[1]]

### Output Signal 90 ###
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Messung'
file = '07_FL_P0.wav'
out_put_90 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([541662,541662+191941+1])
out_put_90 = out_put_90[:, cut_range[0]:cut_range[1]]


### need rms Value? ###

### write data ###
filename_write = 'input_sweep.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, input_sweep.T)

filename_write = 'out_put_m90.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_m90.T)

filename_write = 'out_put_0.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_0.T)

filename_write = 'out_put_90.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_90.T)

##############################################################################################################



### Output Signal 0 ###
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018'
file = 'FL_P0.wav'
out_put_0 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([593844-10000+8400+30,593844-10000+8400+30+191941+1])
out_put_0 = out_put_0[:, cut_range[0]:cut_range[1]]

### Output Signal m45 ###
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018'
file = 'FL_P1.wav'
out_put_m45 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([685844,685844+191941+1])
out_put_m45 = out_put_m45[:, cut_range[0]:cut_range[1]]

### Output Signal 45 ###
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018'
file = 'FL_P2.wav'
out_put_45 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([669199,669199+191941+1])
out_put_45 = out_put_45[:, cut_range[0]:cut_range[1]]




### write data ###

filename_write = 'out_put_m45.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018\cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_m45.T)

filename_write = 'out_put_0.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018\cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_0.T)

filename_write = 'out_put_45.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018\cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_45.T)

###############################################################################################################
# fuer kopfhoere
waves = []
cut_range = [np.array([46000,46000+191941+1]), 
             np.array([66000+50000,66000+50000+191941+1]),
             np.array([66000+40000,66000+40000+191941+1])]
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfhöre\Messung'
for i in range(1,7,2):
    file = 'VR_Kopfhörer_SMD269_Index'+str(i)+'_TimeSignal.wav'
    out_put = Read_sweep_file(os.path.join(path,file))[:-1][0]
    out_put = out_put[:, cut_range[int(i/2)][0]:cut_range[int(i/2)][1]]
    waves.append(out_put)
    filename_write = 'VR_Kopfhörer_SMD269_Index'+str(i)+'_TimeSignal_4s_cut.wav'
    path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfhöre\Messung'
    scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put.T)
    
    
#############################################################################################################


# fuer 1s Signal
    
# cut 1smp from input sweep
#path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Cut_1s'
#file = 'input_sweep.wav'
#outfile = Read_sweep_file(os.path.join(path,file))[:-1][0]
#cut_range = np.array([0,len(outfile)-1])        # need to change
#outfile = outfile[ cut_range[0]:cut_range[1]]

### write data ###
#filename_write = 'input_sweep.wav'
#path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Cut_1s'
#scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, outfile.T)
    



path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Messung'
file = '07_FL_P0.wav'
out_put_0 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([480000,480000+310001+1])        # need to change
out_put_0 = out_put_0[:, cut_range[0]:cut_range[1]]

### write data ###
filename_write = 'out_put_0.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\16.11.2018\VR_Fullscale\Kopfposition\Cut_1s'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_0.T)


##############################################################################################################
# cut new wav file get on 20190102

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019'
file = 'Measurement_1_all_mixdown.wav'
out_put_0 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([480000+477000,480000+477000+120001+1])        # need to change
out_put_0 = out_put_0[0, cut_range[0]:cut_range[1]]

filename_write = 'input_sweep_cut_test_2.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019\cut\input'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_0.T)


###################################

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019'
file = '0grad_FL_1.wav'
out_put_0 = Read_sweep_file(os.path.join(path,file))[:-1][0]
cut_range = np.array([466940+477000-290,466940+477000-290+120001+1])        # need to change
out_put_0 = out_put_0[:, cut_range[0]:cut_range[1]]

filename_write = 'output_cut_test_2.wav'
path_write = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019\cut'
scipy.io.wavfile.write(os.path.join(path_write,filename_write), 48000, out_put_0.T)