import sys
import sqlite3

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

connect = sqlite3.connect('data/coffee.sqlite')
cursor = connect.cursor()
columns_names = [elem[1] for elem in cursor.execute("""PRAGMA table_info(coffee)""").fetchall()]

def get_data():
    result = list(cursor.execute(f"""SELECT id, "Название сорта", "Степень обжарки",
         "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки" FROM coffee""").fetchall())
    return result


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 387)
        Form.setStyleSheet(u"QWidget{font: 10pt \"Segoe Ui\"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")

        self.gridLayout.addWidget(self.addButton, 0, 0, 1, 1)

        self.changeButton = QPushButton(Form)
        self.changeButton.setObjectName(u"changeButton")

        self.gridLayout.addWidget(self.changeButton, 0, 1, 1, 1)

        self.delButton = QPushButton(Form)
        self.delButton.setObjectName(u"delButton")

        self.gridLayout.addWidget(self.delButton, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.addButton.setText(
            QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.changeButton.setText(QCoreApplication.translate("Form",
                                                             u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                             None))
        self.delButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form",
                                                               u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446",
                                                               None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form",
                                                                u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446",
                                                                None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form",
                                                                u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446",
                                                                None));
    # retranslateUi


class Ui_Form_Change_Widget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(414, 300)
        Form.setStyleSheet(u"QWidget{font: 10pt \"Segoe Ui\"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.roastingLineEdit = QLineEdit(Form)
        self.roastingLineEdit.setObjectName(u"roastingLineEdit")

        self.gridLayout.addWidget(self.roastingLineEdit, 2, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.idLineEdit = QLineEdit(Form)
        self.idLineEdit.setObjectName(u"idLineEdit")

        self.gridLayout.addWidget(self.idLineEdit, 0, 1, 1, 1)

        self.sortLineEdit = QLineEdit(Form)
        self.sortLineEdit.setObjectName(u"sortLineEdit")

        self.gridLayout.addWidget(self.sortLineEdit, 1, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.grainsLineEdit = QLineEdit(Form)
        self.grainsLineEdit.setObjectName(u"grainsLineEdit")

        self.gridLayout.addWidget(self.grainsLineEdit, 3, 1, 1, 1)

        self.confirmPushButton = QPushButton(Form)
        self.confirmPushButton.setObjectName(u"confirmPushButton")

        self.gridLayout.addWidget(self.confirmPushButton, 11, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.tasteLineEdit = QLineEdit(Form)
        self.tasteLineEdit.setObjectName(u"tasteLineEdit")

        self.gridLayout.addWidget(self.tasteLineEdit, 4, 1, 1, 1)

        self.priceLineEdit = QLineEdit(Form)
        self.priceLineEdit.setObjectName(u"priceLineEdit")

        self.gridLayout.addWidget(self.priceLineEdit, 5, 1, 1, 1)

        self.sizeLineEdit = QLineEdit(Form)
        self.sizeLineEdit.setObjectName(u"sizeLineEdit")

        self.gridLayout.addWidget(self.sizeLineEdit, 7, 1, 1, 1)

        self.errorLabel = QLabel(Form)
        self.errorLabel.setObjectName(u"errorLabel")

        self.gridLayout.addWidget(self.errorLabel, 11, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430",
                                                        None))
        self.label_6.setText(QCoreApplication.translate("Form",
                                                        u"\u041e\u0431\u044a\u0435\u043c \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0438",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("Form",
                                                        u"\u041c\u043e\u043b\u043e\u0442\u044b\u0439/\u0432 \u0437\u0435\u0440\u043d\u0430\u0445",
                                                        None))
        self.label.setText(QCoreApplication.translate("Form", u"id", None))
        self.confirmPushButton.setText(
            QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c",
                                       None))
        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Form",
                                                        u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430",
                                                        None))
        self.errorLabel.setText("")
    # retranslateUi


class ChangeWidget(QWidget, Ui_Form_Change_Widget):
    def __init__(self, main_wdg_obj):
        super().__init__()

        self.setupUi(self)
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


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Латте макиато")

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
