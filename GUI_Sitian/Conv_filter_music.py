# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:10:52 2018

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
    

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018\cut'
file = 'Filter_FL_0.wav'
Filter_0 = Read_sweep_file(os.path.join(path,file))[:-1][0]

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
file = 'test_music.wav'
Music = Read_sweep_file(os.path.join(path,file))[:-1][0]

Filter_0_ch0 = Filter_0[0]
Filter_0_ch1 = Filter_0[1]

Music_ch0 = Music[0]
Music_ch1 = Music[1]
# both using music channel 0
Music_out0_ch0 = np.convolve(Music_ch0, Filter_0_ch0, mode='full')
Music_out0_ch1 = np.convolve(Music_ch1, Filter_0_ch1, mode='full')

Music_out0 = np.zeros([2,len(Music_out0_ch0)])
Music_out0[0,:] = Music_out0_ch0
Music_out0[1,:] = Music_out0_ch1

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
filename_Music0_wav = 'Music_out_m45.wav'
scipy.io.wavfile.write(os.path.join(path,filename_Music0_wav), 48000, np.real(Music_out0.T))

#########################################################################################################

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018\cut'
file = 'Filter_FL_m45.wav'
Filter_m45 = Read_sweep_file(os.path.join(path,file))[:-1][0]

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
file = 'test_music.wav'
Music = Read_sweep_file(os.path.join(path,file))[:-1][0]

Filter_m45_ch0 = Filter_m45[0]
Filter_m45_ch1 = Filter_m45[1]

Music_ch0 = Music[0]
Music_ch1 = Music[1]
# both using music channel 0
Music_outm45_ch0 = np.convolve(Music_ch0, Filter_m45_ch0, mode='full')
Music_outm45_ch1 = np.convolve(Music_ch1, Filter_m45_ch1, mode='full')

Music_outm45 = np.zeros([2,len(Music_outm45_ch0)])
Music_outm45[0,:] = Music_outm45_ch0
Music_outm45[1,:] = Music_outm45_ch1

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
filename_Musicm45_wav = 'Music_out_m45.wav'
scipy.io.wavfile.write(os.path.join(path,filename_Musicm45_wav), 48000, np.real(Music_outm45.T))

#########################################################################################################

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_19_08_2018\cut'
file = 'Filter_FL_45.wav'
Filter_45 = Read_sweep_file(os.path.join(path,file))[:-1][0]

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
file = 'test_music.wav'
Music = Read_sweep_file(os.path.join(path,file))[:-1][0]

Filter_45_ch0 = Filter_45[0]
Filter_45_ch1 = Filter_45[1]

Music_ch0 = Music[0]
Music_ch1 = Music[1]
# both using music channel 0
Music_out45_ch0 = np.convolve(Music_ch0, Filter_45_ch0, mode='full')
Music_out45_ch1 = np.convolve(Music_ch1, Filter_45_ch1, mode='full')

Music_out45 = np.zeros([2,len(Music_out45_ch0)])
Music_out45[0,:] = Music_out45_ch0
Music_out45[1,:] = Music_out45_ch1

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
filename_Music45_wav = 'Music_out_45.wav'
scipy.io.wavfile.write(os.path.join(path,filename_Music45_wav), 48000, np.real(Music_out45.T))


Music_out22 = np.zeros([2,len(Music_out45_ch0)])
Music_out22[0,:] = Music_out45_ch0/2 + Music_out0_ch0/2
Music_out22[1,:] = Music_out45_ch1/2 + Music_out0_ch1/2
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
filename_Music22_wav = 'Music_out_22.wav'
scipy.io.wavfile.write(os.path.join(path,filename_Music22_wav), 48000, np.real(Music_out22.T))


Music_outm22 = np.zeros([2,len(Music_out45_ch0)])
Music_outm22[0,:] = Music_outm45_ch0/2 + Music_out0_ch0/2
Music_outm22[1,:] = Music_outm45_ch1/2 + Music_out0_ch1/2
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
filename_Musicm22_wav = 'Music_out_m22.wav'
scipy.io.wavfile.write(os.path.join(path,filename_Musicm22_wav), 48000, np.real(Music_outm22.T))





####################################################################################################
# conv with new filter get on 02012019


path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019\cut\Filters'
file = 'Filter_FL_output_cut_test_2_48000_120002.wav'
Filter_P1 = Read_sweep_file(os.path.join(path,file))[:-1][0]

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian'
file = 'test_music.wav'
Music = Read_sweep_file(os.path.join(path,file))[:-1][0]

Filter_P1_ch0 = Filter_P1[0]
Filter_P1_ch1 = Filter_P1[1]

Music_ch0 = Music[0]
Music_ch1 = Music[1]
# both using music channel 0
Music_outP1_ch0 = np.convolve(Music_ch0, Filter_P1_ch0, mode='full')
Music_outP1_ch1 = np.convolve(Music_ch1, Filter_P1_ch1, mode='full')

Music_outP1 = np.zeros([2,len(Music_outP1_ch0)])
Music_outP1[0,:] = Music_outP1_ch0
Music_outP1[1,:] = Music_outP1_ch1

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019\cut\Music'
filename_MusicP1_wav = 'Music_outP1_cut_test_2.wav'
scipy.io.wavfile.write(os.path.join(path,filename_MusicP1_wav), 48000, np.real(Music_outP1.T))


####################################################################################################
# Conv with input not music
path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019\cut\Filters'
file = 'Filter_FL_output_3_48000_310002.wav'
Filter_P1 = Read_sweep_file(os.path.join(path,file))[:-1][0]

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019\cut\input'
file = 'input_sweep_2.wav'
Music = Read_sweep_file(os.path.join(path,file))[:-1][0]

Filter_P1_ch0 = Filter_P1[0]*0.1
Filter_P1_ch1 = Filter_P1[1]*0.1

Music_ch0 = Music
Music_ch1 = Music
# both using music channel 0
Music_outP1_ch0 = np.convolve(Music_ch0, Filter_P1_ch0, mode='full')
Music_outP1_ch1 = np.convolve(Music_ch1, Filter_P1_ch1, mode='full')

Music_outP1 = np.zeros([2,len(Music_outP1_ch0)])
Music_outP1[0,:] = Music_outP1_ch0
Music_outP1[1,:] = Music_outP1_ch1

path = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\09_Dokumenten\04_Sitian\Messung_02_01_2019\cut\out_rec'
filename_MusicP1_wav = 'rebuild_out_2.wav'
scipy.io.wavfile.write(os.path.join(path,filename_MusicP1_wav), 48000, np.real(Music_outP1.T))