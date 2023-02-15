import sqlite3

# connect = sqlite3.connect('name.db')  # create DB
# cursor = connect.cursor()  # create cursor () obj
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT) ''')
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES ('pacific', 'ocean')''')
# connect.commit()
# color = 'red'
# type_of_water = 'sea'
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES (?, ?)''', (color, type_of_water))
# connect.commit()
#
# cursor.execute('SELECT * FROM tab_1')
# val = cursor.fetchall()
# print(val)
# print('*' * 10)
# cursor.execute('''SELECT * FROM tab_1 WHERE col_1='pacific' ''')
# val_1 = cursor.fetchall()
# print(val_1)
# print('*' * 10)
# cursor.execute('''SELECT * FROM tab_1 ORDER BY col_1''')
# val_2 = cursor.fetchall()
# print(val_2)
# print('*' * 10)
# cursor.execute('''SELECT * FROM tab_1 WHERE col_2 LIKE 's%' ''')
# val_3 = cursor.fetchall()
# print(val_3)
#
# num = int(input('ENTER NUMBER: '))
# connect = sqlite3.connect('name_1.db')  # create DB
# cursor = connect.cursor()  # create cursor () obj
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT,
# col_3 INTEGER) ''')
# cursor.execute('''INSERT INTO tab_1 (col_1, col_2, col_3) VALUES ('python', 'hello', ?)''', (num,))
# connect.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# values = cursor.fetchall()
# for value in values:
#     print(value)
#
# cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
# connect.commit()
# cursor.execute('''DELETE FROM tab_1 WHERE col_1='pacific' ''')
# connect.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# val_4 = cursor.fetchall()
# print(val_4)
from random import randint
#
num_1 = randint(0, 9)
num_2 = randint(0, 9)
connect = sqlite3.connect('name_2.db')  # create DB
cursor = connect.cursor()  # create cursor () obj
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,
col_2 INTEGER) ''')
cursor.execute('''INSERT INTO tab_1 (col_1, col_2) VALUES (?, ?)''', (num_1, num_2,))
connect.commit()
cursor.execute('''SELECT * FROM tab_1''')
values = cursor.fetchall()
count = 0
count_1 = 0
for value in values:
    count_1 += 1
    count += (value[1] + value[2])/count_1
    if count > count_1:
        cursor.execute('''DELETE FROM tab_1 WHERE id=4''')
        connect.commit()
        cursor.execute('''SELECT * FROM tab_1''')
print(cursor.fetchall())



