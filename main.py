import sys

from mainUI import *
from mainUI import Ui_MainWindow


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.TableWidget1.setRowCount(1)
        self.ui.TableWidget1.setColumnCount(4)

        # style = '''
        #     QTableWidget::item {background-color: #fffff8; font-size: 12pt}
        # '''
        # self.setStyleShit(style)

        self.ui.toolButton_1.clicked.connect(self.addeqip)
        self.ui.toolButton_2.clicked.connect(self.deleqip)

        self.ui.radioButton_1.clicked.connect(self.controlset)
        self.ui.radioButton_2.clicked.connect(self.controlset)

        self.ui.pushButtonImg.clicked.connect(self.setimg)

        self.table_index = 0
        self.row_cont = 1

        self.ID = None
        self.Name = None
        self.Class = None
        self.Dependence = None
        self.Image = None

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
                print(self.Name)
            else:
                return

            if (len(self.ui.comboBox.currentText())) > 0:
                self.Class = self.ui.comboBox.currentText()
                print(self.Class)
            else:
                return

            if len(self.ui.comboBox_2.currentText()) > 0 and self.ui.radioButton_1.isChecked:
                self.Dependence = self.ui.comboBox_2.currentText()
                print(self.Dependence)
            elif self.ui.radioButton_2.isChecked:
                self.Dependence = "none"
                print(self.Dependence)
            else:
                print("Return")
                return
        except:
            res = QtWidgets.QMessageBox.critical(self, 'Error', 'Something wrong fill in fields')
            if res == QtWidgets.QMessageBox.Ok:
                return

        print("row to be added: |" + self.Name + "|" + self.Class + "|" + self.Dependence + "|")
        i = 0
        try:
            index = []
            print("Start count index")
            print(self.ui.TableWidget1.item(i, 0))

            while self.ui.TableWidget1.item(i, 0).text() != 0:
                index.append(self.ui.TableWidget1.item(i, 0).text())
                print("Index:  {} ; \n i: {}".format(index[i], i))
                i += 1

            maxim = max(index)
            self.ID = maxim + 1

            print(self.ID)
        except:
            txt = "Something wrong in -> {} row"
            res = QtWidgets.QMessageBox.critical(self, 'Error', txt.format(i))
            if res == QtWidgets.QMessageBox.Ok:
                return

        self.ui.TableWidget1.setRowCount(self.row_cont)
        self.ui.TableWidget1.setItem(self.table_index, 0, QtWidgets.QTableWidgetItem(str(self.ID)))
        self.ui.TableWidget1.setItem(self.table_index, 1, QtWidgets.QTableWidgetItem(self.Name))
        self.ui.TableWidget1.setItem(self.table_index, 2, QtWidgets.QTableWidgetItem(self.Class))
        self.ui.TableWidget1.setItem(self.table_index, 3, QtWidgets.QTableWidgetItem(self.Image))

        print("Name: " + self.Name + "\n" + "Class: " + self.Name)

        self.table_index += 1
        self.row_cont += 1

    def deleqip(self):
        pass

    def setimg(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidget()
    ui.show()
    sys.exit(app.exec_())
