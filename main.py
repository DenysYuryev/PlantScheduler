import sys

from mainUI import *
from mainUI import Ui_MainWindow


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton_1.clicked.connect(self.addeqip)
        self.ui.toolButton_2.clicked.connect(self.deleqip)

        self.ui.radioButton_1.clicked.connect(self.controlset)
        self.ui.radioButton_2.clicked.connect(self.controlset)

        self.table_index = 0
        self.row_cont = 1

        self.ID = 0
        self.Name = ""
        self.Class = ""
        self.Dependence = ""
        self.Image = ""

        if not (self.ui.radioButton_1.isChecked() and self.ui.radioButton_2.isChecked()):
            self.ui.radioButton_2.click()

    def controlset(self):
        if not self.ui.radioButton_2.isChecked():
            self.ui.comboBox_2.setEnabled(True)
        else:
            self.ui.comboBox_2.setEnabled(False)

    def addeqip(self):

        try:
            if (len(self.ui.lineEdit.text())) > 0:
                self.Name = self.ui.lineEdit.text()
            else:
                return

            if (len(self.ui.comboBox.text())) > 0:
                self.Class = self.ui.comboBox.text()
            else:
                return

            if (len(self.ui.comboBox_2.text()) and self.ui.radioButton_1.clicked) > 0:
                self.Dependence = self.ui.comboBox_2.text()
            else:
                return
        except:
            res = QtWidgets.QMessageBox.critical(self, 'Помилка', 'Не вірно заповнена форма')
            if res == QtWidgets.QMessageBox.Ok:
                return

        i = 1
        index = [0]
        while self.ui.TableWidget1.item(i, 0) != 0:
            index.append(self.ui.TableWidget1.item(i, 0))

        maxim = max(index)

        self.ID = maxim + 1

        self.ui.TableWidget1.setRowCount(self.row_cont)
        self.ui.TableWidget1.setItem(self.table_index, 0, QtWidgets.QTableWidgetItem(self.ID))
        self.ui.TableWidget1.setItem(self.table_index, 1, QtWidgets.QTableWidgetItem(self.Name))
        self.ui.TableWidget1.setItem(self.table_index, 2, QtWidgets.QTableWidgetItem(self.Class))
        self.ui.TableWidget1.setItem(self.table_index, 3, QtWidgets.QTableWidgetItem(self.Image))

        print("Name: " + self.Name + "\n" + "Class: " + self.Name)

        self.table_index += 1
        self.row_cont += 1

    def deleqip(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidget()
    ui.show()
    sys.exit(app.exec_())
