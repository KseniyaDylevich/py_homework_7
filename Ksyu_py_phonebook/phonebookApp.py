import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QMenuBar, QMenu, QFileDialog, \
    QMessageBox
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
        self.actionOpenCsv.triggered.connect(self.openCsv)  # обработчик нажатия на пункт меню "open csv"

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
