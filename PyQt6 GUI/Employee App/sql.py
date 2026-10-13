import sys
from idlelib import query

from PyQt6.QtWidgets import *
from PyQt6.QtSql import *
from ui_modules.sql_ui import *
from ui_modules.dlgAdd_ui import *

class DlgMain(QDialog, Ui_dlgSql):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setupUi(self)
        self.setLayout(self.lyMain)

        self.lyMain.setStretch(0, 2)
        self.lyMain.setStretch(1, 8)

        self.header = self.tblEmployees.horizontalHeader()
        for i in range(self.tblEmployees.columnCount()):
            self.header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        self.header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("data/employees.db")
        if db.open():
            print(db.tables())
            if "employee" not in db.tables():
                self.createEmployeeTable()
            self.populateTable()
        else:
            QMessageBox.critical(self, "Database Error", "Could not open employee database")

        self.btnAdd.clicked.connect(self.evt_btnAdd_clicked)

    def populateTable(self):
        self.lstEmployee.clear()
        self.tblEmployees.clearContents()
        query = QSqlQuery()
        bOk = query.exec("SELECT * FROM employee ORDER BY lname, fname")
        if bOk:
            while query.next():
                row = self.tblEmployees.rowCount()
                self.tblEmployees.insertRow(row)
                for col in range(6):
                    twi = QTableWidgetItem(str(query.value(col)))
                    if col == 0:
                        twi.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
                    self.tblEmployees.setItem(row, col, twi)
                twi = QTableWidgetItem(returnEmployeeName(query.value('supervisor')))
                self.tblEmployees.setItem(row, 6, twi)
                self.lstEmployee.addItem(returnEmployeeName(query.value('emp_id')))
        else:
            QMessageBox.critical(self, "Database Error", "Database Error\n\n{}".format(query.lastError().text()))


    def createEmployeeTable(self):
        sql = """
            CREATE TABLE IF NOT EXISTS employee (
                emp_id INTEGER PRIMARY KEY,
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                position TEXT,
                supervisor INTEGER
            )
        """

        query = QSqlQuery()
        query.exec(sql)
        query.exec("insert into employee values(101, 'Mike', 'Miller', 'mm@gmail.com', 'x452', 'CEO', 9999)")
        query.exec("insert into employee values(102, 'Roger', 'Smith', 'rs@gmail.com', 'x645', 'VP-Sales', 101)")
        query.exec("insert into employee values(103, 'Bill', 'Jones', 'bj@gmail.com', 'x632', 'VP-Marketing', 101)")
        query.exec("insert into employee values(104, 'Joe', 'Smith', 'js@gmail.com', 'x657', 'PM', 102)")
        query.exec("insert into employee values(105, 'Fred', 'White', 'fw@gmail.com', 'x275', 'PM', 103)")

    def evt_btnAdd_clicked(self):
        dlgAdd = DlgAdd()
        dlgAdd.ledId.setText("NULL")
        dlgAdd.show()
        dlgAdd.exec()

class DlgAdd(QDialog, Ui_dlgAdd):
    def __init__(self):
        super(DlgAdd, self).__init__()
        self.setupUi(self)
        self.setLayout(self.formLayout)

        self.ledId.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.populateSupervisor()

        # self.btnCancel.clicked.connect(self.close)

    def populateSupervisor(self):
        self.cmbSupervisor.clear()
        query = QSqlQuery()
        bOk = query.exec("SELECT emp_id FROM employee ORDER BY lname, fname, possition")
        if bOk:
            while query.next():
                emp_id = query.value('emp_id')
                self.cmbSupervisor.addItem(returnEmployeeName(emp_id))
        else:
            QMessageBox.critical(self, "Database Error", "Database Error\n\n{}".format(query.lastError().text()))

def returnEmployeeName(id):
    query = QSqlQuery()
    sSql = "SELECT fname, lname, position FROM employee WHERE emp_id = {}".format(id)
    bOk = query.exec(sSql)
    if bOk:
        query.next()
        if query.isValid():
            return "{}, {} : {}".format(query.value('lname'), query.value('fname'), query.value('position'))
        else:
            return ""
    else:
        QMessageBox.critical(None,"Database Error", "Database Error\n\n{}".format(query.lastError().text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())
