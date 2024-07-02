from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from qt_mimesis.bd import Server, User, Txt_db
from qt_mimesis.ui.ui_main import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_user)

# добавка имени БД + подключение к БД
    def add_database_name(self):
        if self.ui.lineEdit.text() != "":
            name_bd = self.ui.lineEdit.text()
            s = Server(name_bd)
            return s
        else:
            QMessageBox.warning(
                self,
                "ВНИМАНИЕ",
                "<b style='color: red;'>НЕТ ДАННЫХ!</b>")
            return None

#     добавка количество персонажей
    def add_user_count(self):
        if self.ui.lineEdit_2.text() != "":
            count = self.ui.lineEdit_2.text()
            return int(count)
        else:
            QMessageBox.warning(
                self,
                "ВНИМАНИЕ",
                "<b style='color: red;'>НЕТ ДАННЫХ!</b>")
            return None

# Записывает данные о столбцах таблицы 'User' в список
    def add_data_to_list(self):
        data_list  = []
        if self.ui.checkBox.isChecked()  ==  True:
            data_list.append("name")
        if self.ui.checkBox_2.isChecked()   ==  True:
            data_list.append("surname")
        if self.ui.checkBox_3.isChecked()   ==  True:
            data_list.append("birthdate")
        if self.ui.checkBox_4.isChecked()   ==  True:
            data_list.append("address")
        if self.ui.checkBox_5.isChecked()   ==  True:
            data_list.append("politic")
        if self.ui.checkBox_6.isChecked()   ==  True:
            data_list.append("passpord")
        return data_list

# добавляем таблицу 'User' в БД
    def add_table_to_bd_user(self):
        s = self.add_database_name()
        data_list = self.add_data_to_list()
        print(data_list)
        user_args_txt = Txt_db()
        user_args_txt.user_args_txt(self.ui.lineEdit.text(),data_list)
        s.users(User())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec_())