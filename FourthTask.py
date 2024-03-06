# Добавьте переключатель слоёв карты (схема/спутник/гибрид), при изменении которого надо менять вид карты.

import sys
from PyQt5 import QtCore, QtWidgets
import requests
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def __init__(self):
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_3.setGeometry(QtCore.QRect(430, 360, 161, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4.setGeometry(QtCore.QRect(220, 360, 161, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5.setGeometry(QtCore.QRect(10, 360, 161, 41))
        self.pushButton_5.setObjectName("pushButton_5")

        self.label.setGeometry(QtCore.QRect(0, 0, 601, 351))
        self.label.setObjectName("label")
        pixmap = QPixmap('map.jpeg')
        self.label.setPixmap(pixmap)
        MainWindow.setCentralWidget(self.centralwidget)

        response = requests.get(
            "https://static-maps.yandex.ru/1.x/?ll=37.617901,55.751434&lang=ru_RU&spn=0.01,0.01&l=map&size=601,351")  # схема
        with open("map.jpeg", "wb") as jpeg:
            jpeg.write(response.content)
        pixmap = QPixmap('map.jpeg')
        self.label.setPixmap(pixmap)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_3.clicked.connect(self.show_scheme)
        self.pushButton_4.clicked.connect(self.show_spytnik)
        self.pushButton_5.clicked.connect(self.show_hybrid)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Схема"))
        self.pushButton_4.setText(_translate("MainWindow", "Спутник"))
        self.pushButton_5.setText(_translate("MainWindow", "Гибрид"))

    def show_scheme(self):
        response = requests.get(
            "https://static-maps.yandex.ru/1.x/?ll=37.617901,55.751434&lang=ru_RU&spn=0.01,0.01&l=map&size=601,351")  # схема
        with open("map.jpeg", "wb") as jpeg:
            jpeg.write(response.content)
        pixmap = QPixmap('map.jpeg')
        self.label.setPixmap(pixmap)

    def show_spytnik(self):
        response = requests.get(
            "https://static-maps.yandex.ru/1.x/?ll=37.617901,55.751434&lang=ru_RU&spn=0.01,0.01&&l=sat&size=601,351")  # спутник
        with open("map.jpeg", "wb") as jpeg:
            jpeg.write(response.content)
        pixmap = QPixmap('map.jpeg')
        self.label.setPixmap(pixmap)

    def show_hybrid(self):
        response = requests.get(
            "https://static-maps.yandex.ru/1.x/?ll=37.617901,55.751434&lang=ru_RU&spn=0.01,0.01&&l=skl&size=601,351")  # гибрид
        with open("map.jpeg", "wb") as jpeg:
            jpeg.write(response.content)
        pixmap = QPixmap('map.jpeg')
        self.label.setPixmap(pixmap)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
