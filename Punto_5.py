from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(805, 478)
        #Form.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 31))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(140, 120, 0, 255), stop:0.238636 rgba(255, 255, 255, 255), stop:0.789773 rgba(255, 255, 255, 255), stop:1 rgba(140, 120, 0, 255));")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 350, 261, 111))
        self.label_7.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(530, 410, 261, 51))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("logo ECCI.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.graficar_imagen = QtWidgets.QPushButton(Form)
        self.graficar_imagen.setGeometry(QtCore.QRect(330, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.graficar_imagen.setFont(font)
        self.graficar_imagen.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(40, 255, 0, 255), stop:0.181818 rgba(255, 255, 255, 255), stop:0.835227 rgba(255, 255, 255, 255), stop:1 rgba(106, 255, 0, 255));\n"
"    color: black;\n"
"    border-color: 17px;\n"
"}\n"
"QPushButton:enabled{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 142, 0, 255), stop:0.181818 rgba(255, 255, 255, 255), stop:0.835227 rgba(255, 255, 255, 255), stop:1 rgba(255, 142, 0, 255));\n"
"    color: black;\n"
"    border-color: 17px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(7, 0, 255, 255), stop:0.181818 rgba(255, 255, 255, 255), stop:0.835227 rgba(255, 255, 255, 255), stop:1 rgba(0, 26, 255, 255));\n"
"    color: black;\n"
"    border-color: 17px;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(7, 0, 255, 255), stop:0.181818 rgba(255, 255, 255, 255), stop:0.835227 rgba(255, 255, 255, 255), stop:1 rgba(0, 26, 255, 255));\n"
"    color: black;\n"
"    border-color: 17px;\n"
"}")
        self.graficar_imagen.setObjectName("graficar_imagen")
        self.label_imagen1 = QtWidgets.QLabel(Form)
        self.label_imagen1.setGeometry(QtCore.QRect(90, 50, 301, 281))
        self.label_imagen1.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_imagen1.setText("")
        self.label_imagen1.setObjectName("label_imagen1")
        self.label_imagen2 = QtWidgets.QLabel(Form)
        self.label_imagen2.setGeometry(QtCore.QRect(430, 50, 301, 281))
        self.label_imagen2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_imagen2.setText("")
        self.label_imagen2.setObjectName("label_imagen2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.graficar_imagen.clicked.connect(self.load_image)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:800;\">CONTORNO</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">leidy barragan</span></p><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">Jdaniel quiroga</span></p><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">kevin duenas</span></p><p align=\"center\"><span style=\" font-weight:700; color:#000000;\">gilber cano</span></p></body></html>"))
        self.graficar_imagen.setText(_translate("Form", "Analizar imagen"))

    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Abrir imagen", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            image = cv2.imread(file_name)

            # Convertir a escala de grises
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Umbralización adaptativa con parámetros ajustados
            blockSize = 31  # Tamaño de la region de cada pixel en numero impar
            C = 3  # Valor constante
            thresholded_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize, C)

            # Obtener contornos
            contours, _ = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Crear una imagen en blanco para dibujar los contornos
            contour_image = np.zeros_like(image)

            # Dibujar contornos en la imagen en naranja en BGR
            cv2.drawContours(contour_image, contours, -1, (66, 172, 255), 2)

            # Convertir las imágenes de OpenCV a QPixmap
            pixmap_original = self.convert_cv_to_qp(image)
            pixmap_contour = self.convert_cv_to_qp(contour_image)

            # Escalar las imágenes para que se ajusten al tamaño del QLabel manteniendo la relación de aspecto
            self.label_imagen1.setPixmap(pixmap_original.scaledToWidth(self.label_imagen1.width()))
            self.label_imagen2.setPixmap(pixmap_contour.scaledToWidth(self.label_imagen2.width()))

    def convert_cv_to_qp(self, cv_image):
        # Convertir la imagen de BGR a RGB
        cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        # Convertir la imagen de numpy a QImage
        height, width, channel = cv_image_rgb.shape
        bytes_per_line = channel * width
        q_image = QImage(cv_image_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        return pixmap

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())