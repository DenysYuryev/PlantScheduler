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

        self.ui.radioButton_1.clicked.connect(self.controlset)
        self.ui.radioButton_2.clicked.connect(self.controlset)

        self.ui.pushButtonImg.clicked.connect(self.setimg)

        self.table_index = 0
        self.row_cont = 1

        self.ID = int
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
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Error: {Error}")
            if res == QtWidgets.QMessageBox.Ok:
                return

        print(f"Row to be added: | {self.Name} | {self.Class} | {self.Dependence} |")

        try:
            i = 0
            index = []
            print("Start count index")

            rowcount = self.ui.TableWidget1.rowCount()
            print(f"Row count = {rowcount}")
            if rowcount > 0:
                for i in range(rowcount):
                    x = self.ui.TableWidget1.item(i, 0)
                    print(f"x = {x}")
                    index.append(x)
                    print(f"Index: {index[i]};")
                    i += 1
                i = max(index)
                print(f"max = {i}")
            else:
                i = 0

            self.ID = i + 1
            print(f"ID: {self.ID}")

            self.ui.TableWidget1.setRowCount(self.row_cont)
            self.ui.TableWidget1.setItem(self.table_index, 0, QtWidgets.QTableWidgetItem(self.ID))
            self.ui.TableWidget1.setItem(self.table_index, 1, QtWidgets.QTableWidgetItem(self.Name))
            self.ui.TableWidget1.setItem(self.table_index, 2, QtWidgets.QTableWidgetItem(self.Class))
            self.ui.TableWidget1.setItem(self.table_index, 3, QtWidgets.QTableWidgetItem(self.Image))

            self.table_index += 1
            self.row_cont += 1

        except Exception as Error:
            txt = "Something wrong in -> {} row"
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Error: {Error}\n" + txt.format(i))
            if res == QtWidgets.QMessageBox.Ok:
                return

    def deleqip(self):
        pass

    def setimg(self):
        imgpath = QtWidgets.QFileDialog.getOpenFileName(self, "Вибір зображення", "Ім'я файла", "Image (*.png *jpeg)\n All files *.*")
        print(imgpath)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidget()
    ui.show()
    sys.exit(app.exec_())
