from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from qt_mimesis.bd import Server, User, Txt_db, Email, Phone, Car, Credit, Language, Work
from qt_mimesis.ui.ui_main import Ui_MainWindow

from mimesis import Person,Transport,Numeric
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis import Address
import random

person = Person(Locale.RU)
transport = Transport()
numeric = Numeric()
address = Address(locale="ru")

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_user)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_email)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_phones)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_cars)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_credits)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_languages)
        self.ui.pushButton.clicked.connect(self.add_table_to_bd_work)

# добавка имени БД + подключение к БД
    def add_database_name(self):
        try:
            if self.ui.lineEdit.text() != "":
                name_bd = self.ui.lineEdit.text()
                s = Server(name_bd)
                return s
            else:
                QMessageBox.warning(
                    self,
                    "ВНИМАНИЕ",
                    "<b style='color: red;'>НЕТ ДАННЫХ ИМЕНИ БД!</b>")
                return None
        except:
            return None


#     добавка количество персонажей
    def add_user_count(self):
        try:
            if self.ui.lineEdit_2.text() != "":
                count = self.ui.lineEdit_2.text()
                return int(count)
            else:
                QMessageBox.warning(
                    self,
                    "ВНИМАНИЕ",
                    "<b style='color: red;'>НЕТ ДАННЫХ КОЛ-ВО ПЕРСОНАЖЕЙ!</b>")
                return None
        except:
            return None

# Записывает данные о столбцах таблицы 'User' в список
    def add_data_to_list(self):
        try:
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
                data_list.append("political_views")
            if self.ui.checkBox_6.isChecked()   ==  True:
                data_list.append("passpord")
            return sorted(data_list)
        except:
            return None

# добавляем таблицу 'User' в БД
    def add_table_to_bd_user(self):
        try:
            if self.add_database_name() !=  None:
                s = self.add_database_name()
                data_list = self.add_data_to_list()
                user_args_txt = Txt_db()
                user_args_txt.user_args_txt(self.ui.lineEdit.text(),data_list)
                s.users(User())
                list_insert_user = []
                for _ in range(self.add_user_count()):
                    if 'address' in data_list:
                        adress = address.city() + " " + address.street_name() + " " + address.street_number() +  "  "  + address.postal_code()
                        list_insert_user.append(adress)
                    if  'birthdate' in data_list:
                        birthdate = person.birthdate()
                        list_insert_user.append(str(birthdate))
                    if 'name' in data_list:
                        name = person.name(gender=Gender.MALE)
                        list_insert_user.append(name)
                    if 'passpord' in data_list:
                        passpord = abs(numeric.integer_number(start=100000000, end=999999999))
                        list_insert_user.append(str(passpord))
                    if 'political_views' in data_list:
                        political_views = person.political_views()
                        list_insert_user.append(political_views)
                    if 'surname' in data_list:
                        surname  =  person.surname(gender=Gender.MALE)
                        list_insert_user.append(surname)
                    s.post_users(User(),data_list, tuple(list_insert_user))
                    list_insert_user = []
            else:
                QMessageBox.warning(
                    self,
                    "ВНИМАНИЕ",
                    "<b style='color: red;'>НЕТ ДАННЫХ столбцов таблицы 'User'!</b>")
                return None

        except:
            return None

# добавляем таблицу почты в БД
    def add_table_to_bd_email(self):
        try:
            if self.ui.lineEdit_3.text() !=  "":
                s = self.add_database_name()
                s.email(Email())
            else:
                return None
        except:
            return None

# добавляем таблицу telephon в БД
    def add_table_to_bd_phones(self):
        try:
            if self.ui.lineEdit_4.text() !=  "":
                s = self.add_database_name()
                s.phone(Phone())
            else:
                return None
        except:
            return None

# добавляем таблицу car в БД
    def add_table_to_bd_cars(self):
        try:
            if self.ui.lineEdit_5.text() !=  "":
                s = self.add_database_name()
                s.car(Car())
            else:
                return None
        except:
            return None

# добавляем таблицу credits в БД
    def add_table_to_bd_credits(self):
        try:
            if self.ui.lineEdit_6.text() !=  "":
                s = self.add_database_name()
                s.credit(Credit())
            else:
                return None
        except:
            return None

# добавляем таблицу language в БД
    def add_table_to_bd_languages(self):
        try:
            if self.ui.lineEdit_7.text() !=  "":
                s = self.add_database_name()
                s.language(Language())
            else:
                return None
        except:
            return None

# добавляем таблицу language в БД
    def add_table_to_bd_work(self):
        try:
            if self.ui.lineEdit_8.text() !=  "":
                s = self.add_database_name()
                s.work(Work())
            else:
                return None
        except:
            return None



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec_())