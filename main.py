import sys
import time

from mainUI import *
from mainUI import Ui_MainWindow

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QApplication


# main class window
class MyWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.TableWidget1.setRowCount(0)
        self.ui.TableWidget1.setColumnCount(4)

        # style = '''
        #     QTableWidget::item {background-color: #fffff8; font-size: 12pt}
        # '''
        # self.setStyleShit(style)

        self.ui.toolButton_1.clicked.connect(self.add_eqip)
        self.ui.toolButton_2.clicked.connect(self.del_eqip)

        self.ui.radioButton_1.clicked.connect(self.set_dep)
        self.ui.radioButton_2.clicked.connect(self.control_set)

        self.ui.pushButtonImg.clicked.connect(self.set_img)

        self.ui.pushButton.clicked.connect(self.sql_con)
        self.ui.pushButton_2.clicked.connect(self.disp_data)

        self.table_index = 0
        self.row_cont = 1

        self.ID = None
        self.Name = None
        self.Class = None
        self.Dependence = None
        self.Image = None

        if not (self.ui.radioButton_1.isChecked() and self.ui.radioButton_2.isChecked()):
            self.ui.radioButton_2.click()
            self.ui.comboBox_2.clear()
        elif self.ui.radioButton_2.isChecked():
            self.ui.comboBox_2.clear()

    def set_dep(self):
        try:
            if self.ui.radioButton_1.isChecked():
                obj = []
                rowcount = self.ui.TableWidget1.rowCount()
                if rowcount > 0:
                    for i in range(rowcount):
                        x = str(self.ui.TableWidget1.item(i, 1).text())
                        obj.append(x)
                else:
                    res = QtWidgets.QMessageBox.information(self, 'Information', "No object list")
                    if res == QtWidgets.QMessageBox.Ok:
                        return self.ui.radioButton_2.setChecked(True)
                self.ui.comboBox_2.addItems(obj)
                self.ui.comboBox_2.setEnabled(True)
            else:
                self.ui.comboBox_2.setEnabled(False)
        except Exception as Error:
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Dependency adding error: {Error}.\n")
            if res == QtWidgets.QMessageBox.Ok:
                return

    def control_set(self):
        if not self.ui.radioButton_2.isChecked():
            self.ui.comboBox_2.setEnabled(True)
        else:
            self.ui.comboBox_2.setEnabled(False)
            self.ui.comboBox_2.clear()

    def add_eqip(self):
        try:
            if (len(self.ui.lineEdit.text())) > 0:
                self.Name = self.ui.lineEdit.text()
                print(f"{self.Name}")
                if (len(self.ui.comboBox.currentText())) > 0:
                    self.Class = self.ui.comboBox.currentText()
                    print(f"{self.Class}")

                    if len(self.ui.comboBox_2.currentText()) > 0 and self.ui.radioButton_1.isChecked:
                        self.Dependence = self.ui.comboBox_2.currentText()
                        print(f"{self.Dependence}")
                    elif self.ui.radioButton_2.isChecked:
                        self.Dependence = "none"
                        print(f"{self.Dependence}")
                    else:
                        print("Return")
                        return
                else:
                    return
            else:
                return
        except Exception as Error:
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Read data fields error: {Error}.\n")
            if res == QtWidgets.QMessageBox.Ok:
                return

        print(f"Row to be added: | {self.Name} | {self.Class} | {self.Dependence} |")

        try:
            i = 0
            index = []
            name = []
            print("Start count index")

            rowcount = self.ui.TableWidget1.rowCount()
            print(f"Row count = {rowcount}")
            if rowcount > 0:
                for i in range(rowcount):
                    x = int(self.ui.TableWidget1.item(i, 0).text())
                    index.append(x)
                    y = self.ui.TableWidget1.item(i, 1).text()
                    name.append(y)
                    i += 1
                i = max(index)
                print(f"max = {i}")
            else:
                i = 0

            self.ID = i + 1
            print(f"ID: {self.ID}")
            print(f"List name: {name}")

            i = 0
            list_count = len(name)
            print(f"List count = {list_count}")
            for i in range(list_count):
                nm = self.ui.TableWidget1.item(i, 1).text()
                lst = name[i]
                print(f"Name: {nm} - List: {lst}")
                if self.ui.lineEdit.text() == name[i]:
                    QtWidgets.QMessageBox.information(self, 'Information', f"This name exists.")
                    i = 0
                    return
                else:
                    i += 1

            if self.ui.comboBox_2.currentText() != "" and self.ui.radioButton_1.isChecked():
                self.Dependence = self.ui.comboBox_2.currentText()

            self.ui.TableWidget1.setRowCount(self.row_cont)
            self.ui.TableWidget1.setItem(self.table_index, 0, QtWidgets.QTableWidgetItem(str(self.ID)))
            self.ui.TableWidget1.setItem(self.table_index, 1, QtWidgets.QTableWidgetItem(self.Name))
            self.ui.TableWidget1.setItem(self.table_index, 2, QtWidgets.QTableWidgetItem(self.Class))
            self.ui.TableWidget1.setItem(self.table_index, 3, QtWidgets.QTableWidgetItem(self.Dependence))
            self.ui.TableWidget1.setItem(self.table_index, 4, QtWidgets.QTableWidgetItem(self.Image))

            self.table_index += 1
            self.row_cont += 1

            self.ui.radioButton_2.click()
            self.ui.comboBox_2.clear()

        except Exception as Error:
            txt = "Something wrong in -> {} row"
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Equipment adding error: {Error}.\n")
            if res == QtWidgets.QMessageBox.Ok:
                return

    def del_eqip(self):
        pass

    def set_img(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Select image", "File name", "Image (*.png *jpeg)\n All files *.*")
        print(path[0])
        try:
            self.ui.pushButtonImg.setIcon(self, path[0])
        except Exception as Error:
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Selection image file error: {Error}.")
            if res == QtWidgets.QMessageBox.Ok:
                return

# SQL connection and data reading
    SERVER_NAME = "VM-SV101-TULCHI\\PLANTIT"
    DATABASE_NAME = "dbIdc"
    USERNAME = "sa"
    PASSWORD = "ProAdmin777"

 # SQL connection
    def sql_con(self):

        connection = f'DRIVER={{SQL Server}};' \
                     f'SERVER={self.SERVER_NAME};' \
                     f'UID={self.USERNAME};' \
                     f'PWD={self.PASSWORD};' \
                     f'DATABASE={self.DATABASE_NAME}'
        global db
        try:
            db = QSqlDatabase.addDatabase('QODBC')
            db.setDatabaseName(connection)
            self.ui.plainTextEdit.appendPlainText(f'Processing connection to... : {self.SERVER_NAME}')

            if db.open():
                print('Connection to SQL server successfully')
                self.ui.plainTextEdit.appendPlainText('Connection to SQL server successfully')
            else:
                self.ui.plainTextEdit.appendPlainText('Connection to SQL server failed')
                print('Connection to SQL server failed')
                return
        except Exception as Error:
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Read data from SQL error: {Error}.\n")
            if res == QtWidgets.QMessageBox.Ok:
                db.close()
                return

    def disp_data(self):
        table_name = self.ui.comboBox_3.currentText()

        SQL_STATEMENT = f"SELECT * FROM dbo.{table_name}"
        self.ui.plainTextEdit.appendPlainText('Processing query... : {SQL_STATEMENT}')
        try:
            qry = QSqlQuery(db)
            qry.prepare(SQL_STATEMENT)
            qry.exec()

            fields = qry.record().count()
            rows = qry.numRowsAffected()

            print(f'Fields: {fields} \n'
                  f'Rows: {rows}')
            self.ui.plainTextEdit.appendPlainText(f'Fields: {fields} \n'
                                                  f'Rows: {rows}')
            self.ui.TableWidget2.setColumnCount(fields)

            list_fields = []
            list_fields.clear()
            if fields > 0:
                for field in range(fields):
                    item = qry.record().fieldName(field)
                    list_fields.append(item)
                    self.ui.TableWidget2.setColumnWidth(field, len(list_fields[field]))
                print(f'Item fields: {list_fields}')
                self.ui.TableWidget2.setHorizontalHeaderLabels(list_fields)
                self.ui.TableWidget2.resizeColumnsToContents()

            item = []
            if rows > 0:
                qry.first()
                for r in range(rows):
                    row = self.ui.TableWidget2.rowCount()
                    self.ui.TableWidget2.setRowCount(r + 1)
                    item.clear()
                    for c in range(fields):
                        item.append(qry.value(c))
                        self.ui.TableWidget2.setItem(row, c, QtWidgets.QTableWidgetItem(str(item[c])))
                    qry.next()
                    print(f'Item {row}: {item}')
                self.ui.TableWidget2.resizeColumnsToContents()
            db.close()
            return
        except Exception as Error:
            res = QtWidgets.QMessageBox.critical(self, f'Error', f"Read data from SQL error: {Error}.\n")
            if res == QtWidgets.QMessageBox.Ok:
                db.close()
                return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidget()
    ui.show()
    sys.exit(app.exec_())
