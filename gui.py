import sys
from PyQt5 import QtCore, QtWidgets


class GUI(object):
    def __init__(self):
        self.gui = QtWidgets.QDialog()
        self.gui.setObjectName("PROGRAM")
        self.gui.setFixedSize(700, 170)
        # label
        self.label_web_meter_value = QtWidgets.QLabel(self.gui)
        self.label_web_meter_value.setGeometry(QtCore.QRect(10, 20, 100, 16))
        self.label_web_meter_value.setObjectName("label_web_meter_value")
        self.label_weather_data = QtWidgets.QLabel(self.gui)
        self.label_weather_data.setGeometry(QtCore.QRect(10, 50, 100, 16))
        self.label_weather_data.setObjectName("label_weather_data")
        self.label_weekday_list = QtWidgets.QLabel(self.gui)
        self.label_weekday_list.setGeometry(QtCore.QRect(10, 80, 100, 16))
        self.label_weekday_list.setObjectName("label_weekday_list")

        # line edit
        self.line_web_meter_value = QtWidgets.QLineEdit(self.gui)
        self.line_web_meter_value.setGeometry(QtCore.QRect(110, 20, 470, 20))
        self.line_web_meter_value.setObjectName("line_web_meter_value")
        self.line_weather_data = QtWidgets.QLineEdit(self.gui)
        self.line_weather_data.setGeometry(QtCore.QRect(110, 50, 470, 20))
        self.line_weather_data.setObjectName("line_weather_data")
        self.line_weekday_list = QtWidgets.QLineEdit(self.gui)
        self.line_weekday_list.setGeometry(QtCore.QRect(110, 80, 470, 20))
        self.line_weekday_list.setObjectName("line_weekday_list")
        # ファイル選択ボタン
        self.button_web_meter_value = QtWidgets.QPushButton(self.gui)
        self.button_web_meter_value.setGeometry(QtCore.QRect(600, 20, 80, 23))
        self.button_web_meter_value.setObjectName("button_web_meter_value")
        self.button_weather_data = QtWidgets.QPushButton(self.gui)
        self.button_weather_data.setGeometry(QtCore.QRect(600, 50, 80, 23))
        self.button_weather_data.setObjectName("button_weather_data")
        self.button_weekday_list = QtWidgets.QPushButton(self.gui)
        self.button_weekday_list.setGeometry(QtCore.QRect(600, 80, 80, 23))
        self.button_weekday_list.setObjectName("button_weekday_list")

        # Start
        self.button_start = QtWidgets.QPushButton(self.gui)
        self.button_start.setGeometry(QtCore.QRect(599, 120, 81, 23))
        self.button_start.setObjectName("pushButton_4")
        # Cancel
        self.button_cancel = QtWidgets.QPushButton(self.gui)
        self.button_cancel.setGeometry(QtCore.QRect(506, 120, 81, 23))
        self.button_cancel.setObjectName("pushButton_5")
        # 出力先指定
        self.button_specify_output_path = QtWidgets.QPushButton(self.gui)
        self.button_specify_output_path.setGeometry(QtCore.QRect(1, 120, 100, 23))
        self.button_specify_output_path.setObjectName("button_specify_output_path")

        # translate language
        self.translate_ui()
        # イベントハンドル
        self.button_web_meter_value.clicked.connect(self.b_web_meter_value_func)
        self.button_weather_data.clicked.connect(self.b_weather_data_func)
        self.button_weekday_list.clicked.connect(self.b_weekday_list_func)
        self.button_start.clicked.connect(self.b_start_func)
        self.button_cancel.clicked.connect(self.b_cancel_func)
        self.button_specify_output_path.clicked.connect(self.b_specify_output_path_func)
        QtCore.QMetaObject.connectSlotsByName(self.gui)

    # function list
    def b_web_meter_value_func(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open File', r"$HOME", '*.csv')
        print("WEB検針値")
        if filename:
            print(filename)
            self.line_web_meter_value.setText(filename)

    def b_weather_data_func(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open File', r"$HOME", '*.csv')
        print("気象データ")
        if filename:
            print(filename)
            self.line_weather_data.setText(filename)

    def b_weekday_list_func(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open File', r"$HOME", '*.csv')
        print("平日リスト")
        if filename:
            print(filename)
            self.line_weekday_list.setText(filename)

    @staticmethod
    def b_start_func():
        print("Start")
        # print(self.lineEdit.text())

    @staticmethod
    def b_cancel_func():
        print("cancel")

    @staticmethod
    def b_specify_output_path_func():
        print("出力先指定")

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.gui.setWindowTitle(_translate("gui", "阪大プログラム"))
        self.label_web_meter_value.setText(_translate("gui", "WEB検針値"))
        self.label_weather_data.setText(_translate("gui", "気象データ"))
        self.label_weekday_list.setText(_translate("gui", "平日リスト"))
        self.button_web_meter_value.setText(_translate("gui", "選択"))
        self.button_weather_data.setText(_translate("gui", "選択"))
        self.button_weekday_list.setText(_translate("gui", "選択"))

        self.button_start.setText(_translate("gui", "Start"))
        self.button_cancel.setText(_translate("gui", "Cancel"))
        self.button_specify_output_path.setText(_translate("gui", "出力先指定"))

    def show(self):
        self.gui.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())
