# Создайте оконное приложение, отображающее карту по координатам и в масштабе, который задаётся программно.
import requests
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap


class Find(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Поиск по координатам")
        self.findButton.clicked.connect(self.findf)

    def setupUi(self, MapApp):
        MapApp.setObjectName("MapApp")
        MapApp.resize(600, 600)
        self.label = QtWidgets.QLabel(MapApp)
        self.label.setGeometry(QtCore.QRect(30, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.cords = QtWidgets.QLineEdit(MapApp)
        self.cords.setGeometry(QtCore.QRect(30, 110, 186, 30))
        self.cords.setAutoFillBackground(False)
        self.cords.setStyleSheet("QLineEdit#cords {\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 10px;\n"
                                 "    border-color: beige;\n"
                                 "    font: bold 14px;\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}")
        self.cords.setDragEnabled(False)
        self.cords.setClearButtonEnabled(True)
        self.cords.setObjectName("cords")
        self.zoom = QtWidgets.QLineEdit(MapApp)
        self.zoom.setGeometry(QtCore.QRect(385, 110, 186, 30))
        self.zoom.setStyleSheet("QLineEdit#zoom {\n"
                                "    border-style: outset;\n"
                                "    border-width: 2px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: beige;\n"
                                "    font: bold 14px;\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.zoom.setDragEnabled(False)
        self.zoom.setClearButtonEnabled(True)
        self.zoom.setObjectName("zoom")
        self.label_2 = QtWidgets.QLabel(MapApp)
        self.label_2.setGeometry(QtCore.QRect(385, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.findButton = QtWidgets.QPushButton(MapApp)
        self.findButton.setGeometry(QtCore.QRect(230, 140, 141, 41))
        self.findButton.setStyleSheet("background-color: lightgreen")
        self.findButton.setObjectName("findButton")
        self.background = QtWidgets.QLabel(MapApp)
        self.background.setEnabled(False)
        self.background.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../../Downloads/background.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.map_picture = QtWidgets.QLabel(MapApp)
        self.map_picture.setGeometry(QtCore.QRect(20, 220, 561, 361))
        self.map_picture.setFrameShape(QtWidgets.QFrame.Box)
        self.map_picture.setLineWidth(3)
        self.map_picture.setText("")
        self.map_picture.setScaledContents(True)
        self.map_picture.setObjectName("map_picture")
        self.background.raise_()
        self.label.raise_()
        self.cords.raise_()
        self.zoom.raise_()
        self.label_2.raise_()
        self.findButton.raise_()
        self.map_picture.raise_()

        self.retranslateUi(MapApp)
        QtCore.QMetaObject.connectSlotsByName(MapApp)

    def retranslateUi(self, MapApp):
        _translate = QtCore.QCoreApplication.translate
        MapApp.setWindowTitle(_translate("MapApp", "Form"))
        self.label.setText(_translate("MapApp", "Введите координаты:"))
        self.label_2.setText(_translate("MapApp", "    Введите масштаб:"))
        self.findButton.setText(_translate("MapApp", "ПОИСК"))

    def findf(self):
        coords = self.cords.text().replace(" ", "").split(",")
        zoom = self.zoom.text()
        res = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={coords[1]},{coords[0]}&l=map&z={zoom}")
        if res:
            with open("output.png", "wb") as file:
                file.write(res.content)
            self.pixmap = QPixmap('output.png')
            self.map_picture.setScaledContents(True)
            self.map_picture.setPixmap(self.pixmap)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Find()
    ex.show()
    sys.exit(app.exec_())
