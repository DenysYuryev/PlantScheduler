import sys

from mainUI import *
from mainUI import Ui_MainWindow


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

        self.ui.toolButton_1.clicked.connect(self.addeqip)
        self.ui.toolButton_2.clicked.connect(self.deleqip)

        self.ui.radioButton_1.clicked.connect(self.setdep)
        self.ui.radioButton_2.clicked.connect(self.controlset)

        self.ui.pushButtonImg.clicked.connect(self.setimg)

        self.ui.pushButton.clicked.connect(self.sqlcon)

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

    def setdep(self):
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

    def controlset(self):
        if not self.ui.radioButton_2.isChecked():
            self.ui.comboBox_2.setEnabled(True)
        else:
            self.ui.comboBox_2.setEnabled(False)
            self.ui.comboBox_2.clear()

    def addeqip(self):
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

    def deleqip(self):
        pass

    def setimg(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Select image", "File name", "Image (*.png *jpeg)\n All files *.*")
        print(path[0])
        try:
            self.ui.pushButtonImg.setIcon(self, path[0])
        except Exception as Error:
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Selection image file error: {Error}.")
            if res == QtWidgets.QMessageBox.Ok:
                return

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QApplication

    def sqlcon(self):


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidget()
    ui.show()
    sys.exit(app.exec_())
