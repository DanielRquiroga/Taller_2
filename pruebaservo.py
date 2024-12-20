# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'pruebaservo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
#import RPi.GPIO as GPIO
#import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setwarnings(False)
        #pwm_gpio = 12
        #frequence = 50
        #GPIO.setup(pwm_gpio, GPIO.OUT)
        #pwm = GPIO.PWM(pwm_gpio, frequence)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 721, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 190, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 260, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #---------------------------------
        #--------creacion objetos---------
        #---------------------------------
    
        #---------------------------------
        #------configuro sliders----------
        #---------------------------------
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(180)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        #----------------------------------
        #--------configuros acciones-------
        #----------------------------------
        self.horizontalSlider.valueChanged.connect(self.motor)
    
           


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))



    def motor(self):
        valorslider = self.horizontalSlider.value()
        if valorslider > 180 or valorslider < 0 :
            return False
        start = 4
        end = 12.5
        ratio = (end - start)/180 #Calcul ratio from angle to percent

        angle_as_percent = valorslider * ratio
        valor= start + angle_as_percent
        print(f'% pw {valor}')


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

