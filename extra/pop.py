


from PyQt5 import QtCore, QtGui, QtWidgets


class Db_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.topic_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.topic_comboBox.setGeometry(QtCore.QRect(20, 560, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.topic_comboBox.setFont(font)
        self.topic_comboBox.setObjectName("topic_comboBox")
        self.topic_comboBox.addItem("")
        self.exercises_listView = QtWidgets.QListView(self.centralwidget)
        self.exercises_listView.setGeometry(QtCore.QRect(15, 11, 511, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exercises_listView.setFont(font)
        self.exercises_listView.setMouseTracking(True)
        self.exercises_listView.setObjectName("exercises_listView")
        self.listButton = QtWidgets.QPushButton(self.centralwidget)
        self.listButton.setGeometry(QtCore.QRect(200, 560, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listButton.setFont(font)
        self.listButton.setObjectName("listButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(370, 560, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 510, 451, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 510, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topic_comboBox.setItemText(0, _translate("MainWindow", "Test"))
        self.listButton.setText(_translate("MainWindow", "List result"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.pushButton.setText(_translate("MainWindow", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Db_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
