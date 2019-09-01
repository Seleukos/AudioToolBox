from scipy.fftpack import *
import numpy as np
import matplotlib.pyplot as plt
# Number of sample points

def f(t):
    return np.sin(50.0 * 2.0*np.pi*t) + 0.5*np.sin(80.0 * 2.0*np.pi*t)


def fft_example():
    # Anzahl Samples:
    N = 600
    # sample spacing
    T = 1.0 / 800.0 # f = 800 Hz

    t = np.linspace(0.0, N*T, N)


    xf = np.linspace(+0.0, 1.0/(2.0*T), N//2)
    # 100er = row
    # 10er = column
    # 1er = plot_number
    figure = plt.figure()

    sub1 = figure.add_subplot(111)
    sub1.set_title('FFT')
    sub1.plot(t, fft(f(t)))

    sub2 = figure.add_subplot(212)
    sub2.set_title('IFFT')
    sub2.plot(t, ifft(f(t)))


    #plt.grid()
    plt.show()

   # yif = ifft(y)
    #xif = np.linspace(+0.0, 1.0 / (2.0 * T), N // 2)

   #plt.subplot(xif, 2.0 / N * np.abs(yif[0:N // 2]))

   # plt.grid()
    #plt.show()


def multisine_example():
    print("Multisine!")

def sweep_example():
    print("Sweep!")
