import sys
from phonebookApp import PhonebookApp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QMenuBar, QMenu, QFileDialog, \
    QMessageBox, QDialog


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = PhonebookApp()  # Создаём экземпляр класса PhonebookApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
