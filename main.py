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
    
    def display_widgets(self):
        """
        Display the color widgets on the main window.
        """
        # Create the layout:
        h_layout = QHBoxLayout()
        # Create the container:
        container = QWidget()
        # Create instances of Color class & add it to the layout:
        h_layout.addWidget(Color("#EF0087"))
        h_layout.addWidget(Color("#6945DB"))
        h_layout.addWidget(Color("#34E453"))
        h_layout.addWidget(Color("#FF633A"))
        # Set the container to use the layout:
        container.setLayout(h_layout)
        # Set the container as the central widget for the main window:
        self.setCentralWidget(container)

# Run the program:
if __name__ =="__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
    