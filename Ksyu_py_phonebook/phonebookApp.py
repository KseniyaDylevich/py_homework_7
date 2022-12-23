import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QMenuBar, QMenu, QFileDialog, \
    QMessageBox, QInputDialog
import design
import shutil
from PyQt5.QtGui import QTextCursor


# пишем класс, который наследуется от QMainWindow и от Ui_MainWindow(из нашего design.py)
class PhonebookApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # для инициализации нашего дизайна
        self.tableWidget.setColumnWidth(0, 200)
        self.pathToCsv = ''
        self.readFileButton.clicked.connect(self.loadCsv) #  обработчик нажатия на кнопку 'read file'
        self.saveChangesButton.clicked.connect(self.saveChanges)  # обработчик нажатия на кнопку 'save changes'
        self.actionOpenCsv.triggered.connect(self.openCsv)  # обработчик нажатия на пункт меню "file - open csv"
        self.actionFindContact.triggered.connect(self.findContact)  # обработчик нажатия на пункт меню "contact - find contact"
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)

    def setPathToCsv(self, pathToCsv):
        self.pathToCsv = pathToCsv

    def getPathToCsv(self):
        return self.pathToCsv

    def loadCsv(self):
        if self.getPathToCsv() !='':
            with open(self.getPathToCsv(), "r") as fileInput:
                s = 0 #  индекс записываемой строки
                for row in csv.reader(fileInput):
                    self.tableWidget.setColumnCount(len(row)) #  количество столбцов равно длине прочитанной строки
                    self.tableWidget.setRowCount(s + 1) #  количество отображаемых строк
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setVerticalHeaderItem(s, item)
                    for i in range(0, len(row)):
                        self.tableWidget.setItem(s, i, QtWidgets.QTableWidgetItem(row[i]))
                    s += 1
        else:
            QMessageBox.warning(self, "Внимание", "сначала выберите файл для открытия", QMessageBox.Ok)

    def openCsv(self):
        pathToCsv = QFileDialog.getOpenFileName(self, "Open Image", '*.csv')[0]
        print(pathToCsv)
        self.setPathToCsv(pathToCsv)

    def findContact(self):
        inputText, ok = QInputDialog.getText(self, 'find contact',
                             'input name or phone number:') # QInputDialog.getText() возвращает введенное значение и True/False
        if ok:
            if self.getPathToCsv() != '':
                with open(self.getPathToCsv(), "r") as fileInput:
                    s = 0  # индекс записываемой строки
                    for row in csv.reader(fileInput):
                        for el in row:
                            if inputText in el:
                                self.tableWidget.setRowCount(s + 1)  # количество отображаемых строк
                                item = QtWidgets.QTableWidgetItem()
                                self.tableWidget.setVerticalHeaderItem(s, item)
                                for i in range(0, len(row)):
                                    self.tableWidget.setItem(s, i, QtWidgets.QTableWidgetItem(row[i]))
                                s += 1
                                break
            else:
                QMessageBox.warning(self, "Внимание", "не выбран файл для открытия", QMessageBox.Ok)


    def cell_was_clicked(self):
        rowNumber = self.tableWidget.currentRow()
        columnNumber = self.tableWidget.currentColumn()
        #print([rowNumber, columnNumber])
        #print(self.tableWidget.item(rowNumber, columnNumber).text())


    def saveChanges(self):
        if self.getPathToCsv() != '':
            rowsCount = self.tableWidget.rowCount()
            colsCount = self.tableWidget.columnCount()
            data = []
            for row in range(rowsCount):
                tmp = []
                for col in range(colsCount):
                    try:
                        tmp.append(self.tableWidget.item(row, col).text())
                    except:
                        tmp.append('')
                data.append(tmp)
            with open(self.getPathToCsv(), mode="w", newline='') as w_file:
                writer = csv.writer(w_file)
                for row in data:
                    writer.writerow(row)
        else:
            QMessageBox.warning(self, "Внимание", "не выбран файл для открытия", QMessageBox.Ok)

