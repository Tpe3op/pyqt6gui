import sys
from PyQt6.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.btn1 = QPushButton("Button 1")
        self.btn2 = QPushButton("Button 2")
        self.btn3 = QPushButton("Button 3")
        self.chk1 = QCheckBox("Check Box 1")
        self.led1 = QLineEdit("Editable")
        self.led2 = QLineEdit("Read Only")
        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create("Fusion"))
        self.lst = QListWidget()
        self.lst.addItems(QStyleFactory.keys())
        self.lst.itemDoubleClicked.connect(self.evt_lst_dbl)
        self.led2.setReadOnly(True)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btn1)
        self.lytMain.addWidget(self.btn2)
        self.lytMain.addWidget(self.btn3)
        self.lytMain.addWidget(self.chk1)
        self.lytMain.addWidget(self.led1)
        self.lytMain.addWidget(self.led2)
        self.lytMain.addWidget(self.prg)
        self.lytMain.addWidget(QSlider())
        self.lytMain.addWidget(QDial())
        self.lytMain.addWidget(self.lst)

        self.setLayout(self.lytMain)

    def evt_lst_dbl(self, itm):
        app.setStyle(QStyleFactory.create(itm.text()))
        QMessageBox.information(self, "Set Style", "You selected the '{}' style".format(itm.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())