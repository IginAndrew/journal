import os
import sqlite3


class Txt_db:
    def user_args_txt(self, name_bd, *args):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.seek(0)
            file.truncate()
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS User'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
        for i in range(len(args)):
            if i + 1 != len(args):
                with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
                    file.writelines([f'{args[i]} TEXT NOT NULL,'])
                    file.writelines(['\n'])
            else:
                with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
                    file.writelines([f'{args[i]} TEXT NOT NULL'])
                    file.writelines(['\n'])
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['\n'])

    def email_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS Email'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['email TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['user_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (user_id) REFERENCES User(id)'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['@'])
            file.writelines(['\n'])
            file.writelines(['\n'])

    def phone_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS Phone'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['phone TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['user_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (user_id) REFERENCES User(id)'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['#'])
            file.writelines(['\n'])
            file.writelines(['\n'])

    def car_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS Car'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['nomer TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['marka TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['country TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['user_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (user_id) REFERENCES User(id)'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['$'])
            file.writelines(['\n'])
            file.writelines(['\n'])

    def credit_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS Credit'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['credit_card_number TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['credit_card_expiration_date TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['cvv TEXT NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['user_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (user_id) REFERENCES User(id)'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['^'])
            file.writelines(['\n'])
            file.writelines(['\n'])


    def language_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS Language'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['language TEXT NOT NULL'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['<'])
            file.writelines(['\n'])
            file.writelines(['\n'])

    def user_id_language_id_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS User_id_language_id'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['user_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['language_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (user_id) REFERENCES User(id),'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (language_id) REFERENCES Language(id)'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['>'])
            file.writelines(['\n'])
            file.writelines(['\n'])


class SQLitedb:

    def dell_bd(self,name_bd):
        if os.path.isfile(f'{name_bd}.db'):
            return True
        return False

    def connect(self, name_bd):
        try:
            self.con = sqlite3.connect(f'{name_bd}.db')
            print("Успешное подключение!")
            with self.con:
                self.c = self.con.cursor()
            return self.c
        except Exception:
            print("Ошибка подключения!")

    def get_name_table(self):  # выводит все таблицы из бд
        res = self.c.execute('''
               SELECT name FROM sqlite_master 
                WHERE type='table'
                ''')
        self.res = res.fetchall()
        if not self.res:
            print("Данные не найдены")
            return False
        return [i[0] for i in self.res]


class User(SQLitedb):

    def users(self, name_bd):
        user_args_txt = Txt_db()
        user_args_txt.user_args_txt(name_bd, 'name', 'surname', 'birthdate', 'address', 'passport', 'politic')
        with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
            sql = file.read()
        print(sql)
        self.c.execute(sql)
        self.con.commit()

class Email(SQLitedb):

    def email(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "Email" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            email = Txt_db()
            email.email_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("Email") - 27:sql.rfind("@")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()

class Phone(SQLitedb):

    def phone(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "Phone" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            phone = Txt_db()
            phone.phone_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("Phone") - 27:sql.rfind("#")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()

class Car(SQLitedb):

    def car(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "Car" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            car = Txt_db()
            car.car_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("Car") - 27:sql.rfind("$")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()

class Credit(SQLitedb):

    def credit(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "Credit" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            credit = Txt_db()
            credit.credit_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("Credit") - 27:sql.rfind("^")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()

class Language(SQLitedb):

    def language(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "Language" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            language = Txt_db()
            language.language_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("Language") - 27:sql.rfind("<")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()

    def user_id_language_id(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "User_id_language_id" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            user_id_language_id = Txt_db()
            user_id_language_id.user_id_language_id_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("User_id_language_id") - 27:sql.rfind(">")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()


class Server:
    def __init__(self, name_bd):
        self.name_bd = name_bd

    def users(self, bd):
        bd.connect(self.name_bd)
        bd.users(self.name_bd)

    def email(self, bd):
        bd.connect(self.name_bd)
        bd.email(self.name_bd)

    def phone(self, bd):
        bd.connect(self.name_bd)
        bd.phone(self.name_bd)

    def car(self, bd):
        bd.connect(self.name_bd)
        bd.car(self.name_bd)

    def credit(self, bd):
        bd.connect(self.name_bd)
        bd.credit(self.name_bd)

    def language(self, bd):
        bd.connect(self.name_bd)
        bd.language(self.name_bd)
        bd.user_id_language_id(self.name_bd)



s = Server('test')
s.users(User())
s.email(Email())
s.phone(Phone())
s.car(Car())
s.credit(Credit())
s.language(Language())
