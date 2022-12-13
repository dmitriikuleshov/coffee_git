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


class ChangeWidget(QWidget):
    def __init__(self, main_wdg_obj):
        super().__init__()

        uic.loadUi("addEditCoffeeForm.ui", self)
        # self.setupUi(self)
        self.main_wdg_obj = main_wdg_obj
        self.setWindowTitle('Редактирование')
        self.confirmPushButton.clicked.connect(self.confirm)

    def confirm(self):
        try:
            self.errorLabel.setText('')
            data = get_data()
            id = self.idLineEdit.text()
            sort = self.sortLineEdit.text()
            if not sort:
                raise Exception('Ошибка при заполнении форм')

            roasting = self.roastingLineEdit.text()
            if not roasting:
                raise Exception('Ошибка при заполнении форм')

            grains = self.grainsLineEdit.text()
            if not grains:
                raise Exception('Ошибка при заполнении форм')

            taste = self.tasteLineEdit.text()
            if not taste:
                raise Exception('Ошибка при заполнении форм')

            price = self.priceLineEdit.text()
            if not price:
                raise Exception('Ошибка при заполнении форм')

            size = self.sizeLineEdit.text()
            if not size:
                raise Exception('Ошибка при заполнении форм')

            print(data)
            if int(id) in [elem[0] for elem in data]:
                cursor.execute(f"""UPDATE coffee SET
                                "Название сорта" = '{sort}', "Степень обжарки" = '{roasting}',
                                 "Молотый/в зернах" = '{grains}', "Описание вкуса" = '{taste}',
                                  "Цена" = '{price}', "Объем упаковки" = '{size}'
                                                WHERE "id" = '{id}'""")
            else:
                cursor.execute(f"""INSERT INTO coffee("id", "Название сорта", "Степень обжарки",
                        "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки")
                            VALUES('{id}', '{sort}', '{roasting}', '{grains}', '{taste}', '{price}', '{size}')""")

            self.main_wdg_obj.fill_table()
            self.close()

        except Exception as e:
            self.errorLabel.setText('Ошибка при заполнении форм')
            print(e)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        # self.setupUi(self)
        self.setWindowTitle("Капучино")

        self.addButton.setVisible(False)
        self.delButton.setVisible(False)

        self.changeButton.clicked.connect(self.change_coffee)

        self.tableWidget.setColumnCount(len(columns_names))
        self.tableWidget.setHorizontalHeaderLabels(columns_names)
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len(get_data()))])

        self.change_widget = ChangeWidget(self)

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

    def change_coffee(self):
        self.change_widget.close()
        self.change_widget.show()

    def closeEvent(self, QCloseEvent):
        self.change_widget.close()
        connect.commit()
        connect.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = MyWidget()
    main_widget.show()
    sys.exit(app.exec())
