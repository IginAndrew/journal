import sqlite3


class SQLitedb:
    def connect(self, name_db):
        try:
            self.con = sqlite3.connect(f'{name_db}.db')
            print("Успешное подключение!")
            with self.con:
                self.c = self.con.cursor()
            return self.c
        except Exception:
            print("Ошибка подключения!")


class User(SQLitedb):

    def create_table_user_args(self, *args):
        self.c.execute('''
		    CREATE TABLE IF NOT EXISTS User
		    (
		    id INTEGER PRIMARY KEY AUTOINCREMENT,
		    name TEXT NOT NULL
		    )
		    ''')
        self.con.commit()

    def create_table_user_name(self):
        self.c.execute('''
	    CREATE TABLE IF NOT EXISTS User
	    (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name TEXT NOT NULL
	    )
	    ''')
        self.con.commit()

    def create_table_user_name_surname(self):
        self.c.execute('''
	    CREATE TABLE IF NOT EXISTS User
	    (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name TEXT NOT NULL,
	    surname TEXT NOT NULL
	    )
	    ''')
        self.con.commit()

    def create_table_user_name_surname_birthdate(self):
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS User
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        birthdate TEXT NOT NULL
        )
        ''')
        self.con.commit()

    def create_table_user_name_surname_birthdate_adress(self):
        self.c.execute('''
	    CREATE TABLE IF NOT EXISTS User
	    (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name TEXT NOT NULL,
	    surname TEXT NOT NULL,
	    birthdate TEXT NOT NULL,
	    adress TEXT NOT NULL
	    )
	    ''')
        self.con.commit()

    def create_table_user_name_surname_birthdate_adress_politik(self):
        self.c.execute('''
	    CREATE TABLE IF NOT EXISTS User
	    (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name TEXT NOT NULL,
	    surname TEXT NOT NULL,
	    birthdate TEXT NOT NULL,
	    adress TEXT NOT NULL,
	    politik TEXT NOT NULL
	    )
	    ''')
        self.con.commit()

    def create_table_user_name_surname_birthdate_adress_politik_passport(self):
        self.c.execute('''
	    CREATE TABLE IF NOT EXISTS User
	    (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name TEXT NOT NULL,
	    surname TEXT NOT NULL,
	    birthdate TEXT NOT NULL,
	    adress TEXT NOT NULL,
	    politik TEXT NOT NULL,
	    passport TEXT NOT NULL
	    )
	    ''')
        self.con.commit()


class Server:

    def __init__(self, name_db):
        self.name_db = name_db

    def create_table_user_name_surname_birthdate(self, db):
        db.connect(self.name_db)
        db.create_table_user_name_surname_birthdate()


s = Server('test')
s.create_table_user_name_surname_birthdate(User())
