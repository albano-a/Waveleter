import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import scienceplots

def plot_wavelet_domain_linear(data, x_label, color=None):
        """Plots the time or frequency domain plot of wavelets in linear scale."""
        x_data, y_data = data if isinstance(data, tuple) else (data, None)

        fig, ax = plt.subplots()

        if x_data is not None and y_data is not None:
            ax.plot(x_data, y_data, color=color)
        else:
            ax.plot(x_data, color=color)

        ax.set_title("Wavelet Domain", fontsize=10)
        ax.set_xlabel(x_label, fontsize=9)
        ax.set_ylabel("Amplitude", fontsize=9)
        ax.tick_params(axis="both", labelsize=9)
        plt.grid(which="both", color="gray", linestyle="--", linewidth=0.5)

        canvas = FigureCanvas(fig)
        plt.close(fig)
        return canvas

def compute_wavelet_frequency_espectrum(twlet, wavelet, time):
    freqs = np.fft.rfftfreq(twlet.shape[0], d=time / 1000)
    fft = np.abs(np.fft.rfft(wavelet))
    fft = fft / np.max(fft)

    return freqs, fft

def _clear_and_set_layout(widget, canvas):
    """General function that helps add FigureCanvas into QWidgets"""
    if widget.layout() is not None:
        for i in reversed(range(widget.layout().count())):
            widget.layout().itemAt(i).widget().setParent(None)
    else:
        layout = QVBoxLayout(widget)
        widget.setLayout(layout)

    widget.layout().addWidget(canvas)
