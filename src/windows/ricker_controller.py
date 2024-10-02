from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

RUI = "src/ui/SpecterRickerGenerator.ui"


class RickerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi(RUI, self)

        self.show()
