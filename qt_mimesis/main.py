from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from qt_mimesis.bd import Server, User, Txt_db, Email, Phone, Car, Credit, Language, Work
from qt_mimesis.ui.ui_main import Ui_MainWindow

from mimesis import Person, Transport, Numeric, Payment
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis import Address

import random

person = Person(Locale.RU)
transport = Transport()
numeric = Numeric()
address = Address(locale="ru")
payment = Payment()

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
        # self.ui.pushButton.clicked.connect(self.add_table_to_bd_email_data)


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

# добавляем данные о почте
    def add_table_to_bd_email_data(self):
        try:
            s = self.add_database_name()
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_3.text())
                for _ in range(random.randint(1, x)):
                    email_user = person.email()
                    print(email_user)
                    s.post_email(Email(), email_user, i)
        except:
            return None

# добавляем таблицу почты в БД
    def add_table_to_bd_email(self):
        try:
            if self.ui.lineEdit_3.text() !=  "":
                s = self.add_database_name()
                s.email(Email())
                self.add_table_to_bd_email_data()
            else:
                return None
        except:
            return None



# добавляем таблицу telephon в БД

    def add_table_to_bd_phone_data(self):
        try:
            s = self.add_database_name()
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_4.text())
                for _ in range(random.randint(1, x)):
                    phone_user = person.telephone()
                    print(phone_user)
                    s.post_phone(Phone(), phone_user, i)
        except:
            return None
    def add_table_to_bd_phones(self):
        try:
            if self.ui.lineEdit_4.text() !=  "":
                s = self.add_database_name()
                s.phone(Phone())
                self.add_table_to_bd_phone_data()
            else:
                return None
        except:
            return None

# добавляем таблицу car в БД

    def add_table_to_bd_car_data(self):
        try:
            s = self.add_database_name()
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_5.text())
                for _ in range(random.randint(1, x)):
                    nomer = abs(numeric.integer_number())
                    marka = transport.manufacturer()
                    znak = transport.vehicle_registration_code()
                    s.post_car(Car(), str(nomer), marka, str(znak), i)
        except:
            return None
    def add_table_to_bd_cars(self):
        try:
            if self.ui.lineEdit_5.text() !=  "":
                s = self.add_database_name()
                s.car(Car())
                self.add_table_to_bd_car_data()
            else:
                return None
        except:
            return None

# добавляем таблицу credits в БД

    def add_table_to_bd_credits_data(self):
        try:
            s = self.add_database_name()
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_6.text())
                for _ in range(random.randint(1, x)):
                    credit_card_number = payment.credit_card_number()
                    credit_card_expiration_date = payment.credit_card_expiration_date()
                    cvv = payment.cvv()
                    s.post_credit(Credit(), credit_card_number, credit_card_expiration_date, cvv, i)
        except:
            return None
    def add_table_to_bd_credits(self):
        try:
            if self.ui.lineEdit_6.text() !=  "":
                s = self.add_database_name()
                s.credit(Credit())
                self.add_table_to_bd_credits_data()
            else:
                return None
        except:
            return None

# добавляем таблицу language в БД

    def add_table_to_bd_languages_data(self):
        try:
            s = self.add_database_name()
            l = Language()
            l.connect(self.ui.lineEdit.text())
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_7.text())
                for _ in range(random.randint(1, x)):
                    language_user = person.language()
                    if language_user not in l.get_language():
                        s.post_language(Language(), language_user)
                    else:
                        continue
        except:
            return None

    def add_user_id_language_id_data(self):
        try:
            s = self.add_database_name()
            l = Language()
            l.connect(self.ui.lineEdit.text())
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_7.text())
                for _ in range(random.randint(1, x)):
                    random_id = random.choice(l.get_language_id())
                    if random_id not in l.get_user_id_language_id_language_id():
                        s.post_user_id_language_id(Language(), i, random_id)
                    else:
                        continue
        except:
            return None

    def add_table_to_bd_languages(self):
        try:
            if self.ui.lineEdit_7.text() !=  "":
                s = self.add_database_name()
                s.language(Language())
                self.add_table_to_bd_languages_data()
                self.add_user_id_language_id_data()
            else:
                return None
        except:
            return None

# добавляем таблицу work в БД

    def add_table_to_bd_work_data(self):
        try:
            s = self.add_database_name()
            l = Work()
            l.connect(self.ui.lineEdit.text())
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_8.text())
                for _ in range(random.randint(1, x)):
                    work_user = person.occupation()
                    if work_user not in l.get_work():
                        s.post_work(Work(), work_user)
                    else:
                        continue
        except:
            return None

    def add_user_id_work_id_data(self):
        try:
            s = self.add_database_name()
            l = Work()
            l.connect(self.ui.lineEdit.text())
            for i in range(1, self.add_user_count()+1):
                x = int(self.ui.lineEdit_8.text())
                for _ in range(random.randint(1, x)):
                    random_id = random.choice(l.get_work_id())
                    if random_id not in l.get_user_id_work_id_work_id():
                        s.post_user_id_work_id(Work(), i, random_id)
                    else:
                        continue
        except:
            return None
    def add_table_to_bd_work(self):
        try:
            if self.ui.lineEdit_8.text() !=  "":
                s = self.add_database_name()
                s.work(Work())
                self.add_table_to_bd_work_data()
                self.add_user_id_work_id_data()
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