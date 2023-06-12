import sqlite3

# подключение к базе данных
conn = sqlite3.connect('clothing.db')

# выборка данных из таблицы t_shirts по условию
cursor = conn.execute("SELECT * FROM t_shirts WHERE размер=? AND цена < ? AND цвет != ?", ('L', 100, 'красный'))

# вывод результатов выборки
for row in cursor:
    print(f"{row[0]} - {row[1]}, {row[2]}, ${row[3]}, {row[4]}")

# закрытие базы данных
conn.close()
