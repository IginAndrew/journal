import os
import sqlite3


class Txt_db:

    def user_args_txt(self, name_bd, *args):
        # Открывает файл для добавления данных
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            # Удаляет все данные из файла
            file.seek(0)
            file.truncate()
        # Открывает файл для добавления данных
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            # Записывает строку 'CREATE TABLE IF NOT EXISTS User' в файл
            file.writelines(['CREATE TABLE IF NOT EXISTS User'])
            file.writelines(['\n'])
            # Записывает строку '(id INTEGER PRIMARY KEY AUTOINCREMENT,' в файл
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
        # Проходит по всем элементам списка args
        for i in range(len(args[0])):
            # Если элемент не последний в списке
            if i + 1 != len(args[0]):
                # Открывает файл для добавления данных
                with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
                    # Записывает строку с именем столбца и типом данных в файл
                    file.writelines([f'{args[0][i]} TEXT NOT NULL,'])
                    file.writelines(['\n'])
            # Если элемент последний в списке
            else:
                # Открывает файл для добавления данных
                with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
                    # Записывает строку с именем столбца и типом данных в файл
                    file.writelines([f'{args[0][i]} TEXT NOT NULL'])
                    file.writelines(['\n'])
        # Открывает файл для добавления данных
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            # Записывает строку ')' в файл
            file.writelines([")"])
            file.writelines(['\n'])
            # Записывает строку '\n' в файл
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


    def work_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS Work'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['occupatione TEXT NOT NULL'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['&'])
            file.writelines(['\n'])
            file.writelines(['\n'])

    def user_id_work_id_txt(self, name_bd):
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(['CREATE TABLE IF NOT EXISTS User_id_work_id'])
            file.writelines(['\n'])
            file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
            file.writelines(['\n'])
            file.writelines(['user_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['work_id INTEGER NOT NULL,'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (user_id) REFERENCES User(id),'])
            file.writelines(['\n'])
            file.writelines(['FOREIGN KEY (work_id) REFERENCES Work(id)'])
            file.writelines(['\n'])
            file.writelines([")"])
            file.writelines(['\n'])
            file.writelines(['|'])
            file.writelines(['\n'])
            file.writelines(['\n'])



class SQLitedb:

    def dell_bd(self,name_bd):
        # Проверяет, существует ли файл базы данных
        if os.path.isfile(f'{name_bd}.db'):
            # Если файл существует, возвращает True
            return True
        # Если файла не существует, возвращает False
        return False

    def connect(self, name_bd):
        # Пытается подключиться к базе данных
        try:
            # Подключается к базе данных
            self.con = sqlite3.connect(f'{name_bd}.db')
            # Выводит сообщение об успешном подключении
            print("Успешное подключение!")
            # Создает курсор для выполнения SQL-запросов
            with self.con:
                self.c = self.con.cursor()
            # Возвращает курсор
            return self.c
        # Если возникает ошибка, выводит сообщение об ошибке подключения
        except Exception:
            print("Ошибка подключения!")

    def get_name_table(self):  # выводит все таблицы из бд
        # Выполняет SQL-запрос для получения имен всех таблиц в базе данных
        res = self.c.execute('''
               SELECT name FROM sqlite_master 
                WHERE type='table'
                ''')
        # Получает все результаты запроса
        self.res = res.fetchall()
        # Если результаты не найдены, выводит сообщение и возвращает False
        if not self.res:
            print("Данные не найдены!!!!!!")
            return False
        # Возвращает список имен всех таблиц
        return [i[0] for i in self.res]


class User(SQLitedb):

    def users(self, name_bd):
        # Создает объект класса SQLitedb
        table = SQLitedb()
        # Подключается к базе данных
        table.connect(name_bd)
        # Получает список имен всех таблиц в базе данных
        name_table = table.get_name_table()
        # Если список имен таблиц не пуст и в нем есть строка 'User', выводит сообщение
        if name_table and "User" in name_table:
            print('Есть такая таблица в БД!!!')
        # Если список имен таблиц пуст или в нем нет строки 'User', создает таблицу 'User' в базе данных
        else:
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                # Читает данные из файла
                sql = file.read()
            # Выводит данные из файла
            print(sql)
            # Выполняет SQL-запрос для создания таблицы 'User' в базе данных
            self.c.execute(sql)
            # Фиксирует изменения в базе данных
            self.con.commit()

    def post_user(self,name_bd,tuple_list_user,add_user):
        table = SQLitedb()
        table.connect(name_bd)
        sql = f"INSERT INTO User {tuple(tuple_list_user)} values {add_user}"
        print(sql)
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(sql)
            file.writelines(['\n'])
            file.writelines(['\n'])
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

    def post_email(self,name_bd,email,user_id):
        table = SQLitedb()
        table.connect(name_bd)
        sql = f"INSERT INTO Email (email,user_id) values {email,user_id}"
        print(sql)
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(sql)
            file.writelines(['\n'])
            file.writelines(['\n'])
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

    def post_phone(self,name_bd,phone,user_id):
        table = SQLitedb()
        table.connect(name_bd)
        sql = f"INSERT INTO Phone (phone,user_id) values {phone,user_id}"
        print(sql)
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(sql)
            file.writelines(['\n'])
            file.writelines(['\n'])
        self.c.execute(sql)
        self.con.commit()

