import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import scienceplots


def _clear_and_set_layout(widget, canvas):
    """General function that helps add FigureCanvas into QWidgets"""
    if widget.layout() is not None:
        for i in reversed(range(widget.layout().count())):
            widget.layout().itemAt(i).widget().setParent(None)
    else:
        layout = QVBoxLayout(widget)
        widget.setLayout(layout)

    widget.layout().addWidget(canvas)
