from PyQt5.QtWidgets import QApplication
from main_controller import SpecterMainWindow


def main():
    app = QApplication([])

    controller = SpecterMainWindow()
    app.exec()


if __name__ == "__main__":
    main()
