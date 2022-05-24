"""
Instrucción para convertir la ventana .ui en .py
pyuic5 Window.ui -o Window.py
"""
import sys
import Window as WindowTest
from PyQt5 import QtWidgets

from PyQt5.QtCore import QEvent # Para manejar los eventos del teclado

class MyApp(QtWidgets.QMainWindow, WindowTest.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        WindowTest.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # Área de los Signals
        self.button_1.clicked.connect(self.btnController)
        self.button_2.clicked.connect(self.btnController)
        self.button_3.clicked.connect(self.btnController)
        self.button_4.clicked.connect(self.btnController)
        self.button_5.clicked.connect(self.btnController)
        self.button_6.clicked.connect(self.btnController)
        self.button_7.clicked.connect(self.btnController)
        self.button_8.clicked.connect(self.btnController)
    
        # Área de variables
        
    # Área de los Slots
    def btnController(self):
        sender = self.sender()
        num = int(sender.text())
        id = sender.objectName()[-1]
        exec("state = not self.check_" + id + ".isChecked()")
        exec("self.check_" + id + ".setChecked(state)")
        bin = self.binaryString()
        self.lbl_Bin.setText(bin)
        dec = int(bin,2)
        self.lbl_letter.setText('{} -> ({})'.format(chr(dec), dec))

    def binaryString(self):
        text = ''
        text += str(int(self.check_1.isChecked()))
        text += str(int(self.check_2.isChecked()))
        text += str(int(self.check_3.isChecked()))
        text += str(int(self.check_4.isChecked()))
        text += str(int(self.check_5.isChecked()))
        text += str(int(self.check_6.isChecked()))
        text += str(int(self.check_7.isChecked()))
        text += str(int(self.check_8.isChecked()))

        return text
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



'''
Seccion de Yochua
# 0 0 0 0 0 0 0 0
# A S D F G H J K

# Enter = append letra
# SUPR = borrar palabra

def keyPressEvent(self, event):
    key = event.key()
    if key == QtCore.Qt.Key_Enter:
        self.event
        return

    if key == QtCore.Qt.Key_1:
        self.event
        return
    if key == QtCore.Qt.Key_2:
        self.event
        return
    if key == QtCore.Qt.Key_3:
        self.event
        return
    if key == QtCore.Qt.Key_4:
        self.event
        return
    if key == QtCore.Qt.Key_5:
        self.event
        return
    if key == QtCore.Qt.Key_6:
        self.event
        return
    if key == QtCore.Qt.Key_7:
        self.event
        return
    if key == QtCore.Qt.Key_8:
        self.event
        return

    
    
    

'''