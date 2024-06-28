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
            file.writelines(['#email'])
            file.writelines(['\n'])

class SQLitedb:
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
            print("Данные не найден")
            return False
        return [i[0] for i in self.res]

    def dell_bd(self,name_bd):
        if os.path.isfile(f'{name_bd}.db'):
            return True
        return False


class User(SQLitedb):

    def users(self, name_bd):
        dell_bd = SQLitedb()
        user_args_txt = Txt_db()
        if dell_bd.dell_bd(name_bd):
            print('Такая БД уже существует!!!')
        else:
            user_args_txt.user_args_txt(name_bd, 'name', 'surname')
            with open(f'user_{name_bd}.txt', 'r', encoding='utf-8') as file:
                sql = file.read()
            print(sql)
            self.c.execute(sql)
            self.con.commit()


class Server:
    def __init__(self, name_bd):
        self.name_bd = name_bd


    def users(self, bd):
        bd.connect(self.name_bd)
        bd.users(self.name_bd)


s = Server('test')
s.users(User())
