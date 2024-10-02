from PyQt5.QtWidgets import (
    QMainWindow,
    QMdiArea,
    QAction,
    QWidget,
    QVBoxLayout,
    QMdiSubWindow,
)
from PyQt5.uic import loadUi
from windows.ricker_controller import RickerWindow
from helpers.clear_layout import _clear_and_set_layout

SPECTERUI = "src/ui/SpecterMainWindow.ui"


class SpecterMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi(SPECTERUI, self)

        # Conectando ações da toolbar aos métodos correspondentes
        self.actionRicker.triggered.connect(self.open_ricker_window)
        self.actionRickerToolbar.triggered.connect(self.open_ricker_window)

        self.show()

    def open_ricker_window(self):
        self.srg = RickerWindow()
        self.srg.show()
