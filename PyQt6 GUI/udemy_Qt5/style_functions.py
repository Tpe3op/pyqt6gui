import sys
from PyQt6.QtWidgets import *
import qdarkstyle

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.btnAdd1 = QPushButton("Add Button")
        self.btnAdd1.setStyleSheet(styleAddButton())
        self.btnAdd2 = QPushButton("Add Button")
        self.btnAdd2.setStyleSheet(styleAddButton())
        self.btnDel1 = QPushButton("Delete Button")
        self.btnDel1.setStyleSheet(styleDeleteButton())
        self.btnDel2 = QPushButton("Delete Button")
        self.btnDel2.setStyleSheet(styleDeleteButton())

        self.lyMain = QVBoxLayout()
        self.lyMain.addWidget(self.btnAdd1)
        self.lyMain.addWidget(self.btnAdd2)
        self.lyMain.addWidget(self.btnDel1)
        self.lyMain.addWidget(self.btnDel2)
        self.setLayout(self.lyMain)


def styleAddButton():
    sStyle = """
        QPushButton {
            background-color:#27D3F5;
            border-radius:3px;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #3E38E5;
            color: white;
            border-radius: 3px;
            border: 3px solid gray;
            padding: 8px;
        }
    """
    return sStyle

def styleDeleteButton():
    sStyle = """
        QPushButton {
            background-color:#F54927;
            border-radius:3px;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #C82909;
            color: white;
            border-radius: 3px;
            border: 2px solid gray;
            padding: 8px;
        }
    """
    return sStyle

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())