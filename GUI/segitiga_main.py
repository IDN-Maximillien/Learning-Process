from PyQt5 import QtCore, QtGui, QtWidgets

sifat = ''

class Segitiga:
    def __init__(self, sisi_X, sisi_Y, sisi_Z):
        self.X = sisi_X
        self.Y = sisi_Y
        self.Z = sisi_Z
        
    def jenis_segitiga(self):
        global sifat
        a = self.X
        b = self.Y
        c = self.Z
        if (a >= b and a >= c):
            x = a
            y = b
            z = c
        elif (b >= a and b >= c):
            x = b
            y = a
            z = c
        else:
            x = c
            y = a
            z = b
        
        syarat = bool(a <= b + c)
        
        if syarat:
            if (x*x == (y*y + z*z)):
                sifat = "Segitiga siku-siku"
            elif (a == b == c):
                sifat = "Segitiga sama sisi"
            elif (a == b or b == c) and not (a == b == c):
                sifat = "Segitiga sama kaki"
            else:
                sifat = "Segitiga sembarang"
        else:
            print('Bukan Segitiga!')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 210, 120, 80))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 210, 120, 80))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(480, 210, 120, 80))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 190, 48, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 190, 48, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 190, 48, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 320, 100, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 380, 300, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionCara_Menggunakan = QtWidgets.QAction(MainWindow)
        self.actionCara_Menggunakan.setObjectName("actionCara_Menggunakan")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuHelp.addAction(self.actionCara_Menggunakan)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sisi A"))
        self.label_2.setText(_translate("MainWindow", "Sisi B"))
        self.label_3.setText(_translate("MainWindow", "Sisi C"))
        self.pushButton.setText(_translate("MainWindow", "Tentukan Jenis"))
        self.label_4.setText(_translate("MainWindow", "Tentukan sisi-sisi segitiga!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionCara_Menggunakan.setText(_translate("MainWindow", "Cara Menggunakan"))

        self.pushButton.clicked.connect(self.clicked)

    def clicked(self):
        global sifat
        a = int(input(self.ui.textEdit.toPlainText()))
        b = int(input(self.ui.textEdit_2.toPlainText()))
        c = int(input(self.ui.textEdit_3.toPlainText()))
        Segitiga(a,b,c)
        self.label_4.setText(f"Segitiga anda adalah : {sifat}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
