import sys
from PyQt6.QtWidgets import *


# from gbx_demo_ui_py import *
from PyQt6.QtCore import Qt
from PyQt6 import uic # Dodato

# class DlgMain(QDialog, Ui_Dialog):
class DlgMain(QDialog): # Dodato
    def __init__(self):
        # super(DlgMain, self).__init__()
        super().__init__() # Dodato
        # self.setupUi(self)
        uic.loadUi("gbx_demo.ui", self)

        self.rbtCheckTrue.toggled.connect(self.evt_rbtCheckTrue_toggled)
        self.rbtFlatTrue.toggled.connect(self.evt_rbtFlatTrue_toggled)
        self.rbtLeft.toggled.connect(self.evt_rbtAlignLeft_toggled)
        self.rbtRight.toggled.connect(self.evt_rbtAlignRight_toggled)
        self.rbtCenter.toggled.connect(self.evt_rbtAlignCenter_toggled)

    def evt_rbtCheckTrue_toggled(self, chk):
        self.gbxCheckable.setCheckable(chk)

    def evt_rbtFlatTrue_toggled(self, chk):
        self.gbxFlat.setFlat(chk)

    def evt_rbtAlignLeft_toggled(self, chk):
        if chk:
            self.gbxAligment.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.gbxAligment.setTitle("Left")

    def evt_rbtAlignCenter_toggled(self, chk):
        if chk:
            self.gbxAligment.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.gbxAligment.setTitle("Center")

    def evt_rbtAlignRight_toggled(self, chk):
        if chk:
            self.gbxAligment.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.gbxAligment.setTitle("Right")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())