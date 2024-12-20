# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Punto_A3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 110, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 440, 291, 61))
        self.label.setStyleSheet("border-image: url(:/cct/logo ECCI.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 361, 361))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 251, 121))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 241, 111))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #////////////////////////////////////
        #//////accion del boton graficar/////
        #////////////////////////////////////
        self.im = QPixmap("cartesiano.jpg")                       #creo objeto con la figura para colocar en Qlabel
        self.im_2 = QPixmap("cilindrico.jpg")
        self.im_3 = QPixmap("esferico.jpg")
        #self.pushButton.clicked.connect(self.print_image)
        self.comboBox.clicked.connect(self.print_image)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tipos de Robot"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Robot Cartesiano"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Robot Cilindrico"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Robot Esferico"))
        self.pushButton.setText(_translate("MainWindow", "Info"))
        self.label_4.setText(_translate("MainWindow", "Daniel ricardo quiroga contreras"))

    def print_image(self):
        opcion = self.comboBox.currentText() #variable para menu pop up
        if opcion == "Robot Cartesiano":
            self.label_2.setPixmap(self.im)
            self.label_3.setText("Este robot tiene tres movimientos lineales y\nperpendiculares entre sí, en los tres\nejes cartesianos X, Y y Z.\nEste tipo de robot se emplea en trabajos de\ncarga, desplazamiento\ny descarga de materiales")
               
        elif opcion == "Robot Cilindrico":
            self.label_2.setPixmap(self.im_2)
            self.label_3.setText("Un robot cilindrico cuenta con\nuna articulación rotacional y dos prismáticas.\nSon utilizados en operaciones de\nensamblaje, manejo de herramientas,\nsoldaduras por puntos, y manejo, vaciado\ny moldeado de metales")    
        
        elif opcion == "Robot Esferico":
            self.label_2.setPixmap(self.im_3)
            self.label_3.setText("Un robot esferico posee dos articulaciones\nrotacionales y una prismática;\naplicado en máquinas-herramientas,\nsoldaduras por puntos, vaciado de metales,\nfrezado, soldadura a gas, y\nsoldadura al arco.")
         
        

import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
