# -*- coding: utf-8 -*-

from scipy.signal import lfilter, chirp, spectrogram
from scipy.signal import hilbert
import numpy as np
import os.path
import os
import soundfile as sf
import matplotlib.pyplot as plt
import pandas as pd

import sys


# import sp_tool

# Diese Funktion erzeugt einen Sinus-Sweep:
# fs = Sampling-Frequenz, f1 = Startfrequenz, f2 = Stopfrequenz, phi0 = Phasenverschiebung)
# duration = Länge des Sweeps # method = Methode mit der Sweep erzeugt wird!


def sinesweep(fs, f1, f2, phi0, duration, method):
    if f2 > fs / 2:
        raise ValueError("fstop must not be greater than fs/2")
    else:
        t = np.arange(0, duration, 1 / fs)  # 0=Startwert, duration = Länge des Sweeps (Endwert), 1/fs = Schrittweite
        # Was ist towsw?:
        towsw = t[len(t) - 1]

        if method == 'log':
            L = towsw / np.log(f2 / f1)
            r = 1 / L / np.log(2)
            sweep = np.sin(2 * np.pi * f1 * L * (np.exp(t / L) - 1) + phi0)

        elif method == 'novak':
            L = np.round(f1 * towsw / np.log(f2 / f1)) / f1
            r = 1 / L / np.log(2)
            sweep = np.sin(2 * np.pi * f1 * L * (np.exp(t / L) - 1) + phi0)

        elif method == 'gen':
            sweep = np.sin(2 * np.pi * duration * f1 / np.log(f2 / f1) * (np.exp(t / duration * np.log(f2 / f1)) - 1))

        elif method == 'lin':
            sweep = np.sin(2 * np.pi * ((f2 - f1) / (2 * duration) * t ** 2 + f1 * t))

        high_fade_sample_vec = -np.round((100 * fs / f2 + 2), 0) + t

    return (sweep, t)


# Was macht hilb?: hilbert
def hilb(sweep, fs, t):
    excitation = sweep
    analytic_signal = hilbert(excitation)
    amplitude_envelope = np.abs(analytic_signal)
    instantaneous_phase = np.unwrap(np.angle(analytic_signal))
    instantaneous_frequency = (np.diff(instantaneous_phase) / (2.0 * np.pi) * fs)
    fig = plt.figure()
    ax0 = fig.add_subplot(211)
    ax0.plot(t, excitation, label='signal')
    ax0.plot(t, amplitude_envelope, label='envelope')
    ax0.set_xlabel("time in seconds")
    ax0.legend()
    ax1 = fig.add_subplot(212)
    ax1.plot(t[1:], instantaneous_frequency)
    ax1.set_xlabel("time in seconds")
    ax1.set_ylim(0.0, 30000.0)


def spect(sweep):
    freqs, times, spectrogramsweep = spectrogram(sweep)  # , nperseg=Nperseg)
    plt.plot(spectrogramsweep)

    plt.figure(figsize=(5, 4))
    plt.imshow(spectrogramsweep, aspect='auto', cmap='hot_r', origin='lower')
    plt.title('Spectrogram')
    plt.ylabel('Frequency band')
    plt.xlabel('Time window')
    plt.tight_layout()
    return (freqs, times, spectrogramsweep)


# Hier werden die Ergebnisse in eine Text-Datei abgelegt:
def write(file_name, folder_name, Conv_L, Conv_R, fs, form, ch):
    # Warum gibt es zwei Channels?:
    if ch == '1':
        Conv_sweep = os.path.join(folder_name, file_name)
        conv_left_right = Conv_L
        if form == 'wav':
            # write Input
            sf.write(Conv_sweep, conv_left_right, fs, 'PCM_32')
        elif form == 'dat' or 'txt':
            df = pd.DataFrame(conv_left_right)
            df.to_csv(Conv_sweep, sep=';')

    elif ch == '2':
        Conv_sweep = os.path.join(folder_name, file_name)
        conv_left_right = np.vstack((Conv_L, Conv_R)).T
        if form == 'wav':
            # write Input
            sf.write(Conv_sweep, conv_left_right, fs, 'PCM_32')
        elif form == 'dat' or 'txt':
            df = pd.DataFrame(conv_left_right)
            df.to_csv(Conv_sweep, sep=';')
    return (conv_left_right)


########################################################################################################################
# Hier geht das eigentliche Programm los:
########################################################################################################################
# In[]
f1 = 20
f2 = 20000
fs = 48000
phi0 = 0
methods = ['novak', 'log', 'gen', 'lin']  # novak or log
durations = [0.5, 1, 2, 3, 4, 5]
sweepsignals = []

