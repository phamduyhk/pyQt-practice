import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import _pickle


class Ui_gui(object):
    def browse_file1(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open File', r"/Users/phamduy/Downloads", '*.csv')
        print("WEB検針値")
        if filename:
            print(filename)
            self.lineEdit.setText(filename)

    def browse_file2(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open File', r"/Users/phamduy/Downloads", '*.csv')
        print("気象データ")
        if filename:
            print(filename)
            self.lineEdit_2.setText(filename)

    def browse_file3(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open File', r"/Users/phamduy/Downloads", '*.csv')
        print("平日リスト")
        if filename:
            print(filename)
            self.lineEdit_3.setText(filename)

    def start(self):
        print("Start")
        # print(self.lineEdit.text())

    def cancel(self):
        print("cancel")
    
    def specify_output(self):
        print("出力先指定")


    def setupUi(self, gui):
        gui.setObjectName("HANDAI PROGRAM")
        gui.resize(700, 160)
        # label
        self.label = QtWidgets.QLabel(gui)
        self.label.setGeometry(QtCore.QRect(10, 20, 100, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(gui)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 100, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(gui)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 100, 16))
        self.label_3.setObjectName("label_3")

        # line edit
        self.lineEdit = QtWidgets.QLineEdit(gui)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 470, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(gui)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 50, 470, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(gui)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 80, 470, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        # ファイル選択ボタン
        self.pushButton = QtWidgets.QPushButton(gui)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(gui)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 50, 80, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(gui)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 80, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        # Start
        self.pushButton_4 = QtWidgets.QPushButton(gui)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 120, 80, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        # Cancel
        self.pushButton_5 = QtWidgets.QPushButton(gui)
        self.pushButton_5.setGeometry(QtCore.QRect(505, 120, 80, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        #　出力先指定
        self.pushButton_6 = QtWidgets.QPushButton(gui)
        self.pushButton_6.setGeometry(QtCore.QRect(5, 120, 100, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(gui)
        # イベントハンドル
        self.pushButton.clicked.connect(self.browse_file1)
        self.pushButton_2.clicked.connect(self.browse_file2)
        self.pushButton_3.clicked.connect(self.browse_file3)
        self.pushButton_4.clicked.connect(self.start)
        self.pushButton_5.clicked.connect(self.cancel)
        self.pushButton_6.clicked.connect(self.specify_output)
        QtCore.QMetaObject.connectSlotsByName(gui)


    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "阪大プログラム"))
        self.label.setText(_translate("gui", "WEB検針値"))
        self.label_2.setText(_translate("gui", "気象データ"))
        self.label_3.setText(_translate("gui", "平日リスト"))
        self.pushButton.setText(_translate("gui", "選択"))
        self.pushButton_2.setText(_translate("gui", "選択"))
        self.pushButton_3.setText(_translate("gui", "選択"))

        self.pushButton_4.setText(_translate("gui", "Start"))
        self.pushButton_5.setText(_translate("gui", "Cancel"))
        self.pushButton_6.setText(_translate("gui", "出力先指定"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = QtWidgets.QDialog()
    ui = Ui_gui()
    ui.setupUi(gui)
    gui.show()
    sys.exit(app.exec_())
