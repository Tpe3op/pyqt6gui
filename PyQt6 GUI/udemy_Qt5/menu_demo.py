import sys
from PyQt6.QtWidgets import *
from menu_demo_ui import  *

class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        self.btn = QPushButton("Push Me")
        self.statusbar.addPermanentWidget(self.btn)

        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create("Windows"))
        self.statusbar.addPermanentWidget(self.prg)

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.btnDisplay.clicked.connect(self.evt_btnDisplay_clicked)

    def evt_btnDisplay_clicked(self):
        self.statusbar.showMessage(self.ledMessage.text(), self.sbxMsec.value())

    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open File", "ui/", "User Interface Files (*.ui)")
        if sFile:
            print(sFile)
        else:
            print("Select a valid file")

    def evt_quit_triggered(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menuMain = MenuMain()
    menuMain.show()
    sys.exit(app.exec())