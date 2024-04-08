import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMessageBox
from interface.mainw import Ui_MainWindowWaveleter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from wavelets import Ricker, Butterworth

class MainWin(QMainWindow, Ui_MainWindowWaveleter):
    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Waveleter")
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        
        # Create a QVBoxLayout within your QWidget
        self.plotLayout = QVBoxLayout(self.frame)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.plotLayout.setSpacing(0)  # Remove spacing
        # Add the FigureCanvasQTAgg object to the layout
        self.plotLayout.addWidget(self.canvas)
    
        # Set the layout of the parent widget
        self.matplotlib_toolbar = NavigationToolbar2QT(self.canvas)
        # Create a custom toolbar
        # Create a button for each function and add it to the custom toolbar
        self.homeButton.clicked.connect(self.matplotlib_toolbar.home)
        self.backButton.clicked.connect(self.matplotlib_toolbar.back)
        self.forwardButton.clicked.connect(self.matplotlib_toolbar.forward)
        self.panButton.clicked.connect(self.matplotlib_toolbar.pan)
        self.zoomButton.clicked.connect(self.matplotlib_toolbar.zoom)
        self.configureSubPlots.clicked.connect(self.matplotlib_toolbar.configure_subplots)
        self.editButton.clicked.connect(self.matplotlib_toolbar.edit_parameters)
        self.saveButton.clicked.connect(self.matplotlib_toolbar.save_figure)

        self.actionViewSideBar.triggered.connect(self.toggleSideBar)
        
        self.waveletSelector.addItems(['Ricker', 'Butterworth'])
        
        self.plotWavButton.clicked.connect(self.plot)

    def plot(self):
        self.figure.clear()
        self.high_freq = self.highFreqInput.text()
        self.low_freq = self.lowFreqInput.text()
        self.samples = self.samplesInput.text()
        self.dt = self.timeInput.text()
        self.wavelet = self.waveletSelector.currentText()
        
        if self.wavelet == 'Ricker':
            self.plottingRicker(
                self.high_freq,
                self.samples,
                self.dt,
                self.canvas
            )
        if self.wavelet == 'Butterworth':
            if not self.high_freq or not self.low_freq:
                QMessageBox.warning(self, 'Aviso', 'Frequência Alta e Frequência Baixa são obrigatórios')
            else:
                try:
                    high_freq = float(self.high_freq)
                    low_freq = float(self.low_freq)
                except ValueError:
                    QMessageBox.warning(self, 'Aviso', 'Frequência Alta e Frequência Baixa devem ser números válidos')
                    return

                self.plottingButter(
                    high_freq,
                    low_freq,
                    self.samples,
                    self.dt,
                    self.canvas
                )

    def plottingRicker(self, high_freq, samples, time, canvas):
        self.ricker = Ricker(
            float(high_freq),
            int(samples),
            float(time),
            canvas
            )
        return self.ricker.plotRicker()
    
    def plottingButter(self, high_freq, low_freq, samples, time, canvas):
        self.butterworth = Butterworth(
            high_freq,
            low_freq,
            int(samples),
            float(time),
            canvas
        )
        return self.butterworth.plotButter()
    
    def toggleSideBar(self):
        if self.dockWidget.isVisible():
            self.dockWidget.hide()
        else:
            self.dockWidget.show()
    
def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()