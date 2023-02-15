# # З а д а н и е  № 3
# import sqlite3
# from random import randint, choice
#
# num_1 = randint(0, 9)
# num_2 = randint(0, 9)
# connect = sqlite3.connect('name_3.db')  # create DB
# cursor = connect.cursor()  # create cursor () obj
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,
# col_2 INTEGER) ''')
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES (?, ?)''', (num_1, num_2,))
# connect.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# random_entry = choice(cursor.fetchall())
# random_id = random_entry[0]
# print(random_entry)  # случайное значение
# if random_entry[1] % 2 == 0 and random_entry[2] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_1 WHERE id=?''', (random_id,))
#     connect.commit()
# else:
#     cursor.execute('''UPDATE tab_1 SET col_1=2, col_2=2 WHERE id=?''', (random_id,))
#     connect.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# print(cursor.fetchall())
#
# З а д а н и е  № 4
# import sqlite3
#
# connect = sqlite3.connect('name_4.db')  # create DB
# cursor = connect.cursor()  # create cursor () obj
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
# connect.commit()
#
#
# class BD:
#
#     @staticmethod
#     def count_arg(a=None, b=None, c=None):
#         if a is not None and b is None and c is None:
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
#             connect.commit()
#         elif a is not None and b is not None and c is None:
#             cursor.execute('''DELETE FROM tab_1 WHERE id=(1)''')
#             connect.commit()
#         elif a is not None and b is not None and type(c) is int:
#             cursor.execute('''UPDATE tab_1 SET col_1=(77) WHERE id=(3)''')
#             connect.commit()
#
#
# if __name__ == '__main__':
#     bd = BD()
#     bd.count_arg('1')
#     cursor.execute('''SELECT * FROM tab_1''')
#     bd.count_arg('1', 2)
#     cursor.execute('''SELECT * FROM tab_1''')
#     bd.count_arg('1', 2, 4)
#     cursor.execute('''SELECT * FROM tab_1''')
#     print(cursor.fetchall())

#
# # З а д а н и е  № 5
# import sqlite3
# connect = sqlite3.connect('name_5.db')  # create DB
# cursor = connect.cursor()  # create cursor () obj
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT) ''')
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES ('hi', 'python')''')
# connect.commit()
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES ('ho', 'pothon')''')
# connect.commit()
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES ('hey', 'peyhon')''')
# connect.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# print(cursor.fetchall())   # база до корректировки
# cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
# connect.commit()
# cursor.execute('''UPDATE tab_1 SET col_1='hello', col_2='world' WHERE id=3''')
# connect.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# connect.commit()
# result = cursor.fetchall()  # база после корректировки
# with open('result.txt', 'w', encoding='UTF-8') as file:
#     for i in result:
#         file.write(str(i))
#         file.write('\n')
# print(f'* Ответ в файле: result.txt')

# # Д о м а ш н е е  З а д а н и е
# import sqlite3
# connect = sqlite3.connect('home_work.db')  # create DB
# cursor = connect.cursor()  # create cursor () obj
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGGER) ''')
#
#
# def word_or_number(*args):
#     for value in args:
#         if type(value) is str:
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (value,))
#             connect.commit()
#             cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (len(value),))
#             connect.commit()
#         else:
#             if value % 2 == 0:
#                 cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (value,))
#                 connect.commit()
#             else:
#                 cursor.execute('''INSERT INTO tab_1(col_1) VALUES ('нечётное')''')
#                 connect.commit()
#
#
# def operation():
#     if len(lst_int) > 5:
#         cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
#         connect.commit()
#     else:
#         cursor.execute('''UPDATE tab_1 SET col_1='hello' WHERE id=1''')
#         connect.commit()
#
#
# if __name__ == '__main__':
#     word_or_number('python', 543, 'py', 6, 11, 'world', 2, 4)   # список из чисел и слов
#     cursor.execute('''SELECT col_1 FROM tab_1''')
#     lst_str = cursor.fetchall()
#     print(f'Таблица 1 до редакт.: {lst_str}')
#     cursor.execute('''SELECT col_1 FROM tab_2''')
#     lst_int = cursor.fetchall()
#     print(f'Таблица 2 до редакт.: {lst_int}')
#     operation()
#     cursor.execute('''SELECT col_1 FROM tab_1''')
#     print(f'Таблица 1 после редакт.: {cursor.fetchall()}')
#     cursor.execute('''SELECT col_1  FROM tab_2''')
#     print(f'Таблица 2 после редакт.: {cursor.fetchall()}')
