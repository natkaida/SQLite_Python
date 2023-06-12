import sqlite3
import random

# Создание базы данных и подключение к ней
conn = sqlite3.connect('retailcompany.db')
cursor = conn.cursor()

# Создание таблицы workload_june
cursor.execute('''CREATE TABLE workload_june
                (date TEXT,
                first_name TEXT,
                last_name TEXT,
                position TEXT,
                time_in TEXT,
                time_out TEXT)''')

# Список с именами и фамилиями сотрудников и их должностями
employees = [('Илья', 'Смирнов', 'менеджер по продажам'),
             ('Максим', 'Иванов', 'бухгалтер'),
             ('Артем', 'Кузнецов', 'менеджер по снабжению'),
             ('Михаил', 'Попов', 'консультант'),
             ('Александр', 'Соколов', 'менеджер по продажам'),
             ('Дмитрий', 'Лебедев', 'бухгалтер'),
             ('Мария', 'Козлова', 'менеджер по снабжению'),
             ('Анна', 'Новикова', 'консультант'),
             ('Ольга', 'Морозова', 'менеджер по продажам'),
             ('Ирина', 'Петрова', 'бухгалтер'),
             ('Елена', 'Соловьева', 'менеджер по снабжению'),
             ('Наталья', 'Васильева', 'консультант')]

# Словарь для хранения времени последнего выхода каждого сотрудника
last_login_time = {}

# Заполнение таблицы данными о входах и выходах сотрудников за июнь
for i in range(1, 31):
    if i in [2, 3, 9, 10, 16, 17, 23, 24, 30]: # Исключаем выходные дни
        continue
    for j in range(1, len(employees) + 1):
        employee = employees[j - 1]
        first_name = employee[0]
        last_name = employee[1]
        position = employee[2]
        date = f'{i:02}.06.2023'
        if (first_name, last_name) not in last_login_time or last_login_time[(first_name, last_name)] != date:
            time_in = f'{random.randint(9, 11):02}:{random.randint(0, 59):02}'
            time_out = f'{random.randint(12, 17):02}:{random.randint(0, 59):02}'
            cursor.execute('''INSERT INTO workload_june
                              VALUES (?, ?, ?, ?, ?, ?)''', (date, first_name, last_name, position, time_in, time_out))
            last_login_time[(first_name, last_name)] = date

# Сохранение изменений и закрытие базы данных
conn.commit()
conn.close()