import sys
from PyQt6.QtWidgets import *
from PyQt6.QtSql import *
from ui_modules.sql_ui import *
from ui_modules.tablemodel_ui import *

class DlgMain(QDialog, Ui_dlgTableModel):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setupUi(self)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.splMain)
        self.setLayout(self.lytMain)

        self.setWindowTitle("Employee Database")
        self.splMain.setStretchFactor(0, 25)
        self.splMain.setStretchFactor(1, 75)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("data/employees.db")
        if db.open():
            print(db.tables())
            if "employee" not in db.tables():
                self.createEmployeeTable()
            self.populateTable()

            #self.tmr = QtCore.QTimer()
            #self.tmr.setSingleShot(True)
            #self.tmr.timeout.connect(self.populateTable)

        else:
            QMessageBox.critical(self, "Database Error", "Could not open employee database")

        self.mdlTable.beforeUpdate.connect(self.evt_before_update)
        self.btnAdd.clicked.connect(self.evt_btnAdd_clicked)

    def populateTable(self):
        self.mdList = QSqlQueryModel()
        self.mdList.setQuery("SELECT lname || ', ' || fname || ': ' || position AS name, email, phone, supervisor FROM employee ORDER BY lname, fname, position")

        self.mdlTable = QSqlTableModel()
        self.mdlTable.setTable("employee")
        self.mdlTable.setFilter("1 ORDER BY lname, fname, position")
        # self.mdlTable.setSort(2, QtCore.Qt.SortOrder.AscendingOrder)
        self.mdlTable.select()
        self.mdlTable.selectStatement()

        self.lstEmployee.setModel(self.mdList)
        self.tblEmployee.setModel(self.mdlTable)
        self.trvEmployee.setModel(self.mdList)

        self.tblEmployee.setColumnHidden(0, True)
        self.trvEmployee.setColumnWidth(0, 250)
        self.trvEmployee.setColumnWidth(1, 200)

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

    def evt_before_update(self, row, record):
        QMessageBox.information(self, "Database", "About to Update a record\n\nFirst: {}\nLast: {}\nEmail: {}\nPhone: {}\nPosition: {}\nSupervisor: {}".format(record.value("fname"), record.value("lname"), record.value("email"), record.value("phone"), record.value("position"), record.value("supervisor")))
        #self.tmr.start(500)
        self.mdlTable.dataChanged.connect(self.populateTable)

    def evt_btnAdd_clicked(self):
        empty_record = self.mdlTable.record()
        empty_record.setValue("fname", "")
        empty_record.setValue("lname", "")
        empty_record.setValue("email", "")
        empty_record.setValue("phone", "")
        empty_record.setValue("position", "")
        empty_record.setValue("supervisor", "9999")
        res = self.mdlTable.insertRecord(-1, empty_record)
        if res:
            self.populateTable()
        else:
            QMessageBox.critical(self, "Database Error", "Database Error \n\n{}".format(self.mdlTable.lastError().text()))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())