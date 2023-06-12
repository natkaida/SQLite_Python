import sqlite3

con = sqlite3.connect('sales.db')
cursor = con.cursor()

# Находим дубликаты
cursor.execute('''
    SELECT brand, model, engine_volume, max_speed, price, COUNT(*) FROM items
    GROUP BY LOWER(brand), LOWER(model), engine_volume, max_speed, price
    HAVING COUNT(*) > 1
''')

# Выводим найденные дубликаты
duplicates = cursor.fetchall()
if duplicates:
    print('У этих записей есть дубликаты:')
    for row in duplicates:
        print(row[:-1])
    answer = input('Хотите удалить дубликаты? Введите yes/no ' )
    if answer.lower() == 'yes':
        # Создаем подключение к базе данных
        con = sqlite3.connect('sales.db')

        # Создаем курсор для взаимодействия с базой данных
        cursor = con.cursor()

        # Удаляем дубликаты со значением не начинающимся на заглавную букву
        cursor.execute('''
            DELETE FROM items WHERE ROWID IN (
                SELECT i1.ROWID
                FROM items i1 JOIN items i2 ON (
                    LOWER(i1.brand) = LOWER(i2.brand) AND
                    LOWER(i1.model) = LOWER(i2.model) AND
                    LOWER(i1.color) = LOWER(i2.color) AND
                    i1.engine_volume == i2.engine_volume AND
                    i1.max_speed == i2.max_speed AND
                    i1.price == i2.price AND
                    i1.ROWID != i2.ROWID AND
                    (i1.brand != UPPER(i1.brand) OR i1.model != UPPER(i1.model) OR i1.color != UPPER(i1.color))
                )
            )
        ''')

        # Сохраняем изменения в базе данных
        con.commit()
        print('Дубликаты удалены')
    else:
        print('Не забудьте удалить дубликаты')
else:
    print('Дубликаты не найдены')

# Закрываем соединение с базой данных
con.close()