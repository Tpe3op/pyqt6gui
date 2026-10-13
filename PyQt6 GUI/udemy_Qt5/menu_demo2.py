import sys, os
from PyQt6.QtWidgets import *
from menu_demo2_ui import  *
import treewidget

class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        # In order to autoresize List Widget and Text Widget (split widget) we need to add them to central widget in Main Window class
        self.lytMain = QHBoxLayout()
        self.centralwidget.setLayout(self.lytMain)
        self.lytMain.addWidget(self.splitter)


        self.btn = QPushButton("Push Me")
        self.statusbar.addPermanentWidget(self.btn)

        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create("Windows"))
        self.statusbar.addPermanentWidget(self.prg)

        self.listWidget.addItems(os.listdir("ui_modules/"))

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.actionHelp.triggered.connect(self.evt_help_triggered)
        self.listWidget.itemDoubleClicked.connect(self.evt_lst_dbl)


    def evt_help_triggered(self):
        dlgTrw = treewidget.DlgMain()
        dlgTrw.show()
        dlgTrw.exec()



    def evt_lst_dbl(self, lwi):
        #QMessageBox.information(self, "File", "You selected {}".format(lwi.text()))
        f = open("ui_modules/" + lwi.text())
        self.textEdit.setText(f.read())

    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open File", "ui_modules/", "Any Text File (*.*)")
        if sFile:
            f = open(sFile)
            self.textEdit.setText(f.read())
        else:
            print("Select a valid file")

    def evt_quit_triggered(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menuMain = MenuMain()
    menuMain.show()
    sys.exit(app.exec())