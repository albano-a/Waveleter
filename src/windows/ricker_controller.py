from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
    QFileDialog,
    QMenu,
    QAction,
)
import sys
import helpers.clear_layout as helper
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

RUI = "src/ui/SpecterRickerGenerator.ui"


class RickerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi(RUI, self)

        self.srgGenerateWaveletPushButton.clicked.connect(self.generate_wavelet)
        self.srgExportWaveletPushButton.clicked.connect(self.export_wavelet)

        self.wavelet = pd.DataFrame()  # Aqui tá criando um dataframe vazio

        self.show()

    def ricker(self, peak_freq, samples, time):
        twlet = np.arange(samples) * (time / 1000)
        twlet = np.concatenate((np.flipud(-twlet[1:]), twlet), axis=0)
        try:
            wlet = (
                1.0 - 2.0 * (np.pi**2) * (peak_freq**2) * (twlet**2)
            ) * np.exp((-np.pi**2) * (peak_freq**2) * (twlet**2))
            return pd.DataFrame({"time": twlet, "wavelet": wlet})
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred: {e}")
            return None

    def show_wavelet_data(self, wavelet_dataframe):
        self.srgTableDataViewer.clear()

        self.srgTableDataViewer.setRowCount(len(wavelet_dataframe))
        self.srgTableDataViewer.setColumnCount(len(wavelet_dataframe.columns))

        self.srgTableDataViewer.setHorizontalHeaderLabels(wavelet_dataframe.columns)
        for row in range(len(wavelet_dataframe)):
            for col in range(len(wavelet_dataframe.columns)):
                item = QTableWidgetItem(str(wavelet_dataframe.iat[row, col]))
                self.srgTableDataViewer.setItem(row, col, item)

        header = self.srgTableDataViewer.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

    def generate_wavelet(self):
        peak_freq = (
            int(self.srgPeakFrequencyInput.text())
            if self.srgPeakFrequencyInput.text()
            else 0
        )
        samples = int(self.srgSamplesInput.text()) if self.srgSamplesInput.text() else 0
        time = int(self.srgTimeInput.text()) if self.srgTimeInput.text() else 0

        if peak_freq == 0 or samples == 0 or time == 0:
            QMessageBox.critical(None, "Error", "Please fill all the fields.")
            return

        self.wavelet = self.ricker(
            peak_freq, samples, time
        )  # aqui tá retornando o dataframe

        self.show_wavelet_data(self.wavelet)
        data = (
            self.wavelet["time"],
            self.wavelet["wavelet"],
        )  # Aqui transforma em uma tupla

        freq = helper.compute_wavelet_frequency_espectrum(
            self.wavelet["time"], self.wavelet["wavelet"], time
        )

        canvas_time = helper.plot_wavelet_domain_linear(data, "Time (s)", color="blue")
        canvas_freq = helper.plot_wavelet_domain_linear(
            freq, "Frequency (Hz)", color="red"
        )

        helper._clear_and_set_layout(self.srgTimePlot, canvas_time)
        helper._clear_and_set_layout(self.srgFrequencyPlot, canvas_freq)
        self.connect_buttons(canvas_time)
        self.connect_buttons(canvas_freq)

    def connect_buttons(self, canvas):
        self.matplotlib_toolbar = NavigationToolbar2QT(canvas)

        self.srgSaveImagePushButton.clicked.connect(self.matplotlib_toolbar.save_figure)

    def export_wavelet(self):
        if self.wavelet.empty:
            QMessageBox.critical(None, "Error", "No wavelet to export.")
            return

        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Wavelet", "", "TXT Files (*.txt)"
        )

        if file_name:
            self.wavelet.to_csv(file_name, index=False)
            QMessageBox.information(None, "Success", "Wavelet exported successfully.")
