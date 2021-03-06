import sys
import os
from UI import *
from PyQt5 import QtWidgets
from Steganography import steg, desteg

class Window(QtWidgets.QMainWindow):

    # Init main window
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Set Label(Version)
        self.ui.About_Version_Label.setText("v1.04")

        # Connect buttons with functions
        self.ui.Encode_Container_ToolButton.clicked.connect(self.Encode_Container_Choose)
        self.ui.Encode_InputFile_ToolButton.clicked.connect(self.Encode_InputFile_Choose)
        self.ui.Encode_Password_pushButton.clicked.connect(self.Encode_Start)
        self.ui.Decode_Container_ToolButton.clicked.connect(self.Decode_Container_Choose)
        self.ui.Decode_Password_pushButton.clicked.connect(self.Decode_Start)

    # Open FileDialog window
    def Encode_Container_Choose(self):
        self.ui.Encode_Container_LineEdit.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())[0])
    def Encode_InputFile_Choose(self):
        self.ui.Encode_InputFile_LineEdit.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())[0])
    def Decode_Container_Choose(self):
        self.ui.Decode_Container_LineEdit.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())[0])

    # Start encoding
    def Encode_Start(self):
        if (self.ui.Encode_Container_LineEdit.text() and
                self.ui.Encode_InputFile_LineEdit.text() and
                not self.ui.Encode_Password_LineEdit.text()):
            result = steg(self.ui.Encode_Container_LineEdit.text(),
                          self.ui.Encode_InputFile_LineEdit.text(),
                          UseCryptography=False)
        elif (self.ui.Encode_Container_LineEdit.text() and
                  self.ui.Encode_InputFile_LineEdit.text() and
                  self.ui.Encode_Password_LineEdit.text()):
            result = steg(self.ui.Encode_Container_LineEdit.text(),
                          self.ui.Encode_InputFile_LineEdit.text(),
                          CryptoPassword=self.ui.Encode_Password_LineEdit.text(),
                          UseCryptography=True)

        self.ui.statusbar.showMessage(result, 5000)

    # Start decoding
    def Decode_Start(self):
        if (self.ui.Decode_Container_LineEdit.text() and
                not self.ui.Decode_Password_LineEdit.text()):
            result =  desteg(self.ui.Decode_Container_LineEdit.text(),
                             UseCryptography=False)
        elif (self.ui.Decode_Container_LineEdit.text() and
                  self.ui.Decode_Password_LineEdit.text()):
            result = desteg(self.ui.Decode_Container_LineEdit.text(),
                            CryptoPassword=self.ui.Decode_Password_LineEdit.text(),
                            UseCryptography=True)

        self.ui.statusbar.showMessage(result, 5000)

# TODO: Helper
# TODO: Progress bar

# Show main window
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec_())