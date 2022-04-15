# Import necessary modules and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,QHBoxLayout)
from custom_widget_placeholder import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the main window and display its content
        """
        self.setWindowTitle("Horizontal Layout")
        self.setGeometry(100,50, 800, 600)
        self.display_widgets()
    