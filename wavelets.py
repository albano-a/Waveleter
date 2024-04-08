import pywt
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


plt.style.use(['ggplot'])

class Ricker:
    def __init__(self, high_freq, samples, dt, canvas):
        self.high_freq = high_freq
        self.samples = samples
        self.dt = dt
        self.canvas = canvas
        
    def waveletRicker(self):
        twlet = np.arange(self.samples) * (self.dt / 1000)
        twlet = np.concatenate((np.flipud(-twlet[1:]), twlet), axis=0)
        wlet = (1. -2.*(np.pi**2)*(self.high_freq**2)*(twlet**2))*np.exp(-(np.pi**2)*(self.high_freq**2)*(twlet**2))
        return twlet, wlet
    
    def plotRicker(self):
        twlet, wlet = self.waveletRicker()

        fft_r = abs(np.fft.rfft(wlet))
        freqs_r = np.fft.rfftfreq(twlet.shape[0], d=4/1000)
        fft_r = fft_r / np.max(fft_r)

        ax = self.canvas.figure.add_subplot(211)
        ax.plot(twlet, wlet)
        ax.set_title('Ricker Wavelet')
        ax1 = self.canvas.figure.add_subplot(212)
        ax1.plot(freqs_r, fft_r)
        ax1.set_title('Ricker Spectrum')
        self.canvas.figure.set_tight_layout(True)
        self.canvas.draw()
                
class Butterworth:
    def __init__(self, high_freq, low_freq, samples, dt, canvas):
        self.high_freq = high_freq
        self.low_freq = low_freq
        self.samples = samples
        self.dt = dt
        self.canvas = canvas
        
    def waveletButter(self):
        twlet = np.arange(self.samples) * (self.dt / 1000)
        twlet = np.concatenate((np.flipud(-twlet[1:]), twlet), axis=0)
        # Create impulse signal
        imp = signal.unit_impulse(twlet.shape[0], 'mid')

        # Apply high-pass Butterworth filter
        fs = 1000 * (1 / self.dt)
        b, a = signal.butter(4, self.high_freq, fs=fs)
        response_zp = signal.filtfilt(b, a, imp)

        # Apply low-pass Butterworth filter
        low_b, low_a = signal.butter(2, self.low_freq, 'hp', fs=fs)
        butter_wvlt = signal.filtfilt(low_b, low_a, response_zp)

        return twlet, butter_wvlt
    
    def plotButter(self):
        twlet, butter_wvlt = self.waveletButter()

        fft_b = abs(np.fft.rfft(butter_wvlt))
        freqs_b = np.fft.rfftfreq(twlet.shape[0], d=4/1000)
        fft_b = fft_b / np.max(fft_b)

        ax = self.canvas.figure.add_subplot(211)
        ax.plot(twlet, butter_wvlt)
        ax.set_title('Butterworth Wavelet')
        ax1 = self.canvas.figure.add_subplot(212)
        ax1.plot(freqs_b, fft_b)
        ax1.set_title('Butterworth Spectrum')
        self.canvas.figure.set_tight_layout(True)
        self.canvas.draw()
        
# class 