########################################################################################################################
# Sweep-Signale mit verschiedenen Durations::
########################################################################################################################

for i in range(len(methods)):
    method = methods[i]
    for j in range(len(durations)):
        duration = durations[j]
        # Erzeugung der Sweep-Signale:
        sweep, t = sinesweep(fs, f1, f2, phi0, duration, method)
        zeros = np.zeros(2 * len(sweep))
        zeros_sweep = np.append(zeros, sweep)
        zero_sweep_zeros = np.append(zeros_sweep, zeros)
        sweepsignals.append(zero_sweep_zeros)

sweepsignalsarray = np.concatenate(sweepsignals, axis=0)

zer = np.zeros(12 * fs)
sweepsignalsarrays = np.concatenate((zer, sweepsignalsarray), axis=0)

# plt.plot(sweepsignalsarrays)
# In[write wav data]
# Was bedeutet "Conv"?

########################################################################################################################
#  Ab hier werden alle Sweep-Signale bzw. deren Daten in Textdateien abgelegt:
########################################################################################################################

Conv_L = sweepsignalsarrays
Conv_R = sweepsignalsarrays

# File Names:
file_name_wav_1Ch = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav'
file_name_wav_2Ch = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.wav'
file_name_dat_1Ch = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.dat'
file_name_dat_2Ch = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.dat'
file_name_txt_1Ch = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.txt'
file_name_txt_2Ch = '1_Ch_wav_Sweep_.5_5_s_48000_novak_log_gen_lin.txt'

file_names = [file_name_wav_1Ch, file_name_wav_2Ch,
              file_name_dat_1Ch, file_name_dat_2Ch,
              file_name_txt_1Ch, file_name_txt_2Ch]

file_names = [file_name_wav_1Ch, file_name_wav_2Ch]

# Save folder name:
##### Achtung: Wieder erstes mit reinnehmen!
folder_name = r'\\FRA-MFP-004.iavgroup.local\FREE\Virtual_Audio\12_Messung\Input Signal\Input Signal Measurement'
####Test-Folder (Lokal):
folder_name = r'C:\Users\t02meyer\Documents\Bachelorarbeit_TobiasMeyer\Ablage_Test'

for i in range(len(file_names)):
    file_name = file_names[i]
    form = file_name[len(file_name) - 3:]
    ch = file_name[0]
    print(file_name, folder_name, Conv_L, Conv_R, fs, form, ch)
    write(file_name, folder_name, Conv_L, Conv_R, fs, form, ch)

########################################################################################################################
# Warum hier nochmal Sinussweep-Erzeugung?
########################################################################################################################

# In[]
f1 = 20
f2 = 20000
fs = 48000
phi0 = 0
methods = ['novak', 'log', 'gen', 'lin']  # novak or log
durations = [2, 4]
sweepsignals = []

for i in range(len(methods)):
    method = methods[i]
    for j in range(len(durations)):
        duration = durations[j]
        sweep, t = sinesweep(fs, f1, f2, phi0, duration, method)
        zeros = np.zeros(2 * len(sweep))
        zeros_sweep = np.append(zeros, sweep)
        zero_sweep_zeros = np.append(zeros_sweep, zeros)
        sweepsignals.append(zero_sweep_zeros)

sweepsignalsarray = np.concatenate(sweepsignals, axis=0)

zer = np.zeros(12 * fs)
sweepsignalsarrays = np.concatenate((zer, sweepsignalsarray), axis=0)

# In[]
sys.setrecursionlimit(1500)

f1 = 20
f2 = 20000
fs = 48000
duration = 2
phi0 = 0
method = 'novak'  # novak or log
sweep, t = sinesweep(fs, f1, f2, phi0, duration, method)

# freqs, times, spectrogramsweep = spect(sweep)
hilb(sweep, fs, t)

######
towsw = 1
# In[Nova Kround]

Lnk = np.round(f1 * towsw / np.log(f2 / f1)) / f1
rnk = 1 / Lnk / np.log(2)

######
L = 1

sinnk = np.sin(2 * np.pi * f1 * L * (np.exp(t / Lnk) - 1) + phi0)

plt.plot(sinnk)

freqs, times, spectrogramnk = spectrogram(sinnk)  # , nperseg=Nperseg)

plt.plot(spectrogramnk)

plt.figure(figsize=(5, 4))
plt.imshow(spectrogramnk, aspect='auto', cmap='hot_r', origin='lower')
plt.title('Spectrogram')
plt.ylabel('Frequency band')
plt.xlabel('Time window')
plt.tight_layout()

# Nur für warten ...
x = input("Ihre Gehalt? ")

# In[]
