import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

connect = sqlite3.connect('coffee.sqlite')
cursor = connect.cursor()
columns_names = [elem[1] for elem in cursor.execute("""PRAGMA table_info(coffee)""").fetchall()]


def get_data():
    result = list(cursor.execute(f"""SELECT id, "Название сорта", "Степень обжарки",
         "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки" FROM coffee""").fetchall())
    return result


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        # self.setupUi(self)
        self.setWindowTitle("Эспрессо")

        # self.add_widget = AddWidget(self)
        # self.add_widget.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        # self.addButton.clicked.connect(self.add_coffee)
        #
        # self.change_widget = ChangeWidget(self)
        # self.change_widget.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        # self.changeButton.clicked.connect(self.change_coffee)
        #
        # self.del_widget = DelWidget(self)
        # self.del_widget.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        # self.delButton.clicked.connect(self.del_coffee)

        self.addButton.setVisible(False)
        self.changeButton.setVisible(False)
        self.delButton.setVisible(False)

        self.tableWidget.setColumnCount(len(columns_names))
        self.tableWidget.setHorizontalHeaderLabels(columns_names)
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len(get_data()))])

        self.fill_table()

    def fill_table(self):
        try:
            data = get_data()
            self.tableWidget.setRowCount(len(data))
            for row in range(len(data)):
                for col in range(len(data[0])):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(data[row][col])))
        except Exception as e:
            print(e)

    # def add_coffee(self):
    #     self.close_all_widgets()
    #     self.add_film_widget.show()
    #
    # def change_coffee(self):
    #     self.close_all_widgets()
    #     self.change_film_widget.show()
    #
    # def del_coffee(self):
    #     self.close_all_widgets()
    #     self.del_film_widget.show()

    # def closeEvent(self, QCloseEvent):
    #     self.add_widget.close()
    #     self.change_widget.close()
    #     connect.commit()
    #     connect.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = MyWidget()
    main_widget.show()
    sys.exit(app.exec())
