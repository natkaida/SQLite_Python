import pandas as pd
import sqlite3

# Открываем файл и загружаем данные в DataFrame
df = pd.read_csv('movies.csv')

# Создаем базу данных и таблицу
conn = sqlite3.connect('mymovies.db')
c = conn.cursor()

# Создаем таблицу, используя названия столбцов в DataFrame
c.execute('''CREATE TABLE movies
             (Название фильма TEXT, Рейтинг REAL, Год INTEGER, Режиссер TEXT, Жанр TEXT)''')

# Сохраняем данные из DataFrame в таблицу
for index, row in df.iterrows():
    c.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", row)

# Сохраняем изменения и закрываем соединение
conn.commit()

conn = sqlite3.connect('mymovies.db')

# SQL-запрос на вывод всех фильмов с рейтингом более 8.0,
# выпущенных после 1999 года
query = '''SELECT *
           FROM movies
           WHERE Рейтинг > 8.5 AND Год > 1999'''

# Выполнение запроса и вывод результатов
for row in conn.execute(query):
    print(*row)
conn.close()