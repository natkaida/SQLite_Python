import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('pharmacy.db')
cursor = conn.cursor()

# Запрос на поиск лекарства по названию
medicine_name = input('Введите название препарата: ')
cursor.execute('''SELECT * FROM medicines
                WHERE name=?''', (medicine_name,))

# Вывод всех имеющихся записей с найденным лекарством
rows = cursor.fetchall()
if len(rows) == 0:
    print(f'Препарат {medicine_name} не найден')
else:
    print(f'Найдены записи о препарате {medicine_name}:')
    for row in rows:
        print(row)

# Закрытие базы данных
conn.close()