import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interface.mainw import Ui_MainWindowWaveleter 
# Substitua "sua_pasta" pelo nome da pasta onde está o arquivo Ui_MainWindow.py
# Que contém a tela inicial

class MainWin(QMainWindow, Ui_MainWindowWaveleter):
    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Waveleter")
        
        
        
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()