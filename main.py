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
                print(f"{self.Name}")
            else:
                return

            if (len(self.ui.comboBox.currentText())) > 0:
                self.Class = self.ui.comboBox.currentText()
                print(f"{self.Class}")
            else:
                return

            if len(self.ui.comboBox_2.currentText()) > 0 and self.ui.radioButton_1.isChecked:
                self.Dependence = self.ui.comboBox_2.currentText()
                print(self.Dependence)
            elif self.ui.radioButton_2.isChecked:
                self.Dependence = "none"
                print(f"{self.Dependence}")
            else:
                print("Return")
                return
        except Exception as Error:
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Error: {Error}")
            if res == QtWidgets.QMessageBox.Ok:
                return

        print(f"row to be added: | {self.Name} | {self.Class} | {self.Dependence} |")


        try:
            i = 0
            index = []
            print("Start count index")
            # print("Item: ", self.ui.TableWidget1.item(i, 0))

            while self.ui.TableWidget1.item(i, 0).data() != None:
                index.append(self.ui.TableWidget1.item(i, 0))
                print("Index: {};\ni: {};".format(index[i], i))
                if i >= 10:
                    break
                i += 1

            maxim = max(index)
            print("maxim = ", maxim)

            self.ID = maxim + 1

            print(self.ID)

        except Exception as Error:
            txt = "Something wrong in -> {} row"
            res = QtWidgets.QMessageBox.critical(self, 'Error', f"Error: {Error}\n" + txt.format(i))
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
        imgpath = QtWidgets.QFileDialog.getOpenFileName(self, "Вибір зображення", "Ім'я файла", "Image (*.png *jpeg)\n All files *.*")
        print(imgpath)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidget()
    ui.show()
    sys.exit(app.exec_())
