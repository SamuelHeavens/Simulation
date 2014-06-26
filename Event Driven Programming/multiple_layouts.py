import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CropWindow(QMainWindow):
    """The crop window for my application."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.stacked_layout = QStackedLayout()
        self.create_initial_layout()
        #create stacked layout

        #create two layers required
       
        self.create_hello_layout()
        #set initial layout
        self.stacked_layout.setCurrentIndex(0)
        #Set the central widget to the stacked layout
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)

    def create_initial_layout(self):
        self.text_box = QLineEdit()
        self.submit_button = QPushButton("Submit")
        #create layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        
        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.layout)
        #add to stacked layout
        self.stacked_layout.addWidget(self.initial_widget)
        #connection
        self.submit_button.clicked.connect(self.switch_layout)
        
    def create_hello_layout(self):
        self.label = QLabel()
        self.back_button = QPushButton("back")

        self.hello_layout = QVBoxLayout()

        self.hello_layout.addWidget(self.label)
        self.hello_layout.addWidget(self.back_button)

        self.hello_widget = QWidget()
        self.hello_widget.setLayout(self.hello_layout)

        self.stacked_layout.addWidget(self.hello_widget)
        
        self.back_button.clicked.connect(self.back_clicked_switch)
        
    def switch_layout(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        self.label.setText("Hello {0}".format(name))
        
    def back_clicked_switch(self):
        self.stacked_layout.setCurrentIndex(0)
        self.text_box.clear()
 
    def display_name(self):
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = CropWindow()
    window.show()
    window.raise_()
    application.exec_()