class Car(SQLitedb):

    def car(self,name_bd):
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

    def post_car(self,name_bd,nomer,marka,country,user_id):
        table = SQLitedb()
        table.connect(name_bd)
        sql = f"INSERT INTO Car (nomer,marka,country,user_id) values {nomer,marka,country,user_id}"
        print(sql)
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(sql)
            file.writelines(['\n'])
            file.writelines(['\n'])
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

    def post_credit(self,name_bd,credit_card_number,credit_card_expiration_date,cvv,user_id):
        table = SQLitedb()
        table.connect(name_bd)
        sql = (f"INSERT INTO Credit(credit_card_number,credit_card_expiration_date,cvv,user_id)"
               f"values {credit_card_number,credit_card_expiration_date,cvv,user_id}")
        print(sql)
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(sql)
            file.writelines(['\n'])
            file.writelines(['\n'])
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

    def post_language(self,name_bd,language):
        table = SQLitedb()
        table.connect(name_bd)
        sql = (f"INSERT INTO Language(language) values ('{language}')")
        print(sql)
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(sql)
            file.writelines(['\n'])
            file.writelines(['\n'])
        self.c.execute(sql)
        self.con.commit()

    def get_language(self):
        res = self.c.execute('''SELECT language FROM Language''')
        res = res.fetchall()
        r = ([i[0] for i in res])
        return r

    def get_language_id(self):
        res = self.c.execute('''SELECT id FROM Language''')
        res = res.fetchall()
        r = ([i[0] for i in res])
        return r



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

    def post_user_id_language_id(self,name_bd,user_id,language_id):
        table = SQLitedb()
        table.connect(name_bd)
        sql = (f"INSERT INTO User_id_language_id(user_id,language_id) values {user_id,language_id}")
        print(sql)
        with open(f'user_{name_bd}.txt', 'a', encoding='utf-8') as file:
            file.writelines(sql)
            file.writelines(['\n'])
            file.writelines(['\n'])
        self.c.execute(sql)
        self.con.commit()


class Work(SQLitedb):

    def work(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "Work" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            work = Txt_db()
            work.work_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("Work") - 27:sql.rfind("&")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()

    def user_id_work_id(self, name_bd):
        table = SQLitedb()
        table.connect(name_bd)
        if "User_id_work_id" in table.get_name_table():
            print('Есть такая таблица в БД!!!')
        else:
            user_id_work_id = Txt_db()
            user_id_work_id.user_id_work_id_txt(name_bd)
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            sql = sql[sql.find("User_id_work_id") - 27:sql.rfind("|")]
            print(sql)
            self.c.execute(sql)
            self.con.commit()


class Server:
    def __init__(self, name_bd):
        self.name_bd = name_bd

    def users(self, bd):
        bd.connect(self.name_bd)
        bd.users(self.name_bd)

    def post_users(self, bd,tuple_list_user,add_user):
        bd.connect(self.name_bd)
        bd.post_user(self.name_bd,tuple_list_user,add_user)

    def email(self, bd):
        bd.connect(self.name_bd)
        bd.email(self.name_bd)

    def post_email(self, bd,email,user_id):
        bd.connect(self.name_bd)
        bd.post_email(self.name_bd,email,user_id)

    def phone(self, bd):
        bd.connect(self.name_bd)
        bd.phone(self.name_bd)

    def post_phone(self, bd,phone,user_id):
        bd.connect(self.name_bd)
        bd.post_phone(self.name_bd,phone,user_id)

    def car(self, bd):
        bd.connect(self.name_bd)
        bd.car(self.name_bd)

    def post_car(self, bd,nomer,marka,country,user_id):
        bd.connect(self.name_bd)
        bd.post_car(self.name_bd,nomer,marka,country,user_id)

    def credit(self, bd):
        bd.connect(self.name_bd)
        bd.credit(self.name_bd)

    def post_credit(self, bd,credit_card_number,credit_card_expiration_date,cvv,user_id):
        bd.connect(self.name_bd)
        bd.post_credit(self.name_bd,credit_card_number,credit_card_expiration_date,cvv,user_id)

    def language(self, bd):
        bd.connect(self.name_bd)
        bd.language(self.name_bd)
        bd.user_id_language_id(self.name_bd)

    def get_language(self,bd):
        bd.connect(self.name_bd)
        bd.get_language(self.name_bd)


    def post_language(self, bd,language):
        bd.connect(self.name_bd)
        bd.post_language(self.name_bd,language)

    def post_user_id_language_id(self, bd,user_id,language_id):
        bd.connect(self.name_bd)
        bd.post_user_id_language_id(self.name_bd,user_id,language_id)

    def work(self, bd):
        bd.connect(self.name_bd)
        bd.work(self.name_bd)
        bd.user_id_work_id(self.name_bd)


if __name__=="__main__":
    s = Server('www')
    # s.users(User())
    # s.email(Email())
    # s.phone(Phone())
    # s.car(Car())
    # s.credit(Credit())
    # s.language(Language())
    # s.work(Work())
    # s.post_users(User(),list_user,add_user)
    # s.post_email(Email(),'test@gmail.com',1)
    # s.post_phone(Phone(), '123456', 1)
    # s.post_car(Car(),'123', '123', '123', 1)
    # s.post_credit(Credit(),'123', '123', '123', 1)
    # s.post_language(Language(),'ru')
    # s.post_user_id_language_id(Language(),1,1)
    l = Language()
    l.connect('www')
    print(l.get_language_id())


