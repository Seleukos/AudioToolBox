# -*- coding: utf-8 -*-
"""
Created Nov 2018

@author: s01li

This code generates a GUI of the Toolbox
Read wav file from folder and calculate filters, write filters as wav file into folder
Convolution between signals and filters
"""

import numpy as np
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

import os.path
import soundfile as sf

import scipy.fftpack
import scipy.io.wavfile

def Read_sweep_file(filename):
    eval_file, fs    =   sf.read(filename,dtype='float32')
    return([eval_file.T, fs])

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.figure = Figure()
        self.axes1 = self.figure.add_subplot(211)
        self.axes1.set_ylabel('Filter Left')
        #self.axes1.hold(False)
        self.axes2 = self.figure.add_subplot(212)
        self.axes2.set_xlabel('freq')
        self.axes2.set_ylabel('Filter Right')
        #self.axes2.hold(False)
        self.canvas = FigureCanvas(self, -1, self.figure)
        # 1st row
        self.text_Eingangsignal = wx.StaticText(self, label='Input Signal')
        self.display_path_eingang = wx.ComboBox(self)
        self.button_fileauswahl_Ein = wx.Button(self, label='Choose File')
        # 2nd row
        self.text_Ausgangsignal = wx.StaticText(self, label='Output Signal')
        self.display_path_ausgang = wx.ComboBox(self)
        self.button_fileauswahl_Aus = wx.Button(self, label='choose Folder')
        self.button_fileauswahl_Aus2 = wx.Button(self, label = 'choose File')
        # 3rd row
        self.text_FilterParameter = wx.StaticText(self, label='Filter Parameter:')
        # 4th row
        self.text_SF = wx.StaticText(self, label = ' Sampling Rate: ')
        self.input_SF = wx.TextCtrl(self)
        self.text_bins = wx.StaticText(self, label = 'Bins: ')
        self.input_bins = wx.TextCtrl(self)
        # 5th row
        self.text_MeasurementParameter = wx.StaticText(self, label = 'Measurement Parameter: ')
        # 6th row
        self.text_RoomSize = wx.StaticText(self, label = 'Room Size: ')
        self.input_RoomSize = wx.TextCtrl(self)
        self.text_MeasurementLength = wx.StaticText(self, label = 'Measurement Length: ')
        self.input_MeasurementLength = wx.TextCtrl(self)
        # 7th row
        self.button_calc =wx.Button(self, label="View Filter")
        # 8th row        
        self.text_gespeichert = wx.StaticText(self, label='saved in: ')
        self.display_filter_path = wx.ComboBox(self)
        # 9th row
        self.text_filterLengthSuggested = wx.StaticText(self,label = 'Filter Length Suggested: ')
        self.display_filterLengthSuggested = wx.ComboBox(self)
        # 10th row
        self.text_Faltung = wx.StaticText(self, label = 'Convolution')
        # 11th row
        self.text_conv_signal = wx.StaticText(self, label = 'Signal')
        self.display_path_conv_signal = wx.ComboBox(self)
        self.button_fileauswahl_conv_signal2 = wx.Button(self, label = 'choose File')
        # 12th row
        self.text_conv_filter = wx.StaticText(self, label = 'Filter')
        self.display_path_conv_filter = wx.ComboBox(self)
        self.button_fileauswahl_conv_filter2 = wx.Button(self, label = 'chooseFile')
        # 13th row
        self.button_conv = wx.Button(self, label = 'View Filtered Result')
        # 14th row
        self.text_conv_gespeichert = wx.StaticText(self, label = 'saved in: ')
        self.display_conv_path = wx.ComboBox(self)
        
        
        # Binds:
        self.Bind(wx.EVT_BUTTON, self.OnClick_calc,self.button_calc)
        self.Bind(wx.EVT_BUTTON, self.OnClick_open_explore_ein,self.button_fileauswahl_Ein)
        self.Bind(wx.EVT_BUTTON, self.OnClick_open_explore_aus,self.button_fileauswahl_Aus)
        self.Bind(wx.EVT_BUTTON, self.OnClick_open_explore_file_aus, self.button_fileauswahl_Aus2)
        self.Bind(wx.EVT_BUTTON, self.OnClick_open_explore_conv_signal, self.button_fileauswahl_conv_signal2)
        self.Bind(wx.EVT_BUTTON, self.OnClick_open_explore_conv_filter, self.button_fileauswahl_conv_filter2)
        self.Bind(wx.EVT_BUTTON, self.OnClick_conv, self.button_conv)
        
        
        # Sizers:
        self.topSizer    = wx.BoxSizer(wx.VERTICAL)
        self.sizer_figure = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input5 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input6 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input7 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input8 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input9 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input10 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input11 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input12 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input13 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_input14 = wx.BoxSizer(wx.HORIZONTAL)
        
        # Allocate Elements to Sizers
        self.sizer_figure.Add(self.canvas)
        
        self.sizer_input1.Add(self.text_Eingangsignal, 1,0)
        self.sizer_input1.Add(self.display_path_eingang, 3,0)
        self.sizer_input1.Add(self.button_fileauswahl_Ein, 1,0)
        
        self.sizer_input2.Add(self.text_Ausgangsignal, 1,0)
        self.sizer_input2.Add(self.display_path_ausgang, 3,0)
        self.sizer_input2.Add(self.button_fileauswahl_Aus, 1,0) 
        self.sizer_input2.Add(self.button_fileauswahl_Aus2,1,0)
        
        self.sizer_input3.Add(self.text_FilterParameter,1,0)
        
        self.sizer_input4.Add(self.text_SF, 1,0, wx.ALL)
        self.sizer_input4.Add(self.input_SF, 1,0, wx.ALL)
        self.sizer_input4.Add(self.text_bins, 1,0, wx.LEFT)
        self.sizer_input4.Add(self.input_bins, 1,0, wx.ALL)
        
        self.sizer_input5.Add(self.text_MeasurementParameter)
        
        self.sizer_input6.Add(self.text_RoomSize, 1,0)
        self.sizer_input6.Add(self.input_RoomSize, 1,0)
        self.sizer_input6.Add(self.text_MeasurementLength, 1,0)
        self.sizer_input6.Add(self.input_MeasurementLength, 1,0)

        self.sizer_input7.Add(self.button_calc, 1,0)

        self.sizer_input8.Add(self.text_gespeichert, 1)
        self.sizer_input8.Add(self.display_filter_path, 3)
        
        self.sizer_input9.Add(self.text_filterLengthSuggested, 2)
        self.sizer_input9.Add(self.display_filterLengthSuggested, 3)
        
        self.sizer_input10.Add(self.text_Faltung, 3)
        
        self.sizer_input11.Add(self.text_conv_signal,1)
        self.sizer_input11.Add(self.display_path_conv_signal,3)
        self.sizer_input11.Add(self.button_fileauswahl_conv_signal2,1)
        
        self.sizer_input12.Add(self.text_conv_filter,1)
        self.sizer_input12.Add(self.display_path_conv_filter,3)
        self.sizer_input12.Add(self.button_fileauswahl_conv_filter2,1)
        
        self.sizer_input13.Add(self.button_conv, 1,0)
        
        self.sizer_input14.Add(self.text_conv_gespeichert, 1)
        self.sizer_input14.Add(self.display_conv_path, 3)
        
        # Add to top Sizers
        self.topSizer.Add(self.sizer_figure)
        self.topSizer.Add(self.sizer_input1)
        self.topSizer.Add(self.sizer_input2)
        self.topSizer.Add(self.sizer_input3)
        self.topSizer.Add(self.sizer_input4)
        self.topSizer.Add(self.sizer_input5)
        self.topSizer.Add(self.sizer_input6)
        self.topSizer.Add(self.sizer_input7)
        self.topSizer.Add(self.sizer_input8)
        self.topSizer.Add(self.sizer_input9)
        self.topSizer.Add(self.sizer_input10)
        self.topSizer.Add(self.sizer_input11)
        self.topSizer.Add(self.sizer_input12)
        self.topSizer.Add(self.sizer_input13)
        self.topSizer.Add(self.sizer_input14)
        
        self.SetSizer(self.topSizer)
        self.Fit()
        
        self.read_from_folder_flg = False
        
    
    def draw(self, signals, sf):
        # draw a waveform in the GUI
        freqs = np.linspace(0, sf/2, len(signals[0]))
        self.axes1.plot(freqs, signals[0])
        self.axes2.plot(freqs, signals[1])
        self.axes1.set_ylabel('Filter Left')
        self.axes2.set_xlabel('freq')
        self.axes2.set_ylabel('Filter Right')
        
    def calc_filter(self, raw_signal_ein, raw_signal_aus):
        # given two signals (in/out), the transfer function will be calculated, both time and freq domain
        # notice that this part contains normlization of the time signal, 
        # the freq domain is calculated from the normlized time signal!!
 
        print(raw_signal_ein.max())
        freq_signal_ein = np.fft.rfft(raw_signal_ein)
        freq_signal_aus = np.fft.rfft(raw_signal_aus)
        # use our ita regulaization
        trans_filter = freq_signal_aus*ita_invert_spk_regularization(freq_signal_ein, [20,20000], 48000)
        # similar function as ita toolbox (MATLAB) 'ita_write.m'
        filter_get_time = np.fft.irfft(trans_filter)*len(trans_filter)/2
        return filter_get_time, trans_filter
    
    def resample_filter(self, original_filter, sf):  
        # down-sampling of original filter, if we want to conv with a music/signal with lower sampling frequency
        srO = 48000    # original sampling rate
        srN = sf       # new sampling rate
        nO  = len(original_filter[0])   # length of original filter
        nN  = int(nO/srO*srN)           # length of new filter
        linO = np.linspace(0, 1, nO)
        linN = np.linspace(0, 1, nN)
        resampled_filter = np.zeros([2, nN])
        resampled_filter[0] = np.interp(linN, linO, original_filter[0])
        resampled_filter[1] = np.interp(linN, linO, original_filter[1])
        return resampled_filter
    

    def calc_norm(self, filter_get_time_chs):
        # calculate the norm regarding to all output positions
        filter_get_time_norm_chs = filter_get_time_chs/filter_get_time_chs.max()
        filter_get_freq_norm_chs = np.fft.rfft(filter_get_time_norm_chs)/len(filter_get_time_norm_chs[0])*np.sqrt(2)        
        return filter_get_freq_norm_chs, filter_get_time_norm_chs
        
    def OnClick_open_explore_ein(self, event):
        openFileDialog = wx.FileDialog(fr, "Open", "", "", 
                                      "", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        self.display_path_eingang.SetValue(openFileDialog.GetPath())
        self.ein_path = openFileDialog.GetPath()
        openFileDialog.Destroy()    

    def OnClick_open_explore_aus(self, event):
        self.read_from_folder_flg = True

        openFileDialog = wx.DirDialog (None, "Choose input directory", "",
                                       wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        
        openFileDialog.ShowModal()
        self.display_path_ausgang.SetValue(openFileDialog.GetPath())
        self.aus_path = openFileDialog.GetPath()
        openFileDialog.Destroy()
        
    def OnClick_open_explore_file_aus(self, event):
        self.read_from_folder_flg = False
        openFileDialog = wx.FileDialog(fr, "Open", "", "", 
                                      "", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        openFileDialog.ShowModal()
        self.display_path_ausgang.SetValue(openFileDialog.GetPath())
        self.aus_path = openFileDialog.GetPath()
        self.aus_path_dir = os.path.dirname(self.aus_path)
        self.aus_path_filename = os.path.basename(self.aus_path)
        
        openFileDialog.Destroy()  

    def OnClick_open_explore_conv_signal(self, event):
        openFileDialog = wx.FileDialog(fr, "Open", "", "", 
                                      "", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        self.display_path_conv_signal.SetValue(openFileDialog.GetPath())
        self.conv_signal_path_file = openFileDialog.GetPath()
        openFileDialog.Destroy()
        
    def OnClick_open_explore_conv_filter(self, event):
        openFileDialog = wx.FileDialog(fr, "Open", "", "", 
                                      "", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        self.display_path_conv_filter.SetValue(openFileDialog.GetPath())
        self.conv_filter_path_file = openFileDialog.GetPath()
        openFileDialog.Destroy()    

    def OnClick_calc(self, event):
        # after click we calculate the filter
        
        # check if we read output from file or folder
        if self.read_from_folder_flg == True:
            pos_LS = [x for x in os.listdir(self.aus_path) if x.lower().endswith('.wav')]
        else:
            # in this case we read from file, so there is only one loop
            pos_LS = [self.aus_path_filename]
        
        
        max_value_all = 0
        filter_get_time_chs_all = []
        
        
        for pos in pos_LS:
            # loop over all positions (outputs)
            filename_out = pos
            
            filter_resample_flg = False
            filter_cut_bins_flg = False
            
            # Check status
            sf = self.input_SF.GetValue()
            if sf != '':
                filter_resample_flg = True
                sf = int(sf)
            else:
                sf = 48000
                
            nr_bins = self.input_bins.GetValue()
            if nr_bins != '':
                filter_cut_bins_flg = True
                nr_bins = int(nr_bins)
            
            # read data from wav files
            # get raw data without sampling frequency 
            raw_info_ein = Read_sweep_file(self.ein_path)[:-1]
            if self.read_from_folder_flg == True:
                raw_info_aus = Read_sweep_file(os.path.join(self.aus_path,filename_out))[:-1]
            else:
                raw_info_aus = Read_sweep_file(self.aus_path)[:-1]
            
            # get signal as array data
            raw_info_aus = raw_info_aus[0]
            raw_info_ein = raw_info_ein[0]
            
            if np.shape(raw_info_aus)[0] == 1:
                Channel_Num = 1
            else:
                if len(raw_info_ein) == 1: # only one input channel
                    # repeat:
                    raw_info_ein = np.array([raw_info_ein,raw_info_ein])
                Channel_Num = np.shape(raw_info_aus)[0]
                filter_get_time_chs = np.zeros((Channel_Num, int(np.shape(raw_info_aus)[1])))*0.j
            for i in range(0, Channel_Num):  # for each channel calculate the filter
                if Channel_Num == 1:
                    raw_signal_ein = raw_info_ein
                    raw_signal_aus = raw_info_aus
                else:
                    raw_signal_ein = raw_info_ein
                    raw_signal_aus = raw_info_aus[i]
                filter_get_time, filter_get_freq = self.calc_filter(raw_signal_ein, raw_signal_aus) # calculate filters
                filter_get_time_chs[i,:] = filter_get_time
            # normalization between all channels (left right) this step only for plot not for following calculations
            trans_filter_norm_ch, trans_filter_time_norm_ch = self.calc_norm(np.real(filter_get_time_chs))
            # gether maximum for normallization
            max_value_pos = filter_get_time_chs.max()
            if max_value_pos > max_value_all:
                max_value_all = max_value_pos
            # append all filter with dif positions to a list
            filter_get_time_chs_all.append(filter_get_time_chs)
            
        i = 0
        # Do post-processing (down-sampling in time or frequency domain) and write into wav file
        for pos in pos_LS:
            filter_get_time_chs = filter_get_time_chs_all[i]
            filter_get_time_chs = filter_get_time_chs/max_value_all   # normalize the filters for the positions
            if filter_resample_flg == True:
                filter_get_time_chs = self.resample_filter(filter_get_time_chs, sf)
            if filter_cut_bins_flg == True: 
                # do 'down-sampling' in freq domain and transfrom into time domain again
                # in this way we reduce the length of the filter
                tmp_freq = np.fft.fft(filter_get_time_chs, nr_bins)
                filter_get_time_chs_old = filter_get_time_chs
                filter_get_time_chs = np.fft.ifft(tmp_freq)
                diff = (filter_get_time_chs - filter_get_time_chs_old[:, :len(filter_get_time_chs[0])]).max()/filter_get_time_chs_old.max()
                print('inaccuracy: '+str(diff))
            filename_filter_wav = 'Filter_FL_'+ pos[:-4] + '_'+str(sf)+'_'+ str(len(filter_get_time_chs[0])) +'.wav'
            if self.read_from_folder_flg == True:
                scipy.io.wavfile.write(os.path.join(self.aus_path + '\Filters',filename_filter_wav), sf, np.real(filter_get_time_chs.T))
            else:
                scipy.io.wavfile.write(os.path.join(self.aus_path_dir + '\Filters',filename_filter_wav), sf, np.real(filter_get_time_chs.T))
                
            i = i+1
            
        # only draw the filters of the last measurement position to make sure the measurement is correct and 
        # indicate that the calculation is terminated
        self.draw(np.abs(trans_filter_norm_ch), sf)

        self.display_filter_path.SetValue(self.aus_path_dir + '\Filters')

    def OnClick_conv(self, event):
        # Do convolution
        [conv_signal, sf]= Read_sweep_file(self.conv_signal_path_file)
        conv_signal = Read_sweep_file(self.conv_signal_path_file)[:-1][0]
        conv_filter = Read_sweep_file(self.conv_filter_path_file)[:-1][0]
        
        conv_signal_l = conv_signal[0]
        conv_filter_l = conv_filter[0]
        conv_signal_r = conv_signal[1]
        conv_filter_r = conv_filter[1]
        
        conv_out_l =  np.convolve(conv_signal_l, conv_filter_l, mode='full')*0.1
        conv_out_r =  np.convolve(conv_signal_r, conv_filter_r, mode='full')*0.1
        conv_out   =  np.vstack((conv_out_l, conv_out_r))
        self.conv_filter_filename = os.path.basename(self.conv_filter_path_file)
        file_name = 'Reconstruct_' + self.conv_filter_filename[:-4]+'.wav'
        self.conv_path_dir = os.path.dirname(self.conv_filter_path_file)
        scipy.io.wavfile.write(os.path.join(self.conv_path_dir + '\Reconstruction', file_name), sf, np.real(conv_out.T))
        self.display_conv_path.SetValue(self.conv_path_dir + '\Reconstruction')

#if __name__ == "__main__":


def gui_sitian():
    app = wx.App()
    fr = wx.Frame(None, title='test')
    panel = CanvasPanel(fr)

    fr.Show()
    app.MainLoop()
