import sqlite3
import os

def dell_bd(name_bd):
    if os.path.isfile(name_bd):
        return True
    return False

def get_connection(name_bd):
    try:
        con = sqlite3.connect(
                f'{name_bd}')
        print("Успешное подключение!")
        return con
    except Exception:
        print("Ошибка подключения!")


def user_args_txt(name_bd, *args):
    with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'a', encoding='utf-8') as file:
            file.seek(0)
            file.truncate()
    with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'a', encoding='utf-8') as file:
                file.writelines(['CREATE TABLE IF NOT EXISTS User'])
                file.writelines(['\n'])
                file.writelines(['(id INTEGER PRIMARY KEY AUTOINCREMENT,'])
                file.writelines(['\n'])
    for i in range(len(args)):
        if i+1 != len(args):
            with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'a', encoding='utf-8') as file:
                file.writelines([f'{args[i]} TEXT NOT NULL,'])
                file.writelines(['\n'])
        else:
            with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'a', encoding='utf-8') as file:
                file.writelines([f'{args[i]} TEXT NOT NULL'])
                file.writelines(['\n'])
    with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'a', encoding='utf-8') as file:
                file.writelines([")"])
                file.writelines(['\n'])
                file.writelines(['#user'])
                file.writelines(['\n'])

def email_txt(name_bd):
    with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'a', encoding='utf-8') as file:
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



def user_args_str(*args):
    bd_str = []
    bd_str.append('CREATE TABLE IF NOT EXISTS User ')
    bd_str.append('\n')
    bd_str.append('(id INTEGER PRIMARY KEY AUTOINCREMENT, ')
    bd_str.append('\n')
    for i in range(len(args)):
        if i+1 != len(args):
            bd_str.append(f'{args[i]} TEXT NOT NULL, ')
            bd_str.append('\n')
        else:
            bd_str.append(f'{args[i]} TEXT NOT NULL')
            bd_str.append('\n')
    bd_str.append(")")
    return "".join(bd_str)

def get_name_table(name_bd):# выводит все таблицы из бд
    con = get_connection(name_bd)
    with con:
        c = con.cursor()
    res = c.execute('''
           SELECT name FROM sqlite_master 
            WHERE type='table'
            ''')
    res = res.fetchall()
    if not res:
        print("Данные не найден")
        return False
    return [i[0] for i in res]


def users(name_bd):
    if dell_bd(name_bd):
        print('Такая БД уже существует!!!')
    else:
        user_args_txt(name_bd, 'name', 'surname')
        with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'r', encoding='utf-8') as file:
            sql = file.read()
        con = get_connection(name_bd)
        with con:
            c = con.cursor()
        print(sql)
        c.execute(sql)
        con.commit()

def email(name_bd):
    if "Email" in get_name_table(name_bd):
        print('Есть такая таблица в БД!!!')
    else:
        email_txt(name_bd)
        with open(f'user_{name_bd[:name_bd.rfind(".")]}.txt', 'r', encoding='utf-8') as file:
            sql = file.read()
        sql = sql[sql.find("Email")-27:sql.rfind("#email")]
        con = get_connection(name_bd)
        with con:
            c = con.cursor()
        print(sql)
        c.execute(sql)
        con.commit()



# print(get_name_table('args.db'))
users('args.db')
email('args.db')
# print(test_args_str('name','surname','birthdate'))

# {name_bd[name_bd.find("Email")-27:name_bd.rfind(")")+1]}