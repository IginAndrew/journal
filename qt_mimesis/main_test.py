from mimesis import Person,Transport,Numeric
from mimesis.enums import Gender
from mimesis.locales import Locale
import random

from bd_oop import *

person = Person(Locale.RU)
transport = Transport()
numeric = Numeric()
s = Server('users_mimesis')

def genders(i,gender):
	with open('user.txt', 'a', encoding='utf-8') as file:
				file.writelines([str(i) + ":" + " "])
				name = person.name(gender)
				surname = person.surname(gender)
				birthdate = person.birthdate()
				file.writelines([f'Имя: {name}'])
				file.writelines(['\n'])
				file.writelines([f'Фамилия: {surname}'])
				file.writelines(['\n'])
				file.writelines([f'Дата рождения: {birthdate}'])
				file.writelines(['\n'])
				file.writelines(['\n'])
				s.post_user(SQLitedb(),name,surname,birthdate)

def bd(users:int, email:int, telephone:int, car:int):

	s.create_table_user(SQLitedb())
	if s.get_users(SQLitedb()):
		[s.dell_table(SQLitedb(), i) for i in s.get_name_table(SQLitedb())]

	with open('user.txt', 'a', encoding='utf-8') as file:
			file.seek(0)
			file.truncate()
	with open('email.txt', 'a', encoding='utf-8') as file:
			file.seek(0)
			file.truncate()
	with open('telephone.txt', 'a', encoding='utf-8') as file:
			file.seek(0)
			file.truncate()
	with open('car.txt', 'a', encoding='utf-8') as file:
			file.seek(0)
			file.truncate()
	for i in range(1,users+1):
		gender = ['MALE', 'FEMALE']
		random_gender = (random.choice(gender))
		print(random_gender)
		if random_gender == 'MALE':
			gender = Gender.MALE
			genders(i, gender)
		else:
			gender = Gender.FEMALE
			genders(i, gender)
		for _ in range(random.randint(1,email)):  # добавка почты
			email_user = person.email()
			with open('email.txt', 'a', encoding='utf-8') as file:
				file.writelines([str(i) + ":" + " "])
				file.writelines([f'Почта: {email_user}'])
				file.writelines(['\n'])
				s.create_table_email(SQLitedb())
				s.post_email(SQLitedb(),email_user,i)


		for _ in range(random.randint(1,telephone)): # добавка телефона
			phone = person.telephone()
			with open('telephone.txt', 'a', encoding='utf-8') as file:
				file.writelines([str(i) + ":" + " "])
				file.writelines([f'Телефон: {phone}'])
				file.writelines(['\n'])
				s.create_table_phone(SQLitedb())
				s.post_phone(SQLitedb(),phone,i)

		for _ in range(random.randint(1,car)): # добавка тачки
			nomer = abs(numeric.integer_number())
			marka = transport.manufacturer()
			znak = transport.vehicle_registration_code()
			with open('car.txt', 'a', encoding='utf-8') as file:
				file.writelines([str(i) + ":" + " "])
				file.writelines([f'Номер автомобиля: {numeric}'])
				file.writelines(['\n'])
				file.writelines([f'Марка автомобиля: {marka}'])
				file.writelines(['\n'])
				file.writelines([f'Регистрационный знак: {znak}'])
				file.writelines(['\n'])
				s.create_table_car(SQLitedb())
				s.post_car(SQLitedb(), nomer, marka, znak, i)

if __name__ == '__main__':
	bd(5,3,5,3)