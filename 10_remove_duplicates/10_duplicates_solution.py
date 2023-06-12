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
            DELETE FROM items WHERE id NOT IN (
                SELECT id FROM (
                    SELECT id, ROW_NUMBER() OVER (
                        PARTITION BY LOWER(brand), LOWER(model), color, engine_volume, max_speed, price
                        ORDER BY id
                    ) row_number
                    FROM items
                ) WHERE row_number = 1 or (row_number = 2 and brand = LOWER(brand) and model = LOWER(model))
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