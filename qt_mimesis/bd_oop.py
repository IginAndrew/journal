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


	def create_table_user(self):
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


	def post_user(self,name,surname,birthdate):
		self.c.execute('''
           INSERT INTO User (name, surname,birthdate) values
           (?,?,?);
            ''', (name, surname,birthdate,))
		self.con.commit()

	def get_users(self):
		res = self.c.execute('''
           SELECT name FROM User  
            ''')
		res = res.fetchall()
		return res

	def create_table_email(self):
		self.c.execute('''
    CREATE TABLE IF NOT EXISTS Email
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
    )
    ''')
		self.con.commit()

	def post_email(self,email,user_id):
		self.c.execute('''
           INSERT INTO Email (email,user_id) values
           (?,?);
            ''', (email,user_id,))
		self.con.commit()

	def create_table_phone(self):
		self.c.execute('''
    CREATE TABLE IF NOT EXISTS Phone
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
    )
    ''')
		self.con.commit()

	def post_phone(self,phone,user_id):
		self.c.execute('''
           INSERT INTO Phone (phone,user_id) values
           (?,?);
            ''', (phone,user_id,))
		self.con.commit()

	def create_table_car(self):
		self.c.execute('''
    CREATE TABLE IF NOT EXISTS Car
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nomer TEXT NOT NULL,
    marka TEXT NOT NULL,
    znak EXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
    )
    ''')
		self.con.commit()

	def post_car(self,nomer, marka, znak, user_id):
		self.c.execute('''
           INSERT INTO Car (nomer, marka, znak, user_id) values
           (?,?,?,?);
            ''', (nomer, marka, znak, user_id,))
		self.con.commit()

	def dell(self, table):# стерает данные таблицы
		self.c.execute(f"DELETE FROM {table}")
		self.con.commit()

	def get_name_table(self):# выводит все таблицы из бд
		res = self.c.execute('''
           SELECT name FROM sqlite_master  
            WHERE type='table'
            ''')
		res = res.fetchall()
		if not res:
			print("Данные не найден")
			return False
		return res



class Server:
	# инициализация класса по имени бд
	def __init__(self,name_db):
		self.name_db = name_db

# создание таблиц
	def create_table_user(self, db):
		db.connect(self.name_db)
		db.create_table_user()

	def create_table_email(self, db):
		db.connect(self.name_db)
		db.create_table_email()

	def create_table_phone(self, db):
		db.connect(self.name_db)
		db.create_table_phone()

	def create_table_car(self, db):
		db.connect(self.name_db)
		db.create_table_car()

# добавление юзера почты телефона машины
	def post_user(self,db,name,surname,birthdate):
		db.connect(self.name_db)
		db.post_user(name,surname,birthdate)

	def post_email(self,db,email,user_id):
		db.connect(self.name_db)
		db.post_email(email,user_id)

	def post_phone(self,db,phone,user_id):
		db.connect(self.name_db)
		db.post_phone(phone,user_id)

	def post_car(self,db,nomer, marka, znak, user_id):
		db.connect(self.name_db)
		db.post_car(nomer, marka, znak, user_id)

# вывод юзера
	def get_users(self, db):
		db.connect(self.name_db)
		users = db.get_users()
		return [user[0] for user in users]

# вывод всех таблиц
	def get_name_table(self,db):
		db.connect(self.name_db)
		get_name_table = db.get_name_table()
		if get_name_table:
			return [name_table[0] for name_table in get_name_table]
		else:
			return

# очистка таблицы
	def dell_table(self,db,table):
		db.connect(self.name_db)
		db.dell(table)


# s = Server('users_mimesis')
# s.create_table_user(SQLitedb())
# print(s.get_users(SQLitedb()))
# print(s.get_name_table(SQLitedb()))

# очистка всех таблиц
# [s.dell_table(SQLitedb(), i) for i in s.get_name_table(SQLitedb())] 

# s.post_user(SQLitedb(),'name','surname','birthdate')
# s.post_email(SQLitedb(),'test@tets.ru',1)